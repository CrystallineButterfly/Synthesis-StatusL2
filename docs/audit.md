# Focused security review

Date: 2026-03-19

## Scope

- `src/AutonomousActionCore.sol`
- `src/AutonomousActionHub.sol`
- `src/GaslessActionRelay.sol`
- `agents/partners.py`
- `agents/runtime.py`

## Checks performed

- access-control review against the repo's privileged entry points
- Slither static analysis over the Foundry workspace
- grep pass for `tx.origin`, `selfdestruct`, and zero-address handling in constructors
- Foundry tests
- Python unit tests
- Python bytecode compilation

## Findings fixed in this pass

### Fixed: zero-address guard gaps in the shared core

- `src/AutonomousActionCore.sol`

The shared role constructor and target approval path now reject `address(0)`.

### Fixed: offline execution only stalled on credentials for network partners

- `agents/config.py`
- `agents/partners.py`
- `agents/runtime.py`

Contract-call and Filecoin bundle actions now produce signed or upload-ready artifacts even
when live network credentials are absent. Network-only partners still report missing keys.

### Fixed: receipt anchoring output parsing was brittle

- `agents/partners.py`

`cast send` output is now parsed for `transactionHash` explicitly before falling back to the
raw stdout payload.

### Fixed: execution now requires a recorded dry run

- `src/AutonomousActionHub.sol`
- `test/*.t.sol`

The shared hub recorded dry-run hashes but previously allowed both direct and queued execution
paths to proceed without checking that a dry run existed. Both execution paths now revert when
`lastDryRun[actionId]` is unset, and the Foundry suite covers the direct and queued revert cases.

## Track-specific trust boundaries

- primary wrapper contract: `GaslessActionRelay`
- live-only partners: Status L2, Bankr Gateway
- offline-prepared partners: Celo (prepared_contract_call), ERC-8004 Receipts (prepared_contract_call), ENS (prepared_contract_call), MetaMask Delegations (prepared_contract_call)
- highest-sensitivity actions: bankr_gateway_compute_route, metamask_delegations_delegate_scope
- latest verification artifact: `artifacts/verification/0xd204dc56be483c757f5df2e5e085ac17fdf63442f358af32d828096412d004f7.json`

## Current posture

### Good

- no `tx.origin` authorization in repo contracts
- repo-specific wrapper contracts add no extra state-changing logic beyond construction, so
  the shared hub audit covers the full Solidity surface
- shared execution remains gated by approved targets, approved selectors, caps, cooldowns,
  validity windows, pause state, dry-run enforcement, and receipt anchoring
- local runs now emit reviewable onchain-intent and Filecoin-evidence artifacts without
  needing live partner credentials
- verification output now reports partner statuses and artifact paths

### Expected low-severity notes

- the shared core intentionally uses `block.timestamp` for cooldown and validity windows
- liquid balance is still a trusted reporter input and should be backed by a hardened reporting path
- admin roles remain powerful and should move to multisig control for production use

## Recommended production posture

- split admin, operator, and reporter wallets
- keep the hot operator wallet low-balance
- rotate demo keys after any public live run
- replace placeholder REST endpoints with official partner endpoints before production use
