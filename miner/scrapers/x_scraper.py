"""X (Twitter) scraping via twscrape.

To be implemented in Step 10. Responsibilities:
- Translate an OnDemandJobPayloadX into twscrape queries
  * keywords + time range → search query
  * usernames → user timeline fetch
  * url → tweet_detail lookup
- Allocate N accounts + bound proxies from pools
- Fire parallel queries, first valid response wins
- Return List[XContent] validated against schema
"""
