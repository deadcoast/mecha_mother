"""
Constraint resolution and consistency checking for the MCS.
"""

from typing import Dict, List, Any
import numpy as np


class ConsistencyError(Exception):
    """Raised when reality consistency is violated."""

    ...


class ConstraintResolver:
    """
    Resolves constraints and ensures self-consistency of the MCS.
    """

    def __init__(self):
        """Initialize constraint resolver."""
        self.constraint_history: List[Dict[str, Any]] = []
        self._last_repair: Dict[str, Any] = {}

    def verify(self, state: Any) -> bool:
        """
        Verify that a state is self-consistent.

        Args:
            state: State to verify (could be MCS, quantum state, etc.)

        Returns:
            True if consistent, False otherwise
        """
        # Basic consistency checks
        if state is None:
            return False

        # Check if state has required attributes
        if hasattr(state, "nodes"):
            # MCS state
            return self._verify_mcs_consistency(state)
        elif isinstance(state, np.ndarray):
            # Quantum state
            return self._verify_quantum_consistency(state)
        elif hasattr(state, "reality_state_vector"):
            vector = getattr(state, "reality_state_vector", None)
            if not isinstance(vector, np.ndarray):
                return False
            if not self._verify_quantum_consistency(vector):
                return False
            c_field = getattr(state, "consciousness_field", None)
            if c_field is not None:
                total_fn = getattr(c_field, "total_consciousness", None)
                if callable(total_fn):
                    total_c = float(total_fn())
                    if not np.isfinite(total_c) or total_c < 0:
                        return False
            return True
        else:
            # Generic state - assume consistent if not None
            return True

    def _verify_mcs_consistency(self, mcs) -> bool:
        """Verify MCS consistency."""
        # Check that all nodes have valid amplitudes
        for node in mcs.get_all_nodes():
            amp = complex(node.amplitude)
            if not np.isfinite(np.real(amp)) or not np.isfinite(np.imag(amp)):
                return False

        # Check satisfaction link strengths are finite and bounded.
        for node in mcs.get_all_nodes():
            for other_id, strength in node.satisfaction_links.items():
                if not np.isfinite(float(strength)):
                    return False
                if strength < -1.0 or strength > 1.0:
                    return False
                other_node = mcs.get_node(other_id)
                if other_node:
                    # Check reverse link exists
                    reverse_strength = other_node.satisfaction_links.get(node.id, 0.0)
                    if not np.isfinite(float(reverse_strength)):
                        return False
                    if abs(strength - reverse_strength) > 1e-6:
                        # Not symmetric, but that's okay for directed graphs
                        continue

        return True

    def _verify_quantum_consistency(self, state: np.ndarray) -> bool:
        """Verify quantum state consistency."""
        # Check normalization (should be approximately 1)
        norm = np.linalg.norm(state)
        if abs(norm - 1.0) > 0.1:  # Allow some tolerance
            return False

        # Check for NaN or Inf
        if np.any(np.isnan(state)) or np.any(np.isinf(state)):
            return False

        return True

    def check_constant_change(
        self, constant_name: str, new_value: float, current_state: Any
    ) -> Dict[str, Any]:
        """
        Check if changing a physical constant would break consistency.

        Args:
            constant_name: Name of constant to change
            new_value: Proposed new value
            current_state: Current state of reality

        Returns:
            Dictionary with 'consistent' bool and 'issues' list
        """
        issues: List[str] = []
        viability_ranges = {
            "c": (1e6, 1e10),
            "hbar": (1e-40, 1e-20),
            "G": (1e-15, 1e-5),
            "alpha": (1e-6, 1.0),
        }

        if not np.isfinite(new_value):
            issues.append(f"{constant_name} must be finite")
            return {"consistent": False, "issues": issues}

        # Check for obviously problematic values
        if new_value <= 0 and constant_name in ["c", "hbar", "G"]:
            issues.append(f"{constant_name} must be positive")

        if constant_name in viability_ranges:
            lo, hi = viability_ranges[constant_name]
            if new_value < lo or new_value > hi:
                issues.append(
                    f"{constant_name} outside viability range [{lo:.3e}, {hi:.3e}]"
                )

        if isinstance(current_state, np.ndarray):
            if np.any(np.isnan(current_state)) or np.any(np.isinf(current_state)):
                issues.append("Current state contains NaN/Inf")
            norm = float(np.linalg.norm(current_state))
            if norm <= 0:
                issues.append("Current state has zero norm")

            if constant_name == "hbar" and new_value < 1e-38 and norm > 0:
                issues.append("hbar too small for current state resolution")

        self.constraint_history.append(
            {
                "action": "check_constant_change",
                "constant": constant_name,
                "new_value": float(new_value),
                "consistent": len(issues) == 0,
                "issues": list(issues),
            }
        )

        return {"consistent": len(issues) == 0, "issues": issues}

    def repair_constant_change(
        self, constant_name: str, new_value: float, current_state: Any
    ) -> bool:
        """
        Attempt to repair consistency after constant change.

        Args:
            constant_name: Name of constant
            new_value: New value
            current_state: Current state

        Returns:
            True if repair successful, False otherwise
        """
        check = self.check_constant_change(constant_name, new_value, current_state)
        if check["consistent"]:
            self._last_repair = {
                "constant": constant_name,
                "original": float(new_value),
                "repaired": float(new_value),
                "applied": False,
            }
            return True

        viability_ranges = {
            "c": (1e6, 1e10),
            "hbar": (1e-40, 1e-20),
            "G": (1e-15, 1e-5),
            "alpha": (1e-6, 1.0),
        }
        if constant_name not in viability_ranges or not np.isfinite(new_value):
            return False

        lo, hi = viability_ranges[constant_name]
        repaired = float(np.clip(new_value, lo, hi))
        repaired_check = self.check_constant_change(
            constant_name, repaired, current_state
        )
        if not repaired_check["consistent"]:
            return False

        self._last_repair = {
            "constant": constant_name,
            "original": float(new_value),
            "repaired": repaired,
            "applied": True,
        }
        self.constraint_history.append(
            {
                "action": "repair_constant_change",
                "constant": constant_name,
                "original": float(new_value),
                "repaired": repaired,
            }
        )
        return True

    def get_repaired_value(self, constant_name: str, fallback: float) -> float:
        """Return last repaired value for a constant if available."""
        if self._last_repair.get("constant") == constant_name:
            repaired = self._last_repair.get("repaired")
            if repaired is not None:
                return float(repaired)
        return float(fallback)
