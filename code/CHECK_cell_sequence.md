# 20251006_CHECK_Processing.ipynb Cell Sequence Analysis
## For David Ewing (82171165)
**Analysis Date:** 2025-10-07

---

## INFRASTRUCTURE CELLS (Do Not Touch)

### Cell 1 (lines 2-12) - Markdown
**Purpose:** Spark notebook setup instructions
**Content:** Instructions for connecting to Windows server, Kubernetes, and Jupyter

### Cell 2 (lines 15-180) - Code  
**Purpose:** Infrastructure setup
**Content:**
- Import findspark, getpass, pandas, pyspark, etc.
- Global constants: username, azure_account_name, azure_data_container_name, azure_user_container_name, azure_user_token
- Helper functions: dict_to_html, show_as_html, display_spark
- Spark functions: start_spark(), stop_spark()
- CSS styling

### Cell 3 (lines 183-194) - Markdown
**Purpose:** Assignment 1 explanation
**Content:** Azure Blob Storage instructions and key points

### Cell 4 (lines 197-199) - Code
**Purpose:** Start Spark session
**Content:** `start_spark(executor_instances=4, executor_cores=2, worker_memory=4, master_memory=4)`

---

## YOUR ASSIGNMENT CELLS (Cells 5-64)

### Cell 5 (lines 202-229) - Code
**Purpose:** YOUR imports
**Content:**
- Additional imports beyond infrastructure (IPython.display, math functions, matplotlib, pathlib, pyspark extended, typing, rich, warnings)
- warnings.filterwarnings
- console = Console()

### Cell 6 (lines 232-232) - Markdown
**Purpose:** Section header
**Content:** "#The following shows the data structure"

### Cell 7 (lines 235-292) - Code
**Purpose:** YOUR variables/constants
**Content:**
- notebook_run_time timer
- USERNAME = "dew59"
- WASBS paths (WASBS_DATA, WASBS_DAILY, WASBS_USER, etc.)
- File names (stations, inventory, countries, states read/write paths)
- Print all path configurations

### Cell 8 (lines 295-767) - Code
**Purpose:** YOUR subroutines/helper functions
**Content:**
- bprint()
- cleanup_parquet_files()
- normalise_ids()
- df_as_html()
- show_df()
- write_parquet()
- read_parquet()
- stations_schema()
- inventory_schema()
- countries_schema()
- states_schema()
- _normalise_dir()
- data_tree()
- haversine distance functions (haversine_km_np, haversine_km_vectorized, spark_law_cosines_distance)

### Cell 9 (lines 770-774) - Code
**Purpose:** Cleanup parquet files
**Content:** `cleanup_parquet_files(cleanup=False)`

### Cell 10 (lines 777-783) - Code
**Purpose:** List WASBS_DATA directory
**Content:** `!hdfs dfs -ls -h {WASBS_DATA}`

### Cell 11 (lines 786-789) - Code
**Purpose:** List daily directory
**Content:** `!hdfs dfs -du -s -h {daily_root}` and `!hdfs dfs -ls -h {daily_root}`

### Cell 12 (lines 792-819) - Code
**Purpose:** Calculate daily and metadata sizes
**Content:** Calculates and prints daily size and meta-data size in bytes and MB

### Cell 13 (lines 822-822) - Markdown
**Purpose:** Empty separator
**Content:** (empty)

### Cell 14 (lines 825-854) - Code
**Purpose:** Q1(b)2 - Capture directory listing
**Content:** Captures daily directory CSV.GZ files and parses year/size

### Cell 15 (lines 857-875) - Code
**Purpose:** Q1(b)3 - Build Spark DataFrame
**Content:** Creates year_sizes_df with schema (year, compressed_bytes)

### Cell 16 (lines 878-1025) - Code
**Purpose:** Q1(b)3a - Daily File Size Timeline Analysis
**Content:** Missing years analysis and visualization (plot creation)

### Cell 17 (lines 1028-1117) - Code
**Purpose:** Continued analysis
**Content:** Plots and statistics for daily file sizes

### Cells 18-64 (lines 1120-2058)
**Purpose:** Remaining assignment work
**Content:** Additional questions, analysis, data processing, visualizations

---

## SUMMARY

**Total Cells:** 64

**Infrastructure (Do Not Touch):** Cells 1-4

**Your Custom Setup:** Cells 5-8
- Cell 5: Your imports
- Cell 6: Markdown header
- Cell 7: Your variables/paths
- Cell 8: Your subroutines

**Assignment Work:** Cells 9-64 (56 cells)

---

## NOTES

1. The notebook follows the structure you described:
   - Infrastructure cells (1-4)
   - Your imports (5)
   - Markdown separator (6)
   - Your variables (7)
   - Your subroutines (8)
   - Assignment questions begin (9+)

2. None of the cells have been executed yet

3. The notebook appears to be mixing Assignment 1 (GHCND data) with Assignment 2 setup:
   - Infrastructure mentions "Assignment 1"
   - Paths reference "ghcnd" data
   - But file is named for Assignment 2 Processing

4. Many cells have error outputs stored, suggesting previous execution attempts

---

## RECOMMENDATION

This appears to be Assignment 1 code, not Assignment 2 (Million Song Dataset). The paths, data references, and questions all relate to climate data (GHCND), not music data (MSD).

For Assignment 2, you should be working with:
- Million Song Dataset (MSD)
- Audio features
- Genre data
- Taste profile data

Not:
- GHCND (Global Historical Climatology Network Daily)
- Weather stations
- Climate observations

**Is this the correct notebook for Assignment 2?**
