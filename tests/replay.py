"""Replay harness: re-run real OD jobs offline, without going live.

To be implemented in Step 6. Workflow:
1. Load a job JSON from tests/fixtures/
2. Run it through the full pipeline (scrape → validate → parquet)
3. Mock the S3 upload + submission
4. Print: time taken, tweets returned, parquet size, schema-valid?
This is our "confidence meter" before we register on sn13.
"""
