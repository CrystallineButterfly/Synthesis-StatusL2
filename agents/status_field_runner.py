"""Project-specific context for Gasless Field Runner."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "Gasless Field Runner",
    "track": "Status L2 Go Gasless",
    "pitch": "A gasless-first action relay that assembles execution bundles and proofs suitable for Status L2 Sepolia while keeping live relayer wiring optional.",
    "overlap_targets": [
        "Celo",
        "Bankr Gateway",
        "ERC-8004 Receipts",
        "ENS",
        "MetaMask Delegations",
        "Cook"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
