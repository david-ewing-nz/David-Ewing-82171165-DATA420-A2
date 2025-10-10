## Comprehensive File Operation Map for 20251012Z-A2-Processing.ipynb

### Current File Operations Requiring Existence Checking

#### CSV Files (3 operations)
1. **audio_column_name_mapping.csv** (Cell #VSC-64a29ea8, around line 3143)
   - Path: `../report/supplementary/audio_column_name_mapping.csv`
   - Operation: `mapping_df.to_csv(csv_output_path, index=False)`
   - Status: ❌ No existence check implemented

2. **dataset_statistics.csv** (Cell around line 3352)
   - Path: `../report/supplementary/dataset_statistics.csv`
   - Operation: DataFrame.to_csv()
   - Status: ❌ No existence check implemented

3. **row_counts_per_dataset.csv** (inferred from JSON save pattern)
   - Path: `../report/supplementary/` + filename
   - Operation: DataFrame.to_csv()
   - Status: ❌ No existence check implemented

#### PNG Files (8+ operations)
1. **msd_directory_tree.png** (Cell #VSC-6ebb7518, line 1357)
   - Path: `../report/supplementary/msd_directory_tree.png`
   - Operation: `plt.savefig(png_path, bbox_inches='tight', dpi=150)`
   - Status: ✅ Already has existence check (lines 1363, 1435)

2. **dataset_statistics.png** (around line 3354)
   - Path: `../report/supplementary/dataset_statistics.png`
   - Operation: `plt.savefig()`
   - Status: ❌ No existence check implemented

3. **schema_comparison.png** (around line 3500)
   - Path: `../report/supplementary/schema_comparison.png`
   - Operation: `plt.savefig()`
   - Status: ❌ No existence check implemented

4. **row_counts.png** (around line 4164)
   - Path: `../report/supplementary/row_counts.png`
   - Operation: `plt.savefig()`
   - Status: ❌ No existence check implemented

5. **aom_schema.png** (around line 4297)
   - Path: `../report/supplementary/aom_schema.png`
   - Operation: `plt.savefig()`
   - Status: ✅ Already has existence check (skipped message)

6. **lpc_schema.png** (around line 4298)
   - Path: `../report/supplementary/lpc_schema.png`
   - Operation: `plt.savefig()`
   - Status: ✅ Already has existence check (skipped message)

7. **spectral_schema.png** (around line 4299)
   - Path: `../report/supplementary/spectral_schema.png`
   - Operation: `plt.savefig()`
   - Status: ✅ Already has existence check (skipped message)

8. **timbral_schema.png** (around line 4300)
   - Path: `../report/supplementary/timbral_schema.png`
   - Operation: `plt.savefig()`
   - Status: ✅ Already has existence check (skipped message)

9. **file_sizes_chart.png** (around line 4488)
   - Path: `../report/supplementary/file_sizes_chart.png`
   - Operation: `plt.savefig()`
   - Status: ❌ Needs existence check implementation

#### JSON Files (5 operations)
1. **dataset_statistics.json** (around line 3353)
   - Path: `../report/supplementary/dataset_statistics.json`
   - Operation: `json.dump(stats_dict, f, indent=2)`
   - Status: ❌ No existence check implemented

2. **schema_validation.json** (around line 3496)
   - Path: `../report/supplementary/schema_validation.json`
   - Operation: `json.dump(validation_results, f, indent=2)`
   - Status: ❌ No existence check implemented

3. **row_counts.json** (around line 4163)
   - Path: `../report/supplementary/row_counts.json`
   - Operation: `json.dump(row_counts, f, indent=2)`
   - Status: ❌ No existence check implemented

4. **audio_schemas.json** (around line 4400)
   - Path: `../report/supplementary/audio_schemas.json`
   - Operation: `json.dump(all_schemas_json, f, indent=2)`
   - Status: ❌ No existence check implemented

5. **[Individual schema stats].json** (around line 4458)
   - Path: `../report/supplementary/{dataset_key}_stats.json`
   - Operation: `json.dump(stats, f, indent=2)`
   - Status: ❌ No existence check implemented

### Pattern to Implement
For each file operation, implement the pattern:
```python
if os.path.exists(file_path):
    print(f"[display] reading from disk: {file_path}")
    # Load existing file (CSV: pd.read_csv(), JSON: json.load(), PNG: display)
else:
    # Create new file
    # Save file operation
    print(f"[saved] file_type: {file_path}")
```

### Priority Order for Implementation
1. **High Priority**: CSV and JSON files (data files that take time to regenerate)
2. **Medium Priority**: PNG visualisation files (except schema PNGs which already have checks)
3. **Already Complete**: msd_directory_tree.png and individual schema PNGs

### Total File Operations Needing Implementation
- **CSV**: 3 operations
- **JSON**: 5 operations  
- **PNG**: 4 operations (4 already implemented)
- **Total**: 12 file operations need existence checking implementation