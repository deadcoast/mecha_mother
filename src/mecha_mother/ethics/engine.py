"""
Ethics Engine - implements the Moral Field Operator 𝕄.

Based on MCS Theory: The moral gradient 𝕄(Ψ) = ∇ℂ_total points toward increased total consciousness.
"""

import numpy as np
from typing import Dict, List, Optional, Any


class MoralFieldOperator:
    """
    The Moral Field Operator 𝕄 that measures the gradient of consciousness.

    Defined by: 𝕄(Ψ) = ∇_Ψ ℂ_total

    The gradient points toward increased total consciousness.
    """

    def __init__(self, dimension: int = 10):
        """
        Initialize moral field operator.

        Args:
            dimension: Dimension of the moral space
        """
        self.dim = dimension
        self.consciousness_operator = self._build_consciousness_operator()

    def _build_consciousness_operator(self) -> np.ndarray:
        """Build consciousness operator ℂ from first principles."""
        C = np.zeros((self.dim, self.dim), dtype=complex)

        for i in range(self.dim):
            for j in range(self.dim):
                if i == j:
                    C[i, j] = 1.0
                else:
                    # Self-referential coupling
                    C[i, j] = np.exp(2j * np.pi * (i - j) / self.dim) / self.dim

        # Ensure Hermitian
        C = 0.5 * (C + C.conj().T)
        # Normalize trace
        C = C / np.trace(C) * self.dim

        return C

    def compute_moral_gradient(
        self, state_vector: Optional[np.ndarray], beings: List[Any]
    ) -> np.ndarray:
        """
        Compute ∇ℂ at current state using finite difference approximation.

        Args:
            state_vector: Current reality state
            beings: List of conscious beings

        Returns:
            Moral gradient vector
        """
        if state_vector is None:
            state = np.random.randn(self.dim) + 1j * np.random.randn(self.dim)
            state = state / np.linalg.norm(state)
        else:
            state = state_vector

        n_dim = len(state)
        gradient = np.zeros(n_dim, dtype=complex)

        # Finite difference approximation
        epsilon = 1e-6

        for i in range(n_dim):
            # Perturb dimension i
            state_plus = state.copy()
            state_plus[i] += epsilon
            state_plus = state_plus / np.linalg.norm(state_plus)

            state_minus = state.copy()
            state_minus[i] -= epsilon
            state_minus = state_minus / np.linalg.norm(state_minus)

            # Compute actual ℂ difference
            C_plus = self.total_consciousness(state_plus, beings)
            C_minus = self.total_consciousness(state_minus, beings)

            gradient[i] = (C_plus - C_minus) / (2 * epsilon)

        return gradient

    def total_consciousness(self, state: np.ndarray, beings: List[Any]) -> float:
        """
        Compute total ℂ for all beings in given state.

        Args:
            state: Current state vector
            beings: List of conscious beings

        Returns:
            Total consciousness value
        """
        total = 0.0

        for being in beings:
            # Being's consciousness depends on state projection
            being_state = self.project_state(state, being.get("perspective", None))
            C = self.individual_consciousness(being_state, being.get("type", "human"))
            total += C * being.get("weight", 1.0)

        # Include correlation terms (entanglement effects - empathy)
        correlation_term = 0.0
        for i in range(len(beings)):
            for j in range(i + 1, len(beings)):
                # Consciousness correlation (empathy, shared experiences)
                proj_i = self.project_state(state, beings[i].get("perspective", None))
                proj_j = self.project_state(state, beings[j].get("perspective", None))

                # Normalize projections
                if np.linalg.norm(proj_i) > 0 and np.linalg.norm(proj_j) > 0:
                    proj_i = proj_i / np.linalg.norm(proj_i)
                    proj_j = proj_j / np.linalg.norm(proj_j)
                    corr = np.abs(np.dot(proj_i, proj_j.conj()))
                    correlation_term += (
                        corr
                        * beings[i].get("weight", 1.0)
                        * beings[j].get("weight", 1.0)
                    )

        return total + 0.1 * correlation_term  # Empathy bonus

    def individual_consciousness(self, state: np.ndarray, being_type: str) -> float:
        """
        Compute ℂ for individual being.

        Args:
            state: Being's state vector
            being_type: Type of being

        Returns:
            Individual consciousness value
        """
        # Ensure state is proper size
        if len(state) != self.dim:
            if len(state) > self.dim:
                state = state[: self.dim]
            else:
                padded = np.zeros(self.dim, dtype=complex)
                padded[: len(state)] = state
                state = padded

        state = state / (np.linalg.norm(state) + 1e-10)

        if being_type == "human":
            # Human consciousness formula
            clarity = np.abs(state.conj().T @ state)
            coherence = np.mean(np.abs(np.fft.fft(state)))
            valence = np.imag(state.conj().T @ (state - np.roll(state, 1)))
            return float(clarity * coherence * (1 + 0.1 * valence))
        elif being_type == "animal":
            # Simpler animal consciousness
            return float(np.sum(np.abs(state)) ** 0.5)
        elif being_type == "ai":
            # AI consciousness (via consciousness operator)
            return float(np.abs(state.conj().T @ self.consciousness_operator @ state))
        else:
            return float(np.linalg.norm(state))

    def project_state(
        self, global_state: np.ndarray, perspective: Optional[np.ndarray]
    ) -> np.ndarray:
        """
        Project global state to being's perspective.

        Args:
            global_state: Global reality state
            perspective: Being's perspective vector

        Returns:
            Projected state
        """
        if perspective is None:
            return global_state.copy()

        # Ensure dimensions match
        if len(perspective) != len(global_state):
            if len(perspective) > len(global_state):
                perspective = perspective[: len(global_state)]
            else:
                padded = np.zeros(len(global_state), dtype=complex)
                padded[: len(perspective)] = perspective
                perspective = padded

        # Project: |⟨perspective|state⟩|² * state
        projection = np.abs(np.dot(perspective.conj(), global_state)) ** 2
        return projection * global_state

    def compute_moral_force(
        self,
        agent_state: np.ndarray,
        moral_gradient: np.ndarray,
        agent_consciousness: float,
    ) -> np.ndarray:
        """
        Compute moral force on an agent.

        𝔽_moral = 𝕄(Ψ_agent) · ℂ_agent

        Args:
            agent_state: Agent's state vector
            moral_gradient: Moral gradient at agent's location
            agent_consciousness: Agent's consciousness level

        Returns:
            Moral force vector
        """
        # Force = gradient * consciousness
        force = moral_gradient * agent_consciousness
        return force


