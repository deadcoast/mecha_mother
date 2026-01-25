"""
Basic tests for mecha_mother.
"""

import numpy as np
import pytest
from mecha_mother import Reality, RealityConfig
from mecha_mother.core import MonolithicSubstrate, MCSNode


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
    assert reality.initialize() == True
    assert reality.state.value == 2  # ACTIVE


def test_particle_creation():
    """Test particle creation."""
    reality = Reality(RealityConfig())
    reality.initialize()
    
    particle_id = reality.create_particle(
        particle_type='electron',
        position=np.array([0.0, 0.0, 0.0])
    )
    
    assert particle_id.startswith('particle_')
    assert len(reality.quantum_engine.particles) > 0


def test_conscious_being_creation():
    """Test conscious being creation."""
    config = RealityConfig(consciousness_support=True)
    reality = Reality(config)
    reality.initialize()
    
    being_id = reality.create_conscious_being(
        being_type='human',
        initial_consciousness=15.0
    )
    
    assert being_id.startswith('being_')
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
    assert 'λ_1' in qualia
    
    # Test consciousness measurement
    state = np.random.randn(5) + 1j * np.random.randn(5)
    state = state / np.linalg.norm(state)
    c = op.measure_consciousness(state)
    
    assert c >= 0
    assert isinstance(c, float)
