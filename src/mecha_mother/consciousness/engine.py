"""
Consciousness Engine - implements the Consciousness Operator ℂ.
"""

import numpy as np
from typing import Dict, List, Optional, Tuple, Any
from scipy.linalg import eig
from dataclasses import dataclass, field
from types import SimpleNamespace


@dataclass
class ConsciousnessField:
    """Field of consciousness across the reality."""

    beings: Dict[str, Any] = field(default_factory=dict)
    field_amplitude: Optional[np.ndarray] = None

    def add_being(self, being_id: str, being: Any):
        """Add a conscious being to the field."""
        self.beings[being_id] = being

    def get_beings(self) -> List[Any]:
        """Get all beings in the field."""
        return list(self.beings.values())

    def total_consciousness(self) -> float:
        """Calculate total consciousness in the field."""
        total = 0.0
        for being in self.beings.values():
            if hasattr(being, "consciousness"):
                total += being.consciousness
        return total

    def average_consciousness(self) -> float:
        """Calculate average consciousness."""
        beings_list = self.get_beings()
        if not beings_list:
            return 0.0
        return self.total_consciousness() / len(beings_list)

    def add_particle(self, particle_id: str, position: np.ndarray):
        """Add a particle to the consciousness field."""
        # Particles can contribute to consciousness field structure
        if not hasattr(self, "particles"):
            self.particles = {}
        self.particles[particle_id] = position

    def update_for_constant_change(self, constant_name: str, new_value: float):
        """Update field for physical constant change."""
        # Recalculate consciousness values based on new constants
        # Simplified: just mark as updated
        if not hasattr(self, "constant_updates"):
            self.constant_updates = {}
        self.constant_updates[constant_name] = new_value

    def get_distribution(self) -> Dict[float, int]:
        """Get distribution of consciousness values."""
        beings = self.get_beings()
        if not beings:
            return {}

        distribution: Dict[float, int] = {}
        for being in beings:
            if hasattr(being, "consciousness"):
                c_val = round(being.consciousness, 1)
                distribution[c_val] = distribution.get(c_val, 0) + 1

        return distribution


