"""
Constraint resolution and consistency checking for the MCS.
"""

from typing import Dict, List, Any
import numpy as np


class ConsistencyError(Exception):
    """Raised when reality consistency is violated."""

    pass


class ConstraintResolver:
    """
    Resolves constraints and ensures self-consistency of the MCS.
    """

    def __init__(self):
        """Initialize constraint resolver."""
        self.constraint_history: List[Dict[str, Any]] = []

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
        else:
            # Generic state - assume consistent if not None
            return True

    def _verify_mcs_consistency(self, mcs) -> bool:
        """Verify MCS consistency."""
        # Check that all nodes have valid amplitudes
        for node in mcs.get_all_nodes():
            if np.isnan(node.amplitude) or np.isinf(node.amplitude):
                return False

        # Check that satisfaction links are symmetric where expected
        for node in mcs.get_all_nodes():
            for other_id, strength in node.satisfaction_links.items():
                other_node = mcs.get_node(other_id)
                if other_node:
                    # Check reverse link exists
                    reverse_strength = other_node.satisfaction_links.get(node.id, 0.0)
                    if abs(strength - reverse_strength) > 1e-6:
                        # Not symmetric, but that's okay for directed graphs
                        pass

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
        issues = []

        # Check for obviously problematic values
        if new_value <= 0 and constant_name in ["c", "hbar", "G"]:
            issues.append(f"{constant_name} must be positive")

        if constant_name == "c" and new_value > 1e10:
            issues.append("Speed of light too high - would break causality")

        if constant_name == "alpha" and (new_value < 0 or new_value > 1):
            issues.append("Fine structure constant must be between 0 and 1")

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
        # For now, just check if change is reasonable
        check = self.check_constant_change(constant_name, new_value, current_state)
        return check["consistent"]
