"""
Tests for ethics and aesthetics components.
"""

import numpy as np
from mecha_mother import Reality, RealityConfig
from mecha_mother.ethics import EthicsEngine, EthicalDecisionEngine, EthicsCompiler
from mecha_mother.aesthetics import AestheticsEngine, BeautyOperator


def test_ethics_engine():
    """Test ethics engine."""
    engine = EthicsEngine()

    # Test moral value computation
    beings = []
    action = {"type": "help", "time_until_effect": 0}
    value = engine.compute_moral_value(action, beings)
    assert isinstance(value, float)


def test_ethics_engine_moral_value_gradient_signs():
    """Gradient-based moral value should reward help and penalize harm."""
    engine = EthicsEngine()
    beings = [{"type": "human", "weight": 1.0}]
    baseline = np.array([1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j], dtype=complex)

    help_action = {"type": "help", "effect_vector": np.array([0.2, 0.1, 0.0])}
    harm_action = {"type": "harm", "effect_vector": np.array([-0.2, -0.1, 0.0])}

    help_value = engine.decision_engine.compute_moral_value(
        help_action, beings, current_state=baseline, time_horizon=20
    )
    harm_value = engine.decision_engine.compute_moral_value(
        harm_action, beings, current_state=baseline, time_horizon=20
    )

    assert help_value > harm_value


def test_ethical_decision_engine():
    """Test ethical decision engine."""
    engine = EthicalDecisionEngine()

    beings = []
    options = [
        {"type": "help", "name": "Help all"},
        {"type": "harm", "name": "Harm all"},
        {"type": "neutral", "name": "Do nothing"},
    ]

    result = engine.moral_decision(options=options, current_state=None, beings=beings)

    assert "best_option" in result
    assert "moral_value" in result
    assert "best_magnitude" in result
    assert "all_magnitudes" in result
    assert result["best_option"] is not None
    assert result["best_magnitude"] >= 0


def test_beauty_operator():
    """Test beauty operator."""
    op = BeautyOperator(dimension=8)

    # Test beauty computation
    test_array = np.array([1, 0.618, 0.382, 0.236, 0.146, 0.090, 0.056, 0.034])
    beauty = op.compute_beauty(test_array)

    assert 0 <= beauty <= 10
    assert isinstance(beauty, float)
    vec = test_array / (np.linalg.norm(test_array) + 1e-10)
    complexity = op._compute_complexity(vec)
    compression = 1.0 / (1.0 + complexity)
    symmetry = op._compute_symmetry(vec)
    novelty = op._compute_novelty(vec)
    meaning = op._compute_meaning(vec)
    vc41 = 0.35 * compression + 0.25 * symmetry + 0.20 * novelty + 0.20 * meaning
    vc39 = (compression / (complexity + 1e-10)) * (1.0 - novelty)
    eigvals = np.linalg.eigvals(op.B)
    expected = np.clip(
        (0.5 * vc39 + 0.5 * vc41) * 10.0 / (np.max(np.abs(eigvals)) + 1e-10),
        0.0,
        10.0,
    )
    assert np.isclose(beauty, float(expected), atol=1e-6, rtol=1e-6)

    # Test text beauty
    text_beauty = op.compute_beauty("Golden light through fractal leaves")
    assert 0 <= text_beauty <= 10


def test_beauty_metrics_monotonicity():
    """Symmetry and complexity metrics should respond monotonically to perturbations."""
    op = BeautyOperator(dimension=8)
    symmetric = np.array([1.0, 0.8, 0.6, 0.4, 0.4, 0.6, 0.8, 1.0], dtype=float)
    asymmetric = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=float)
    repetitive = np.ones(8, dtype=float)
    noisy = np.array([0.11, 0.93, 0.47, 0.72, 0.05, 0.66, 0.31, 0.88], dtype=float)

    sym_score = op._compute_symmetry(symmetric)
    asym_score = op._compute_symmetry(asymmetric)
    rep_complexity = op._compute_complexity(repetitive)
    noisy_complexity = op._compute_complexity(noisy)

    assert sym_score > asym_score
    assert rep_complexity <= noisy_complexity


