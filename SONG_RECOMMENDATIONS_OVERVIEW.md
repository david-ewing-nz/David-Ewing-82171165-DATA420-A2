# SONG RECOMMENDATIONS SECTION - OVERALL GOAL & REQUIREMENTS
## Complete Overview for Assignment 2

**Date:** October 8, 2025  
**Student:** dew59 (David Ewing)  
**Section:** Song Recommendations (Collaborative Filtering)

---

## 🎯 OVERALL GOAL

### **Primary Objective:**
Build a **music recommendation system** using **collaborative filtering** to predict songs that users will enjoy based on their listening history and the listening patterns of similar users.

### **Core Problem:**
Given a dataset of **user-song-play count triplets** (48+ million interactions), recommend songs to users that they haven't listened to yet but are likely to enjoy.

### **Real-World Application:**
This is how Spotify, Apple Music, and other streaming services work! You're building the core recommendation engine that powers "Discover Weekly" or "For You" playlists.

---

## 📊 THE DATASET: Million Song Dataset - Taste Profile

### **Data Source:**
- **File:** `/data/msd/tasteprofile/triplets.tsv`
- **Size:** 488.41 MB
- **Records:** 48,373,586 user-song-play interactions

### **Schema:**
```
user_id    | song_id           | play_count
-----------|-------------------|------------
b80344d0   | SOAKIMP12A58A7A8E9 | 1
b80344d0   | SOAPDEY12A58A7A8E9 | 5
b80344d0   | SOBBMDR12A8C13253B | 2
...
```

### **Dataset Statistics (from ywa286's work):**
- **Unique Users:** ~1,019,318
- **Unique Songs:** ~384,546
- **Total Plays:** 48,373,586
- **Most Active User:** Played 4,316 unique songs (1.12% of all songs!)
- **Average Plays per User:** ~47.47
- **Average Plays per Song:** ~125.75

### **Data Distribution Characteristics:**
- **Highly Skewed:** Power law distribution
- **Long Tail:** Most songs have very few plays; few songs have many plays
- **User Activity:** Most users listen to relatively few songs; power users listen to thousands
- **Sparsity:** User-song matrix is ~99.99% sparse (most user-song pairs have NO interactions)

---

## 🔬 SECTION BREAKDOWN: What You Need to Do

### **Q1: Taste Data Exploration (20-25% of Recommendations section)**

**Goal:** Understand the dataset before building models

**Tasks:**
1. **Load and prepare the data:**
   - Load triplets.tsv with proper schema
   - Repartition for optimal performance (important for large dataset!)
   - Cache the DataFrame for repeated operations

2. **Calculate basic statistics:**
   - Number of unique users and songs
   - Total play count
   - Average plays per user/song
   - Most active user analysis

3. **Analyze distributions:**
   - Play count distribution (use percentiles: 25%, 50%, 75%)
   - Song popularity distribution (histogram)
   - User activity distribution (histogram)
   - **Expected Finding:** Both distributions are heavily skewed (long tail)

4. **Identify challenges:**
   - Data sparsity issues
   - Cold start problem (new users/songs)
   - Scalability considerations

**Key Insight:** This dataset is MASSIVE and SPARSE - you need to filter/sample strategically!

---

### **Q2: Collaborative Filtering with ALS (75-80% of Recommendations section)**

**Goal:** Build and evaluate a recommendation system using **Alternating Least Squares (ALS)**

#### **(a) Data Filtering & Preparation**

**Why Filter?**
- Reduce noise from users/songs with too few interactions
- Improve model training speed
- Better quality recommendations

**Tasks:**
1. **Filter unpopular songs:**
   - Remove songs with < N total plays (ywa286 used N=8)
   - **Rationale:** Songs with very few plays don't have enough signal

2. **Filter inactive users:**
   - Remove users with < M total plays (ywa286 used M=34)
   - **Rationale:** Users with few plays don't provide enough information

3. **Iterative filtering:**
   - After removing songs, re-check users (some may now have too few plays)
   - After removing users, re-check songs (some may now have too few plays)
   - **Important:** This is an iterative process!

4. **Calculate impact:**
   - How many users/songs were excluded?
   - What percentage of the data remains?
   - **Trade-off:** Quality vs Quantity

**Expected Results:**
- Excluding ~5-15% of users/songs typically improves model quality significantly
- Final dataset should still have millions of interactions

---

#### **(b) String Indexing**

**Why Needed?**
- ALS requires **integer IDs** for users and songs
- Original IDs are strings (e.g., "b80344d0", "SOAKIMP12A58A7A8E9")

