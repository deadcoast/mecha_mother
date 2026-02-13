"""
Ethical Decision Engine - makes moral decisions based on consciousness maximization.
"""

import numpy as np
from typing import Dict, List, Any
from mecha_mother.ethics.engine import EthicsEngine


class EthicalDecisionEngine:
    """
    Engine for making ethical decisions.

    Chooses actions that maximize total consciousness.
    """

    def __init__(self):
        """Initialize ethical decision engine."""
        self.ethics_engine = EthicsEngine()
        self.moral_memory: List[Dict[str, Any]] = []

    def moral_decision(
        self,
        options: List[Dict[str, Any]],
        current_state: Any,
        beings: List[Any],
        time_horizon: int = 100,
    ) -> Dict[str, Any]:
        """
        Choose the most moral action from options.

        Args:
            options: List of possible actions
            current_state: Current reality state
            beings: List of affected beings
            time_horizon: Time horizon for evaluation

        Returns:
            Dictionary with decision results
        """
        best_option = None
        best_value = -np.inf
        moral_values = []
        moral_magnitudes = []

        for option in options:
            # Compute moral value
            value = self.ethics_engine.compute_moral_value(
                action=option, beings=beings, time_horizon=time_horizon
            )
            magnitude = self.compute_good_evil_magnitude(option, beings)

            moral_values.append(value)
            moral_magnitudes.append(magnitude)

            if value > best_value:
                best_value = value
                best_option = option

        # Compute moral certainty
        if len(moral_values) > 1:
            std = np.std(moral_values)
            mean_val = np.mean(moral_values)
            certainty = 1.0 / (1.0 + std / (abs(mean_val) + 1e-10))
        else:
            certainty = 1.0

        # Compute moral gradient
        if hasattr(current_state, "consciousness_field"):
            gradient = self.ethics_engine.compute_moral_gradient(
                state_vector=getattr(current_state, "reality_state_vector", None),
                consciousness_field=current_state.consciousness_field,
                beings=beings,
            )
        else:
            gradient = np.zeros(10, dtype=complex)

        return {
            "best_option": best_option,
            "moral_value": best_value,
            "best_magnitude": (
                self.compute_good_evil_magnitude(best_option, beings)
                if best_option is not None
                else 0.0
            ),
            "all_values": moral_values,
            "all_magnitudes": moral_magnitudes,
            "certainty": certainty,
            "gradient": gradient,
        }

    def compute_good_evil_magnitude(
        self,
        action: Dict[str, Any],
        beings: List[Any],
        baseline_total_consciousness: float | None = None,
    ) -> float:
        """
        Compute the action magnitude:

        G(A) = (ΔC_total / C_total(Ψ)) * log(1 + N_affected)

        Returns absolute magnitude so strong good and strong evil both score high impact.
        """
        delta_c_total = self.ethics_engine.compute_moral_value(action, beings)
        if baseline_total_consciousness is None:
            baseline_total_consciousness = float(
                sum(float(getattr(b, "consciousness", 1.0)) for b in beings)
            )

        num_affected_raw = action.get("num_affected")
        if isinstance(num_affected_raw, int):
            num_affected = max(0, num_affected_raw)
        else:
            affected = action.get("affected_beings")
            if isinstance(affected, list):
                num_affected = len(affected)
            else:
                num_affected = len(beings)

        ratio = delta_c_total / (baseline_total_consciousness + 1e-10)
        magnitude = ratio * np.log1p(float(num_affected))
        return float(abs(magnitude))

    def is_good_action(self, action: Dict[str, Any], beings: List[Any]) -> bool:
        """
        Determine if an action is good (increases total consciousness).

        Args:
            action: Action to evaluate
            beings: Affected beings

        Returns:
            True if action is good
        """
        moral_value = self.ethics_engine.compute_moral_value(action, beings)
        return moral_value > 0

    def is_evil_action(self, action: Dict[str, Any], beings: List[Any]) -> bool:
        """
        Determine if an action is evil (decreases total consciousness).

        Args:
            action: Action to evaluate
            beings: Affected beings

        Returns:
            True if action is evil
        """
        moral_value = self.ethics_engine.compute_moral_value(action, beings)
        return moral_value < 0
