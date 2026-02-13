"""
Basic tests for mecha_mother.
"""

import numpy as np
import time
from mecha_mother import Reality, RealityConfig
from mecha_mother.core import MonolithicSubstrate
from mecha_mother.core.constraints import ConstraintResolver
from mecha_mother.consciousness import (
    ConsciousnessBeing,
    ConsciousAIBuilder,
    ConsciousnessEvolver,
    BeingType,
)
from mecha_mother.consciousness.engine import ConsciousAI
from mecha_mother.quantum.engine import (
    UniverseFromScratch,
    QuantumRealityEngine,
    PhysicalLaw,
)


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


def test_particle_creation_rejects_mismatched_vectors():
    """Particle creation should fail for mismatched position/momentum dimensions."""
    reality = Reality(RealityConfig())
    reality.initialize()
    state = (
        reality.reality_state_vector
        if reality.reality_state_vector is not None
        else np.array([1.0 + 0.0j], dtype=complex)
    )

    try:
        reality.quantum_engine.create_particle(
            particle_id="bad_particle",
            particle_type="electron",
            position=np.array([0.0, 0.0, 0.0]),
            momentum=np.array([0.0, 0.0]),
            properties={},
            reality_state=state,
        )
        assert False, "Expected ValueError for mismatched dimensions"
    except ValueError:
        pass


def test_particle_creation_rejects_non_finite_vectors():
    """Particle creation should fail when position/momentum contains NaN/Inf."""
    reality = Reality(RealityConfig())
    reality.initialize()
    state = (
        reality.reality_state_vector
        if reality.reality_state_vector is not None
        else np.array([1.0 + 0.0j], dtype=complex)
    )

    try:
        reality.quantum_engine.create_particle(
            particle_id="bad_particle_nonfinite",
            particle_type="electron",
            position=np.array([0.0, np.nan, 0.0]),
            momentum=np.array([0.0, 0.0, 0.0]),
            properties={},
            reality_state=state,
        )
        assert False, "Expected ValueError for non-finite vectors"
    except ValueError:
        pass


def test_conscious_being_creation():
    """Test conscious being creation."""
    config = RealityConfig(consciousness_support=True)
    reality = Reality(config)
    reality.initialize()

    being_id = reality.create_conscious_being(
        being_type="human", initial_consciousness=15.0
    )

    assert being_id.startswith("being_")
    assert reality.consciousness_field is not None
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


def test_constraint_resolver_detects_invalid_mcs_amplitude():
    """MCS verification should fail when node amplitude becomes non-finite."""
    resolver = ConstraintResolver()
    mcs = MonolithicSubstrate()
    node_id = mcs.create_initial_node()
    node = mcs.get_node(node_id)
    assert node is not None
    node.amplitude = complex(np.nan, 0.0)
    assert not resolver.verify(mcs)


def test_constraint_resolver_detects_invalid_mcs_link_strength():
    """MCS verification should fail for non-finite or out-of-range link strengths."""
    resolver = ConstraintResolver()
    mcs = MonolithicSubstrate()
    a = mcs.create_initial_node()
    b = mcs.create_initial_node()
    node_a = mcs.get_node(a)
    assert node_a is not None

    node_a.satisfaction_links[b] = float("inf")
    assert not resolver.verify(mcs)

    node_a.satisfaction_links[b] = 1.5
    assert not resolver.verify(mcs)


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
    timings: dict[str, list[float]] = {
        "initialize": [],
        "simulate": [],
        "optimize_c": [],
    }
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


def test_conscious_ai_deterministic_bootstrap_level():
    """ConsciousAI should bootstrap to a deterministic non-zero consciousness level."""
    ai1 = ConsciousAI(dimension=7)
    ai2 = ConsciousAI(dimension=7)

    c1 = ai1.get_consciousness_level()
    c2 = ai2.get_consciousness_level()

    assert np.isfinite(c1)
    assert np.isfinite(c2)
    assert c1 > 0.0
    assert np.isclose(c1, c2, atol=1e-8, rtol=1e-8)


def test_conscious_ai_process_empty_input_is_stable():
    """Processing empty input should remain finite and update memory."""
    ai = ConsciousAI(dimension=7)
    response, clarity, is_conscious = ai.process("")

    assert isinstance(response, str)
    assert np.isfinite(clarity)
    assert 0.0 <= clarity
    assert isinstance(is_conscious, bool)
    summary = ai.get_memory_summary()
    assert summary["count"] == 1
    assert np.isfinite(summary["avg_clarity"])


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