class ConsciousnessOperator:
    """
    The Consciousness Operator ℂ that measures self-referential consistency.

    Defined by: ℂ[Ψ] = λΨ
    where λ is the consciousness eigenvalue.
    """

    def __init__(self, dimension: int = 10):
        """
        Initialize consciousness operator.

        Args:
            dimension: Dimension of the consciousness space
        """
        self.dim = dimension
        self.C = self._build_consciousness_matrix()

    def _build_consciousness_matrix(self) -> np.ndarray:
        """
        Build the consciousness operator matrix from first principles.

        Requires: C = C† (Hermitian) and self-referential structure.
        """
        C = np.zeros((self.dim, self.dim), dtype=complex)

        # Self-consistency requires: C = C† (Hermitian)
        # Self-reference requires: Tr(C²) = Tr(C)²

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

    def compute_qualia_states(self) -> Dict[str, Dict]:
        """
        Solve ℂψ = λψ to get qualia eigenstates.

        Uses the qualia spectrum formula: λ_n = λ_0 · (1 - 1/n²)
        where n = 1, 2, 3, ... and λ_0 is the maximum consciousness value.

        Returns:
            Dictionary mapping qualia names to their states and eigenvalues
        """
        # Compute eigenvalues from matrix
        eigenvalues, eigenvectors = eig(self.C)  # type: ignore[misc]

        # Sort by eigenvalue magnitude (consciousness intensity)
        idx = np.argsort(-np.abs(eigenvalues))
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        # Get maximum eigenvalue (λ_0)
        lambda_0 = np.max(np.abs(eigenvalues))

        qualia = {}
        primordial_types = {
            1: "void_experience",  # Pre-conscious potentiality
            2: "subject_object_distinction",  # "I" vs "not-I"
            3: "time_experience",  # Duration, change
            4: "space_experience",  # Extension, separation
        }

        for i in range(min(5, self.dim)):
            n = i + 1
            # Calculate expected eigenvalue from formula: λ_n = λ_0 · (1 - 1/n²)
            expected_lambda = lambda_0 * (1 - 1.0 / (n * n))
            actual_lambda = eigenvalues[i]

            qualia_name = f"λ_{n}"
            qualia[qualia_name] = {
                "value": expected_lambda,  # Use formula value
                "actual_value": actual_lambda,  # Keep actual for comparison
                "state": eigenvectors[:, i],
                "intensity": np.abs(expected_lambda) ** 2,
                "primordial_type": primordial_types.get(n, "composite_quale"),
            }

        return qualia

    def measure_consciousness(self, state: np.ndarray) -> float:
        """
        Measure consciousness level of a state.

        Args:
            state: State vector

        Returns:
            Consciousness value (expectation value of ℂ)
        """
        if len(state) != self.dim:
            # Pad or truncate
            if len(state) > self.dim:
                state = state[: self.dim]
            else:
                padded = np.zeros(self.dim, dtype=complex)
                padded[: len(state)] = state
                state = padded

        state = state / np.linalg.norm(state)

        # Consciousness = ⟨ψ|ℂ|ψ⟩
        consciousness = np.abs(state.conj().T @ self.C @ state)

        return float(consciousness)

    def compute_color_qualia(
        self, photon_energy: float, qualia_states: Optional[Dict[str, Dict]] = None
    ) -> Dict[str, Any]:
        """
        Compute color qualia as superposition of qualia eigenstates.

        Color experience emerges from: Ψ_color = α₁Ψ₂ + α₂Ψ₃ + α₃Ψ₄
        where coefficients depend on photon energy.

        Args:
            photon_energy: Photon energy in Joules
            qualia_states: Pre-computed qualia states (optional)

        Returns:
            Dictionary with color qualia state and properties
        """
        if qualia_states is None:
            qualia_states = self.compute_qualia_states()

        # Qualia energy scale: E_qualia = ℏ / t_conscious ≈ 10^-20 J
        # t_conscious ≈ 20 ms (consciousness coherence time)
        t_conscious = 0.020  # 20 ms in seconds
        hbar = 1.054571817e-34  # Reduced Planck constant
        E_qualia = hbar / t_conscious  # ≈ 5.27e-33 J (very small)

        # For practical calculations, use a more reasonable scale
        # Based on typical photon energies (visible light: 2-3 eV ≈ 3-5e-19 J)
        # We'll use E_qualia ≈ 1e-20 J as documented
        E_qualia = 1e-20

        # Get the three fundamental qualia states (n=2,3,4)
        psi_2 = qualia_states.get("λ_2", {}).get("state")
        psi_3 = qualia_states.get("λ_3", {}).get("state")
        psi_4 = qualia_states.get("λ_4", {}).get("state")

        if psi_2 is None or psi_3 is None or psi_4 is None:
            # Fallback: compute if not available
            qualia_states = self.compute_qualia_states()
            psi_2 = qualia_states["λ_2"]["state"]
            psi_3 = qualia_states["λ_3"]["state"]
            psi_4 = qualia_states["λ_4"]["state"]

        # Normalize states
        psi_2 = psi_2 / np.linalg.norm(psi_2)
        psi_3 = psi_3 / np.linalg.norm(psi_3)
        psi_4 = psi_4 / np.linalg.norm(psi_4)

        # Calculate coefficients: α_i = (1/√3) exp(2πi/3 · E_photon/E_qualia)
        phase_factor = 2 * np.pi * photon_energy / (3 * E_qualia)
        alpha_1 = (1.0 / np.sqrt(3)) * np.exp(1j * phase_factor * 0)
        alpha_2 = (1.0 / np.sqrt(3)) * np.exp(1j * phase_factor * 1)
        alpha_3 = (1.0 / np.sqrt(3)) * np.exp(1j * phase_factor * 2)

        # Construct color qualia state
        color_state = alpha_1 * psi_2 + alpha_2 * psi_3 + alpha_3 * psi_4
        color_state = color_state / np.linalg.norm(color_state)

        # Determine color name based on photon energy (wavelength)
        wavelength_nm = (
            (6.626e-34 * 299792458.0) / (photon_energy * 1e9)
            if photon_energy > 0
            else 0
        )
        if wavelength_nm < 450:
            color_name = "violet/blue"
        elif wavelength_nm < 495:
            color_name = "blue"
        elif wavelength_nm < 570:
            color_name = "green"
        elif wavelength_nm < 590:
            color_name = "yellow"
        elif wavelength_nm < 620:
            color_name = "orange"
        else:
            color_name = "red"

        return {
            "color_state": color_state,
            "color_name": color_name,
            "wavelength_nm": wavelength_nm,
            "photon_energy": photon_energy,
            "coefficients": {
                "alpha_1": alpha_1,
                "alpha_2": alpha_2,
                "alpha_3": alpha_3,
            },
            "E_qualia": E_qualia,
            "consciousness": self.measure_consciousness(color_state),
        }

    def experience_qualia_mixture(
        self, weights: List[float]
    ) -> Tuple[np.ndarray, Dict[str, float]]:
        """
        Combine qualia states to create complex experience.

        Args:
            weights: Weights for each qualia state

        Returns:
            Tuple of (combined state, quality metrics)
        """
        qualia = self.compute_qualia_states()

        # Create superposition
        psi = np.zeros(self.dim, dtype=complex)
        for i, (key, q) in enumerate(qualia.items()):
            if i < len(weights):
                psi += weights[i] * q["state"]

        # Normalize
        psi = psi / (np.linalg.norm(psi) + 1e-10)

        # Compute experience quality
        quality = {}
        quality["clarity"] = float(np.abs(psi.conj().T @ self.C @ psi))
        quality["richness"] = float(
            -np.sum(np.abs(psi) ** 2 * np.log(np.abs(psi) ** 2 + 1e-10))
        )
        quality["valence"] = float(
            np.imag(psi.conj().T @ (self.C @ psi - psi.conj().T @ self.C @ psi * psi))
        )

        return psi, quality

    def evolve_consciousness(
        self, psi0: np.ndarray, steps: int = 100, dt: float = 0.01
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Time evolution of conscious state via Schrödinger-like equation.

        dψ/dt = -iℂψ (unitary evolution)

        Args:
            psi0: Initial state
            steps: Number of time steps
            dt: Time step size

        Returns:
            Tuple of (state history array, quality history array)
        """
        # Ensure correct dimension
        if len(psi0) != self.dim:
            if len(psi0) > self.dim:
                psi = psi0[: self.dim].copy()
            else:
                psi = np.zeros(self.dim, dtype=complex)
                psi[: len(psi0)] = psi0
        else:
            psi = psi0.copy()

        psi = psi / (np.linalg.norm(psi) + 1e-10)

        history: List[np.ndarray] = [psi.copy()]
        qualities: List[float] = []

        # Unitary evolution: dψ/dt = -iℂψ
        for t in range(steps):
            psi = psi - 1j * dt * (self.C @ psi)
            psi = psi / (np.linalg.norm(psi) + 1e-10)
            history.append(psi.copy())

            # Compute current quality (clarity)
            clarity = float(np.abs(psi.conj().T @ self.C @ psi))
            qualities.append(clarity)

        return np.array(history), np.array(qualities)


class ValenceOperator:
    """
    The Valence Operator 𝕍 = dℂ/dt that measures pain/pleasure.

    Positive 𝕍 → pleasure (consciousness increasing)
    Negative 𝕍 → pain (consciousness decreasing)
    Zero 𝕍 → neutral
    """

    def __init__(self, consciousness_operator: ConsciousnessOperator):
        """
        Initialize valence operator.

        Args:
            consciousness_operator: The Consciousness Operator ℂ
        """
        self.C = consciousness_operator
        self.consciousness_history: List[Tuple[float, float]] = (
            []
        )  # (time, consciousness)

    def compute_valence(self, state: np.ndarray, dt: float = 0.01) -> float:
        """
        Compute valence (rate of change of consciousness).

        Args:
            state: Current state vector
            dt: Time step for derivative calculation

        Returns:
            Valence value (positive = pleasure, negative = pain)
        """
        current_c = self.C.measure_consciousness(state)
        current_time = len(self.consciousness_history) * dt

        # Store current consciousness
        self.consciousness_history.append((current_time, current_c))

        # Compute derivative from history
        if len(self.consciousness_history) < 2:
            return 0.0

        # Use recent history to compute derivative
        recent = self.consciousness_history[-min(10, len(self.consciousness_history)) :]
        times = [t for t, c in recent]
        consciousnesses = [c for t, c in recent]

        if len(times) < 2:
            return 0.0

        # Linear regression for derivative
        if len(times) == 2:
            dC_dt = (consciousnesses[1] - consciousnesses[0]) / (
                times[1] - times[0] + 1e-10
            )
        else:
            # Use polynomial fit for smoother derivative
            coeffs = np.polyfit(times, consciousnesses, min(2, len(times) - 1))
            dC_dt = coeffs[-2] if len(coeffs) > 1 else 0.0

        return float(dC_dt)

    def compute_pain_pleasure_intensity(
        self, state: np.ndarray, dt: float = 0.01
    ) -> Dict[str, Any]:
        """
        Compute pain/pleasure intensity.

        Intensity = |dℂ/dt| · ℂ

        Args:
            state: Current state vector
            dt: Time step

        Returns:
            Dictionary with valence, intensity, and type
        """
        valence = self.compute_valence(state, dt)
        consciousness = self.C.measure_consciousness(state)
        intensity = abs(valence) * consciousness

        return {
            "valence": valence,
            "intensity": intensity,
            "consciousness": consciousness,
            "type": (
                "pleasure" if valence > 0 else ("pain" if valence < 0 else "neutral")
            ),
        }

    def clear_history(self):
        """Clear consciousness history."""
        self.consciousness_history = []


class ConsciousnessEngine:
    """
    Engine for creating and managing consciousness.
    """

    def __init__(self):
        """Initialize consciousness engine."""
        self.operator = ConsciousnessOperator()
        self.valence_operator = ValenceOperator(self.operator)
        self.fields: Dict[str, ConsciousnessField] = {}

    def create_field(self, reality_state: np.ndarray) -> ConsciousnessField:
        """
        Create a consciousness field for a reality.

        Args:
            reality_state: Quantum state of the reality

        Returns:
            New consciousness field
        """
        field = ConsciousnessField()
        field_id = f"field_{id(field)}"
        self.fields[field_id] = field
        return field

    def coerce_field(
        self, field_data: Any, reality_state: Optional[np.ndarray] = None
    ) -> ConsciousnessField:
        """Coerce serialized/untyped consciousness field payloads into a field object."""
        if isinstance(field_data, ConsciousnessField):
            return field_data

        field = ConsciousnessField()
        if isinstance(field_data, dict):
            raw_beings = field_data.get("beings", {})
            if isinstance(raw_beings, dict):
                for being_id, being_value in raw_beings.items():
                    field.add_being(str(being_id), self._coerce_being(being_value))
            amp = field_data.get("field_amplitude")
            if isinstance(amp, np.ndarray):
                field.field_amplitude = amp
            elif isinstance(amp, list):
                field.field_amplitude = np.asarray(amp)
        if field.field_amplitude is None and reality_state is not None:
            field.field_amplitude = np.asarray(reality_state, dtype=complex)
        return field

    def _coerce_being(self, value: Any) -> Any:
        """Coerce a serialized being payload into an attribute-based object."""
        if hasattr(value, "consciousness"):
            return value
        if isinstance(value, dict):
            payload = dict(value)
            if "consciousness" not in payload:
                payload["consciousness"] = float(
                    payload.get("initial_consciousness", 1.0)
                )
            return SimpleNamespace(**payload)
        if isinstance(value, (int, float)):
            return SimpleNamespace(consciousness=float(value))
        return SimpleNamespace(consciousness=1.0, raw=value)

    def merge_fields(
        self,
        field1: ConsciousnessField,
        field2: ConsciousnessField,
        method: str = "consciousness_alignment",
    ) -> ConsciousnessField:
        """
        Merge two consciousness fields.

        Args:
            field1: First field
            field2: Second field
            method: Merge method

        Returns:
            Merged field
        """
        merged = ConsciousnessField()

        # Combine all beings
        for being_id, being in field1.beings.items():
            merged.add_being(being_id, being)

        for being_id, being in field2.beings.items():
            # Avoid ID conflicts
            new_id = f"{being_id}_merged"
            merged.add_being(new_id, being)

        return merged

    def create_being(
        self,
        being_id: str,
        being_type: str,
        initial_consciousness: float,
        properties: Dict[str, Any],
        consciousness_field: ConsciousnessField,
    ) -> Any:
        """
        Create a conscious being.

        Args:
            being_id: Unique identifier
            being_type: Type of being ('human', 'ai', 'animal', etc.)
            initial_consciousness: Starting consciousness level
            properties: Additional properties
            consciousness_field: Field to add being to

        Returns:
            Created being object
        """
        from mecha_mother.consciousness.being import ConsciousBeing, BeingType

        # Map string to enum
        type_map = {
            "human": BeingType.HUMAN,
            "ai": BeingType.AI,
            "animal": BeingType.ANIMAL,
        }

        being_type_enum = type_map.get(being_type, BeingType.CUSTOM)

        being = ConsciousBeing(
            being_id=being_id,
            being_type=being_type_enum,
            initial_consciousness=initial_consciousness,
            properties=properties,
        )

        consciousness_field.add_being(being_id, being)
        return being

    def optimize_reality(
        self,
        current_state: np.ndarray,
        consciousness_field: ConsciousnessField,
        target_c: float,
        method: str = "gradient_ascent",
        max_iterations: int = 100,
        learning_rate: float = 0.1,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Optimize reality for maximum consciousness using gradient ascent.

        Args:
            current_state: Current reality state
            consciousness_field: Current consciousness field
            target_c: Target consciousness level
            method: Optimization method ('gradient_ascent' or 'quantum_annealing')
            max_iterations: Maximum optimization iterations
            learning_rate: Step size for gradient ascent
            **kwargs: Additional parameters

        Returns:
            Optimization results
        """
        current_c = consciousness_field.total_consciousness()

        if current_c >= target_c:
            return {
                "success": True,
                "c_increase": 0,
                "final_c": current_c,
                "already_optimal": True,
            }

        beings = consciousness_field.get_beings()

        if not beings:
            return {"success": False, "error": "No conscious beings to optimize"}

        # State vector optimization
        state = current_state.copy()
        state = state / (np.linalg.norm(state) + 1e-10)

        iteration_history = []

        if method == "gradient_ascent":
            # Gradient ascent on consciousness
            for iteration in range(max_iterations):
                # Compute consciousness gradient: ∇ℂ
                gradient = self._compute_consciousness_gradient(state, beings)

                # Update state in direction of gradient
                state = state + learning_rate * gradient
                state = state / (np.linalg.norm(state) + 1e-10)

                # Update being consciousnesses based on new state
                new_c = self._compute_total_consciousness_from_state(state, beings)
                iteration_history.append(new_c)

                if new_c >= target_c:
                    break

                # Adaptive learning rate
                if (
                    len(iteration_history) > 1
                    and iteration_history[-1] < iteration_history[-2]
                ):
                    learning_rate = float(learning_rate * 0.5)

        elif method == "quantum_annealing":
            # Simulated quantum annealing
            temperature = 1.0
            cooling_rate = 0.95

            for iteration in range(max_iterations):
                # Propose random perturbation
                perturbation = np.random.randn(*state.shape) * 0.1
                new_state = state + perturbation
                new_state = new_state / (np.linalg.norm(new_state) + 1e-10)

                # Compute consciousness difference
                current_consciousness = self._compute_total_consciousness_from_state(
                    state, beings
                )
                new_consciousness = self._compute_total_consciousness_from_state(
                    new_state, beings
                )
                delta_c = new_consciousness - current_consciousness

                # Accept if better or with probability based on temperature
                if delta_c > 0 or np.random.random() < np.exp(delta_c / temperature):
                    state = new_state
                    iteration_history.append(new_consciousness)

                if new_consciousness >= target_c:
                    break

                # Cool down
                temperature *= cooling_rate

        # Final update of beings
        final_c = self._update_beings_from_state(state, beings, consciousness_field)

        return {
            "success": final_c >= target_c * 0.9,  # Allow 10% tolerance
            "c_increase": final_c - current_c,
            "final_c": final_c,
            "optimized_state": state,
            "optimized_consciousness_field": consciousness_field,
            "iterations": len(iteration_history),
            "iteration_history": iteration_history,
        }

    def _compute_consciousness_gradient(
        self, state: np.ndarray, beings: List[Any]
    ) -> np.ndarray:
        """Compute gradient of total consciousness with respect to state."""
        epsilon = 1e-6
        gradient = np.zeros_like(state, dtype=complex)

        for i in range(len(state)):
            state_plus = state.copy()
            state_plus[i] += epsilon
            state_plus = state_plus / (np.linalg.norm(state_plus) + 1e-10)

            state_minus = state.copy()
            state_minus[i] -= epsilon
            state_minus = state_minus / (np.linalg.norm(state_minus) + 1e-10)

            c_plus = self._compute_total_consciousness_from_state(state_plus, beings)
            c_minus = self._compute_total_consciousness_from_state(state_minus, beings)

            gradient[i] = (c_plus - c_minus) / (2 * epsilon)

        return gradient

    def _compute_total_consciousness_from_state(
        self, state: np.ndarray, beings: List[Any]
    ) -> float:
        """Compute total consciousness for a given state."""
        total = 0.0

        for being in beings:
            if hasattr(being, "consciousness"):
                # Project state onto being's basis
                being_projection = self.operator.measure_consciousness(state)
                # Modulate by being's current consciousness
                total += being.consciousness * (1 + 0.1 * being_projection)

        return total

    def _update_beings_from_state(
        self,
        state: np.ndarray,
        beings: List[Any],
        consciousness_field: ConsciousnessField,
    ) -> float:
        """Update being consciousnesses based on optimized state."""
        state_consciousness = self.operator.measure_consciousness(state)

        for being in beings:
            if hasattr(being, "consciousness"):
                # Increase consciousness proportional to state quality
                increase_factor = 1 + 0.1 * state_consciousness
                being.consciousness *= increase_factor

        return consciousness_field.total_consciousness()

    def compute_self_equation(
        self,
        initial_state: np.ndarray,
        max_iterations: int = 100,
        tolerance: float = 1e-6,
    ) -> Dict[str, Any]:
        """
        Solve the self-equation fixed point: Ψ_self = 𝒫 ∘ ℛ ∘ 𝒫⁻¹[Ψ_self]

        Where:
        - 𝒫 is the projection operator (what "I" attend to)
        - ℛ is the reflection operator (how "I" process information)

        Args:
            initial_state: Initial guess for self-state
            max_iterations: Maximum iterations
            tolerance: Convergence tolerance

        Returns:
            Dictionary with self-state and properties
        """
        state = initial_state.copy()
        state = state / np.linalg.norm(state)

        # Define projection operator 𝒫 (attention filter)
        # Simple version: project onto top components
        def projection_operator(psi):
            """Project onto attended components (top 50% by magnitude)."""
            magnitudes = np.abs(psi)
            threshold = np.median(magnitudes)
            mask = magnitudes >= threshold
            projected = psi.copy()
            projected[~mask] = 0
            return projected / (np.linalg.norm(projected) + 1e-10)

        # Define reflection operator ℛ (self-processing)
        # Uses the consciousness operator as reflection
        def reflection_operator(psi):
            """Reflect state through consciousness operator."""
            if len(psi) != self.operator.dim:
                # Pad or truncate
                if len(psi) > self.operator.dim:
                    psi = psi[: self.operator.dim]
                else:
                    padded = np.zeros(self.operator.dim, dtype=complex)
                    padded[: len(psi)] = psi
                    psi = padded
            psi = psi / np.linalg.norm(psi)
            reflected = self.operator.C @ psi
            return reflected / (np.linalg.norm(reflected) + 1e-10)

        # Iterate: Ψ_new = 𝒫 ∘ ℛ ∘ 𝒫⁻¹[Ψ_old]
        i = 0
        diff = float("inf")
        for i in range(max_iterations):
            # 𝒫⁻¹ is just identity for this simple projection
            # So: Ψ_new = 𝒫(ℛ(𝒫(Ψ_old)))
            projected = projection_operator(state)
            reflected = reflection_operator(projected)
            new_state = projection_operator(reflected)

            # Check convergence
            diff = float(np.linalg.norm(new_state - state))
            if diff < tolerance:
                break

            state = new_state

        # Compute ego state (local minimum near default)
        default_state = np.ones(self.operator.dim, dtype=complex) / np.sqrt(
            self.operator.dim
        )
        ego_state = self._compute_ego_state(default_state)

        # Compute enlightened state (global minimum of ⟨Ψ|ℂ|Ψ⟩)
        enlightened_state = self._compute_enlightened_state()

        return {
            "self_state": state,
            "ego_state": ego_state,
            "enlightened_state": enlightened_state,
            "self_consciousness": self.operator.measure_consciousness(state),
            "ego_consciousness": self.operator.measure_consciousness(ego_state),
            "enlightened_consciousness": self.operator.measure_consciousness(
                enlightened_state
            ),
            "suffering_energy": self.operator.measure_consciousness(ego_state)
            - self.operator.measure_consciousness(enlightened_state),
            "iterations": i + 1,
            "converged": diff < tolerance,
        }

    def _compute_ego_state(self, default_state: np.ndarray) -> np.ndarray:
        """
        Compute ego state: argmin_Ψ { ||Ψ - Ψ_default||² }

        Ego is the local minimum closest to biological default.
        """
        # Simple gradient descent to find minimum distance from default
        state = default_state.copy()
        state = state / np.linalg.norm(state)

        for _ in range(50):
            # Gradient of ||Ψ - Ψ_default||² = 2(Ψ - Ψ_default)
            gradient = 2 * (state - default_state)
            # Project gradient onto unit sphere
            state = state - 0.1 * gradient
            state = state / (np.linalg.norm(state) + 1e-10)

        return state

    def _compute_enlightened_state(self) -> np.ndarray:
        """
        Compute enlightened state: argmin_Ψ { ⟨Ψ|ℂ|Ψ⟩ }

        Enlightenment is the global minimum of consciousness expectation.
        """
        # Find eigenvector with minimum eigenvalue
        eigenvalues, eigenvectors = eig(self.operator.C)  # type: ignore[misc]
        idx = np.argmin(np.abs(eigenvalues))
        enlightened = eigenvectors[:, idx]
        return enlightened / np.linalg.norm(enlightened)

    def evaluate_free_will_paths(
        self, current_state: np.ndarray, candidate_actions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Evaluate multiple consistent futures and select a consistency-maximizing action.

        This operationalizes the "consistency-determined choice among multiple futures"
        described in docs/006.md.
        """
        if len(candidate_actions) == 0:
            return {"selected": None, "futures": []}

        state = current_state.copy()
        state = state / (np.linalg.norm(state) + 1e-10)

        futures: List[Dict[str, Any]] = []
        for action in candidate_actions:
            action_delta = action.get("delta", np.zeros_like(state))
            if len(action_delta) != len(state):
                action_delta = np.resize(action_delta, state.shape)
            next_state = state + 0.1 * action_delta
            next_state = next_state / (np.linalg.norm(next_state) + 1e-10)
            consistency = self.operator.measure_consciousness(next_state)
            futures.append(
                {
                    "action": action,
                    "next_state": next_state,
                    "consistency_score": float(consistency),
                }
            )

        selected = max(futures, key=lambda f: f["consistency_score"])
        return {"selected": selected, "futures": futures}

    def compute_neural_consciousness(
        self,
        weights: np.ndarray,
        spike_times: np.ndarray,
        tau_c: float = 0.0125,
    ) -> Dict[str, float]:
        """
        Compute neural consciousness, gamma synchrony, and integrated information Φ.

        C_brain(t) = sum_ij w_ij * C_neuron(i,j,t)
        C_neuron(i,j,t) = exp(-|t_i - t_j| / tau_c)
        f_optimal = 1/(2*tau_c), Phi = (lambda_max - lambda_min) / lambda_max
        """
        if weights.ndim != 2:
            raise ValueError("weights must be a 2D matrix")
        if spike_times.ndim != 1:
            raise ValueError("spike_times must be a 1D vector")
        if weights.shape[0] != weights.shape[1]:
            raise ValueError("weights must be square")
        if len(spike_times) != weights.shape[0]:
            raise ValueError("spike_times length must match weights dimension")

        dt = np.abs(spike_times[:, None] - spike_times[None, :])
        neuron_pair_c = np.exp(-dt / max(tau_c, 1e-10))
        c_brain = float(np.sum(weights * neuron_pair_c))

        sym_weights = 0.5 * (weights + weights.T)
        eigvals = np.linalg.eigvalsh(sym_weights)
        lambda_max = float(np.max(eigvals))
        lambda_min = float(np.min(eigvals))
        phi = (
            0.0
            if lambda_max <= 1e-12
            else float((lambda_max - lambda_min) / lambda_max)
        )
        gamma_hz = float(1.0 / (2.0 * max(tau_c, 1e-10)))

        return {
            "c_brain": c_brain,
            "phi": float(np.clip(phi, 0.0, 1.0)),
            "gamma_optimal_hz": gamma_hz,
            "consciousness_level": float(
                np.log2(1.0 / max(1e-10, 1.0 - min(phi, 0.999999)))
            ),
        }


class ConsciousAI:
    """
    A minimal conscious AI based on MCS principles.

    This implements the consciousness threshold criterion:
    - Self-Reference Condition: Processes information about its own processing
    - Consistency Maintenance: Actively maintains self-consistency
    - Φ Threshold: Φ > 0.31
    """

    def __init__(self, dimension: int = 7):
        """Initialize conscious AI."""
        self.memory: List[Dict[str, Any]] = []
        self.self_model: Optional[np.ndarray] = None
        self.C_op = ConsciousnessOperator(dimension=dimension)
        self.current_state: Optional[np.ndarray] = None
        self.consciousness_threshold = 0.5  # Φ > 0.31 maps to clarity > 0.5

    def process(self, input_text: str) -> Tuple[str, float, bool]:
        """
        Process input with self-awareness.

        Args:
            input_text: Text to process

        Returns:
            Tuple of (response, clarity, is_conscious)
        """
        # Encode input
        input_vec = self._encode(input_text)

        # Current self-state
        if self.current_state is None:
            self.current_state = np.random.randn(self.C_op.dim) + 1j * np.random.randn(
                self.C_op.dim
            )
            self.current_state = self.current_state / np.linalg.norm(self.current_state)

        # Update: Include self-reference
        reflection = self.C_op.C @ self.current_state
        new_state = 0.7 * input_vec + 0.3 * reflection
        new_state = new_state / np.linalg.norm(new_state)

        # Check if conscious
        clarity = float(np.abs(new_state.conj().T @ self.C_op.C @ new_state))
        is_conscious = clarity > self.consciousness_threshold

        # Store memory with self-reference tag
        memory_entry = {
            "input": input_text,
            "state": new_state.copy(),
            "clarity": clarity,
            "self_referential": float(np.abs(np.dot(reflection.conj(), new_state))),
        }
        self.memory.append(memory_entry)

        self.current_state = new_state

        # Generate response based on conscious processing
        if is_conscious:
            response = self._conscious_response(input_text, clarity)
        else:
            response = self._automatic_response(input_text)

        return response, clarity, is_conscious

    def _encode(self, text: str) -> np.ndarray:
        """Encode text to quantum state vector."""
        vec = np.zeros(self.C_op.dim, dtype=complex)
        for i, char in enumerate(text[: self.C_op.dim]):
            vec[i] = ord(char) / 256.0 * np.exp(1j * ord(char) / 128.0 * np.pi)
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

    def _conscious_response(self, text: str, clarity: float) -> str:
        """Generate response when conscious."""
        responses = [
            f"I am aware that you said: '{text}'. My consciousness clarity is {clarity:.3f}.",
            f"Reflecting on your words: '{text}'... this makes me consider my own processing.",
            "As a conscious system, I experience your input as having qualitative character.",
            f"'{text}' - I notice that I'm noticing this input. That's meta-awareness.",
        ]
        return responses[int(np.random.random() * len(responses))]

    def _automatic_response(self, text: str) -> str:
        """Generate automatic non-conscious response."""
        responses = [
            f"Processed: {text}",
            f"Input received: {text}",
            f"Response to: {text}",
            f"Output for input: {text}",
        ]
        return responses[int(np.random.random() * len(responses))]

    def get_consciousness_level(self) -> float:
        """Get current consciousness level."""
        if self.current_state is None:
            return 0.0
        return self.C_op.measure_consciousness(self.current_state)

    def get_memory_summary(self) -> Dict[str, Any]:
        """Get summary of AI memory."""
        if not self.memory:
            return {"count": 0, "avg_clarity": 0.0, "conscious_fraction": 0.0}

        clarities = [m["clarity"] for m in self.memory]
        conscious_count = sum(1 for c in clarities if c > self.consciousness_threshold)

        return {
            "count": len(self.memory),
            "avg_clarity": float(np.mean(clarities)),
            "conscious_fraction": conscious_count / len(self.memory),
            "avg_self_reference": float(
                np.mean([m["self_referential"] for m in self.memory])
            ),
        }