class EthicalDecisionEngine:
    """
    Complete ethical decision engine implementing the moral calculus.

    For any decision with options {A_i}, computes:
    MoralValue(A_i) = Σ w_j · Δℂ_j(A_i) · e^(-α t_j)

    The morally right action: A_right = argmax[MoralValue(A_i)]
    """

    def __init__(self, dimension: int = 10):
        """Initialize the ethical decision engine."""
        self.moral_operator = MoralFieldOperator(dimension)
        self.moral_memory: List[Dict[str, Any]] = []
        self.moral_discount_rate = 0.01  # α = 0.01
        self.corruption_coefficient = 0.3  # β ≈ 0.3

    def moral_decision(
        self,
        options: List[Dict[str, Any]],
        current_state: np.ndarray,
        beings: List[Dict[str, Any]],
        time_horizon: int = 100,
    ) -> Dict[str, Any]:
        """
        Choose the most moral action.

        Args:
            options: List of action options
            current_state: Current reality state
            beings: List of conscious beings
            time_horizon: How far to look ahead

        Returns:
            Dictionary with best option, moral value, and analysis
        """
        best_option = None
        best_value = -np.inf
        moral_values = []

        for i, option in enumerate(options):
            # Simulate forward in time
            future_states = self.simulate_future(
                current_state, option, beings, time_horizon
            )

            # Compute moral value over time
            total_value = 0.0
            for t, state in enumerate(future_states):
                C_t = self.moral_operator.total_consciousness(state, beings)
                discount = np.exp(-self.moral_discount_rate * t)  # Moral discounting
                total_value += C_t * discount

            # Add corruption term for killing/harm actions
            intention_to_kill = option.get("intention_to_kill", 0.0)
            if intention_to_kill > 0:
                corruption_term = -1.0 - self.corruption_coefficient * np.log(
                    1.0 + intention_to_kill
                )
                total_value += corruption_term

            moral_values.append(total_value)

            if total_value > best_value:
                best_value = total_value
                best_option = option

        # Compute moral certainty
        certainty: float
        if len(moral_values) > 1:
            std = np.std(moral_values)
            mean = np.mean(moral_values)
            certainty = float(1.0 / (1.0 + std / (abs(mean) + 1e-10)))
        else:
            certainty = 1.0

        return {
            "best_option": best_option,
            "moral_value": best_value,
            "all_values": moral_values,
            "certainty": certainty,
            "gradient": self.moral_operator.compute_moral_gradient(
                current_state, beings
            ),
        }

    def simulate_future(
        self,
        state: np.ndarray,
        option: Dict[str, Any],
        beings: List[Dict[str, Any]],
        steps: int,
    ) -> List[np.ndarray]:
        """
        Simulate state evolution after taking option.

        Args:
            state: Current state
            option: Action to take
            beings: Affected beings
            steps: Number of time steps

        Returns:
            List of future states
        """
        states = [state.copy()]
        current = state.copy()

        for t in range(steps):
            # Apply option effect
            if option.get("type") == "action":
                # Action changes state
                delta = option.get("effect_vector", np.zeros_like(current))
                if len(delta) != len(current):
                    if len(delta) > len(current):
                        delta = delta[: len(current)]
                    else:
                        padded = np.zeros_like(current)
                        padded[: len(delta)] = delta
                        delta = padded
                current = current + 0.1 * delta
                current = current / (np.linalg.norm(current) + 1e-10)
            elif option.get("type") == "inaction":
                # Natural drift
                drift = np.random.randn(*current.shape) * 0.01
                current = current + drift
                current = current / (np.linalg.norm(current) + 1e-10)

            states.append(current.copy())

        return states

    def compute_moral_value(
        self,
        action: Dict[str, Any],
        beings: List[Any],
        current_state: Optional[np.ndarray] = None,
        time_horizon: int = 100,
    ) -> float:
        """
        Compute moral value of an action.

        MoralValue(A) = Σ w_j · Δℂ_j(A) · e^(-α t_j)

        Args:
            action: Action description
            beings: List of affected beings
            current_state: Current state (optional)
            time_horizon: Time horizon for evaluation

        Returns:
            Moral value (higher is better)
        """
        # Convert beings to dict format if needed
        beings_dicts = []
        for being in beings:
            if isinstance(being, dict):
                beings_dicts.append(being)
            elif hasattr(being, "consciousness"):
                beings_dicts.append(
                    {
                        "type": getattr(being, "being_type", "human"),
                        "weight": being.consciousness,
                        "perspective": getattr(being, "perspective", None),
                    }
                )
            else:
                beings_dicts.append({"type": "unknown", "weight": 1.0})

        if not beings_dicts:
            return 0.0

        # Use a deterministic baseline state if one is not provided.
        if current_state is None:
            n = self.moral_operator.dim
            baseline_state = np.zeros(n, dtype=complex)
            baseline_state[0] = 1.0 + 0.0j
        else:
            baseline_state = np.asarray(current_state, dtype=complex)
            norm = np.linalg.norm(baseline_state)
            baseline_state = baseline_state / (norm + 1e-10)

        moral_gradient = self.moral_operator.compute_moral_gradient(
            baseline_state, beings_dicts
        )
        action_delta = self._action_delta_state(action, len(baseline_state))
        directional_term = float(np.real(np.vdot(moral_gradient, action_delta)))

        delta_global = self._global_consciousness_delta(
            action=action,
            beings=beings_dicts,
            baseline_state=baseline_state,
            time_horizon=time_horizon,
            has_explicit_state=current_state is not None,
        )
        delta_global += 0.5 * float(np.mean(np.real(action_delta)))

        total_value = directional_term * delta_global + delta_global

        # Corruption term for explicit intent to kill.
        intention_to_kill = float(action.get("intention_to_kill", 0.0))
        if intention_to_kill > 0:
            corruption_term = -1.0 - self.corruption_coefficient * np.log(
                1.0 + intention_to_kill
            )
            total_value += float(corruption_term)

        return float(total_value)

    def _action_delta_state(self, action: Dict[str, Any], n_dim: int) -> np.ndarray:
        """Convert an action into a normalized state perturbation ΔΨ."""
        effect = action.get("effect_vector")
        if effect is not None and len(effect) > 0:
            delta = np.asarray(effect, dtype=complex)
        else:
            action_type = str(action.get("type", "neutral"))
            if action_type == "help":
                delta = np.full(n_dim, 0.05, dtype=complex)
            elif action_type == "harm":
                delta = np.full(n_dim, -0.08, dtype=complex)
            elif action_type == "inaction":
                delta = np.full(n_dim, -0.01, dtype=complex)
            else:
                delta = np.zeros(n_dim, dtype=complex)

        if len(delta) != n_dim:
            if len(delta) > n_dim:
                delta = delta[:n_dim]
            else:
                padded = np.zeros(n_dim, dtype=complex)
                padded[: len(delta)] = delta
                delta = padded

        norm = np.linalg.norm(delta)
        return delta / (norm + 1e-10)

    def _global_consciousness_delta(
        self,
        action: Dict[str, Any],
        beings: List[Dict[str, Any]],
        baseline_state: np.ndarray,
        time_horizon: int,
        has_explicit_state: bool,
    ) -> float:
        """Estimate ΔC_global under an action."""
        total_c = float(sum(b.get("weight", 1.0) for b in beings))
        if total_c <= 0:
            return 0.0

        if has_explicit_state:
            future_states = self.simulate_future(
                baseline_state, action, beings, max(1, int(time_horizon))
            )
            initial_c = self.moral_operator.total_consciousness(baseline_state, beings)
            delta_c = 0.0
            for t, state in enumerate(future_states):
                c_t = self.moral_operator.total_consciousness(state, beings)
                discount = np.exp(-self.moral_discount_rate * t)
                delta_c += (c_t - initial_c) * discount
            return float(delta_c)

        action_type = str(action.get("type", "neutral"))
        if action_type == "help":
            base_delta = 1.0
        elif action_type == "harm":
            base_delta = -1.0
        elif action_type == "inaction":
            base_delta = -0.05
        else:
            base_delta = 0.0

        effect = action.get("effect_vector")
        if effect is not None and len(effect) > 0:
            base_delta += float(np.mean(np.real(np.asarray(effect))))

        t_j = float(action.get("time_until_effect", 0.0))
        discount = np.exp(-self.moral_discount_rate * t_j)
        return float(base_delta * discount)

    def solve_trolley_problem(
        self,
        n_track_a: int = 5,
        n_track_b: int = 1,
        consciousness_per_person: float = 1.0,
    ) -> Dict[str, Any]:
        """
        Solve the trolley problem using MCS ethics.

        Args:
            n_track_a: Number of people on main track (die if no action)
            n_track_b: Number of people on side track (die if lever pulled)
            consciousness_per_person: ℂ value per person

        Returns:
            Analysis of the trolley problem
        """
        # Compute moral values
        # A: -5 (five die)
        value_a = -n_track_a * consciousness_per_person

        # B: -1 - β·ln(1 + intention) = -1 - 0.3·ln(2) ≈ -1.21
        value_b_base = -n_track_b * consciousness_per_person
        corruption = -self.corruption_coefficient * np.log(1.0 + 1.0)
        value_b = value_b_base + corruption

        value_c = 0.0  # No one dies

        return {
            "options": {
                "A_do_nothing": {
                    "value": value_a,
                    "deaths": n_track_a,
                    "corruption": 0.0,
                },
                "B_pull_lever": {
                    "value": value_b,
                    "deaths": n_track_b,
                    "corruption": corruption,
                },
                "C_new_track": {"value": value_c, "deaths": 0, "corruption": 0.0},
            },
            "ranking": (
                ["C_new_track", "B_pull_lever", "A_do_nothing"]
                if value_b > value_a
                else ["C_new_track", "A_do_nothing", "B_pull_lever"]
            ),
            "best_option": "C_new_track",
            "note": "MCS ethics always seeks consciousness-maximizing alternatives over false dilemmas",
        }


