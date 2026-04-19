"""X account pool manager + rotation.

To be implemented in Step 9. Responsibilities:
- Allocate accounts to workers based on health + cooldown
- Sticky binding: each account uses its assigned proxy always
- Mark accounts as rate-limited / banned / healthy
- Reload pool from SQLite on startup
"""
