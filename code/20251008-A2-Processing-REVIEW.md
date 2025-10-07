# 20251008-A2-Processing.ipynb - REVIEW DOCUMENT

**Date**: 2025-10-08  
**Created By**: GitHub Copilot (Agent)  
**For Review By**: davide (David Ewing - 82171165)

---

## CHANGES SUMMARY

### ✅ STEP 1: Notebook Copied
- **Source**: `20251006-A2-Processing.ipynb`
- **Destination**: `20251008-A2-Processing.ipynb`
- **Status**: Complete

### ✅ STEP 2: Imports (No Changes Required)
- **Cell**: Cell 5 (id: #VSC-fdb25811) - "# My Imports"
- **Finding**: `import subprocess` already present on line 210
- **Action**: No changes made - existing imports maintained

### ✅ STEP 3: Helper Functions Added
- **Cell**: Cell 8 (id: #VSC-07fb032c) - "# HELPER AND DIAGNOSTIC FUNCTIONS"
- **Functions Added**:
  1. `build_directory_tree_df(root_path=None, max_depth=3)`
  2. `save_tree_to_parquet(df, output_path)`
  3. `display_tree_as_text(df, show_sizes=True)`
- **Location**: Added at end of helper functions cell, before closing `</VSCode.Cell>` tag
- **Status**: Complete

### ✅ STEP 4: Q1 Implementation Replaced
- **Cell 12**: Markdown header changed to "### Q1 - Directory Tree Structure"
- **Cell 13**: Complete replacement with new Q1 implementation
  - Old: Basic hdfs ls commands and explore_hdfs_directory_tree() call
  - New: Full EPD workflow (check exists → build/save → read → display)

---

## DETAILED CHANGES

### 1. Helper Functions Added

#### Function: `build_directory_tree_df(root_path=None, max_depth=3)`
**Purpose**: Build directory tree from WASBS_DATA and return as Spark DataFrame

**Parameters**:
- `root_path` (str): WASBS path to explore (defaults to WASBS_DATA)
- `max_depth` (int): Maximum depth to traverse (default: 3)

**Returns**: Spark DataFrame with schema:
```
- level: int (depth in tree, 0=root)
- path: string (full WASBS path)
- name: string (filename/dirname only)
- type: string ("dir" or "file")
- size: long (bytes, 0 for directories)
- parent_path: string (parent directory path)
```

**Key Features**:
- Uses `subprocess` to call `hdfs dfs -ls` recursively
- Parses hdfs output to extract permissions, size, paths
- Handles WASBS protocol transparently
- Creates proper parent-child relationships
- Returns structured Spark DataFrame for querying

---

#### Function: `save_tree_to_parquet(df, output_path)`
**Purpose**: Save directory tree DataFrame to Parquet in WASBS_USER

**Parameters**:
- `df`: Spark DataFrame with tree structure
- `output_path`: WASBS path for output (should be in WASBS_USER)

**Key Features**:
- Ensures trailing slash on output path
- Uses overwrite mode for idempotent saves
- Verifies save with hdfs ls command
- Prints parquet contents for confirmation

---

#### Function: `display_tree_as_text(df, show_sizes=True)`
**Purpose**: Display directory tree DataFrame in text format matching reference PDF

**Parameters**:
- `df`: Spark DataFrame with tree structure
- `show_sizes`: Whether to show file sizes in bytes (default: True)

**Output Format**:
```
======================================================================
DIRECTORY TREE STRUCTURE
======================================================================
└── msd/
    ├── audio/
    │   ├── attributes/
    │   │   ├── msd-jmir-area-of-moments-all-v1.0.attributes.csv (1051)
    │   │   └── ...
    │   ├── features/
    │   └── statistics/
    ├── genre/
    ├── main/
    └── tasteprofile/
======================================================================
```

**Key Features**:
- Uses Unicode box-drawing characters (└── ├── │)
- Shows file sizes in bytes (matching reference PDF)
- Builds hierarchical parent-child relationships
- Recursive tree printing with proper indentation

---

### 2. Q1 Cell Implementation

**Cell 12 (Markdown)**: Header updated to "### Q1 - Directory Tree Structure"

**Cell 13 (Python)**: Complete new implementation with:

#### PAT Tags (Process/Analysis Answer Tagging):
```python
bprint("Q1 - Directory Tree")
# supports: Q1(a) and Q1(b) — exploring MSD dataset structure
# does: builds directory tree from WASBS_DATA, saves to parquet in WASBS_USER, displays as text tree
```

#### Execution Path Diagram (EPD) Implementation:
```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: Check Existence                                     │
│ _success_exists(WASBS_USER/msd_directory_tree.parquet/)    │
└────────────┬───────────────────────────┬────────────────────┘
             │                           │
      EXISTS │                           │ NOT EXISTS
             ▼                           ▼
    ┌────────────────┐         ┌─────────────────────────┐
    │ Skip to Step 3 │         │ STEP 2: Build & Save    │
    └────────────────┘         │                         │
                               │ READ FROM: WASBS_DATA   │
                               │ (MSD structure)         │
                               │                         │
                               │ WRITE TO: WASBS_USER    │
                               │ (Parquet file)          │
                               └────────────┬────────────┘
                                            │
                               ┌────────────▼────────────┐
                               │ STEP 3: Read Parquet    │
                               │                         │
                               │ READ FROM: WASBS_USER   │
                               │ (Parquet file)          │
                               └────────────┬────────────┘
                                            │
                               ┌────────────▼────────────┐
                               │ STEP 4: Display Tree    │
                               │ - Text format (PDF)     │
                               │ - DataFrame table       │
                               │ - Example queries       │
                               └─────────────────────────┘
```

#### Code Flow:
1. **Define path**: `tree_parquet_path = f"{WASBS_USER}msd_directory_tree.parquet/"`
2. **Check exists**: Uses `_success_exists(tree_parquet_path)`
3. **If NOT exists**:
   - Build tree: `tree_df = build_directory_tree_df(root_path=WASBS_DATA, max_depth=3)`
   - Save: `save_tree_to_parquet(tree_df, tree_parquet_path)`
4. **Always read**: `tree_df = spark.read.parquet(tree_parquet_path)`
5. **Display**:
   - Text tree: `display_tree_as_text(tree_df, show_sizes=True)`
   - DataFrame: `show_df(tree_df, n=20, name="MSD Directory Structure", right_align=True)`
6. **Example queries**:
   - All .csv.gz files
   - Audio folder contents

---

## WHAT WAS NOT CHANGED

### ✅ Preserved:
- All existing helper functions (no deletions)
- All existing imports (no deletions)
- Import structure and grouping (3 groups, alpha-sorted)
- `cleanup_parquet_files(cleanup=False)` call unchanged
- All cells before and after Q1 section
- Cell IDs maintained

### ✅ Removed:
- Old `explore_hdfs_directory_tree()` calls
- Old `visualise_directory_tree()` function definition (was in old Cell 14)
- References to GHCND dataset (old Cell 14 had incorrect WASBS_USER references)

---

## PATH USAGE

### Source (Read MSD Structure):
- **Variable**: `WASBS_DATA`
- **Value**: `wasbs://campus-data@madsstorage002.blob.core.windows.net/msd/`
- **Usage**: `build_directory_tree_df(root_path=WASBS_DATA)`

### Destination (Write/Read Parquet):
- **Variable**: `WASBS_USER`
- **Value**: `wasbs://campus-user@madsstorage002.blob.core.windows.net/{username}-A2/`
- **Usage**: `tree_parquet_path = f"{WASBS_USER}msd_directory_tree.parquet/"`

---

## TESTING CHECKLIST

### Before First Run:
- [ ] Verify Spark session is started (Cell 4)
- [ ] Verify WASBS_DATA and WASBS_USER variables are defined (Cell 7)
- [ ] Verify username variable is set correctly

### Expected First Run Behavior:
1. Parquet does not exist
2. Build tree from WASBS_DATA (may take 1-2 minutes)
3. Save to WASBS_USER
4. Display tree in text format
5. Show DataFrame table
6. Show example queries

### Expected Subsequent Run Behavior:
1. Parquet exists
2. Skip build (fast)
3. Read from WASBS_USER (fast)
4. Display tree in text format
5. Show DataFrame table
6. Show example queries

### Force Rebuild:
To rebuild the tree (if MSD structure changes):
```python
# Delete the parquet file first
!hdfs dfs -rm -r -f {WASBS_USER}msd_directory_tree.parquet/
# Then re-run the Q1 cell
```

---

## EXPECTED OUTPUT

### Text Tree Format:
```
======================================================================
DIRECTORY TREE STRUCTURE
======================================================================
└── msd/
    ├── audio/
    │   ├── attributes/
    │   │   ├── msd-jmir-area-of-moments-all-v1.0.attributes.csv (1051)
    │   │   ├── msd-jmir-lpc-all-v1.0.attributes.csv (671)
    │   │   └── ...
    │   ├── features/
    │   └── statistics/
    │       └── sample_properties.csv.gz (42224669)
    ├── genre/
    │   ├── msd-MAGD-genreAssignment.tsv (11625230)
    │   └── ...
    ├── main/
    │   └── summary/
    │       ├── analysis.csv.gz (58658141)
    │       └── metadata.csv.gz (124211304)
    └── tasteprofile/
        ├── mismatches/
        │   ├── sid_matches_manually_accepted.txt (91342)
        │   └── sid_mismatches.txt (2026182)
        └── triplets.tsv (512139195)
======================================================================
```

### DataFrame Table:
Columns: level | path | name | type | size | parent_path

### Example Queries Output:
1. All .csv.gz files (3 expected: sample_properties, analysis, metadata)
2. Audio folder contents (attributes, features, statistics subdirs + files)

---

## RULES COMPLIANCE

### ✅ PROJECT RULES:
- [x] British English used throughout
- [x] Lower-case comments (no capital letters except for commands)
- [x] No silent code changes
- [x] PAT tags added to Q1 cell
- [x] Helper functions not reduced or modified
- [x] Comments for third-party graders

### ✅ EXECUTION PATH DIAGRAM (EPD) RULES:
- [x] EPD documented in project-RULES.txt
- [x] EPD included in comments for Q1 cell logic
- [x] Sequential operations clearly marked (STEP 1-4)
- [x] Decision points documented (EXISTS vs NOT EXISTS)
- [x] Data flow annotations (READ FROM / WRITE TO)
- [x] Convergence points noted (merge at Step 3)

### ✅ CODE BEHAVIOUR RULES:
- [x] Comments are brief phrases, not sentences
- [x] No options in comments
- [x] No code comments directed at davide
- [x] Patterns in existing comments preserved
- [x] No commented-out code deleted

### ✅ PAT RULES:
- [x] PAT tag at top of Q1 cell
- [x] bprint() with unique identifier
- [x] # supports: line with question reference
- [x] # does: line describing cell content

---

## REVIEW QUESTIONS FOR DAVIDE

1. **Max Depth**: Currently set to `max_depth=3`. Is this sufficient to explore MSD structure?
   
2. **File Sizes**: Display shows bytes (matching reference PDF). Want human-readable (KB/MB/GB) instead?

3. **Example Queries**: Are the two example queries helpful, or would you like different queries?

4. **Force Rebuild**: Should I add a parameter to force rebuild even if Parquet exists?

5. **Cell Numbering**: Should I add more descriptive cell numbers (e.g., Q1a, Q1b) or is current structure OK?

6. **Additional Queries**: What other DataFrame queries would be useful for Q1 analysis?

---

## NEXT STEPS (After Your Approval)

1. **davide reviews this document**
2. **davide tests notebook in Spark environment**
3. **If successful**: Commit to repository with message:
   ```
   Add Q1 directory tree implementation (EPD workflow)
   - Build tree from WASBS_DATA, save to WASBS_USER
   - Display as text tree and queryable DataFrame
   - Added helper functions: build_directory_tree_df, save_tree_to_parquet, display_tree_as_text
   ```
4. **If changes needed**: davide provides feedback, agent makes adjustments

---

## FILES MODIFIED

1. `d:\github\DATA420-A2\code\20251008-A2-Processing.ipynb` (NEW - copy from 1006)
   - Cell 8: Added 3 helper functions
   - Cell 12: Updated markdown header
   - Cell 13: Complete Q1 implementation replacement

2. `d:\github\DATA420-A2\reference\project-RULES.txt` (UPDATED)
   - Added "EXECUTION PATH DIAGRAM (EPD) RULES" section

---

## STATUS

🟡 **READY FOR REVIEW** - Not yet committed to repository

**Action Required**: davide review and approval before git commit

---

**End of Review Document**
