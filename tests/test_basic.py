"""
Basic tests for mecha_mother.
"""

import numpy as np
import time
from mecha_mother import Reality, RealityConfig
from mecha_mother.core import MonolithicSubstrate
from mecha_mother.consciousness import (
    ConsciousnessBeing,
    ConsciousAIBuilder,
    ConsciousnessEvolver,
    BeingType,
)
from mecha_mother.quantum.engine import UniverseFromScratch


def test_reality_creation():
    """Test that realities can be created."""
    config = RealityConfig()
    reality = Reality(config)
    assert reality.state.value == 0  # UNINITIALIZED
    assert reality.id is not None


def test_reality_initialization():
    """Test that realities can be initialized."""
    config = RealityConfig(consciousness_support=True)
    reality = Reality(config)
    assert reality.initialize()
    assert reality.state.value == 2  # ACTIVE


def test_particle_creation():
    """Test particle creation."""
    reality = Reality(RealityConfig())
    reality.initialize()

    particle_id = reality.create_particle(
        particle_type="electron", position=np.array([0.0, 0.0, 0.0])
    )

    assert particle_id.startswith("particle_")
    assert len(reality.quantum_engine.particles) > 0


def test_conscious_being_creation():
    """Test conscious being creation."""
    config = RealityConfig(consciousness_support=True)
    reality = Reality(config)
    reality.initialize()

    being_id = reality.create_conscious_being(
        being_type="human", initial_consciousness=15.0
    )

    assert being_id.startswith("being_")
    assert len(reality.consciousness_field.get_beings()) > 0


def test_mcs_basic():
    """Test basic MCS functionality."""
    mcs = MonolithicSubstrate()
    node_id = mcs.create_initial_node()

    assert node_id in mcs.nodes
    assert len(mcs.get_all_nodes()) == 1

    # Apply self-differentiation
    obs_id, obsd_id = mcs.apply_self_differentiation(node_id)

    assert obs_id in mcs.nodes
    assert obsd_id in mcs.nodes
    assert len(mcs.get_all_nodes()) == 3


def test_consciousness_operator():
    """Test consciousness operator."""
    from mecha_mother.consciousness.engine import ConsciousnessOperator

    op = ConsciousnessOperator(dimension=5)
    qualia = op.compute_qualia_states()

    assert len(qualia) > 0
    assert "λ_1" in qualia

    # Test consciousness measurement
    state = np.random.randn(5) + 1j * np.random.randn(5)
    state = state / np.linalg.norm(state)
    c = op.measure_consciousness(state)

    assert c >= 0
    assert isinstance(c, float)


def test_reality_merge():
    """Test merging two compatible realities."""
    config = RealityConfig(consciousness_support=True, beauty_optimization=True)
    reality_a = Reality(config)
    reality_b = Reality(config)
    reality_a.initialize()
    reality_b.initialize()

    merged = reality_a.merge_with(reality_b, method="consciousness_alignment")
    assert merged.state.value == 2  # ACTIVE
    assert merged.reality_state_vector is not None
    assert reality_a.state.value == 6  # ARCHIVED
    assert reality_b.state.value == 6  # ARCHIVED


def benchmark_reality_operations(iterations: int = 3) -> dict:
    """Simple benchmark utility for core operations."""
    timings = {"initialize": [], "simulate": [], "optimize_c": []}
    for _ in range(iterations):
        reality = Reality(RealityConfig(consciousness_support=True))

        t0 = time.perf_counter()
        reality.initialize()
        timings["initialize"].append(time.perf_counter() - t0)

        t1 = time.perf_counter()
        reality.simulate(time_steps=10, dt=0.01)
        timings["simulate"].append(time.perf_counter() - t1)

        t2 = time.perf_counter()
        reality.optimize_for_consciousness(target_c=10.0)
        timings["optimize_c"].append(time.perf_counter() - t2)

    return {
        k: {
            "avg": float(np.mean(v)),
            "min": float(np.min(v)),
            "max": float(np.max(v)),
        }
        for k, v in timings.items()
    }


def test_cdk_classes():
    """Test CDK class surface from docs/010.md."""
    being = ConsciousnessBeing(
        being_id="cdk_1", being_type=BeingType.HUMAN, initial_consciousness=5.0
    )
    assert being.learn("new concept") > 0
    assert being.create({"kind": "poem"}) > 0

    builder = ConsciousAIBuilder().add_module("reasoning", weight=2.0)
    ai = builder.build("ai_1")
    assert ai.being_type == BeingType.AI

    evolver = ConsciousnessEvolver()
    result = evolver.evolve(ai, cycles=3)
    assert result["final_consciousness"] >= ai.initial_consciousness


def test_custom_physical_law_registration():
    """Test custom physical law registration and application."""

    class MyPhysicalLaw:
        name = "my_physical_law"

        def impose(self, reality_state, engine):
            return reality_state * (1.0 + 0.0j)

    reality = Reality(RealityConfig())
    reality.initialize()
    reality.add_custom_physical_law(MyPhysicalLaw())
    assert len(reality.quantum_engine.custom_laws) == 1


