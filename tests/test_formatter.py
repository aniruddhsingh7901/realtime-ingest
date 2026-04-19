"""Unit tests for the parquet formatter.

To be implemented in Step 5. Checks:
- Schema columns match sn13 exactly
- File naming follows the data_{YYYYMMDD_HHMMSS}_{count}_{16hex}.parquet rule
- Snappy compression applied
- Can round-trip through pyarrow without type errors
"""
