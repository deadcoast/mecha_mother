# Placeholder Elimination Backlog

## Guardrails
- Do not mark any item complete without code + tests + full CI (`ruff`, `black --check`, `mypy`, `pytest`).
- `pass`, placeholder comments, and fixed fallback constants are treated as incomplete unless proven intentional and low-risk.
- Update `TODO.md` / `VERIFIED.md` only after implementation is merged and validated.

## Completed In This Pass
- Replaced beauty-field placeholder path with concrete `BeautyField` metrics/update model.
  - `src/mecha_mother/aesthetics/engine.py`
  - `src/mecha_mother/reality/reality.py`
  - Tests: `tests/test_ethics_aesthetics.py`
- Replaced no-op physical-law imposition methods with concrete state transforms.
  - `src/mecha_mother/quantum/engine.py`
  - Tests: `tests/test_basic.py`
- Hardened reality-state merge and consciousness backup semantics.
  - `merge_realities(...)` now deterministic with phase alignment and dimension-safe normalization
  - `backup_consciousness(...)` now stores snapshot copies
  - Tests: `tests/test_basic.py`
- Hardened import/export rehydration for runtime components.
  - Consciousness field coercion added
  - Beauty field coercion integrated in import path
  - Roundtrip integration test exercises both optimization APIs
  - Files: `src/mecha_mother/consciousness/engine.py`, `src/mecha_mother/reality/reality.py`, `tests/test_basic.py`
- Added operator-level derivation comments and tunable law parameters, plus stability regression coverage.
  - Files: `src/mecha_mother/quantum/engine.py`, `tests/test_basic.py`
- Replaced ambiguous pass/no-op hygiene items listed in P2 and removed stale simplified wording.
  - Files: `src/mecha_mother/core/constraints.py`, `src/mecha_mother/reality/reality.py`, `src/mecha_mother/consciousness/being.py`, `src/mecha_mother/aesthetics/engine.py`

## P0 (Correctness / Runtime Behavior)
All currently tracked P0 items are implemented and validated.

## P1 (Theory Fidelity / Feature Depth)
1. `src/mecha_mother/quantum/engine.py`
- Physical law transforms are concrete and parameterized; remaining work is deeper theoretical calibration.
- Acceptance:
  - [x] Add operator-level derivation comments and parameterized controls.
  - [x] Add stability/regression tests over multiple steps.
  - [ ] Calibrate parameter defaults against documented target regimes.

1. `src/mecha_mother/aesthetics/engine.py`
- Some high-level routines still use heuristic consciousness proxies.
- Acceptance:
  - [x] Replace proxy constants with derived values from field/operator where available.
  - [x] Add tests asserting monotonic response to signal complexity/symmetry perturbations.

## P2 (Code Hygiene / Low Risk)
1. Remove/justify benign `pass` usages:
- `src/mecha_mother/core/constraints.py` (intentional no-op in validation branch)
- `src/mecha_mother/reality/reality.py` (enum parse fallback)
- `src/mecha_mother/consciousness/being.py` (`ConsciousnessBeing` alias class)
- Acceptance:
  - Convert to explicit comments or targeted handling where ambiguity exists.

1. Remove stale “simplified” comments once upgraded to concrete behavior.

## Verification Command Set
- `uv run ruff check src tests`
- `uv run black --check src tests`
- `uv run mypy src tests`
- `uv run pytest`