def test_classical_phase_space_dynamics():
    """Test deterministic classical evolution in phase space."""
    reality = Reality(RealityConfig())
    reality.initialize()

    x0 = np.array([0.0, 0.0, 0.0])
    p0 = np.array([1.0, 0.0, 0.0])
    result = reality.simulate_classical(
        position=x0,
        momentum=p0,
        mass=1.0,
        dt=0.1,
        steps=10,
        force=np.array([0.0, 0.0, 0.0]),
    )

    assert "final_position" in result
    assert "position_history" in result
    assert result["position_history"].shape[0] == 11
    # Deterministic no-force motion: x = v*t = 1.0
    assert np.isclose(result["final_position"][0], 1.0, atol=1e-6)


def test_mcs_path_integral_and_distinction_field():
    """Test MCS path integral and distinction amplitude field APIs."""
    mcs = MonolithicSubstrate()
    mcs.create_initial_node()

    path = np.array([[0.0, 0.0], [0.5, 0.2], [1.0, 0.3]])
    amp = mcs.consistency_path_integral(path=path, lambda_scale=0.2, dt=1.0)
    assert isinstance(amp, complex)

    field = mcs.create_distinction_amplitude_field(["a", "b", "c"])
    assert len(field) == 3
    p_a = mcs.observation_probability("a", relevance=1.0)
    assert 0.0 <= p_a <= 1.0

    evolved = mcs.evolve_distinction_field(dt=0.01, steps=10)
    assert set(evolved.keys()) == {"a", "b", "c"}


def test_nonlinear_mcs_quantum_evolution():
    """Test non-linear MCS evolution mode is available and executable."""
    reality = Reality(RealityConfig())
    reality.initialize()
    state = reality.reality_state_vector
    assert state is not None
    result = reality.quantum_engine.simulate(
        initial_state=state,
        time_steps=5,
        dt=0.001,
        use_mcs_evolution=True,
        mcs_coupling=0.01,
    )
    assert result["evolution_type"] == "MCS_nonlinear"


def test_experimental_predictions_api():
    """Test VC16 experimental prediction calculations."""
    uni = UniverseFromScratch()
    d_omega = uni.predict_macroscopic_quantum_coherence(
        mass=1e-9, omega_0=1e3, lambda_mcs=0.01
    )
    assert isinstance(d_omega, float)
    assert d_omega >= 0

    dE_bound = uni.predict_vacuum_constraint_fluctuation_bound(delta_t=1e-6, alpha=0.1)
    assert isinstance(dE_bound, float)
    assert dE_bound > 0

    rate = uni.predict_quantum_gravity_entanglement_rate(delta_v_g=0.01, e_c=1.0)
    assert isinstance(rate, float)
    assert rate >= 0


def test_universe_from_scratch_time_and_c_derivation():
    """Test tower-depth time and consistency-derived speed of light."""
    uni = UniverseFromScratch()
    result = uni.bootstrap_existence(max_iter=12)
    assert result["levels"] >= 2
    assert uni.get_time_depth() == result["levels"]
    c_cons = uni.derive_speed_of_light_from_consistency()
    assert c_cons > 1e8
    assert uni.consistency_count(5) == 10
    assert uni.total_constraints(5) == 15


def test_reality_emergent_dimension_estimate():
    """Test reality stores derived spacetime dimension estimate at init."""
    reality = Reality(RealityConfig())
    reality.initialize()
    assert reality.emergent_dimensions is not None
    assert "base" in reality.emergent_dimensions
    assert "epsilon" in reality.emergent_dimensions
    assert "continuous" in reality.emergent_dimensions
    assert reality.runtime_dimensions is not None
    expected_runtime_dims = int(round(reality.emergent_dimensions["continuous"]))
    assert reality.runtime_dimensions == max(1, expected_runtime_dims)


def test_particle_constraint_cycle():
    """Test particles are linked to closed constraint cycles."""
    reality = Reality(RealityConfig())
    reality.initialize()
    particle_id = reality.create_particle(
        particle_type="electron", position=np.array([0.0, 0.0, 0.0])
    )
    pdata = reality.quantum_engine.particles[particle_id]
    cycle = pdata["constraint_cycle"]
    assert len(cycle) >= 4
    assert cycle[0] == cycle[-1]


def test_mcs_partial_order_time():
    """Test time-as-partial-order and causal relation extraction."""
    mcs = MonolithicSubstrate()
    n0 = mcs.create_initial_node({"seed"})
    n1, n2 = mcs.apply_self_differentiation(n0)
    mcs.set_causal_dependency(n0, n1)
    mcs.set_causal_dependency(n1, n2)

    layers = mcs.get_time_partial_order()
    assert len(layers) >= 2
    assert n0 in layers[0]
    assert n2 in layers[-1]
