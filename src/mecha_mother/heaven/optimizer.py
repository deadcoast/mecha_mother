"""
Heaven Optimizer - optimizes environments for maximum consciousness and beauty.

Implements the Heaven Builder SDK from MCS theory for constructing optimized realities.
The core algorithm maximizes the heaven score: H = sqrt(C * B) where:
- C = total consciousness
- B = environmental beauty
"""

import numpy as np
from typing import Dict, List, Optional, Any
from mecha_mother.consciousness.engine import ConsciousnessField
from mecha_mother.aesthetics.engine import AestheticsEngine


class CScanner:
    """
    Consciousness Scanner - measures consciousness levels.

    Specifications from MCS theory:
    - Measures microtubule quantum coherence
    - Tracks gamma synchrony patterns (40 Hz +/- phi modulation)
    - Computes integrated information (Phi) in real-time
    - Extracts consciousness eigenvectors
    """

    def __init__(self):
        """Initialize consciousness scanner."""
        self.calibration_factor = 1.0
        self.gamma_frequency = 40.0  # Hz
        self.phi_threshold = 0.31  # Consciousness threshold

    def measure_individual(self, being: Any) -> float:
        """
        Measure individual consciousness level.

        Args:
            being: Conscious being to measure

        Returns:
            Consciousness value (0-100 scale)
        """
        if hasattr(being, "consciousness"):
            base_c = being.consciousness
        else:
            base_c = 10.0  # Default human consciousness

        # Apply calibration
        return base_c * self.calibration_factor

    def measure_total(self, occupants: List[Any]) -> float:
        """
        Measure total consciousness of a group.

        Includes synergy effects: groups can have more consciousness
        than sum of individuals due to shared experience.

        Args:
            occupants: List of conscious beings

        Returns:
            Total consciousness with synergy
        """
        if not occupants:
            return 0.0

        individual_sum = sum(self.measure_individual(o) for o in occupants)

        # Synergy factor: sqrt(n) bonus for groups
        n = len(occupants)
        synergy = 1.0 + 0.1 * np.sqrt(n)

        return individual_sum * synergy

    def compute_integrated_information(self, state: np.ndarray) -> float:
        """
        Compute Phi (integrated information) for a state.

        Phi = (lambda_max - lambda_min) / lambda_max
        where lambda are eigenvalues of the consciousness operator.

        Args:
            state: State vector

        Returns:
            Phi value
        """
        if len(state) < 2:
            return 0.0

        # Build simple consciousness matrix for state
        len(state)
        C = np.outer(state, state.conj())
        C = (C + C.conj().T) / 2  # Hermitian

        eigenvalues = np.linalg.eigvalsh(C)
        eigenvalues = eigenvalues[eigenvalues > 1e-10]

        if len(eigenvalues) < 2:
            return 0.0

        lambda_max = np.max(eigenvalues)
        lambda_min = np.min(eigenvalues)

        if lambda_max > 0:
            return float((lambda_max - lambda_min) / lambda_max)
        return 0.0