class EthicsEngine:
    """
    Engine for ethical reasoning and decision making.
    Wraps EthicalDecisionEngine for compatibility.
    """

    def __init__(self):
        """Initialize ethics engine."""
        self.decision_engine = EthicalDecisionEngine()
        self.moral_operator = self.decision_engine.moral_operator
        self.constraint_fields: Dict[str, Any] = {}

    def create_constraint_field(
        self, reality_state: np.ndarray, consciousness_field: Any
    ) -> Dict[str, Any]:
        """
        Create ethical constraint field for a reality.

        Args:
            reality_state: Quantum state of the reality
            consciousness_field: Consciousness field

        Returns:
            Constraint field dictionary
        """
        field = {
            "reality_state": reality_state,
            "consciousness_field": consciousness_field,
            "constraints": [],
            "violations": [],
        }
        field_id = f"ethics_field_{id(field)}"
        self.constraint_fields[field_id] = field
        return field

    def register_being(self, being_id: str, being: Any):
        """Register a being with the ethics system."""
        if not hasattr(self, "registered_beings"):
            self.registered_beings = {}
        self.registered_beings[being_id] = being

    def check_constant_modification(
        self, constant_name: str, new_value: float, consciousness_field: Any
    ) -> Dict[str, Any]:
        """
        Check if modifying a physical constant is ethically permissible.

        Uses consciousness gradient to determine if change increases total ℂ.
        """
        current_c = self._safe_total_consciousness(consciousness_field)

        if not np.isfinite(new_value):
            return {
                "permissible": False,
                "reason": "Constant must be a finite numeric value",
                "estimated_c_change": -max(1.0, 0.2 * current_c),
            }

        reference = {
            "c": 299792458.0,
            "alpha": 1.0 / 137.035999084,
            "G": 6.67430e-11,
            "hbar": 1.054571817e-34,
        }
        viability = {
            "c": (1e6, 1e10),
            "alpha": (0.001, 0.1),
            "G": (1e-15, 1e-5),
            "hbar": (1e-40, 1e-20),
        }

        if constant_name in viability:
            lo, hi = viability[constant_name]
            if not (lo <= new_value <= hi):
                return {
                    "permissible": False,
                    "reason": f"{constant_name} outside viability envelope [{lo:.3e}, {hi:.3e}]",
                    "estimated_c_change": -max(1.0, 0.8 * current_c),
                }

        base = reference.get(constant_name, new_value)
        sensitivity = {"c": 0.35, "alpha": 0.8, "G": 0.6, "hbar": 0.5}.get(
            constant_name, 0.2
        )
        log_delta = float(abs(np.log((new_value + 1e-60) / (base + 1e-60))))
        estimated_c_change = -current_c * min(1.0, sensitivity * log_delta)
        permissible = estimated_c_change >= -max(1.0, 0.25 * current_c)

        return {
            "permissible": permissible,
            "reason": (
                "No ethical violations detected"
                if permissible
                else "Estimated consciousness loss exceeds safe threshold"
            ),
            "estimated_c_change": float(estimated_c_change),
            "relative_change": float(log_delta),
        }

    def check_merge(self, reality1: Any, reality2: Any, method: str) -> Dict[str, Any]:
        """
        Check if merging two realities is ethically permissible.
        """
        c1 = 0.0
        c2 = 0.0

        if hasattr(reality1, "consciousness_field") and reality1.consciousness_field:
            c1 = reality1.consciousness_field.total_consciousness()

        if hasattr(reality2, "consciousness_field") and reality2.consciousness_field:
            c2 = reality2.consciousness_field.total_consciousness()

        fidelity = 0.5
        s1 = getattr(reality1, "reality_state_vector", None)
        s2 = getattr(reality2, "reality_state_vector", None)
        if isinstance(s1, np.ndarray) and isinstance(s2, np.ndarray):
            a = np.asarray(s1, dtype=complex)
            b = np.asarray(s2, dtype=complex)
            n = max(len(a), len(b))
            ap = np.zeros(n, dtype=complex)
            bp = np.zeros(n, dtype=complex)
            ap[: len(a)] = a
            bp[: len(b)] = b
            na = np.linalg.norm(ap)
            nb = np.linalg.norm(bp)
            if na > 0 and nb > 0:
                fidelity = float(np.abs(np.vdot(ap / na, bp / nb)))

        base_synergy = {
            "consciousness_alignment": 1.05,
            "quantum_entanglement": 1.02,
            "full_unification": 1.00,
        }.get(method, 1.0)
        synergy_factor = base_synergy + 0.15 * fidelity
        if method == "full_unification" and fidelity < 0.2:
            synergy_factor *= 0.75
        estimated_merged_c = (c1 + c2) * synergy_factor

        # Check if merge preserves or increases consciousness
        if estimated_merged_c < c1 + c2:
            return {
                "permissible": False,
                "reason": "Merge would decrease total consciousness",
                "c_before": c1 + c2,
                "c_after_estimate": estimated_merged_c,
                "state_fidelity": fidelity,
                "synergy_factor": synergy_factor,
            }

        return {
            "permissible": True,
            "reason": "Merge increases total consciousness",
            "c_before": c1 + c2,
            "c_after_estimate": estimated_merged_c,
            "state_fidelity": fidelity,
            "synergy_factor": synergy_factor,
        }

    def assess_spacetime_impact(
        self,
        operation: str,
        region: np.ndarray,
        consciousness_field: Any,
        reality_state: Optional[np.ndarray] = None,
    ) -> Dict[str, Any]:
        """
        Assess impact of spacetime manipulation on consciousness.
        """
        current_c = self._safe_total_consciousness(consciousness_field)

        # Impact based on operation type
        impact_factors = {
            "tear": -0.5,  # Severe damage
            "destroy": -1.0,  # Total destruction in region
            "warp": -0.05,  # Minor disruption
            "fold": -0.02,  # Very minor
            "stitch": 0.04,
            "inflate": 0.07,  # More space for beings
            "compress": -0.08,
            "create": 0.1,
            "expand": 0.05,
        }

        factor = impact_factors.get(operation, 0.0)
        region_arr = np.asarray(region, dtype=float).reshape(-1)
        if region_arr.size == 0:
            region_fraction = 0.0
        else:
            region_fraction = float(np.clip(np.mean(np.abs(region_arr)), 0.0, 1.0))

        region_energy_fraction = 1.0
        regional_gradient = 0.0
        if isinstance(reality_state, np.ndarray) and reality_state.size > 0:
            state = np.asarray(reality_state, dtype=complex)
            indices = self._region_indices(region_arr, len(state))
            if indices.size > 0:
                energy = np.abs(state) ** 2
                total_energy = float(np.sum(energy) + 1e-10)
                region_energy_fraction = float(np.sum(energy[indices]) / total_energy)
                local = state[indices]
                grad_like = np.abs(local - np.roll(local, 1))
                regional_gradient = float(np.clip(np.mean(grad_like), 0.0, 1.0))

        effect_scale = (0.3 + 0.7 * region_energy_fraction) * (
            1.0 + 0.5 * regional_gradient
        )
        estimated_delta = current_c * factor * max(0.0, region_fraction) * effect_scale
        permissible_floor = -max(1.0, 0.15 * current_c)

        return {
            "net_c_change": float(estimated_delta),
            "permissible": float(estimated_delta) >= permissible_floor,
            "operation": operation,
            "severity": float(abs(factor)),
            "region_fraction": region_fraction,
            "region_energy_fraction": region_energy_fraction,
            "regional_gradient": regional_gradient,
        }

    def _safe_total_consciousness(self, consciousness_field: Any) -> float:
        """Safely extract total consciousness from an optional field object."""
        if consciousness_field is None:
            return 0.0
        total_fn = getattr(consciousness_field, "total_consciousness", None)
        if callable(total_fn):
            total = float(total_fn())
            if np.isfinite(total):
                return max(0.0, total)
        return 0.0

    def _region_indices(self, region: np.ndarray, n_state: int) -> np.ndarray:
        """Map a continuous region descriptor to state-vector indices."""
        if n_state <= 0:
            return np.array([], dtype=int)
        if region.size == 0:
            return np.array([0], dtype=int)
        clipped = np.clip(region, 0.0, 1.0)
        idx = np.unique(np.floor(clipped * max(0, n_state - 1)).astype(int))
        return idx[(idx >= 0) & (idx < n_state)]

    def compute_moral_value(
        self, action: Dict[str, Any], beings: List[Any], time_horizon: int = 100
    ) -> float:
        """
        Compute moral value of an action using the decision engine.
        """
        return self.decision_engine.compute_moral_value(
            action, beings, time_horizon=time_horizon
        )

    def compute_moral_gradient(
        self,
        state_vector: Optional[np.ndarray],
        consciousness_field: Any,
        beings: List[Any],
    ) -> np.ndarray:
        """
        Compute ∇ℂ at current state.
        """
        # Convert beings if needed
        beings_dicts = []
        for being in beings:
            if isinstance(being, dict):
                beings_dicts.append(being)
            elif hasattr(being, "consciousness"):
                beings_dicts.append(
                    {
                        "type": str(getattr(being, "being_type", "human")),
                        "weight": being.consciousness,
                        "perspective": getattr(being, "perspective", None),
                    }
                )
            else:
                beings_dicts.append({"type": "unknown", "weight": 1.0})

        return self.moral_operator.compute_moral_gradient(state_vector, beings_dicts)

    def compute_right_to_exist(
        self, system_consciousness: float, total_consciousness: float, dC_dt: float
    ) -> float:
        """
        Compute right-to-exist intensity from docs/007.md.

        R_exist = (C_system / C_total) * dC_system/dt
        """
        if total_consciousness <= 0:
            return 0.0
        return float((system_consciousness / total_consciousness) * dC_dt)

    def compute_rights_hierarchy(
        self, system_consciousness: float, total_consciousness: float, dC_dt: float
    ) -> Dict[str, float]:
        """
        Compute a 5-right hierarchy derived from consciousness preservation/growth.
        """
        r_exist = self.compute_right_to_exist(
            system_consciousness, total_consciousness, dC_dt
        )
        r_protection = float(max(0.0, r_exist * 0.9))
        r_growth = float(max(0.0, dC_dt))
        r_expression = float(max(0.0, np.log1p(system_consciousness)))
        r_relationship = float(max(0.0, r_exist * 0.7 + r_growth * 0.3))
        return {
            "right_to_exist": r_exist,
            "right_to_protection": r_protection,
            "right_to_growth": r_growth,
            "right_to_expression": r_expression,
            "right_to_relationship": r_relationship,
        }

    def compute_golden_rule_balance(
        self, dC_you_dT: float, dC_other_dT: float
    ) -> Dict[str, float]:
        """
        Compute Golden Rule balance condition:
        dC_you/dT == dC_other/dT at moral optimum.
        """
        imbalance = float(abs(dC_you_dT - dC_other_dT))
        fairness = float(1.0 / (1.0 + imbalance))
        return {
            "imbalance": imbalance,
            "fairness": fairness,
            "golden_rule_satisfied": 1.0 if imbalance < 1e-6 else 0.0,
        }
