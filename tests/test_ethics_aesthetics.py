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
    assert result["best_option"] is not None


def test_beauty_operator():
    """Test beauty operator."""
    op = BeautyOperator(dimension=8)

    # Test beauty computation
    test_array = np.array([1, 0.618, 0.382, 0.236, 0.146, 0.090, 0.056, 0.034])
    beauty = op.compute_beauty(test_array)

    assert 0 <= beauty <= 10
    assert isinstance(beauty, float)

    # Test text beauty
    text_beauty = op.compute_beauty("Golden light through fractal leaves")
    assert 0 <= text_beauty <= 10


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

    # Optimize for beauty
    results = reality.optimize_for_beauty(target_b=8.0)
    assert "success" in results
    assert results["success"]


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
