# Gasless Field Runner

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-StatusL2
- **Primary track:** Status L2 Go Gasless
- **Overlap targets:** Celo, Bankr Gateway, ERC-8004 Receipts, ENS, MetaMask Delegations, Cook
- **Primary contract:** GaslessActionRelay
- **Primary operator module:** status_field_runner
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A gasless-first action relay that assembles execution bundles and proofs suitable for Status L2 Sepolia while keeping live relayer wiring optional.

## Track evidence

- `artifacts/onchain_intents/celo_payment_settle.json`
- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`
- `artifacts/onchain_intents/ens_ens_publish.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "Gasless Field Runner",
  "track": "Status L2 Go Gasless",
  "plan_id": "0xd204dc56be483c757f5df2e5e085ac17fdf63442f358af32d828096412d004f7",
  "simulation_hash": "0xeef422c9cfdb9ac1ab919801932751a8b44905858edf29593fe04a5466efe90a",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/celo_payment_settle.json",
    "artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json",
    "artifacts/onchain_intents/ens_ens_publish.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json"
  ],
  "partner_statuses": {
    "Status L2": "awaiting_credentials",
    "Celo": "prepared_contract_call",
    "Bankr Gateway": "awaiting_credentials",
    "ERC-8004 Receipts": "prepared_contract_call",
    "ENS": "prepared_contract_call",
    "MetaMask Delegations": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:19+00:00"
}
```
