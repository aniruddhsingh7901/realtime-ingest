"""Proxy pool manager + rotation.

To be implemented in Step 8. Responsibilities:
- Load proxies from .env / proxies.txt (Webshare format)
- Health-check proxies periodically (ping api.x.com)
- Assign a proxy to each X account (sticky)
- Evict dead proxies, log bad ones
"""