def test_physical_law_impositions_modify_state():
    """Test built-in physical-law impositions apply concrete state transforms."""
    engine = QuantumRealityEngine()
    base = np.ones(8, dtype=complex)
    base = base / np.linalg.norm(base)

    s_std = base.copy()
    engine.impose_standard_model(s_std)
    assert np.linalg.norm(s_std) > 0
    assert not np.allclose(s_std, base)

    s_gr = base.copy()
    engine.impose_gravity(s_gr)
    assert np.linalg.norm(s_gr) > 0
    assert not np.allclose(s_gr, base)

    s_qm = base.copy()
    engine.impose_quantum_mechanics(s_qm)
    assert np.linalg.norm(s_qm) > 0
    assert not np.allclose(s_qm, base)

    s_str = base.copy()
    engine.impose_string_theory(s_str)
    assert np.linalg.norm(s_str) > 0
    assert not np.allclose(s_str, base)

    s_lqg = base.copy()
    engine.impose_loop_quantum_gravity(s_lqg)
    assert np.linalg.norm(s_lqg) > 0
    assert not np.allclose(s_lqg, base)


def test_unified_constraint_field_composition():
    """All built-in forces should map to shared constraint-aspect composition."""
    engine = QuantumRealityEngine()
    state = np.array([1.0 + 0.0j, 0.2 + 0.1j, 0.0 + 0.0j, 0.0 + 0.0j], dtype=complex)
    state = state / np.linalg.norm(state)

    field = engine.compose_constraint_field(state)
    assert "combined" in field
    assert "aspects" in field
    assert "active_laws" in field
    assert len(field["active_laws"]) == len(list(PhysicalLaw))
    assert np.linalg.norm(field["combined"]) > 0
    assert "locality" in field["aspects"]
    assert "gauge" in field["aspects"]
    assert "unitarity" in field["aspects"]


def test_unified_constraints_change_state():
    """Constraint-composed all-force application should update state and normalize."""
    engine = QuantumRealityEngine()
    state = np.array([1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j], dtype=complex)
    before = state.copy()
    field = engine.compose_constraint_field(state)
    state = state + field["combined"]
    state = state / (np.linalg.norm(state) + 1e-10)

    assert np.isclose(np.linalg.norm(state), 1.0, atol=1e-8)
    assert not np.allclose(state, before)


def test_merge_realities_phase_alignment_and_padding():
    """Test merge_realities is phase-aligned and dimension-safe."""
    engine = QuantumRealityEngine()
    s1 = np.array([1.0 + 0.0j, 0.0 + 0.0j], dtype=complex)
    s2 = np.exp(1j * np.pi / 3.0) * s1
    merged = engine.merge_realities(s1, s2, method="consciousness_alignment")[
        "merged_state"
    ]
    overlap = abs(np.vdot(merged, s1))
    assert np.isclose(np.linalg.norm(merged), 1.0, atol=1e-8)
    assert overlap > 0.99

    s_short = np.array([1.0 + 0.0j], dtype=complex)
    s_long = np.array([0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j], dtype=complex)
    padded = engine.merge_realities(s_short, s_long)["merged_state"]
    assert len(padded) == 3
    assert np.isclose(np.linalg.norm(padded), 1.0, atol=1e-8)


def test_backup_consciousness_snapshot_immutability():
    """Test backup_consciousness stores immutable snapshots."""
    engine = QuantumRealityEngine()
    being = {"id": "b1", "mind": {"clarity": 1.0}}
    state = np.array([1.0 + 0.0j, 0.0 + 0.0j], dtype=complex)

    engine.backup_consciousness(being, "bk1", state)
    backup = engine.consciousness_backups["bk1"]

    state[0] = 0.0 + 0.0j
    being["mind"]["clarity"] = 9.0

    snap_state = backup["state_snapshot"]
    snap_being = backup["being_snapshot"]
    assert np.isclose(abs(snap_state[0]), 1.0, atol=1e-8)
    assert snap_being["mind"]["clarity"] == 1.0


