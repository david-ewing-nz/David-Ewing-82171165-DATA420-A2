# QUICK REFERENCE: Column Naming Convention

## Format: `{AA}{NNN}`

### Dataset Codes
| Code | Dataset Name | Features | Range |
|------|-------------|----------|-------|
| **AO** | area-of-moments | 20 | AO001-AO020 |
| **LP** | lpc | 20 | LP001-LP020 |
| **SP** | spectral-all | 16 | SP001-SP016 |
| **TI** | timbral/marsyas | 124 | TI001-TI124 |
| **-** | *(join key)* | 1 | MSD_TRACKID |

**Total:** 180 features + 1 join key = **181 unique columns** after merge

---

## Example Translations

### Area-of-Moments (AO)
```
Method_of_Moments_Overall_Standard_Deviation_1 → AO001
Method_of_Moments_Overall_Standard_Deviation_2 → AO002
Method_of_Moments_Overall_Average_1 → AO011
Method_of_Moments_Overall_Average_5 → AO020
```

### LPC (LP)
```
LPC_Overall_Standard_Deviation_1 → LP001
LPC_Overall_Average_10 → LP020
```

### Spectral-All (SP)
```
Spectral_Centroid_Overall_Standard_Deviation → SP001
Spectral_Rolloff_Overall_Average → SP016
```

### Marsyas-Timbral (TI)
```
Zero_Crossings_Overall_Standard_Deviation → TI001
Spectral_Flux_Overall_Average → TI124
```

---

## Translation Table Location

**File:** `report/supplementary/audio_column_name_mapping.csv`

**Columns:**
- `dataset_code` (AO, LP, SP, TI)
- `dataset_name` (full dataset name)
- `original_column_name`
- `new_column_name`
- `original_length`
- `new_length`
- `is_join_key` (Yes/No)

**Usage:**
```python
# Load mapping table
mapping_df = pd.read_csv('report/supplementary/audio_column_name_mapping.csv')

# Look up original name
original = mapping_df[mapping_df['new_column_name'] == 'AO001']['original_column_name'].values[0]

# Look up new name
new = mapping_df[mapping_df['original_column_name'] == 'Zero_Crossings_Overall_Average']['new_column_name'].values[0]
```

---

## Key Properties

✅ **Fixed Length:** Always 5 characters  
✅ **Unique:** No collisions across datasets  
✅ **Consistent:** Same pattern for all features  
✅ **ML-Friendly:** Short, predictable identifiers  
✅ **Scalable:** Supports up to 999 features per dataset  
✅ **Traceable:** Full mapping preserved in CSV  

---

## Implementation Functions

### Schema Generation (Q2b)
```python
schema = create_struct_type_from_attributes(attributes_list)
```

### Column Renaming (Q2d)
```python
renamed_df, mapping = rename_audio_columns(df, dataset_code='AO', keep_msd_trackid=True)
```

---

**Quick Reference Card - 20251008D**
