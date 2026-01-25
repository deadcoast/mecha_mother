"""
Particle definitions and types.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any
import numpy as np


class ParticleType(Enum):
    """Standard particle types."""
    ELECTRON = "electron"
    PROTON = "proton"
    NEUTRON = "neutron"
    PHOTON = "photon"
    QUARK_UP = "quark_up"
    QUARK_DOWN = "quark_down"


@dataclass
class Particle:
    """Represents a fundamental particle."""
    
    id: str
    particle_type: ParticleType
    position: np.ndarray
    momentum: np.ndarray
    properties: Dict[str, Any]
    
    def __post_init__(self):
        """Validate particle properties."""
        if len(self.position) != len(self.momentum):
            raise ValueError("Position and momentum must have same dimension")