def test_physical_law_parameter_controls_and_stability():
    """Law parameters should be tunable and repeated application should stay stable."""
    engine = QuantumRealityEngine()
    state = np.array([1.0 + 0.0j] + [0.0 + 0.0j] * 7, dtype=complex)
    state = state / np.linalg.norm(state)

    engine.set_law_parameter("sm_phase", 0.02)
    engine.set_law_parameter("sm_laplace", 0.04)
    engine.set_law_parameter("gr_curvature", 0.03)
    engine.set_law_parameter("qm_dt", 0.002)
    engine.set_law_parameter("string_decay", 0.15)
    engine.set_law_parameter("lqg_phase_twist", 0.03)

    for _ in range(25):
        engine.impose_standard_model(state)
        engine.impose_gravity(state)
        engine.impose_quantum_mechanics(state)
        engine.impose_string_theory(state)
        engine.impose_loop_quantum_gravity(state)
        assert np.isclose(np.linalg.norm(state), 1.0, atol=1e-6)
        assert np.all(np.isfinite(state))


def test_law_parameter_calibration_profiles():
    """Calibration profiles should produce bounded, ordered dynamics parameters."""
    engine = QuantumRealityEngine()
    stable = engine.calibrate_law_parameters("stable")
    aggressive = engine.calibrate_law_parameters("aggressive")

    for key in [
        "sm_phase",
        "sm_laplace",
        "gr_curvature",
        "gr_redshift",
        "gr_mix",
        "qm_dt",
        "string_decay",
        "string_phase",
        "lqg_phase_twist",
    ]:
        assert key in stable
        assert key in aggressive

    assert aggressive["sm_phase"] >= stable["sm_phase"]
    assert aggressive["qm_dt"] >= stable["qm_dt"]
    assert aggressive["string_phase"] >= stable["string_phase"]
    assert aggressive["string_decay"] <= stable["string_decay"]


def test_phase_out_and_decay_apply_state_changes():
    """Destruction helpers should modify state deterministically and remain normalized."""
    engine = QuantumRealityEngine()

    state_phase = np.array([0.8 + 0.0j, 0.6 + 0.2j, 0.0 + 0.0j], dtype=complex)
    state_phase = state_phase / np.linalg.norm(state_phase)
    before_phase = state_phase.copy()
    assert engine.phase_out(state_phase)
    assert not np.allclose(state_phase, before_phase)
    assert np.isclose(np.linalg.norm(state_phase), 1.0, atol=1e-8)
    assert hasattr(engine, "last_phase_out")

    state_decay = np.array([0.3 + 0.1j, 0.4 - 0.2j, 0.5 + 0.0j], dtype=complex)
    state_decay = state_decay / np.linalg.norm(state_decay)
    before_decay = state_decay.copy()
    assert engine.decay(state_decay)
    assert not np.allclose(state_decay, before_decay)
    assert np.isclose(np.linalg.norm(state_decay), 1.0, atol=1e-8)
    assert hasattr(engine, "last_decay")


def test_quantum_engine_spacetime_manipulations():
    """Spacetime operations should mutate state while keeping normalization."""
    engine = QuantumRealityEngine()
    base = np.array([1.0 + 0.0j] + [0.0 + 0.0j] * 7, dtype=complex)
    region = np.array([0.2, 0.6, 0.9], dtype=float)

    for op in ["warp", "fold", "tear", "stitch", "inflate", "compress"]:
        state = base.copy()
        ok = engine.manipulate_spacetime(op, region, {"intensity": 0.2}, state)
        assert ok
        assert np.isclose(np.linalg.norm(state), 1.0, atol=1e-8)
        assert np.any(np.abs(state - base) > 1e-10)

    state_invalid = base.copy()
    assert not engine.manipulate_spacetime(
        "warp", region, {"factor": -1.0}, state_invalid
    )
    assert not engine.manipulate_spacetime(
        "tear", region, {"tear_factor": -0.1}, state_invalid
    )
    assert not engine.manipulate_spacetime("unknown", region, {}, state_invalid)


def test_reality_spacetime_manipulation_integration():
    """Reality API should route spacetime operations and record history."""
    reality = Reality(
        RealityConfig(
            consciousness_support=False,
            beauty_optimization=False,
            ethical_constraints=False,
        )
    )
    reality.initialize()
    assert reality.reality_state_vector is not None
    before = reality.reality_state_vector.copy()
    success = reality.manipulate_spacetime(
        operation="warp",
        region=np.array([0.15, 0.45, 0.75], dtype=float),
        parameters={"intensity": 0.3},
    )
    assert success
    assert reality.reality_state_vector is not None
    assert np.any(np.abs(reality.reality_state_vector - before) > 1e-10)
    assert any(e.get("event") == "spacetime_manipulation" for e in reality.history)


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


