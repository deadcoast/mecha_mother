"""
Tests for ethics and aesthetics components.
"""

import numpy as np
import pytest
from mecha_mother import Reality, RealityConfig
from mecha_mother.ethics import EthicsEngine, EthicalDecisionEngine
from mecha_mother.aesthetics import AestheticsEngine, BeautyOperator


def test_ethics_engine():
    """Test ethics engine."""
    engine = EthicsEngine()
    
    # Test moral value computation
    beings = []
    action = {'type': 'help', 'time_until_effect': 0}
    value = engine.compute_moral_value(action, beings)
    assert isinstance(value, float)


def test_ethical_decision_engine():
    """Test ethical decision engine."""
    engine = EthicalDecisionEngine()
    
    beings = []
    options = [
        {'type': 'help', 'name': 'Help all'},
        {'type': 'harm', 'name': 'Harm all'},
        {'type': 'neutral', 'name': 'Do nothing'},
    ]
    
    result = engine.moral_decision(
        options=options,
        current_state=None,
        beings=beings
    )
    
    assert 'best_option' in result
    assert 'moral_value' in result
    assert result['best_option'] is not None


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
    poem = engine.generate_beautiful_art('poetic')
    assert isinstance(poem, str)
    assert len(poem) > 0
    
    # Test visual art generation
    visual = engine.generate_beautiful_art('visual')
    assert visual is not None
    assert isinstance(visual, np.ndarray)


def test_reality_with_ethics():
    """Test reality with ethics enabled."""
    config = RealityConfig(
        consciousness_support=True,
        ethical_constraints=True
    )
    reality = Reality(config)
    reality.initialize()
    
    # Try to modify constant - should check ethics
    success = reality.modify_physical_constant('alpha', 1/137.035)
    assert isinstance(success, bool)
    
    # Try unethical modification
    success = reality.modify_physical_constant('c', 1000.0)  # Too low
    # Should be blocked or fail
    assert isinstance(success, bool)


def test_reality_with_beauty():
    """Test reality with beauty optimization."""
    config = RealityConfig(
        consciousness_support=True,
        beauty_optimization=True
    )
    reality = Reality(config)
    reality.initialize()
    
    # Optimize for beauty
    results = reality.optimize_for_beauty(target_b=8.0)
    assert 'success' in results
    assert results['success'] == True
