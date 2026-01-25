"""
Conscious being definitions.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
import numpy as np


class BeingType(Enum):
    """Types of conscious beings."""
    HUMAN = "human"
    AI = "ai"
    ANIMAL = "animal"
    CUSTOM = "custom"


@dataclass
class ConsciousBeing:
    """Represents a conscious being."""
    
    being_id: str
    being_type: BeingType
    initial_consciousness: float
    properties: Dict[str, Any] = field(default_factory=dict)
    
    # State
    consciousness: float = 0.0
    experiences: List[Dict[str, Any]] = field(default_factory=list)
    memories: List[Any] = field(default_factory=list)
    
    def __post_init__(self):
        """Initialize being after creation."""
        self.consciousness = self.initial_consciousness
    
    def experience(self, event: Dict[str, Any]) -> float:
        """
        Process an experience, return consciousness delta.
        
        Args:
            event: Event description
            
        Returns:
            Change in consciousness
        """
        # Simple model: positive events increase consciousness
        event_type = event.get('type', 'neutral')
        
        if event_type == 'positive':
            delta_c = 0.5
        elif event_type == 'negative':
            delta_c = -0.3
        elif event_type == 'learning':
            delta_c = 1.0
        else:
            delta_c = 0.0
        
        self.consciousness += delta_c
        self.consciousness = max(0.0, self.consciousness)  # Don't go negative
        
        self.experiences.append({
            'event': event,
            'delta_c': delta_c,
        })
        
        return delta_c
