"""Tweets → parquet bytes in sn13's expected format.

To be implemented in Step 5. Responsibilities:
- Serialize List[XContent] into a parquet file
- Respect sn13 naming convention:
    data_{YYYYMMDD_HHMMSS}_{count}_{16hex}.parquet
- Compression: snappy
- Strict schema match against sn13 spot-check expectations
"""
