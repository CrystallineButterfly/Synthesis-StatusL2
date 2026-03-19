# Live readiness

- **Project:** Gasless Field Runner
- **Track:** Status L2 Go Gasless
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:19+00:00`

## Trust boundaries

- **Status L2** — `rest_json` — Prepare gasless relay bundles for Status L2.
- **Celo** — `contract_call` — Settle stablecoin-native transfers on Celo rails.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.

## Offline-ready partner paths

- **Celo** — prepared_contract_call
- **ERC-8004 Receipts** — prepared_contract_call
- **ENS** — prepared_contract_call
- **MetaMask Delegations** — prepared_contract_call

## Live-only partner blockers

- **Status L2**: STATUS_RPC_URL, STATUS_RELAYER_URL — https://status.app/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/

## Highest-sensitivity actions

- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.
- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for GaslessActionRelay.
- Run python3 scripts/run_agent.py to produce a dry run for status_field_runner.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
