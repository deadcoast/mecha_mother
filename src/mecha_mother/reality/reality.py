"""
Reality API - primary interface for manipulating universes.
"""

import numpy as np
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum

from mecha_mother.quantum.engine import QuantumRealityEngine, PhysicalLaw
from mecha_mother.consciousness.engine import ConsciousnessEngine, ConsciousnessField
from mecha_mother.core.constraints import ConstraintResolver, ConsistencyError


class RealityState(Enum):
    """Possible states of a reality instance."""
    UNINITIALIZED = 0
    INITIALIZING = 1
    ACTIVE = 2
    PAUSED = 3
    ARCHIVED = 6


@dataclass
class RealityConfig:
    """Configuration for a new reality instance."""
    
    dimensions: int = 3
    time_enabled: bool = True
    consciousness_support: bool = True
    physical_laws: List[PhysicalLaw] = field(default_factory=lambda: [
        PhysicalLaw.QUANTUM_MECHANICS
    ])
    initial_energy: float = 1e9
    entropy_seed: int = 42
    ethical_constraints: bool = True
    beauty_optimization: bool = False  # Will implement later
    auto_consistency: bool = True


class Reality:
    """
    The primary interface to manipulate reality.
    
    This class provides methods to:
    - Create/destroy universes
    - Modify physical laws and constants
    - Create conscious beings
    - Optimize for consciousness
    - Query reality state
    """
    
    def __init__(self, config: Optional[RealityConfig] = None):
        """
        Initialize a new reality instance.
        
        Args:
            config: Configuration for the reality. If None, uses defaults.
        """
        self.config = config or RealityConfig()
        self.state = RealityState.UNINITIALIZED
        self.id = self._generate_reality_id()
        
        # Core subsystems
        self.quantum_engine = QuantumRealityEngine()
        self.consciousness_engine = ConsciousnessEngine()
        self.consistency_resolver = ConstraintResolver()
        
        # State tracking
        self.reality_state_vector: Optional[np.ndarray] = None
        self.consciousness_field: Optional[ConsciousnessField] = None
        
        # History
        self.history: List[Dict[str, Any]] = []
        
        print(f"Reality instance {self.id} created.")
    
    def initialize(self) -> bool:
        """
        Initialize the reality with Big Bang or equivalent.
        
        Returns:
            True if successful, False otherwise
        """
        if self.state != RealityState.UNINITIALIZED:
            raise RuntimeError(f"Reality already in state {self.state}")
        
        self.state = RealityState.INITIALIZING
        print(f"Initializing reality {self.id}...")
        
        try:
            # Step 1: Create fundamental quantum field
            print("  Creating quantum vacuum...")
            self.reality_state_vector = self.quantum_engine.create_vacuum_state(
                dimensions=self.config.dimensions,
                energy=self.config.initial_energy,
                seed=self.config.entropy_seed
            )
            
            # Step 2: Impose physical laws
            print("  Imposing physical laws...")
            for law in self.config.physical_laws:
                if law == PhysicalLaw.QUANTUM_MECHANICS:
                    self.quantum_engine.impose_quantum_mechanics(self.reality_state_vector)
                elif law == PhysicalLaw.STANDARD_MODEL:
                    self.quantum_engine.impose_standard_model(self.reality_state_vector)
                elif law == PhysicalLaw.GENERAL_RELATIVITY:
                    self.quantum_engine.impose_gravity(self.reality_state_vector)
            
            # Step 3: Initialize time if enabled
            if self.config.time_enabled:
                print("  Initializing time dimension...")
                self.quantum_engine.initialize_time(self.reality_state_vector)
            
            # Step 4: Initialize consciousness field if enabled
            if self.config.consciousness_support:
                print("  Initializing consciousness field...")
                self.consciousness_field = self.consciousness_engine.create_field(
                    self.reality_state_vector
                )
            
            # Step 5: Run consistency checks
            if self.config.auto_consistency:
                print("  Running consistency checks...")
                if not self.consistency_resolver.verify(self):
                    raise ConsistencyError("Reality failed consistency check")
            
            self.state = RealityState.ACTIVE
            self.history.append({
                'event': 'initialization',
                'success': True
            })
            
            print(f"✓ Reality {self.id} successfully initialized!")
            print(f"  Dimensions: {self.config.dimensions}")
            print(f"  Consciousness: {'Enabled' if self.config.consciousness_support else 'Disabled'}")
            
            return True
            
        except Exception as e:
            print(f"✗ Failed to initialize reality: {e}")
            self.state = RealityState.UNINITIALIZED
            self.history.append({
                'event': 'initialization',
                'success': False,
                'error': str(e)
            })
            return False
    
    def create_particle(
        self,
        particle_type: str,
        position: np.ndarray,
        momentum: Optional[np.ndarray] = None,
        properties: Optional[Dict] = None
    ) -> str:
        """
        Create a fundamental particle.
        
        Args:
            particle_type: Type of particle ('electron', 'proton', etc.)
            position: Position in spacetime
            momentum: Initial momentum (optional)
            properties: Additional properties
            
        Returns:
            Particle ID
        """
        if self.state != RealityState.ACTIVE:
            raise RuntimeError("Reality not active")
        
        particle_id = f"particle_{len(self.quantum_engine.particles)}"
        
        if momentum is None:
            momentum = np.zeros(self.config.dimensions)
        
        self.quantum_engine.create_particle(
            particle_id=particle_id,
            particle_type=particle_type,
            position=position,
            momentum=momentum,
            properties=properties or {},
            reality_state=self.reality_state_vector
        )
        
        self.history.append({
            'event': 'particle_creation',
            'particle_id': particle_id,
            'type': particle_type
        })
        
        print(f"Created {particle_type} with ID {particle_id}")
        return particle_id
    
    def create_conscious_being(
        self,
        being_type: str = 'human',
        initial_consciousness: float = 10.0,
        properties: Optional[Dict] = None
    ) -> str:
        """
        Create a conscious being.
        
        Args:
            being_type: Type of being ('human', 'ai', 'animal')
            initial_consciousness: Starting consciousness level
            properties: Additional properties
            
        Returns:
            Being ID
        """
        if self.state != RealityState.ACTIVE:
            raise RuntimeError("Reality not active")
        
        if not self.config.consciousness_support:
            raise RuntimeError("Consciousness not enabled in this reality")
        
        being_id = f"being_{len(self.consciousness_field.get_beings())}"
        
        being = self.consciousness_engine.create_being(
            being_id=being_id,
            being_type=being_type,
            initial_consciousness=initial_consciousness,
            properties=properties or {},
            consciousness_field=self.consciousness_field
        )
        
        self.history.append({
            'event': 'being_creation',
            'being_id': being_id,
            'type': being_type,
            'initial_c': initial_consciousness
        })
        
        print(f"Created {being_type} being with ID {being_id}, ℂ={initial_consciousness}")
        return being_id
    
    def modify_physical_constant(
        self,
        constant_name: str,
        new_value: float,
        reason: Optional[str] = None
    ) -> bool:
        """
        Modify a fundamental physical constant.
        
        Args:
            constant_name: Name of constant ('c', 'hbar', 'G', 'alpha', etc.)
            new_value: New value
            reason: Reason for modification
            
        Returns:
            True if successful
        """
        if self.state != RealityState.ACTIVE:
            raise RuntimeError("Reality not active")
        
        # Check consistency
        consistency_check = self.consistency_resolver.check_constant_change(
            constant_name, new_value, self.reality_state_vector
        )
        
        if not consistency_check['consistent']:
            print(f"Would break consistency: {consistency_check['issues']}")
            if self.config.auto_consistency:
                repaired = self.consistency_resolver.repair_constant_change(
                    constant_name, new_value, self.reality_state_vector
                )
                if not repaired:
                    return False
            else:
                return False
        
        # Apply the change
        old_value = self.quantum_engine.get_constant(constant_name)
        self.quantum_engine.set_constant(constant_name, new_value)
        
        self.history.append({
            'event': 'constant_modification',
            'constant': constant_name,
            'old_value': old_value,
            'new_value': new_value,
            'reason': reason
        })
        
        print(f"Modified {constant_name}: {old_value} → {new_value}")
        return True
    
    def optimize_for_consciousness(
        self,
        target_c: float = 100.0,
        method: str = 'gradient_ascent',
        constraints: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Optimize reality for maximum consciousness.
        
        Args:
            target_c: Target consciousness level
            method: Optimization method
            constraints: Additional constraints
            
        Returns:
            Optimization results
        """
        if self.state != RealityState.ACTIVE:
            raise RuntimeError("Reality not active")
        
        if not self.config.consciousness_support:
            raise RuntimeError("Consciousness not enabled")
        
        print(f"Optimizing reality for consciousness (target: ℂ={target_c})...")
        
        results = self.consciousness_engine.optimize_reality(
            current_state=self.reality_state_vector,
            consciousness_field=self.consciousness_field,
            target_c=target_c,
            method=method,
            **(constraints or {})
        )
        
        if results['success']:
            self.consciousness_field = results.get('optimized_consciousness_field', 
                                                   self.consciousness_field)
            
            c_increase = results.get('c_increase', 0)
            final_c = results.get('final_c', 0)
            
            print(f"✓ Consciousness optimization successful!")
            print(f"  ℂ increased to {final_c:.1f}")
            print(f"  Improvement: +{c_increase:.1f}")
        
        return results
    
    def get_state(self, component: str = 'full') -> Dict[str, Any]:
        """
        Get the current state of reality.
        
        Args:
            component: Which component ('full', 'quantum', 'consciousness')
            
        Returns:
            State information
        """
        if self.state != RealityState.ACTIVE:
            raise RuntimeError("Reality not active")
        
        if component == 'full':
            return {
                'quantum': self.reality_state_vector is not None,
                'consciousness': self.consciousness_field.total_consciousness() if self.consciousness_field else None,
                'num_beings': len(self.consciousness_field.get_beings()) if self.consciousness_field else 0,
                'num_particles': len(self.quantum_engine.particles),
            }
        elif component == 'quantum':
            return {'state_vector': self.reality_state_vector}
        elif component == 'consciousness':
            if not self.config.consciousness_support:
                raise ValueError("Consciousness not enabled")
            return {
                'total_consciousness': self.consciousness_field.total_consciousness(),
                'num_beings': len(self.consciousness_field.get_beings()),
                'average_consciousness': self.consciousness_field.average_consciousness(),
            }
        else:
            raise ValueError(f"Unknown component: {component}")
    
    def _generate_reality_id(self) -> str:
        """Generate unique reality ID."""
        import uuid
        import hashlib
        import time
        
        seed = f"{uuid.uuid4()}{time.time()}{np.random.random()}"
        return hashlib.sha256(seed.encode()).hexdigest()[:16]
