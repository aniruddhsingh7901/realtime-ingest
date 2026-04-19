"""Main orchestrator loop.

To be implemented in Step 16. Responsibilities:
- Poll Macrocosmos API every ~5s for new OD jobs
- Dedupe against already-processed job_ids
- Push jobs into an asyncio work queue
- Spawn N worker coroutines that consume the queue
- Each worker: cache lookup → scrape → validate → parquet → upload → submit
- Record per-job timing + metrics
"""
