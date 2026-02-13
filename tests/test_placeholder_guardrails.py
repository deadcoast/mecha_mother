"""
Guardrail tests to prevent reintroduction of placeholder implementation markers.
"""

from pathlib import Path

CRITICAL_MODULES = [
    Path("src/mecha_mother/quantum/engine.py"),
    Path("src/mecha_mother/reality/reality.py"),
    Path("src/mecha_mother/aesthetics/engine.py"),
    Path("src/mecha_mother/consciousness/engine.py"),
]


BANNED_MARKERS = [
    "In full implementation",
    "placeholder for future implementation",
    "simplified - full version",
    "TODO: implement",
    "not implemented",
]


def test_no_placeholder_markers_in_critical_modules():
    """Critical runtime modules should not contain placeholder implementation markers."""
    violations: list[str] = []
    for module_path in CRITICAL_MODULES:
        text = module_path.read_text(encoding="utf-8")
        for marker in BANNED_MARKERS:
            if marker in text:
                violations.append(f"{module_path}: {marker}")

    assert not violations, "Placeholder markers found:\n" + "\n".join(violations)
