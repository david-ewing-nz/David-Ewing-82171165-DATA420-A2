# DATA420 ASSIGNMENT 2 - COMPLETE EXECUTION PATH
## Visual Roadmap: All Tasks from Start to Finish

**Student:** dew59 (David Ewing)  
**Date:** October 8, 2025  
**Status Legend:** ✅ Complete | ⏳ In Progress | ❌ Not Started | 📝 Report Writing | 💻 Coding

---

## 📊 OVERALL ASSIGNMENT STRUCTURE

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DATA420 ASSIGNMENT 2                              │
│                 Music Recommendation System                          │
│                                                                      │
│  Three Main Sections + Report Assembly                              │
│                                                                      │
│  1. Data Processing (20%)                                           │
│  2. Audio Similarity (40%)                                          │
│  3. Song Recommendations (40%)                                      │
│  4. Final Report Assembly                                           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🗺️ COMPLETE EXECUTION PATH DIAGRAM

```
════════════════════════════════════════════════════════════════════════
                    PHASE 0: SETUP & PREPARATION
════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────┐
│ ✅ 0.1 Environment Setup                                    [DONE]│
│ 💻 - Clone repository                                             │
│ 💻 - Set up Spark cluster connection                             │
│ 💻 - Configure WASBS paths                                        │
│ 💻 - Test Spark session                                           │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 0.2 Reference Analysis                                   [DONE]│
│ 📝 - Analyze ywa286's notebooks                                   │
│ 📝 - Identify gaps and missing work                               │
│ 📝 - Create comprehensive analysis document                       │
│ 📝 - Understand grading rubric                                    │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 0.3 Planning Documents Created                           [DONE]│
│ 📝 - COMPREHENSIVE_ANALYSIS_ywa286_work.md                        │
│ 📝 - PROCESSING_Q2_COLUMN_NAMING_PLAN.md                          │
│ 📝 - SONG_RECOMMENDATIONS_OVERVIEW.md                             │
│ 📝 - ASSIGNMENT_EXECUTION_PATH.md (this document)                 │
└──────────────────────────────────────────────────────────────────┘


════════════════════════════════════════════════════════════════════════
                 PHASE 1: DATA PROCESSING SECTION (20%)
════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────┐
│ ✅ 1.1 Q1: Exploring Dataset in High-Level                  [DONE]│
│ 💻 Task: Get overview of MSD dataset structure                    │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ✅ 1.1a: Generate directory tree structure                        │
│ ✅ 1.1b: Calculate file sizes and row counts                      │
│ ✅ 1.1c: Create summary statistics table                          │
│                                                                   │
│ Deliverables:                                                     │
│ ✅ - Directory tree visualization                                 │
│ ✅ - file_info.txt with sizes/counts                              │
│ ✅ - Summary table in notebook                                    │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ✅ - Markdown description of dataset structure                    │
│ ✅ - Observations about data organization                         │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ⏳ 1.2 Q2a: Load Audio Feature Attributes              [IN PROGRESS]│
│ 💻 Task: Read attribute files and understand schemas              │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ✅ 2.2a: Create generate_schema() function                        │
│ ❌ 2.2b: Load all 13 attribute files                              │
│ ❌ 2.2c: Display sample schemas                                   │
│ ❌ 2.2d: Count columns per dataset                                │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain attribute file format                                │
│ ❌ - Discuss schema generation approach                           │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 1.3 Q2b: Create StructType Automatically              [TO DO]  │
│ 💻 Task: Automated schema creation from attributes                │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.3a: Implement type mapping (string/real/numeric)             │
│ ❌ 2.3b: Test schema generation on sample dataset                 │
│ ❌ 2.3c: Verify all 13 datasets                                   │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain type mapping logic                                   │
│ ❌ - Show example schema output                                   │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 1.4 Q2c: Column Naming Discussion                     [TO DO]  │
│ 📝 Task: Analyze advantages/disadvantages of column names         │
├──────────────────────────────────────────────────────────────────┤
│ This is PURE REPORT WRITING - No coding required!                │
│                                                                   │
│ 📝 Report Sections to Write:                                      │
│ ❌ 2.4a: Examine actual column names from datasets                │
│ ❌ 2.4b: List advantages (2-3 paragraphs):                        │
│          - Descriptive and self-documenting                       │
│          - Traceable to original research                         │
│          - Prevents ambiguity                                     │
│ ❌ 2.4c: List disadvantages (2-3 paragraphs):                     │
│          - Too long for practical use                             │
│          - Not ML-friendly                                        │
│          - Collision risk when merging                            │
│          - Inconsistent naming conventions                        │
│ ❌ 2.4d: Conclusion paragraph                                     │
│          - Need systematic renaming for ML work                   │
│                                                                   │
│ Supporting Code (just for examples):                              │
│ ❌ - Display sample column names from 2-3 datasets                │
│ ❌ - Check for column name collisions                             │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 1.5 Q2d: Systematic Column Renaming                   [TO DO]  │
│ 💻 Task: Develop and implement renaming convention                │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.5a: Design naming convention (prefix_feature)                │
│ ❌ 2.5b: Create dataset prefix mapping                            │
│ ❌ 2.5c: Implement rename_audio_columns() function                │
│ ❌ 2.5d: Test on sample dataset (show before/after)               │
│ ❌ 2.5e: Create column mapping documentation table                │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain chosen naming convention                             │
│ ❌ - Justify design decisions                                     │
│ ❌ - Show example transformations                                 │
│ ❌ - Reference mapping table in supplementary                     │
│                                                                   │
│ Deliverables:                                                     │
│ ❌ - rename_audio_columns() function                              │
│ ❌ - column_name_mapping.csv (supplementary)                      │
│ ❌ - Before/after comparison table                                │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 1.6 Processing Section - Report Assembly             [TO DO]  │
│ 📝 Task: Finalize all Processing markdown and explanations        │
├──────────────────────────────────────────────────────────────────┤
│ Report Components:                                                │
│ ❌ - Introduction to Processing section                           │
│ ❌ - Q1 observations and insights                                 │
│ ❌ - Q2 schema generation explanation                             │
│ ❌ - Q2c column naming discussion (CRITICAL - HIGH MARKS)         │
│ ❌ - Q2d renaming strategy rationale                              │
│ ❌ - Processing section conclusion                                │
│                                                                   │
│ Quality Checks:                                                   │
│ ❌ - All code has markdown explanations                           │
│ ❌ - All decisions have reasoning                                 │
│ ❌ - Tables are properly formatted                                │
│ ❌ - Visualizations have captions                                 │
└──────────────────────────────────────────────────────────────────┘


════════════════════════════════════════════════════════════════════════
              PHASE 2: AUDIO SIMILARITY SECTION (40%)
════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────┐
│ ❌ 2.1 Q1a: Load and Merge Audio Features               [TO DO]  │
│ 💻 Task: Load 4 required audio feature datasets                   │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.1a: Load msd-jmir-area-of-moments-all-v1.0                   │
│ ❌ 2.1b: Load msd-jmir-lpc-all-v1.0                               │
│ ❌ 2.1c: Load msd-jmir-spectral-all-all-v1.0                      │
│ ❌ 2.1d: Load msd-marsyas-timbral-v1.0                            │
│ ❌ 2.1e: Rename columns using Q2d function                        │
│ ❌ 2.1f: Merge all datasets on MSD_TRACKID                        │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain dataset selection                                    │
│ ❌ - Show merged schema                                           │
│ ❌ - Report final column count                                    │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 2.2 Q1a: Preprocess Audio Features                   [TO DO]  │
│ 💻 Task: Handle outliers, transform, standardize                  │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.2a: Winsorization (cap outliers at 1st/99th percentile)      │
│ ❌ 2.2b: Log transformation for skewed features                   │
│ ❌ 2.2c: Standardization (StandardScaler)                         │
│ ❌ 2.2d: Generate descriptive statistics                          │
│ ❌ 2.2e: Create box plots for processed features                  │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain preprocessing rationale                              │
│ ❌ - Show before/after statistics                                 │
│ ❌ - Discuss outlier treatment                                    │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 2.3 Q1a: Correlation Analysis                        [TO DO]  │
│ 💻 Task: Identify and handle correlated features                  │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.3a: Calculate correlation matrix                             │
│ ❌ 2.3b: Create correlation heatmap                               │
│ ❌ 2.3c: Identify highly correlated features (>0.9)               │
│ ❌ 2.3d: Remove redundant features                                │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Discuss correlation findings                                 │
│ ❌ - Justify feature removal decisions                            │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 2.4 Q1b: Load and Explore Genre Data                 [TO DO]  │
│ 💻 Task: Load MAGD genre assignments                              │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.4a: Load msd-MAGD-genreAssignment.tsv                        │
│ ❌ 2.4b: Count tracks per genre                                   │
│ ❌ 2.4c: Create genre distribution bar chart                      │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Describe genre distribution                                  │
│ ❌ - Identify class imbalance                                     │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 2.5 Q1c: Merge Audio Features + Genres               [TO DO]  │
│ 💻 Task: Join processed audio with genre labels                   │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.5a: Inner join on MSD_TRACKID                                │
│ ❌ 2.5b: Count resulting rows                                     │
│ ❌ 2.5c: Verify no nulls introduced                               │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Report merge statistics                                      │
│ ❌ - Explain any data loss                                        │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 2.6 Q2: Binary Classification - Electronic Genre     [TO DO]  │
│ 💻 Task: Build binary classifier (Electronic vs Others)           │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.6a: Create binary label (Electronic=1, Others=0)             │
│ ❌ 2.6b: Visualize class distribution                             │
│ ❌ 2.6c: Stratified train-test split (80/20)                      │
│ ❌ 2.6d: Apply combined sampling (address imbalance)              │
│ ❌ 2.6e: Train Logistic Regression                                │
│ ❌ 2.6f: Train Random Forest                                      │
│ ❌ 2.6g: Train Gradient Boosted Trees                             │
│ ❌ 2.6h: Evaluate all models (Accuracy, Precision, Recall, F1)    │
│ ❌ 2.6i: Create confusion matrices                                │
│ ❌ 2.6j: Compare model performance                                │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain binary classification task                           │
│ ❌ - Justify sampling strategy                                    │
│ ❌ - Interpret confusion matrices                                 │
│ ❌ - Compare model strengths/weaknesses                           │
│ ❌ - Select best model with reasoning                             │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 2.7 Q3: Multi-Class Classification - All Genres      [TO DO]  │
│ 💻 Task: Build multi-class classifier (21 genres)                 │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 2.7a: Convert genres to numeric labels (StringIndexer)         │
│ ❌ 2.7b: Visualize multi-class distribution                       │
│ ❌ 2.7c: Stratified train-test split                              │
│ ❌ 2.7d: Apply multi-class balancing                              │
│ ❌ 2.7e: Train Logistic Regression (multinomial)                  │
│ ❌ 2.7f: Train Random Forest                                      │
│ ❌ 2.7g: Train Gradient Boosted Trees                             │
│ ❌ 2.7h: Evaluate with multi-class metrics                        │
│ ❌ 2.7i: Create per-genre performance table                       │
│ ❌ 2.7j: Confusion matrix for all 21 classes                      │
│ ❌ 2.7k: Analyze which genres are hard to classify                │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain multi-class challenge                                │
│ ❌ - Discuss balancing approach                                   │
│ ❌ - Interpret per-genre performance                              │
│ ❌ - Identify confused genre pairs                                │
│ ❌ - Recommend best model                                         │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 2.8 Audio Similarity - Report Assembly               [TO DO]  │
│ 📝 Task: Complete all Audio Similarity explanations               │
├──────────────────────────────────────────────────────────────────┤
│ Report Components:                                                │
│ ❌ - Introduction to Audio Similarity section                     │
│ ❌ - Feature preprocessing rationale (CRITICAL)                   │
│ ❌ - Binary vs multi-class comparison                             │
│ ❌ - Model selection justification (CRITICAL)                     │
│ ❌ - Limitations and future improvements                          │
│ ❌ - Audio Similarity conclusion                                  │
│                                                                   │
│ Quality Checks:                                                   │
│ ❌ - All visualizations labeled and captioned                     │
│ ❌ - All tables have descriptions                                 │
│ ❌ - Model comparisons in summary table                           │
│ ❌ - Strong reasoning for all decisions                           │
└──────────────────────────────────────────────────────────────────┘


════════════════════════════════════════════════════════════════════════
            PHASE 3: SONG RECOMMENDATIONS SECTION (40%)
════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.1 Q1: Taste Data Exploration                       [TO DO]  │
│ 💻 Task: Analyze 48M+ user-song-play triplets                     │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.1a: Load triplets.tsv                                        │
│ ❌ 3.1b: Repartition for optimal parallelism                      │
│ ❌ 3.1c: Cache DataFrame                                          │
│ ❌ 3.1d: Count unique users and songs                             │
│ ❌ 3.1e: Find most active user                                    │
│ ❌ 3.1f: Calculate play count statistics                          │
│ ❌ 3.1g: Compute percentiles (25%, 50%, 75%)                      │
│ ❌ 3.1h: Create song popularity histogram                         │
│ ❌ 3.1i: Create user activity histogram                           │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Describe dataset scale                                       │
│ ❌ - Discuss sparsity challenge (99.99%)                          │
│ ❌ - Explain power law distribution                               │
│ ❌ - Identify cold start problem                                  │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.2 Q2a: Data Filtering                              [TO DO]  │
│ 💻 Task: Remove noise from sparse dataset                         │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.2a: Filter songs with < N plays (e.g., N=8)                  │
│ ❌ 3.2b: Filter users with < M plays (e.g., M=34)                 │
│ ❌ 3.2c: Iteratively re-filter (2-3 passes)                       │
│ ❌ 3.2d: Calculate exclusion statistics                           │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Justify N and M threshold choices (CRITICAL)                 │
│ ❌ - Report % of data excluded                                    │
│ ❌ - Discuss quality vs quantity trade-off                        │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.3 Q2b: String Indexing                             [TO DO]  │
│ 💻 Task: Convert string IDs to integers for ALS                   │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.3a: StringIndexer for user_id → user (int)                   │
│ ❌ 3.3b: StringIndexer for song_id → song (int)                   │
│ ❌ 3.3c: Transform filtered DataFrame                             │
│ ❌ 3.3d: Save mapping for reverse lookup                          │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain why ALS needs integer IDs                            │
│ ❌ - Show transformed schema                                      │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.4 Q2c: Stratified Train-Test Split                 [TO DO]  │
│ 💻 Task: Per-user 80/20 split                                     │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.4a: Assign random rank within each user                      │
│ ❌ 3.4b: Calculate 80% split point per user                       │
│ ❌ 3.4c: Create train_df and test_df                              │
│ ❌ 3.4d: Verify every user in both sets                           │
│ ❌ 3.4e: Print split statistics                                   │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain why per-user split needed                            │
│ ❌ - Report train/test sizes                                      │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.5 Q2d: Train ALS with Implicit Feedback            [TO DO]  │
│ 💻 Task: Build collaborative filtering model                      │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.5a: Convert play_count to implicit feedback (binary)         │
│ ❌ 3.5b: Initialize ALS with implicitPrefs=True                   │
│ ❌ 3.5c: Set hyperparameters (rank, regParam, maxIter)            │
│ ❌ 3.5d: Fit model on train_df                                    │
│ ❌ 3.5e: Cache model for reuse                                    │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain implicit vs explicit feedback (CRITICAL)             │
│ ❌ - Justify hyperparameter choices                               │
│ ❌ - Describe ALS algorithm briefly                               │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.6 Q2e: Generate Sample Recommendations             [TO DO]  │
│ 💻 Task: Manual inspection of recommendation quality              │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.6a: Select 3-5 sample users from test set                    │
│ ❌ 3.6b: Generate top-10 recommendations for each                 │
│ ❌ 3.6c: Get actual test songs for each user                      │
│ ❌ 3.6d: Calculate Precision@10 per user                          │
│ ❌ 3.6e: Display comparison table                                 │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Show sample recommendations                                  │
│ ❌ - Discuss quality observations                                 │
│ ❌ - Explain why Precision is low                                 │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.7 Q2f: Evaluate with Ranking Metrics               [TO DO]  │
│ 💻 Task: Formal evaluation with Precision@K, MAP@K, NDCG@K        │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.7a: Generate recommendations for all users                   │
│ ❌ 3.7b: Collect relevant items from test set                     │
│ ❌ 3.7c: Merge recommendations and relevant items                 │
│ ❌ 3.7d: Calculate Precision@10                                   │
│ ❌ 3.7e: Calculate MAP@10                                         │
│ ❌ 3.7f: Calculate NDCG@10                                        │
│ ❌ 3.7g: Create metrics summary table                             │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Explain each ranking metric (CRITICAL)                       │
│ ❌ - Interpret results                                            │
│ ❌ - Discuss why metrics are low for sparse data                  │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.8 BONUS: Train ALS with Explicit Feedback          [BONUS]  │
│ 💻 Task: Compare implicit vs explicit approaches                  │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.8a: Use play_count as explicit ratings                       │
│ ❌ 3.8b: Initialize ALS with implicitPrefs=False                  │
│ ❌ 3.8c: Train explicit feedback model                            │
│ ❌ 3.8d: Evaluate with same metrics                               │
│ ❌ 3.8e: Create comparison table                                  │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Compare implicit vs explicit results                         │
│ ❌ - Discuss which works better and why                           │
│ ❌ - Recommend best approach                                      │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 3.9 BONUS: Hyperparameter Tuning                     [BONUS]  │
│ 💻 Task: Optimize ALS parameters                                  │
├──────────────────────────────────────────────────────────────────┤
│ Subtasks:                                                         │
│ ❌ 3.9a: Try different rank values (5, 10, 20)                    │
│ ❌ 3.9b: Try different regParam values (0.01, 0.1, 1.0)           │
│ ❌ 3.9c: Try different maxIter values (5, 10, 20)                 │
│ ❌ 3.9d: Create hyperparameter comparison table                   │
│ ❌ 3.9e: Identify best configuration                              │
│                                                                   │
│ 📝 Report Writing:                                                │
│ ❌ - Show hyperparameter sensitivity                              │
│ ❌ - Recommend optimal settings                                   │
│ ❌ - Discuss trade-offs (accuracy vs speed)                       │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 3.10 Recommendations - Report Assembly               [TO DO]  │
│ 📝 Task: Complete all Recommendations section explanations        │
├──────────────────────────────────────────────────────────────────┤
│ Report Components:                                                │
│ ❌ - Introduction to collaborative filtering                      │
│ ❌ - Why ALS for this problem                                     │
│ ❌ - Implicit vs explicit discussion (CRITICAL)                   │
│ ❌ - Hyperparameter choices justification                         │
│ ❌ - Metric interpretations                                       │
│ ❌ - Limitations and challenges                                   │
│ ❌ - Future improvements suggestions                              │
│ ❌ - Recommendations section conclusion                           │
│                                                                   │
│ Quality Checks:                                                   │
│ ❌ - All decisions have strong reasoning                          │
│ ❌ - Metrics comparison table                                     │
│ ❌ - Visualizations properly labeled                              │
│ ❌ - Discussion of practical implications                         │
└──────────────────────────────────────────────────────────────────┘


════════════════════════════════════════════════════════════════════════
                 PHASE 4: FINAL REPORT ASSEMBLY
════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────┐
│ 📝 4.1 Title Page and Abstract                          [TO DO]  │
│ 📝 PURE REPORT WRITING - No coding                                │
├──────────────────────────────────────────────────────────────────┤
│ Components:                                                       │
│ ❌ 4.1a: Title page with course info                              │
│ ❌ 4.1b: Abstract (150-250 words)                                 │
│          - Overview of assignment                                 │
│          - Key findings summary                                   │
│          - Main results                                           │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 4.2 Introduction Section                             [TO DO]  │
│ 📝 PURE REPORT WRITING - No coding                                │
├──────────────────────────────────────────────────────────────────┤
│ Components:                                                       │
│ ❌ 4.2a: Assignment context and objectives                        │
│ ❌ 4.2b: Million Song Dataset overview                            │
│ ❌ 4.2c: Problem statement                                        │
│ ❌ 4.2d: Report structure overview                                │
│                                                                   │
│ Length: 1-2 pages                                                 │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 4.3 Methodology Section                              [TO DO]  │
│ 📝 PURE REPORT WRITING - No coding                                │
├──────────────────────────────────────────────────────────────────┤
│ Components:                                                       │
│ ❌ 4.3a: Overall approach description                             │
│ ❌ 4.3b: Tools and technologies (Spark, PySpark)                  │
│ ❌ 4.3c: Data preprocessing methodology                           │
│ ❌ 4.3d: Classification methodology                               │
│ ❌ 4.3e: Recommendation system methodology                        │
│                                                                   │
│ Length: 2-3 pages                                                 │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 4.4 Processing Section (Finalize)                       [DONE]│
│ 📝 Review and polish existing work                                │
├──────────────────────────────────────────────────────────────────┤
│ Review Checklist:                                                 │
│ ❌ 4.4a: Q1 explanations complete                                 │
│ ❌ 4.4b: Q2 explanations complete                                 │
│ ❌ 4.4c: All code commented                                       │
│ ❌ 4.4d: All tables formatted                                     │
│ ❌ 4.4e: Section transitions smooth                               │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 4.5 Audio Similarity Section (Finalize)              [TO DO]  │
│ 📝 Review and polish after completion                             │
├──────────────────────────────────────────────────────────────────┤
│ Review Checklist:                                                 │
│ ❌ 4.5a: All Q1 explanations complete                             │
│ ❌ 4.5b: Q2 binary classification complete                        │
│ ❌ 4.5c: Q3 multi-class classification complete                   │
│ ❌ 4.5d: Model comparisons clear                                  │
│ ❌ 4.5e: Confusion matrices labeled                               │
│ ❌ 4.5f: Strong conclusions                                       │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ❌ 4.6 Recommendations Section (Finalize)               [TO DO]  │
│ 📝 Review and polish after completion                             │
├──────────────────────────────────────────────────────────────────┤
│ Review Checklist:                                                 │
│ ❌ 4.6a: Q1 exploration complete                                  │
│ ❌ 4.6b: Q2 ALS implementation complete                           │
│ ❌ 4.6c: Implicit vs explicit comparison                          │
│ ❌ 4.6d: Ranking metrics explained                                │
│ ❌ 4.6e: Strong reasoning throughout                              │
│ ❌ 4.6f: Limitations discussed                                    │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 4.7 Results and Discussion                           [TO DO]  │
│ 📝 PURE REPORT WRITING - No coding                                │
├──────────────────────────────────────────────────────────────────┤
│ Components:                                                       │
│ ❌ 4.7a: Key findings from Processing                             │
│ ❌ 4.7b: Classification results summary                           │
│ ❌ 4.7c: Recommendation system results                            │
│ ❌ 4.7d: Cross-section insights                                   │
│ ❌ 4.7e: Comparison with expectations                             │
│ ❌ 4.7f: Discussion of implications                               │
│                                                                   │
│ Length: 3-4 pages                                                 │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 4.8 Conclusion                                       [TO DO]  │
│ 📝 PURE REPORT WRITING - No coding                                │
├──────────────────────────────────────────────────────────────────┤
│ Components:                                                       │
│ ❌ 4.8a: Summary of work completed                                │
│ ❌ 4.8b: Key achievements                                         │
│ ❌ 4.8c: Main limitations                                         │
│ ❌ 4.8d: Future work recommendations                              │
│ ❌ 4.8e: Final thoughts                                           │
│                                                                   │
│ Length: 1-2 pages                                                 │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 4.9 Supplementary Materials Organization             [TO DO]  │
│ 📝 File organization and documentation                            │
├──────────────────────────────────────────────────────────────────┤
│ Organize:                                                         │
│ ❌ 4.9a: All PNG visualizations                                   │
│ ❌ 4.9b: Column name mapping CSV                                  │
│ ❌ 4.9c: Model performance tables                                 │
│ ❌ 4.9d: Additional analysis outputs                              │
│ ❌ 4.9e: Create supplementary index file                          │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ 📝 4.10 Final Quality Assurance                         [TO DO]  │
│ 📝 Comprehensive review and polish                                │
├──────────────────────────────────────────────────────────────────┤
│ Final Checks:                                                     │
│ ❌ 4.10a: Spell check entire document                             │
│ ❌ 4.10b: Grammar review                                          │
│ ❌ 4.10c: Consistent formatting                                   │
│ ❌ 4.10d: All figures referenced in text                          │
│ ❌ 4.10e: All tables referenced in text                           │
│ ❌ 4.10f: Page numbers correct                                    │
│ ❌ 4.10g: Table of contents updated                               │
│ ❌ 4.10h: All code runs without errors                            │
│ ❌ 4.10i: Export to PDF                                           │
│ ❌ 4.10j: Verify file size < submission limit                     │
└──────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 4.11 SUBMISSION                                      [FINAL]  │
│ 📦 Submit all required files                                      │
├──────────────────────────────────────────────────────────────────┤
│ Submission Package:                                               │
│ ❌ - Processing notebook (.ipynb)                                 │
│ ❌ - Audio Similarity notebook (.ipynb)                           │
│ ❌ - Song Recommendations notebook (.ipynb)                       │
│ ❌ - Final report (PDF)                                           │
│ ❌ - Supplementary materials folder                               │
│ ❌ - README or submission notes                                   │
│                                                                   │
│ ✅ ASSIGNMENT COMPLETE! 🎉                                        │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📊 PROGRESS SUMMARY

### **Current Status by Section:**

| Section | Total Tasks | Completed | In Progress | Not Started | % Complete |
|---------|-------------|-----------|-------------|-------------|------------|
| **0. Setup** | 3 | 3 | 0 | 0 | **100%** ✅ |
| **1. Processing** | 6 | 1 | 1 | 4 | **17%** ⏳ |
| **2. Audio Similarity** | 8 | 0 | 0 | 8 | **0%** ❌ |
| **3. Recommendations** | 10 | 0 | 0 | 10 | **0%** ❌ |
| **4. Final Report** | 11 | 0 | 0 | 11 | **0%** ❌ |
| **TOTAL** | **38** | **4** | **1** | **33** | **~11%** |

---

## 🎯 CRITICAL PATH (Highest Priority)

### **Must Complete for Minimum Viable Assignment:**

1. **Processing Q2c & Q2d** (Column naming) - **CRITICAL** for reasoning marks
2. **Audio Similarity Q1** (Feature preprocessing) - Foundation for classification
3. **Audio Similarity Q2** (Binary classification) - Core requirement
4. **Audio Similarity Q3** (Multi-class) - Core requirement
5. **Recommendations Q2d-f** (ALS with implicit) - Core requirement
6. **Final Report Assembly** - Tie everything together

### **Bonus Tasks (If Time Permits):**

- Recommendations: Explicit feedback comparison
- Recommendations: Hyperparameter tuning
- Additional visualizations throughout
- Deeper analysis and insights

---

## ⏱️ TIME ESTIMATES

### **Rough Time Allocation:**

| Phase | Estimated Hours | Priority |
|-------|----------------|----------|
| Processing Q2c-d | 3-4 hours | 🔥 HIGH |
| Audio Similarity | 10-12 hours | 🔥 HIGH |
| Recommendations | 10-12 hours | 🔥 HIGH |
| Report Writing | 6-8 hours | 🔥 HIGH |
| Polish & QA | 2-3 hours | ⚡ MEDIUM |
| Bonus Tasks | 4-6 hours | ⭐ OPTIONAL |
| **TOTAL** | **35-45 hours** | |

---

## 📝 CODING vs REPORT WRITING BREAKDOWN

### **Pure Coding Tasks:** (~60% of work)
- Data loading and preprocessing
- Model training and evaluation
- Metric calculations
- Visualization generation
- Function implementations

### **Pure Report Writing:** (~40% of work)
- Section introductions
- Methodology explanations
- Result interpretations
- Discussion sections
- Conclusions
- Abstract and summary

### **Mixed Tasks:** (Both coding + writing)
- Every question requires:
  1. **Code:** Implementation
  2. **Report:** Explanation + reasoning + interpretation

---

## 🎓 GRADING WEIGHT REMINDER

**From Rubric:**
- **Reasoning:** 45% ← Most important! Explain EVERYTHING
- **Answers:** 14%
- **Visualizations:** 11%
- **Writing:** 11%
- **Coding:** 10%
- **Tables:** 9%

**Key Insight:** Code alone = 10%. Code + Reasoning = 55%!

---

## ✅ NEXT IMMEDIATE STEPS

1. **Complete Processing Q2c** (Column naming discussion) - 1-2 hours
2. **Complete Processing Q2d** (Systematic renaming) - 1-2 hours
3. **Start Audio Similarity Q1a** (Load and merge features) - 2-3 hours
4. **Continue through Audio Similarity** - Follow diagram
5. **Move to Recommendations** - Follow diagram
6. **Final Report Assembly** - Follow diagram

---

**Good luck with your assignment! Follow this roadmap and you'll have a comprehensive, high-quality submission! 🚀**