**Tasks:**
1. **Use StringIndexer:**
   ```python
   user_indexer = StringIndexer(inputCol="user_id", outputCol="user_index")
   song_indexer = StringIndexer(inputCol="song_id", outputCol="song_index")
   ```

2. **Transform dataset:**
   - Convert user_id → user (int)
   - Convert song_id → song (int)
   - Keep play_count as-is

3. **Result Schema:**
   ```
   user (int) | song (int) | play_count (int)
   -----------|------------|------------------
   0          | 1234       | 1
   0          | 5678       | 5
   1          | 1234       | 2
   ```

**Important:** Save the mapping for later reverse lookup (to show actual song names)!

---

#### **(c) Train-Test Split**

**Goal:** Split data so each user has both training and test data

**Why Special Split Needed?**
- Can't use random split (would leave some users with NO test data)
- Need **per-user stratified split** (80% train, 20% test for EACH user)

**Tasks:**
1. **Stratified Split by User:**
   ```python
   # For each user, randomly split their plays 80/20
   window = Window.partitionBy("user").orderBy(F.rand())
   df_ranked = df.withColumn("rank", F.rank().over(window))
   # Calculate split point per user...
   ```

2. **Verify Split:**
   - Every user should appear in BOTH train and test
   - ~80% of interactions in train, ~20% in test
   - Print statistics to confirm

**Critical:** This ensures you can evaluate recommendations for all users!

---

#### **(d) Train ALS Model with Implicit Feedback**

**Goal:** Train collaborative filtering model using **implicit feedback**

**What is Implicit Feedback?**
- **Explicit:** Users rate items (1-5 stars) → "I liked this"
- **Implicit:** Users interact with items (play count) → "I engaged with this"
- **Our case:** Play count is implicit feedback (user listened → implicit preference)

**Why Implicit?**
- We don't have ratings, only play counts
- Play count indicates preference (more plays = more interest)
- implicitPrefs=True in ALS handles this properly

**Tasks:**
1. **Convert play_count to binary implicit feedback:**
   ```python
   # Any play_count > 0 → implicit positive feedback
   df = df.withColumn("implicit_feedback", (col("play_count") > 0).cast("double"))
   ```

2. **Initialize ALS with implicit preferences:**
   ```python
   als = ALS(
       maxIter=5,              # Number of iterations
       regParam=0.01,          # Regularization parameter
       userCol="user",
       itemCol="song",
       ratingCol="implicit_feedback",
       coldStartStrategy="drop",  # Drop users/songs not seen in training
       implicitPrefs=True      # ← KEY: Use implicit feedback
   )
   ```

3. **Train the model:**
   ```python
   model = als.fit(train_df)
   ```

**What Happens Inside ALS?**
- Creates **latent factor matrices** (user factors × song factors)
- Learns hidden features (e.g., "rockiness", "danceability", "energy")
- Users and songs represented as vectors in latent space
- Recommendation = dot product of user vector and song vectors

**Hyperparameters to Consider:**
- `rank`: Number of latent factors (default: 10)
- `maxIter`: More iterations = better fit (but slower)
- `regParam`: Regularization to prevent overfitting
- `alpha`: Confidence scaling for implicit feedback

---

#### **(e) Generate and Inspect Recommendations**

**Goal:** Generate top-N recommendations and manually inspect quality

**Tasks:**
1. **Generate recommendations for sample users:**
   ```python
   num_recommendations = 10
   user_recs = model.recommendForUserSubset(sample_users, num_recommendations)
   ```

2. **Compare with actual test data:**
   - What songs did the user actually play in test set?
   - How many recommended songs were actually played?
   - Calculate **Precision@10**: hits / 10

3. **Manual Inspection:**
   - Look at 3-5 sample users
   - Do recommendations make sense?
   - Are they diverse or repetitive?
   - Do they align with user's test set behavior?

**Example Output:**
```
User ID: 42
Top 10 Recommended Songs: [1234, 5678, 9012, ...]
Actual Songs Played: [5678, 3456, 7890, ...]
Precision@10: 0.10 (1 hit out of 10)
```

**Why Low Precision is OK:**
- Test set is small sample of what user might like
- User could like recommendations even if not in test set
- This is just a sanity check, not the main evaluation

---

#### **(f) Evaluate Using Ranking Metrics**

**Goal:** Formally evaluate recommendation quality using proper ranking metrics

**Why Ranking Metrics?**
- Classification metrics (accuracy, F1) don't apply here
- We care about TOP-K recommendations (order matters!)
- Standard metrics: Precision@K, MAP@K, NDCG@K

**Tasks:**

