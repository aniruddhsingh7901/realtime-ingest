"""SQLite-backed account state store.

To be implemented in Step 9. Schema (sketch):
    accounts(
        id, username, auth_token, cookies_json,
        proxy_id, state, last_used_at, cooldown_until,
        ban_count, total_requests, created_at, updated_at
    )
"""