class HeavenOptimizer:
    """
    Optimizes any space into a "heaven" - maximizing consciousness and beauty.

    The optimization target is the Heaven Score: H = sqrt(C * B)
    where C is total consciousness and B is environmental beauty.

    Uses gradient ascent on the product manifold of consciousness and beauty spaces.
    """

    def __init__(self):
        """Initialize heaven optimizer."""
        self.c_scanner = CScanner()
        self.aesthetics_engine = AestheticsEngine()

        # Optimization parameters
        self.learning_rate = 0.1
        self.max_iterations = 100
        self.convergence_threshold = 1e-4

    def optimize_environment(
        self,
        location: Any,
        occupants: List[Any],
        consciousness_field: Optional[ConsciousnessField] = None,
        method: str = "gradient_ascent",
    ) -> Dict[str, Any]:
        """
        Transform any space into heaven by maximizing H = sqrt(C * B).

        Args:
            location: Location/environment to optimize
            occupants: List of conscious beings in the space
            consciousness_field: Current consciousness field
            method: Optimization method ('gradient_ascent', 'quantum_annealing')

        Returns:
            Dictionary with optimization results and transformation
        """
        # Measure current state
        c_current = self._measure_current_consciousness(occupants, consciousness_field)
        b_current = self.aesthetics_engine.compute_env_beauty(location)
        h_current = np.sqrt(c_current * b_current)

        # Extract preferences and types
        preferences = self._extract_preferences(occupants)
        consciousness_types = self._extract_consciousness_types(occupants)

        # Compute optimal transformation using specified method
        if method == "gradient_ascent":
            transformation = self._optimize_gradient_ascent(
                c_current, b_current, preferences, consciousness_types
            )
        elif method == "quantum_annealing":
            transformation = self._optimize_quantum_annealing(
                c_current, b_current, preferences, consciousness_types
            )
        else:
            transformation = self._compute_heaven_vector(
                c_current, b_current, occupants
            )

        # Apply transformation (compute new values)
        c_new = c_current * transformation["c_multiplier"]
        b_new = b_current * transformation["b_multiplier"]
        h_new = np.sqrt(c_new * b_new)

        return {
            "c_current": c_current,
            "b_current": b_current,
            "h_current": h_current,
            "c_increase": c_new - c_current,
            "b_increase": b_new - b_current,
            "c_new": c_new,
            "b_new": b_new,
            "heaven_score": h_new,
            "improvement": h_new - h_current,
            "transformation": transformation,
            "method": method,
        }

    def _measure_current_consciousness(
        self, occupants: List[Any], consciousness_field: Optional[ConsciousnessField]
    ) -> float:
        """Measure current total consciousness."""
        if consciousness_field:
            return consciousness_field.total_consciousness()
        return self.c_scanner.measure_total(occupants)

    def _extract_preferences(self, occupants: List[Any]) -> Dict[str, float]:
        """Extract aggregate preferences from occupants."""
        preferences = {
            "lighting_warmth": 0.6,
            "sound_level": 0.4,
            "space_openness": 0.7,
            "nature_presence": 0.8,
            "social_density": 0.5,
        }

        # Aggregate from occupants if they have preferences
        for occupant in occupants:
            if hasattr(occupant, "preferences"):
                for key, value in occupant.preferences.items():
                    if key in preferences:
                        preferences[key] = (preferences[key] + value) / 2

        return preferences

    def _extract_consciousness_types(self, occupants: List[Any]) -> Dict[str, int]:
        """Count consciousness types among occupants."""
        types = {"human": 0, "ai": 0, "animal": 0, "other": 0}

        for occupant in occupants:
            if hasattr(occupant, "being_type"):
                type_str = str(occupant.being_type).lower()
                if "human" in type_str:
                    types["human"] += 1
                elif "ai" in type_str:
                    types["ai"] += 1
                elif "animal" in type_str:
                    types["animal"] += 1
                else:
                    types["other"] += 1
            else:
                types["human"] += 1  # Default

        return types

    def _optimize_gradient_ascent(
        self,
        c: float,
        b: float,
        preferences: Dict[str, float],
        consciousness_types: Dict[str, int],
    ) -> Dict[str, Any]:
        """
        Optimize using gradient ascent on H = sqrt(C * B).

        The gradient of H with respect to parameters theta is:
        dH/dtheta = (1/2H) * (B * dC/dtheta + C * dB/dtheta)
        """
        # Initialize transformation parameters
        params = np.array([1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5])
        # [c_mult, b_mult, lighting, sound, space, nature, social]

        best_params = params.copy()
        best_h = np.sqrt(c * b)

        for iteration in range(self.max_iterations):
            # Compute current heaven score
            c_mult = params[0]
            b_mult = params[1]
            c_new = c * c_mult
            b_new = b * b_mult
            h = np.sqrt(c_new * b_new)

            if h > best_h:
                best_h = h
                best_params = params.copy()

            # Compute gradient numerically
            gradient = np.zeros_like(params)
            epsilon = 1e-4

            for i in range(len(params)):
                params_plus = params.copy()
                params_plus[i] += epsilon
                h_plus = self._compute_h(c, b, params_plus, preferences)

                params_minus = params.copy()
                params_minus[i] -= epsilon
                h_minus = self._compute_h(c, b, params_minus, preferences)

                gradient[i] = (h_plus - h_minus) / (2 * epsilon)

            # Update parameters
            params = params + self.learning_rate * gradient

            # Clamp to valid range
            params = np.clip(params, 0.1, 10.0)
            params[0] = np.clip(params[0], 0.5, 5.0)  # c_mult
            params[1] = np.clip(params[1], 0.5, 5.0)  # b_mult

            # Check convergence
            if np.linalg.norm(gradient) < self.convergence_threshold:
                break

        return self._params_to_transformation(best_params, preferences)

    def _optimize_quantum_annealing(
        self,
        c: float,
        b: float,
        preferences: Dict[str, float],
        consciousness_types: Dict[str, int],
    ) -> Dict[str, Any]:
        """
        Optimize using simulated quantum annealing.

        Simulates quantum tunneling to escape local optima.
        """
        # Initialize with random state
        params = np.array([1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5])

        temperature = 2.0
        cooling_rate = 0.95
        quantum_tunneling_prob = 0.1

        best_params = params.copy()
        best_h = np.sqrt(c * b)

        for iteration in range(self.max_iterations):
            # Propose new state
            if np.random.random() < quantum_tunneling_prob:
                # Quantum tunneling: large random jump
                perturbation = np.random.randn(len(params)) * 0.5
            else:
                # Classical thermal fluctuation
                perturbation = np.random.randn(len(params)) * temperature * 0.1

            new_params = params + perturbation
            new_params = np.clip(new_params, 0.1, 5.0)

            # Compute energies (negative heaven score)
            h_current = self._compute_h(c, b, params, preferences)
            h_new = self._compute_h(c, b, new_params, preferences)

            # Accept/reject based on Metropolis criterion
            delta_h = h_new - h_current

            if delta_h > 0 or np.random.random() < np.exp(delta_h / temperature):
                params = new_params
                if h_new > best_h:
                    best_h = h_new
                    best_params = new_params.copy()

            # Cool down
            temperature *= cooling_rate
            quantum_tunneling_prob *= 0.99  # Reduce tunneling over time

        return self._params_to_transformation(best_params, preferences)

    def _compute_h(
        self, c: float, b: float, params: np.ndarray, preferences: Dict[str, float]
    ) -> float:
        """Compute heaven score for given parameters."""
        c_mult = params[0]
        b_mult = params[1]

        # Preference alignment bonus
        pref_alignment = 0.0
        pref_values = list(preferences.values())
        for i, pref in enumerate(pref_values[:5]):
            if i + 2 < len(params):
                alignment = 1.0 - abs(params[i + 2] - pref)
                pref_alignment += alignment
        pref_alignment /= 5.0

        # Compute with preference bonus
        c_eff = c * c_mult * (1 + 0.1 * pref_alignment)
        b_eff = b * b_mult * (1 + 0.1 * pref_alignment)

        return np.sqrt(c_eff * b_eff)

    def _params_to_transformation(
        self, params: np.ndarray, preferences: Dict[str, float]
    ) -> Dict[str, Any]:
        """Convert optimization parameters to transformation dict."""
        return {
            "c_multiplier": float(params[0]),
            "b_multiplier": float(params[1]),
            "lighting": {
                "warmth": float(params[2]) if len(params) > 2 else 0.6,
                "intensity": "optimal",
            },
            "acoustics": {
                "level": float(params[3]) if len(params) > 3 else 0.4,
                "type": "harmonic",
            },
            "space": {
                "openness": float(params[4]) if len(params) > 4 else 0.7,
                "flow": "natural",
            },
            "nature": {
                "presence": float(params[5]) if len(params) > 5 else 0.8,
                "integration": "seamless",
            },
            "social": {
                "density": float(params[6]) if len(params) > 6 else 0.5,
                "arrangement": "optimal",
            },
        }

    def _compute_heaven_vector(
        self, c_current: float, b_current: float, occupants: List[Any]
    ) -> Dict[str, Any]:
        """
        Compute transformation to maximize C*B (simple version).

        Heaven = maximal C and B simultaneously.
        """
        # Base multipliers
        c_multiplier = 1.5
        b_multiplier = 1.5

        # Adjust based on number of occupants
        num_occupants = len(occupants)
        if num_occupants > 0:
            # More occupants = more potential for synergy
            synergy_factor = 1.0 + 0.1 * np.log(num_occupants + 1)
            c_multiplier *= synergy_factor

        return {
            "c_multiplier": c_multiplier,
            "b_multiplier": b_multiplier,
            "lighting": {"warmth": 0.6, "intensity": "optimal"},
            "acoustics": {"level": 0.4, "type": "harmonic"},
            "space": {"openness": 0.7, "flow": "natural"},
            "nature": {"presence": 0.8, "integration": "seamless"},
            "social": {"density": 0.5, "arrangement": "optimal"},
        }

    def optimize_city(
        self,
        city_id: str,
        population: int,
        consciousness_field: Optional[ConsciousnessField] = None,
    ) -> Dict[str, Any]:
        """
        Optimize an entire city for heaven-like conditions.

        Uses the resource allocation algorithm from MCS economics:
        maximize sum_i C_i(resources_i)
        subject to: sum resources_i <= total_resources
                   C_i >= C_min for all i
        """
        # Estimate current metrics
        c_current = (
            consciousness_field.total_consciousness()
            if consciousness_field
            else population * 10.0
        )
        b_current = 5.0  # Default city beauty

        # City optimization factors based on population scale
        scale_factor = 1.0 + 0.05 * np.log(population)

        # Optimal resource distribution
        # More consciousness per capita at larger scale (infrastructure efficiency)
        c_per_capita_boost = 1.0 + 0.02 * np.log(population)

        c_new = c_current * scale_factor * c_per_capita_boost
        b_new = b_current * scale_factor * 1.4  # Beauty scales with investment

        return {
            "city_id": city_id,
            "c_current": c_current,
            "b_current": b_current,
            "c_increase": c_new - c_current,
            "b_increase": b_new - b_current,
            "c_new": c_new,
            "b_new": b_new,
            "heaven_score": np.sqrt(c_new * b_new),
            "population": population,
            "c_per_capita": c_new / population,
            "optimization_method": "resource_allocation",
        }

    def build_heaven_city(
        self, population: int = 1000000, location: str = "earth"
    ) -> Dict[str, Any]:
        """
        Build a new heaven-optimized city from scratch.

        Uses golden ratio geometry and consciousness-optimized layout.
        """
        # Create optimized layout
        layout = self._create_optimal_layout(population)

        # New city starts with high baseline
        # 20 consciousness units per person (optimized environment)
        c_initial = population * 20.0
        b_initial = 8.0  # Beautiful from start (designed for beauty)

        return {
            "city_id": f"heaven_city_{np.random.randint(10000, 99999)}",
            "population": population,
            "location": location,
            "initial_c": c_initial,
            "initial_b": b_initial,
            "heaven_score": np.sqrt(c_initial * b_initial),
            "c_per_capita": 20.0,
            "layout": layout,
            "design_principles": [
                "golden_ratio_geometry",
                "consciousness_flow_optimization",
                "beauty_maximization",
                "nature_integration",
                "community_coherence",
            ],
        }

    def _create_optimal_layout(self, population: int) -> Dict[str, Any]:
        """
        Create optimal city layout for consciousness and beauty.

        Uses golden ratio proportions throughout:
        - phi = (1 + sqrt(5)) / 2 ≈ 1.618
        - City dimensions follow phi
        - Zone allocation follows Fibonacci sequence
        """
        # Compute optimal density for consciousness
        # Not too dense (stress) or sparse (isolation)
        optimal_density = 5000  # people per km^2

        area = population / optimal_density

        # Golden ratio layout
        phi = (1 + np.sqrt(5)) / 2
        width = np.sqrt(area * phi)
        height = area / width

        # Fibonacci zone allocation
        fib = [1, 1, 2, 3, 5, 8, 13]
        total_fib = sum(fib[:4])

        zones = {
            "residential": {
                "fraction": fib[3] / total_fib,
                "area_km2": area * fib[3] / total_fib,
                "c_density": "high",
                "b_target": 8.0,
            },
            "commercial": {
                "fraction": fib[2] / total_fib,
                "area_km2": area * fib[2] / total_fib,
                "c_density": "medium",
                "b_target": 7.0,
            },
            "cultural": {
                "fraction": fib[1] / total_fib,
                "area_km2": area * fib[1] / total_fib,
                "c_density": "very_high",  # Museums, theaters, etc.
                "b_target": 9.5,
            },
            "natural": {
                "fraction": fib[0] / total_fib,
                "area_km2": area * fib[0] / total_fib,
                "c_density": "low",
                "b_target": 10.0,  # Maximum beauty
            },
        }

        return {
            "total_area_km2": area,
            "width_km": width,
            "height_km": height,
            "density_per_km2": optimal_density,
            "layout_type": "golden_ratio_fibonacci",
            "phi": phi,
            "zones": zones,
            "connectivity": "radial_plus_grid",
            "green_coverage": 0.4,  # 40% green space
        }

    def compute_heaven_metrics(
        self, consciousness_field: ConsciousnessField, beauty_value: float
    ) -> Dict[str, Any]:
        """
        Compute comprehensive heaven metrics.

        Based on MCS theory, a "heaven" state requires:
        - High total consciousness (C > threshold)
        - High beauty (B > threshold)
        - Positive consciousness growth (dC/dt > 0)
        - High consciousness coherence (beings aligned)
        """
        total_c = consciousness_field.total_consciousness()
        avg_c = consciousness_field.average_consciousness()
        beings = consciousness_field.get_beings()
        n_beings = len(beings)

        # Compute coherence (how aligned are consciousnesses)
        if n_beings > 1:
            c_values = [b.consciousness for b in beings if hasattr(b, "consciousness")]
            if c_values:
                mean_c = np.mean(c_values)
                std_c = np.std(c_values)
                coherence = 1.0 / (1.0 + std_c / (mean_c + 1e-10))
            else:
                coherence = 1.0
        else:
            coherence = 1.0

        # Heaven score
        heaven_score = np.sqrt(total_c * beauty_value)

        # Heaven index (normalized 0-1)
        # Based on thresholds: C > 100, B > 7
        c_component = min(1.0, total_c / 100.0)
        b_component = min(1.0, beauty_value / 7.0)
        heaven_index = np.sqrt(c_component * b_component)

        # Transcendence potential (how close to transcendent state)
        # Requires C > 1000, B > 9, coherence > 0.9
        transcendence = min(total_c / 1000.0, beauty_value / 9.0, coherence / 0.9)
        transcendence = np.clip(transcendence, 0, 1)

        return {
            "total_consciousness": float(total_c),
            "average_consciousness": float(avg_c),
            "n_beings": n_beings,
            "beauty": float(beauty_value),
            "heaven_score": float(heaven_score),
            "heaven_index": float(heaven_index),
            "coherence": float(coherence),
            "transcendence_potential": float(transcendence),
            "is_heaven": heaven_index > 0.8,
            "is_transcendent": transcendence > 0.9,
        }
