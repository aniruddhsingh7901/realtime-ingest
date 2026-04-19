"""S3 uploader via presigned URL.

To be implemented in Step 14. Responsibilities:
- Request presigned-POST URL from Macrocosmos API per submission
- PUT parquet bytes, retry on 5xx
- Return s3_path + etag + content_length for the submission payload
"""
