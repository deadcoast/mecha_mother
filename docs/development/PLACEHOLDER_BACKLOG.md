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

## P0 (Correctness / Runtime Behavior)
1. `src/mecha_mother/quantum/engine.py`
- `merge_realities(...)` still uses basic vector averaging and labels itself simplified.
- `backup_consciousness(...)` stores raw references without immutability/serialization guard.
- Acceptance:
  - Introduce deterministic merge policy with explicit norm/correlation handling and tests for unequal dimensions + phase invariance.
  - Ensure backups are snapshot-safe (copy semantics) with tests proving later state mutation does not alter backup.

2. `src/mecha_mother/reality/reality.py`
- Import/export path currently rehydrates beauty field but other complex typed state remains weakly structured.
- Acceptance:
  - Add typed coercion checks for all exported/imported components used at runtime.
  - Add integration test: export -> import -> optimize_for_beauty and optimize_for_consciousness both function.

## P1 (Theory Fidelity / Feature Depth)
1. `src/mecha_mother/quantum/engine.py`
- Physical law transforms are now concrete but heuristic; needs tighter mapping to documented operators.
- Acceptance:
  - Add operator-level derivation comments and parameterized controls.
  - Add stability/regression tests over multiple steps.

2. `src/mecha_mother/aesthetics/engine.py`
- Some high-level routines still use heuristic consciousness proxies.
- Acceptance:
  - Replace proxy constants with derived values from field/operator where available.
  - Add tests asserting monotonic response to signal complexity/symmetry perturbations.

## P2 (Code Hygiene / Low Risk)
1. Remove/justify benign `pass` usages:
- `src/mecha_mother/core/constraints.py` (intentional no-op in validation branch)
- `src/mecha_mother/reality/reality.py` (enum parse fallback)
- `src/mecha_mother/consciousness/being.py` (`ConsciousnessBeing` alias class)
- Acceptance:
  - Convert to explicit comments or targeted handling where ambiguity exists.

2. Remove stale “simplified” comments once upgraded to concrete behavior.

## Verification Command Set
- `uv run ruff check src tests`
- `uv run black --check src tests`
- `uv run mypy src tests`
- `uv run pytest`
