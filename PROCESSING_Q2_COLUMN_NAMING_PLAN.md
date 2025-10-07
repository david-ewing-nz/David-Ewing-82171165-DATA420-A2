# PROCESSING Q2(c) & Q2(d): Column Naming Strategy
## Complete Analysis and Implementation Plan

**Date:** October 8, 2025  
**Student:** dew59 (David Ewing)  
**Objective:** Answer Q2(c) and Q2(d) about audio feature column naming

---

## UNDERSTANDING THE QUESTION

### Q2(c): Are the audio feature attribute names convenient to use?
**What they're asking:**
- Evaluate the ORIGINAL column names from the audio feature datasets
- Discuss advantages and disadvantages
- Think about using them in ML models (feature selection, debugging, reporting)

### Q2(d): Develop a systematic column renaming strategy
**What they're asking:**
- Create a NAMING CONVENTION for all audio features
- Handle name collisions when merging datasets
- Make names: SHORT, INTUITIVE, EASY TO READ
- Demonstrate HOW you would rename (don't actually merge all datasets)

---

## THE DATASETS TO CONSIDER

### Audio Feature Datasets (from reference):
Based on ywa286's work and the assignment, there are **13 audio feature datasets**:

1. **msd-jmir-area-of-moments-all-v1.0** (~20 features)
2. **msd-jmir-lpc-all-v1.0** (20 features - Linear Predictive Coding)
3. **msd-jmir-methods-of-moments-all-v1.0** (~10 features)
4. **msd-jmir-mfcc-all-v1.0** (~26 features - Mel Frequency Cepstral Coefficients)
5. **msd-jmir-spectral-all-v1.0** (~16 features)
6. **msd-jmir-spectral-derivatives-all-v1.0** (~16 features)
7. **msd-marsyas-timbral-v1.0** (~124 features)
8. **msd-mvd-v1.0** (~420 features - Modulation Frequency Variance)
9. **msd-rh-v1.0** (~60 features - Rhythm Histograms)
10. **msd-rp-v1.0** (~1440 features - Rhythm Patterns)
11. **msd-ssd-v1.0** (~168 features - Statistical Spectrum Descriptors)
12. **msd-trh-v1.0** (~420 features - Temporal Rhythm Histograms)
13. **msd-tssd-v1.0** (~1176 features - Temporal Statistical Spectrum Descriptors)

**TOTAL: ~2,916 audio features across all datasets!**

### Required for Assignment (Audio Similarity Q1):
You only need to load and merge **4 specific datasets**:
- msd-jmir-area-of-moments-all-v1.0
- msd-jmir-lpc-all-v1.0
- msd-jmir-spectral-all-all-v1.0 (note: "all-all" in name)
- msd-marsyas-timbral-v1.0

---

## STEP 1: EXAMINE ORIGINAL COLUMN NAMES

### What We Need to See:
1. **Load each attribute file** (the .attributes.csv files)
2. **Examine actual column names** - are they descriptive?
3. **Check for patterns** - do they have consistent naming?
4. **Look for collisions** - do multiple datasets use the same column name?

### Example Column Names (from ARFF format):

**msd-jmir-area-of-moments-all-v1.0:**
```
MSD_TRACKID
Method_of_Moments_Overall_Standard_Deviation_1
Method_of_Moments_Overall_Standard_Deviation_2
Area_Method_of_Moments_Overall_Average_1
Area_Method_of_Moments_Overall_Average_2
...
```

**msd-jmir-lpc-all-v1.0:**
```
MSD_TRACKID
LPC_Overall_Standard_Deviation_1
LPC_Overall_Standard_Deviation_2
LPC_Overall_Average_1
...
```

**msd-marsyas-timbral-v1.0:**
```
MSD_TRACKID
MFCC_0_Mean
MFCC_1_Mean
MFCC_2_Mean
Spectral_Centroid_Mean
Spectral_Rolloff_Mean
Spectral_Flux_Mean
Zero_Crossings_Mean
...
```

### Observations:
- ✓ Column names are DESCRIPTIVE (you can understand what they measure)
- ✓ Include statistical aggregations (Mean, StdDev, Average)
- ✗ Names are VERY LONG (50-80 characters common)
- ✗ Use underscores and mixed case (not consistent style)
- ✗ Could have collisions (multiple datasets might use "Mean", "StdDev")
- ✗ Hard to type/reference in code

---

## Q2(c) ANSWER: ADVANTAGES AND DISADVANTAGES

### ✅ ADVANTAGES of Original Column Names:

1. **Self-Documenting:**
   - Names clearly describe the feature (e.g., "Spectral_Centroid_Mean")
   - Include statistical aggregation method (Mean, StdDev)
   - No need to constantly refer to documentation

2. **Traceability:**
   - Can trace back to original audio processing method
   - Useful for research and reproducibility
   - Helps understand feature engineering pipeline

3. **Prevents Ambiguity:**
   - "MFCC_0_Mean" is clear about which coefficient and aggregation
   - Reduces confusion about what the column represents

### ❌ DISADVANTAGES of Original Column Names:

1. **Too Long for Practical Use:**
   - Hard to type: `Area_Method_of_Moments_Overall_Standard_Deviation_1`
   - Error-prone when writing code
   - Makes code less readable with long feature lists

2. **Not ML-Friendly:**
   - Some ML libraries have column name length limits
   - Hard to display in tables, plots, feature importance charts
   - Difficult to use in SQL queries or Spark SQL

3. **Collision Risk When Merging:**
   - Multiple datasets might use "Mean", "StdDev" suffixes
   - Without dataset prefix, you can't tell which dataset a feature came from
   - Risk of overwriting columns during joins

4. **Inconsistent Naming Conventions:**
   - Mix of CamelCase and Underscores
   - Some use "Average", others use "Mean"
   - Inconsistent abbreviations

5. **Poor for Feature Selection:**
   - Hard to reference in feature importance analysis
   - Difficult to create feature groups programmatically
   - Challenging to visualize in correlation heatmaps

6. **Not Suitable for LaTeX/Reports:**
   - Column names too long for table headers
   - Need abbreviations anyway for publication
   - Hard to format in academic writing

---

## Q2(d) ANSWER: SYSTEMATIC RENAMING STRATEGY

### PROPOSED NAMING CONVENTION:

**Format:** `{dataset_prefix}_{feature_number}` or `{dataset_prefix}_{feature_desc}`

### Strategy Options:

#### **Option A: Dataset Prefix + Sequential Number**
```python
# msd-jmir-area-of-moments-all-v1.0 → aom_001, aom_002, ...
# msd-jmir-lpc-all-v1.0 → lpc_001, lpc_002, ...
# msd-jmir-spectral-all-v1.0 → spec_001, spec_002, ...
# msd-marsyas-timbral-v1.0 → timb_001, timb_002, ...
```

**Pros:**
- ✓ Very short (8 characters max)
- ✓ Easy to type and reference
- ✓ Guaranteed no collisions
- ✓ Clean for tables and plots

**Cons:**
- ✗ Lost semantic meaning (need lookup table)
- ✗ Hard to interpret feature importance
- ✗ Need separate documentation

#### **Option B: Dataset Prefix + Abbreviated Description**
```python
# Area of Moments Overall Std Dev 1 → aom_ovr_std_1
# LPC Overall Average 5 → lpc_ovr_avg_5
# MFCC 0 Mean → timb_mfcc0_m
# Spectral Centroid Mean → spec_cent_m
```

**Pros:**
- ✓ Retains semantic meaning
- ✓ Still relatively short (15-20 chars)
- ✓ Interpretable feature names
- ✓ Good balance of brevity and clarity

**Cons:**
- ~ Need consistent abbreviation rules
- ~ Slightly longer than Option A

#### **Option C: Hybrid (Recommended)**
```python
# For well-known features: use abbreviation
timb_mfcc_0_m      # MFCC 0 Mean
timb_centroid_m    # Spectral Centroid Mean
timb_rolloff_m     # Spectral Rolloff Mean

# For generic/numbered features: use sequential
aom_f01, aom_f02   # Area of Moments feature 1, 2
lpc_f01, lpc_f02   # LPC feature 1, 2
```

**Pros:**
- ✓ Best of both worlds
- ✓ Important features are interpretable
- ✓ Generic features are concise
- ✓ Flexible approach

---

## IMPLEMENTATION PLAN

### Step 1: Create Dataset Prefix Mapping
```python
DATASET_PREFIXES = {
    'msd-jmir-area-of-moments-all-v1.0': 'aom',
    'msd-jmir-lpc-all-v1.0': 'lpc',
    'msd-jmir-spectral-all-v1.0': 'spec',
    'msd-marsyas-timbral-v1.0': 'timb',
    'msd-jmir-methods-of-moments-all-v1.0': 'mom',
    'msd-jmir-mfcc-all-v1.0': 'mfcc',
    'msd-jmir-spectral-derivatives-all-v1.0': 'sder',
    'msd-mvd-v1.0': 'mvd',
    'msd-rh-v1.0': 'rh',
    'msd-rp-v1.0': 'rp',
    'msd-ssd-v1.0': 'ssd',
    'msd-trh-v1.0': 'trh',
    'msd-tssd-v1.0': 'tssd'
}
```

### Step 2: Create Abbreviation Rules
```python
ABBREVIATIONS = {
    'Mean': 'm',
    'Standard_Deviation': 'std',
    'Average': 'avg',
    'Overall': 'ovr',
    'Centroid': 'cent',
    'Rolloff': 'roll',
    'Method_of_Moments': 'mom',
    'Spectral': 'spec',
    'Temporal': 'temp',
    # ... add more as needed
}
```

### Step 3: Create Renaming Function
```python
def rename_audio_columns(df, dataset_name):
    """
    Rename columns in audio feature dataset with systematic convention.
    
    Args:
        df: Spark DataFrame with original column names
        dataset_name: Name of the dataset (e.g., 'msd-jmir-lpc-all-v1.0')
    
    Returns:
        DataFrame with renamed columns
    """
    prefix = DATASET_PREFIXES.get(dataset_name, 'unk')
    
    # Keep MSD_TRACKID as-is (it's the join key)
    new_column_names = ['MSD_TRACKID']
    
    # Rename feature columns
    for i, col_name in enumerate(df.columns[1:], 1):
        # Option 1: Simple sequential numbering
        new_name = f"{prefix}_f{i:03d}"
        
        # Option 2: Abbreviated description (if you want semantic names)
        # new_name = abbreviate_column_name(col_name, prefix)
        
        new_column_names.append(new_name)
    
    # Apply renaming
    return df.toDF(*new_column_names)
```

### Step 4: Create Mapping Table for Documentation
```python
def create_column_mapping_table(df, dataset_name):
    """
    Create a mapping table documenting original → new column names.
    Save this for reference in your report!
    """
    prefix = DATASET_PREFIXES.get(dataset_name, 'unk')
    
    mapping = []
    for i, orig_name in enumerate(df.columns[1:], 1):
        new_name = f"{prefix}_f{i:03d}"
        mapping.append({
            'dataset': dataset_name,
            'original_name': orig_name,
            'new_name': new_name,
            'description': extract_description(orig_name)
        })
    
    return pd.DataFrame(mapping)
```

---

## WHAT WE NEED TO DO FIRST

### Priority 1: Examine Actual Column Names
**Let's load one attribute file and see the real column names:**

```python
# Load the attribute file for one dataset
attr_path = f"{WASBS_DATA}/audio/attributes/msd-jmir-lpc-all-v1.0.attributes.csv"
attr_rdd = spark.sparkContext.textFile(attr_path)
attr_lines = attr_rdd.collect()

# Print first 10 column names
for line in attr_lines[:10]:
    print(line)
```

This will show us:
- Exact column name format
- Length of names
- Naming patterns
- Any special characters

### Priority 2: Check for Name Collisions
**Load attribute files for all 4 required datasets and check overlaps:**

```python
datasets = [
    'msd-jmir-area-of-moments-all-v1.0',
    'msd-jmir-lpc-all-v1.0',
    'msd-jmir-spectral-all-v1.0',
    'msd-marsyas-timbral-v1.0'
]

all_columns = {}
for ds in datasets:
    attr_path = f"{WASBS_DATA}/audio/attributes/{ds}.attributes.csv"
    attr_rdd = spark.sparkContext.textFile(attr_path)
    columns = [line.split(',')[0] for line in attr_rdd.collect()]
    all_columns[ds] = columns[1:]  # Skip MSD_TRACKID
    
# Check for collisions
from collections import Counter
all_col_names = []
for cols in all_columns.values():
    all_col_names.extend(cols)
    
collisions = {name: count for name, count in Counter(all_col_names).items() if count > 1}
print("Column name collisions:", collisions)
```

### Priority 3: Design Naming Convention
**Based on what we see in steps 1-2, choose:**
- Option A (sequential): `aom_001, lpc_001, ...`
- Option B (abbreviated): `aom_ovr_std_1, lpc_ovr_avg_5, ...`
- Option C (hybrid): Mix of both

### Priority 4: Implement Renaming Function
**Create and test the function on one dataset:**

```python
# Load one dataset
lpc_df = spark.read.csv(
    f"{WASBS_DATA}/audio/features/msd-jmir-lpc-all-v1.0.csv",
    schema=generate_schema('msd-jmir-lpc-all-v1.0'),
    header=False
)

# Rename columns
lpc_renamed = rename_audio_columns(lpc_df, 'msd-jmir-lpc-all-v1.0')

# Show before/after
print("Original columns:", lpc_df.columns[:5])
print("Renamed columns:", lpc_renamed.columns[:5])
```

### Priority 5: Create Mapping Documentation
**Generate the mapping table for your report:**

```python
# Create mapping table
mapping_df = create_column_mapping_table(lpc_df, 'msd-jmir-lpc-all-v1.0')

# Save to CSV for report
mapping_df.to_csv('../report/supplementary/column_name_mapping.csv', index=False)

# Display in notebook
display(mapping_df.head(20))
```

---

## DELIVERABLES FOR REPORT

### For Q2(c):
**Write 1-2 paragraphs discussing:**
1. Original column names are descriptive but too long (give examples)
2. Advantages: self-documenting, traceable, prevents ambiguity
3. Disadvantages: hard to type, not ML-friendly, collision risk, poor for visualization
4. Conclusion: Need systematic renaming for practical ML work

### For Q2(d):
**Write 1-2 paragraphs + code explaining:**
1. Your chosen naming convention (e.g., Option C hybrid)
2. Rationale: balance between brevity and interpretability
3. Implementation: show `rename_audio_columns()` function
4. Documentation: reference the mapping table in supplementary materials
5. Example: show before/after column names for one dataset

### Supplementary Materials:
1. **column_name_mapping.csv** - Full mapping table for all datasets
2. **Column renaming code** in your Processing notebook
3. **Helper function** for future use in Audio Similarity section

---

## NEXT STEPS FOR YOU

1. **Open your 20251008C notebook**
2. **Add cells to examine column names** (Priority 1)
3. **Check for collisions** (Priority 2)
4. **Decide on naming convention** (Priority 3)
5. **Implement renaming function** (Priority 4)
6. **Generate mapping table** (Priority 5)
7. **Write Q2(c) discussion** (advantages/disadvantages)
8. **Write Q2(d) explanation** (your systematic approach)

**Ready to start? Let me know which dataset you'd like to examine first, and I'll help you write the code!**
