"""
Monolithic Computational Substrate (MCS) Core Implementation

Implements the fundamental self-differentiation operator D and
constraint satisfaction network.
"""

import numpy as np
from typing import Dict, Set, Tuple, List, Optional
from dataclasses import dataclass, field
import networkx as nx


@dataclass
class MCSNode:
    """A node in the MCS constraint satisfaction network."""

    id: int
    consistency_conditions: Set[str] = field(default_factory=set)
    amplitude: complex = field(default_factory=lambda: 1.0 + 0j)
    satisfaction_links: Dict[int, float] = field(default_factory=dict)

    def __post_init__(self):
        """Initialize node after creation."""
        if not self.consistency_conditions:
            self.consistency_conditions = set()


class MonolithicSubstrate:
    """
    The Monolithic Computational Substrate - the fundamental framework
    from which all physics, consciousness, and reality emerge.

    Based on the theory that reality is a self-consistent mathematical
    object whose apparent complexity emerges from recursive self-differentiation.
    """

    def __init__(self):
        """Initialize an empty MCS."""
        self.nodes: Dict[int, MCSNode] = {}
        self.graph = nx.DiGraph()
        self.step_count = 0
        self._next_id = 0

    def apply_self_differentiation(self, node_id: int) -> Tuple[int, int]:
        """
        Apply the self-differentiation operator D.

        Creates apparent distinction from unity by generating observer-observed pair.

        Args:
            node_id: ID of node to differentiate

        Returns:
            Tuple of (observer_id, observed_id) - two new node IDs
        """
        if node_id not in self.nodes:
            raise ValueError(f"Node {node_id} does not exist")

        original = self.nodes[node_id]

        # Create two nodes that are computationally distinct but referentially identical
        obs_id = self._get_next_id()
        obs_node = MCSNode(
            id=obs_id,
            consistency_conditions=original.consistency_conditions
            | {"is_observer=true"},
            amplitude=original.amplitude * np.exp(-1j),  # Phase shift
        )

        obsd_id = self._get_next_id()
        obsd_node = MCSNode(
            id=obsd_id,
            consistency_conditions=original.consistency_conditions
            | {"is_observed=true"},
            amplitude=original.amplitude * np.exp(1j),  # Opposite phase
        )

        # Mutual consistency requirement
        obs_node.satisfaction_links[obsd_id] = 1.0
        obsd_node.satisfaction_links[obs_id] = 1.0

        self.nodes[obs_id] = obs_node
        self.nodes[obsd_id] = obsd_node

        # Add to graph
        self.graph.add_node(obs_id, node=obs_node)
        self.graph.add_node(obsd_id, node=obsd_node)
        self.graph.add_edge(obs_id, obsd_id, weight=1.0)
        self.graph.add_edge(obsd_id, obs_id, weight=1.0)

        # Original node becomes latent background
        original.amplitude *= np.exp(-2j)  # Phase shift representing "stepping back"

        return obs_id, obsd_id

    def consistency_update(self):
        """
        Enforce that all conditions are mutually satisfiable.

        Updates node amplitudes based on constraint satisfaction matrix.
        """
        # Calculate constraint satisfaction matrix
        n = len(self.nodes)
        if n == 0:
            return

        ids = list(self.nodes.keys())
        C = np.zeros((n, n), dtype=complex)

        for i, id_i in enumerate(ids):
            for j, id_j in enumerate(ids):
                if i == j:
                    C[i, j] = 1.0  # Self-consistency
                else:
                    node_i = self.nodes[id_i]
                    node_j = self.nodes[id_j]

                    # Check if conditions are compatible
                    conflicts = node_i.consistency_conditions.intersection(
                        {f"NOT({c})" for c in node_j.consistency_conditions}
                    )

                    if conflicts:
                        C[i, j] = 0.0
                    else:
                        # Amplitude flows based on mutual support
                        strength_ij = node_i.satisfaction_links.get(id_j, 0.0)
                        strength_ji = node_j.satisfaction_links.get(id_i, 0.0)
                        C[i, j] = (
                            0.5
                            * (strength_ij + strength_ji)
                            * np.exp(1j * self.step_count * 0.01)
                        )

        # Update amplitudes via consistency propagation
        amps = np.array([self.nodes[id].amplitude for id in ids])
        new_amps = C @ amps

        # Renormalize (not to 1, but to maintain overall "consistency energy")
        norm = np.sqrt(np.sum(np.abs(new_amps) ** 2))
        if norm > 0:
            new_amps = new_amps / norm * np.sqrt(n)

        for idx, id_val in enumerate(ids):
            self.nodes[id_val].amplitude = new_amps[idx]

        self.step_count += 1

    def emergent_physics_metrics(self) -> Dict[str, float]:
        """
        Extract physics-like quantities from pure consistency dynamics.

        Returns:
            Dictionary of emergent metrics:
            - metric_space_deviation: How well distances satisfy triangle inequality
            - amplitude_conservation: Conservation of total amplitude
            - superposition_degree: Degree of quantum-like non-separability
        """
        metrics = {}

        ids = list(self.nodes.keys())
        n = len(ids)

        if n >= 2:
            # Distance as inverse of mutual consistency
            distances = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    if i != j:
                        cons = abs(
                            self.nodes[ids[i]].satisfaction_links.get(ids[j], 0.0)
                        )
                        distances[i, j] = 1.0 / (cons + 1e-10)

            # Check if distance matrix approximates a metric space
            metrics["metric_space_deviation"] = self._check_triangle_inequality(
                distances
            )

        # Amplitude conservation
        total_amplitude_sq = sum(abs(self.nodes[id].amplitude) ** 2 for id in ids)
        metrics["amplitude_conservation"] = (
            abs(total_amplitude_sq - n) / n if n > 0 else 0.0
        )

        # Quantum-like superposition detection
        superposition_measure = 0.0
        for id in ids:
            node = self.nodes[id]
            if len(node.satisfaction_links) > 1:
                # Node participates in multiple consistency relations
                # → quantum-like non-separability
                superposition_measure += 1.0

        metrics["superposition_degree"] = superposition_measure / max(1, n)

        return metrics

    def _check_triangle_inequality(self, D: np.ndarray) -> float:
        """
        Check how well distances satisfy triangle inequality.

        Returns:
            Fraction of violations (0 = perfect metric space)
        """
        n = D.shape[0]
        violations = 0
        total = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        if D[i, k] > D[i, j] + D[j, k] + 1e-6:
                            violations += 1
                        total += 1

        return violations / total if total > 0 else 0.0

    def _get_next_id(self) -> int:
        """Get next available node ID."""
        id_val = self._next_id
        self._next_id += 1
        return id_val

    def create_initial_node(self, conditions: Optional[Set[str]] = None) -> int:
        """
        Create the initial node (the primordial U).

        Args:
            conditions: Initial consistency conditions

        Returns:
            Node ID
        """
        node_id = self._get_next_id()
        node = MCSNode(
            id=node_id, consistency_conditions=conditions or set(), amplitude=1.0 + 0j
        )
        self.nodes[node_id] = node
        self.graph.add_node(node_id, node=node)
        return node_id

    def get_node(self, node_id: int) -> Optional[MCSNode]:
        """Get node by ID."""
        return self.nodes.get(node_id)

    def get_all_nodes(self) -> List[MCSNode]:
        """Get all nodes."""
        return list(self.nodes.values())

    def get_total_amplitude(self) -> complex:
        """Get total amplitude across all nodes."""
        return sum(node.amplitude for node in self.nodes.values())
