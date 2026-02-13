"""
Particle definitions and types.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Any, List
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
    constraint_cycle: List[int] = field(default_factory=list)

    def __post_init__(self):
        """Validate particle properties."""
        if len(self.position) != len(self.momentum):
            raise ValueError("Position and momentum must have same dimension")

    def is_closed_constraint_loop(self) -> bool:
        """Whether this particle has an explicit closed constraint cycle."""
        return (
            len(self.constraint_cycle) >= 3
            and self.constraint_cycle[0] == self.constraint_cycle[-1]
        )