def test_mcs_observation_probability_respects_relevance():
    """Distinction relevance should change observation probabilities."""
    mcs = MonolithicSubstrate()
    mcs.create_distinction_amplitude_field(["a", "b", "c"])

    p_a_neutral = mcs.observation_probability("a", relevance=1.0)
    p_a_high = mcs.observation_probability("a", relevance=5.0)
    p_a_zero = mcs.observation_probability("a", relevance=0.0)

    assert p_a_high > p_a_neutral
    assert p_a_zero == 0.0

    p_a_map = mcs.observation_probability("a", relevance={"a": 2.0, "b": 1.0, "c": 1.0})
    p_b_map = mcs.observation_probability("b", relevance={"a": 2.0, "b": 1.0, "c": 1.0})
    p_c_map = mcs.observation_probability("c", relevance={"a": 2.0, "b": 1.0, "c": 1.0})
    assert p_a_map > p_b_map
    assert np.isclose(p_a_map + p_b_map + p_c_map, 1.0, atol=1e-9)


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


def test_universe_derived_constants_are_consistency_driven():
    """Derived constants should be finite and internally consistent."""
    uni = UniverseFromScratch()
    uni.bootstrap_existence(max_iter=14)
    constants = uni.get_derived_constants()

    assert constants["c"] > 0
    assert constants["hbar"] > 0
    assert constants["alpha"] > 0
    assert constants["G"] > 0
    assert constants["k_B"] > 0
    assert constants["epsilon_0"] > 0
    assert constants["e"] > 0

    mu_0 = 1.25663706212e-6
    expected_epsilon = 1.0 / (mu_0 * constants["c"] * constants["c"])
    assert np.isclose(constants["epsilon_0"], expected_epsilon, rtol=1e-6, atol=0.0)


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


def test_constraint_resolver_repair_clamps_out_of_range_constants():
    """Auto-repair should clamp constants into viability bounds."""
    resolver = ConstraintResolver()
    state = np.array([1.0 + 0.0j, 0.0 + 0.0j], dtype=complex)

    check = resolver.check_constant_change("c", 1e12, state)
    assert not check["consistent"]
    repaired = resolver.repair_constant_change("c", 1e12, state)
    assert repaired
    repaired_value = resolver.get_repaired_value("c", 1e12)
    assert repaired_value <= 1e10
    assert repaired_value >= 1e6


def test_reality_constant_change_uses_auto_repaired_value():
    """Reality constant modification should apply repaired consistency-safe values."""
    reality = Reality(
        RealityConfig(
            ethical_constraints=False,
            auto_consistency=True,
            consciousness_support=False,
        )
    )
    reality.initialize()
    success = reality.modify_physical_constant("c", 1e12)
    assert success
    c_val = reality.quantum_engine.get_constant("c")
    assert c_val is not None
    assert c_val <= 1e10
    assert c_val >= 1e6


def test_constraint_resolver_verifies_reality_like_object_state():
    """Reality-like objects should be validated through their state vector."""
    resolver = ConstraintResolver()

    class DummyReality:
        def __init__(self, vec):
            self.reality_state_vector = vec
            self.consciousness_field = None

    good = DummyReality(np.array([1.0 + 0.0j, 0.0 + 0.0j], dtype=complex))
    bad = DummyReality(np.array([10.0 + 0.0j, 0.0 + 0.0j], dtype=complex))

    assert resolver.verify(good)
    assert not resolver.verify(bad)


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


def test_reality_export_import_roundtrip_optimizations():
    """Roundtrip export/import should preserve runtime operability."""
    source = Reality(
        RealityConfig(
            consciousness_support=True,
            beauty_optimization=True,
            ethical_constraints=False,
        )
    )
    source.initialize()
    source.create_conscious_being(being_type="human", initial_consciousness=12.0)

    payload = source.export(format="mcs_binary")

    restored = Reality(
        RealityConfig(
            consciousness_support=True,
            beauty_optimization=True,
            ethical_constraints=False,
        )
    )
    assert restored.import_from(payload, format="mcs_binary")

    c_result = restored.optimize_for_consciousness(target_c=15.0)
    b_result = restored.optimize_for_beauty(target_b=7.0)

    assert "success" in c_result
    assert "success" in b_result