def test_aesthetics_engine():
    """Test aesthetics engine."""
    engine = AestheticsEngine()

    # Test art generation
    poem = engine.generate_beautiful_art("poetic")
    assert isinstance(poem, str)
    assert len(poem) > 0

    # Test visual art generation
    visual = engine.generate_beautiful_art("visual")
    assert visual is not None
    assert isinstance(visual, np.ndarray)


def test_reality_with_ethics():
    """Test reality with ethics enabled."""
    config = RealityConfig(consciousness_support=True, ethical_constraints=True)
    reality = Reality(config)
    reality.initialize()

    # Try to modify constant - should check ethics
    success = reality.modify_physical_constant("alpha", 1 / 137.035)
    assert isinstance(success, bool)

    # Try unethical modification
    success = reality.modify_physical_constant("c", 1000.0)  # Too low
    # Should be blocked or fail
    assert isinstance(success, bool)


def test_reality_with_beauty():
    """Test reality with beauty optimization."""
    config = RealityConfig(consciousness_support=True, beauty_optimization=True)
    reality = Reality(config)
    reality.initialize()
    assert reality.beauty_field is not None
    initial_b = reality.beauty_field.average_beauty()
    assert 0.0 <= initial_b <= 10.0

    # Optimize for beauty
    results = reality.optimize_for_beauty(target_b=8.0)
    assert "success" in results
    assert results["success"]
    assert reality.beauty_field is not None
    assert reality.beauty_field.average_beauty() >= initial_b


def test_beauty_field_updates_on_constant_change():
    """Test beauty field reacts to physical constant updates."""
    config = RealityConfig(
        consciousness_support=True, beauty_optimization=True, ethical_constraints=False
    )
    reality = Reality(config)
    reality.initialize()
    assert reality.beauty_field is not None
    before = reality.beauty_field.average_beauty()
    reality.modify_physical_constant("alpha", 1 / 120.0)
    assert reality.beauty_field.constant_sensitivity != 1.0
    after = reality.beauty_field.average_beauty()
    assert 0.0 <= before <= 10.0
    assert 0.0 <= after <= 10.0


def test_rights_and_golden_rule():
    """Test rights hierarchy and golden-rule balance calculations."""
    engine = EthicsEngine()
    rights = engine.compute_rights_hierarchy(
        system_consciousness=10.0, total_consciousness=100.0, dC_dt=1.5
    )
    assert "right_to_exist" in rights
    assert rights["right_to_exist"] > 0

    balance = engine.compute_golden_rule_balance(dC_you_dT=1.0, dC_other_dT=1.0)
    assert balance["golden_rule_satisfied"] == 1.0


def test_masterpiece_metric():
    """Test masterpiece criterion computation."""
    engine = AestheticsEngine()
    history = np.array([8.0, 8.5, 9.0, 9.3, 9.5, 9.6, 9.7])
    score = engine.masterpiece_score(history, dt=1.0, theta_masterpiece=10.0)
    assert "score" in score
    assert "is_masterpiece" in score


def test_eigenvalue_pattern_verification():
    """Test eigenvalue pattern verification API."""
    engine = AestheticsEngine()
    result = engine.verify_eigenvalue_patterns()
    assert "observed" in result
    assert "targets" in result
    assert "matches_expected" in result


def test_ethics_compiler_transform():
    """Test ethics compiler transforms unsafe operations."""
    compiler = EthicsCompiler()
    compiled = compiler.compile_program(
        [{"type": "help"}, {"type": "harm"}, {"type": "destroy"}]
    )
    transformed_types = [c["type"] for c in compiled]
    assert "assist" in transformed_types
    assert "decommission_safely" in transformed_types


def test_good_evil_magnitude_formula():
    """Test good/evil magnitude calculation API."""
    engine = EthicalDecisionEngine()

    beings = [
        type("B", (), {"consciousness": 5.0})(),
        type("B", (), {"consciousness": 3.0})(),
    ]
    help_action = {"type": "help", "num_affected": 2}
    harm_action = {"type": "harm", "num_affected": 2}

    help_mag = engine.compute_good_evil_magnitude(help_action, beings)
    harm_mag = engine.compute_good_evil_magnitude(harm_action, beings)
    zero_base_mag = engine.compute_good_evil_magnitude(
        help_action, beings, baseline_total_consciousness=0.0
    )

    assert help_mag >= 0.0
    assert harm_mag >= 0.0
    assert zero_base_mag >= 0.0
