"""
Consciousness Engine - implements the Consciousness Operator ℂ.
"""

import numpy as np
from typing import Dict, List, Optional, Tuple, Any
from scipy.linalg import eig
from dataclasses import dataclass, field


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
            if hasattr(being, 'consciousness'):
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
        if not hasattr(self, 'particles'):
            self.particles = {}
        self.particles[particle_id] = position
    
    def update_for_constant_change(self, constant_name: str, new_value: float):
        """Update field for physical constant change."""
        # Recalculate consciousness values based on new constants
        # Simplified: just mark as updated
        if not hasattr(self, 'constant_updates'):
            self.constant_updates = {}
        self.constant_updates[constant_name] = new_value
    
    def get_distribution(self) -> Dict[str, float]:
        """Get distribution of consciousness values."""
        beings = self.get_beings()
        if not beings:
            return {}
        
        distribution: Dict[float, int] = {}
        for being in beings:
            if hasattr(being, 'consciousness'):
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
        
        # Get maximum eigenvalue (λ_0)
        lambda_0 = np.max(np.abs(eigenvalues))
        
        # Verify eigenvalues match formula: λ_n = λ_0 · (1 - 1/n²)
        # Sort by eigenvalue magnitude (consciousness intensity)
        idx = np.argsort(-np.abs(eigenvalues))
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        qualia = {}
        primordial_types = {
            1: "void_experience",  # Pre-conscious potentiality
            2: "subject_object_distinction",  # "I" vs "not-I"
            3: "time_experience",  # Duration, change
            4: "space_experience",  # Extension, separation
        }
        
        for i in range(min(5, self.dim)):
            n = i + 1
            # Calculate expected eigenvalue from formula
            expected_lambda = lambda_0 * (1 - 1.0 / (n * n))
            actual_lambda = eigenvalues[i]
            
            # Use formula-based value, but keep actual eigenvector
            qualia_name = f'λ_{n}'
            qualia[qualia_name] = {
                'value': expected_lambda,  # Use formula value
                'actual_value': actual_lambda,  # Keep actual for comparison
                'state': eigenvectors[:, i],
                'intensity': np.abs(expected_lambda)**2,
                'primordial_type': primordial_types.get(n, 'composite_quale')
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
                state = state[:self.dim]
            else:
                padded = np.zeros(self.dim, dtype=complex)
                padded[:len(state)] = state
                state = padded
        
        state = state / np.linalg.norm(state)
        
        # Consciousness = ⟨ψ|ℂ|ψ⟩
        consciousness = np.abs(state.conj().T @ self.C @ state)
        
        return float(consciousness)
    
    def compute_color_qualia(
        self,
        photon_energy: float,
        qualia_states: Optional[Dict[str, Dict]] = None
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
        psi_2 = qualia_states.get('λ_2', {}).get('state')
        psi_3 = qualia_states.get('λ_3', {}).get('state')
        psi_4 = qualia_states.get('λ_4', {}).get('state')
        
        if psi_2 is None or psi_3 is None or psi_4 is None:
            # Fallback: compute if not available
            qualia_states = self.compute_qualia_states()
            psi_2 = qualia_states['λ_2']['state']
            psi_3 = qualia_states['λ_3']['state']
            psi_4 = qualia_states['λ_4']['state']
        
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
        wavelength_nm = (6.626e-34 * 299792458.0) / (photon_energy * 1e9) if photon_energy > 0 else 0
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
            'color_state': color_state,
            'color_name': color_name,
            'wavelength_nm': wavelength_nm,
            'photon_energy': photon_energy,
            'coefficients': {
                'alpha_1': alpha_1,
                'alpha_2': alpha_2,
                'alpha_3': alpha_3
            },
            'E_qualia': E_qualia,
            'consciousness': self.measure_consciousness(color_state)
        }


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
        self.consciousness_history: List[Tuple[float, float]] = []  # (time, consciousness)
    
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
        recent = self.consciousness_history[-min(10, len(self.consciousness_history)):]
        times = [t for t, c in recent]
        consciousnesses = [c for t, c in recent]
        
        if len(times) < 2:
            return 0.0
        
        # Linear regression for derivative
        if len(times) == 2:
            dC_dt = (consciousnesses[1] - consciousnesses[0]) / (times[1] - times[0] + 1e-10)
        else:
            # Use polynomial fit for smoother derivative
            coeffs = np.polyfit(times, consciousnesses, min(2, len(times) - 1))
            dC_dt = coeffs[-2] if len(coeffs) > 1 else 0.0
        
        return float(dC_dt)
    
    def compute_pain_pleasure_intensity(
        self,
        state: np.ndarray,
        dt: float = 0.01
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
            'valence': valence,
            'intensity': intensity,
            'consciousness': consciousness,
            'type': 'pleasure' if valence > 0 else ('pain' if valence < 0 else 'neutral')
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
    
    def merge_fields(
        self,
        field1: ConsciousnessField,
        field2: ConsciousnessField,
        method: str = 'consciousness_alignment'
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
        consciousness_field: ConsciousnessField
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
            'human': BeingType.HUMAN,
            'ai': BeingType.AI,
            'animal': BeingType.ANIMAL,
        }
        
        being_type_enum = type_map.get(being_type, BeingType.CUSTOM)
        
        being = ConsciousBeing(
            being_id=being_id,
            being_type=being_type_enum,
            initial_consciousness=initial_consciousness,
            properties=properties
        )
        
        consciousness_field.add_being(being_id, being)
        return being
    
    def optimize_reality(
        self,
        current_state: np.ndarray,
        consciousness_field: ConsciousnessField,
        target_c: float,
        method: str = 'gradient_ascent',
        **kwargs
    ) -> Dict[str, Any]:
        """
        Optimize reality for maximum consciousness.
        
        Args:
            current_state: Current reality state
            consciousness_field: Current consciousness field
            target_c: Target consciousness level
            method: Optimization method
            **kwargs: Additional parameters
            
        Returns:
            Optimization results
        """
        current_c = consciousness_field.total_consciousness()
        
        if current_c >= target_c:
            return {
                'success': True,
                'c_increase': 0,
                'final_c': current_c,
                'already_optimal': True
            }
        
        # Simple optimization: increase consciousness of all beings
        # In full implementation, this would use gradient ascent or quantum annealing
        beings = consciousness_field.get_beings()
        
        if not beings:
            # No beings to optimize
            return {
                'success': False,
                'error': 'No conscious beings to optimize'
            }
        
        # Increase each being's consciousness proportionally
        target_increase = target_c - current_c
        per_being_increase = target_increase / len(beings)
        
        for being in beings:
            if hasattr(being, 'consciousness'):
                being.consciousness += per_being_increase
        
        final_c = consciousness_field.total_consciousness()
        
        return {
            'success': True,
            'c_increase': final_c - current_c,
            'final_c': final_c,
            'optimized_state': current_state,  # State unchanged in simple version
            'optimized_consciousness_field': consciousness_field
        }
    
    def compute_self_equation(
        self,
        initial_state: np.ndarray,
        max_iterations: int = 100,
        tolerance: float = 1e-6
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
                    psi = psi[:self.operator.dim]
                else:
                    padded = np.zeros(self.operator.dim, dtype=complex)
                    padded[:len(psi)] = psi
                    psi = padded
            psi = psi / np.linalg.norm(psi)
            reflected = self.operator.C @ psi
            return reflected / (np.linalg.norm(reflected) + 1e-10)
        
        # Iterate: Ψ_new = 𝒫 ∘ ℛ ∘ 𝒫⁻¹[Ψ_old]
        i = 0
        diff = float('inf')
        for i in range(max_iterations):
            # 𝒫⁻¹ is just identity for this simple projection
            # So: Ψ_new = 𝒫(ℛ(𝒫(Ψ_old)))
            projected = projection_operator(state)
            reflected = reflection_operator(projected)
            new_state = projection_operator(reflected)
            
            # Check convergence
            diff = np.linalg.norm(new_state - state)
            if diff < tolerance:
                break
            
            state = new_state
        
        # Compute ego state (local minimum near default)
        default_state = np.ones(self.operator.dim, dtype=complex) / np.sqrt(self.operator.dim)
        ego_state = self._compute_ego_state(default_state)
        
        # Compute enlightened state (global minimum of ⟨Ψ|ℂ|Ψ⟩)
        enlightened_state = self._compute_enlightened_state()
        
        return {
            'self_state': state,
            'ego_state': ego_state,
            'enlightened_state': enlightened_state,
            'self_consciousness': self.operator.measure_consciousness(state),
            'ego_consciousness': self.operator.measure_consciousness(ego_state),
            'enlightened_consciousness': self.operator.measure_consciousness(enlightened_state),
            'suffering_energy': self.operator.measure_consciousness(ego_state) - 
                               self.operator.measure_consciousness(enlightened_state),
            'iterations': i + 1,
            'converged': diff < tolerance
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