1. **Prepare Evaluation Data:**
   ```python
   # For each user in test set:
   # - recommendations: Top 10 predicted songs (ordered by score)
   # - relevant: Actual songs user played (ordered by play count)
   
   recommendations = model.recommendForAllUsers(10)
   relevant = test_df.groupBy("user").agg(
       F.sort_array(F.collect_list(...)).alias("relevant")
   )
   ```

2. **Calculate Ranking Metrics:**
   ```python
   evaluator = RankingEvaluator(
       predictionCol="recommendations", 
       labelCol="relevant"
   )
   
   precision_at_k = evaluator.evaluate(temp, {
       evaluator.metricName: "precisionAtK",
       evaluator.k: 10
   })
   
   map_at_k = evaluator.evaluate(temp, {
       evaluator.metricName: "meanAveragePrecisionAtK",
       evaluator.k: 10
   })
   
   ndcg_at_k = evaluator.evaluate(temp, {
       evaluator.metricName: "ndcgAtK",
       evaluator.k: 10
   })
   ```

3. **Interpret Results:**
   - **Precision@K:** % of recommendations that user actually played
   - **MAP@K:** Mean Average Precision - considers ranking order
   - **NDCG@K:** Normalized Discounted Cumulative Gain - rewards relevant items at top

**Expected Results (from ywa286's work):**
```
Implicit Feedback Model:
- Precision @ 10: ~0.00050 (0.05%)
- MAP @ 10:       ~0.00025 (0.025%)
- NDCG @ 10:      ~0.00075 (0.075%)
```

**Why So Low?**
- Dataset is EXTREMELY SPARSE (99.99%)
- Test set is tiny sample of user preferences
- Many good recommendations may not be in test set
- These metrics are harsh for sparse data

**What's Important:**
- Relative comparison (implicit vs explicit, different hyperparameters)
- Understanding trade-offs
- Discussing limitations

---

## 📈 GRADING EXPECTATIONS

### **From Grading Rubric:**
- **Reasoning (45%):** Explain WHY you made choices
  - Why these N/M thresholds for filtering?
  - Why implicit feedback vs explicit?
  - Why these hyperparameters?
  - What do the metrics tell us?
  
- **Answers (14%):** Respond to specific questions
  - Statistics calculations
  - Metric interpretations
  
- **Visualizations (11%):** Charts must be clear and informative
  - Song popularity distribution
  - User activity distribution
  - Play count distribution
  
- **Coding (10%):** Code must be correct and efficient
  - Proper data pipeline
  - Efficient Spark operations
  - Correct ALS implementation
  
- **Tables (9%):** Summary statistics tables
  - Dataset statistics
  - Evaluation metrics comparison
  
- **Writing (11%):** Clear, concise, well-structured
  - Markdown explanations
  - Analysis sections
  - Conclusions

### **What ywa286 Did Well (70-80% complete):**
✅ Q1 Data Exploration (complete)
✅ Q2(a) Filtering (complete)
✅ Q2(b) String Indexing (complete)
✅ Q2(c) Train-Test Split (complete)
✅ Q2(d) ALS Training (complete)
✅ Q2(e) Sample Recommendations (complete)
✅ Q2(f) Ranking Evaluation (complete with all 3 metrics)

### **What's Missing or Could Be Improved:**
❌ **Reasoning/Discussion:**
  - Why N=8 and M=34? (No explanation)
  - Why these ALS hyperparameters?
  - Deeper interpretation of results
  - Comparison with baseline or alternative approaches
  
❌ **Additional Analysis:**
  - Impact of different hyperparameters (rank, regParam)
  - Comparison: Implicit vs Explicit feedback
  - Cold start problem discussion
  - Scalability considerations
  
❌ **Explicit Feedback Implementation:**
  - Assignment asks to TRY explicit feedback too
  - Compare implicit vs explicit results
  - Discuss which works better and why

---

## 🎯 YOUR ACTION PLAN

### **To Get Full Marks:**

1. **Complete the Missing Pieces:**
   - Add reasoning for all parameter choices
   - Implement explicit feedback variant
   - Compare implicit vs explicit metrics
   - Add discussion sections

2. **Enhance Explanations:**
   - Why collaborative filtering for this problem?
   - What are the assumptions?
   - What are the limitations?
   - When would this approach fail?

3. **Hyperparameter Tuning (if time permits):**
   - Try different rank values (5, 10, 20)
   - Try different regParam values (0.01, 0.1, 1.0)
   - Compare results in a table
   - Recommend best configuration

4. **Additional Visualizations:**
   - Latent factor visualization (if possible)
   - Recommendation diversity analysis
   - Coverage analysis (% of songs ever recommended)

5. **Write Strong Conclusions:**
   - Summarize findings
   - Discuss practical implications
   - Suggest improvements for production system

---

## 🔑 KEY CONCEPTS TO UNDERSTAND

### **Collaborative Filtering:**
- **User-Based:** "Users similar to you liked..."
- **Item-Based:** "Songs similar to what you played..."
- **Matrix Factorization:** ALS learns latent factors for both

### **ALS (Alternating Least Squares):**
- Decomposes user-song matrix into user factors × song factors
- Alternates: Fix user factors → optimize song factors → Fix song factors → optimize user factors
- Scales to massive datasets (billions of interactions)

### **Implicit vs Explicit Feedback:**
| Aspect | Explicit | Implicit |
|--------|----------|----------|
| Signal | Ratings (1-5 stars) | Play counts, clicks |
| Meaning | "I liked this" | "I engaged with this" |
| Confidence | High (direct preference) | Lower (maybe background play) |
| Availability | Rare (requires user effort) | Abundant (automatic) |
| Our case | ❌ Not available | ✅ We have this |

### **Ranking Metrics:**
- **Precision@K:** Of top K recommendations, how many are relevant?
- **MAP@K:** Average precision across all users, considers order
- **NDCG@K:** Weighted by position, higher score for relevant items at top

### **Challenges:**
- **Sparsity:** Most user-song pairs have no interaction
- **Cold Start:** New users/songs have no history
- **Scalability:** 48M interactions, 1M users, 384K songs
- **Popularity Bias:** Tends to recommend popular songs
- **Filter Bubble:** May not recommend diverse/novel content

---

## 💡 PRO TIPS

1. **Start Small, Scale Up:**
   - Test on filtered/sampled data first
   - Once working, scale to full dataset
   - Use `.cache()` on frequently accessed DataFrames

2. **Partition Wisely:**
   - Repartition based on cluster size
   - ywa286 used 8 partitions for 16 cores
   - More partitions = better parallelism (up to a point)

3. **Monitor Spark UI:**
   - Check for data skew
   - Monitor memory usage
   - Optimize shuffle operations

4. **Iterate on Hyperparameters:**
   - Start with defaults
   - Adjust based on results
   - Document what you tried

5. **Focus on Reasoning:**
   - Reasoning is 45% of your grade!
   - Explain EVERY decision
   - Connect to theory and practical considerations

---

## 📚 RESOURCES

### **Key PySpark Classes:**
- `ALS`: pyspark.ml.recommendation.ALS
- `RankingEvaluator`: pyspark.ml.evaluation.RankingEvaluator
- `StringIndexer`: pyspark.ml.feature.StringIndexer

### **Important Concepts:**
- Collaborative Filtering
- Matrix Factorization
- Implicit Feedback
- Cold Start Problem
- Ranking Metrics

### **Assignment Files:**
- Data: `/data/msd/tasteprofile/triplets.tsv`
- Reference: `reference/SongRecommendations.ipynb` (ywa286's work)
- Your notebook: Create new one for your implementation

---

## ✅ SUCCESS CHECKLIST

**Data Exploration (Q1):**
- [ ] Load and cache triplets data
- [ ] Calculate unique users/songs
- [ ] Analyze most active user
- [ ] Calculate play count statistics
- [ ] Create distribution visualizations
- [ ] Discuss sparsity and challenges

**Collaborative Filtering (Q2):**
- [ ] Filter songs and users (with reasoning)
- [ ] String index user_id and song_id
- [ ] Stratified train-test split per user
- [ ] Train ALS with implicit feedback
- [ ] Generate sample recommendations
- [ ] Manually inspect quality
- [ ] Calculate Precision@K, MAP@K, NDCG@K
- [ ] **BONUS:** Try explicit feedback
- [ ] **BONUS:** Compare implicit vs explicit
- [ ] **BONUS:** Hyperparameter tuning
- [ ] Discuss results and limitations
- [ ] Write conclusions

**Documentation:**
- [ ] Clear markdown explanations
- [ ] Code comments
- [ ] Reasoning for all decisions
- [ ] Tables summarizing results
- [ ] Visualizations with labels
- [ ] Conclusion with recommendations

---

## 🎓 FINAL THOUGHTS

**The Big Picture:**
You're building a **production-grade recommendation system** similar to what Spotify uses. This involves:
1. Understanding massive, sparse data
2. Preparing data efficiently (filtering, indexing)
3. Training scalable ML models (ALS)
4. Evaluating with proper metrics (Precision@K, MAP, NDCG)
5. Interpreting results critically
6. Making informed recommendations

**Success = Code + Analysis + Reasoning**

Good luck! 🚀
