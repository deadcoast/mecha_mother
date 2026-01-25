"""
Core MCS framework - self-differentiation and constraint satisfaction.
"""

from mecha_mother.core.mcs import MonolithicSubstrate, MCSNode
from mecha_mother.core.constraints import ConstraintResolver, ConsistencyError

__all__ = [
    "MonolithicSubstrate",
    "MCSNode",
    "ConstraintResolver",
    "ConsistencyError",
]
