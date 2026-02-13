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
        self.causal_graph = nx.DiGraph()
        self.step_count = 0
        self._next_id = 0
        self.distinction_amplitudes: Dict[str, complex] = {}
        self.theta_context: Dict[str, float] = {}

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
        self.causal_graph.add_node(node_id)
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

    def set_causal_dependency(self, prerequisite_id: int, dependent_id: int) -> None:
        """
        Add causal relation a ≺ b: a is necessary for b.
        """
        if prerequisite_id not in self.nodes or dependent_id not in self.nodes:
            raise ValueError("Both nodes must exist before adding causal dependency")
        self.causal_graph.add_edge(prerequisite_id, dependent_id)

    def derive_causal_relations(self, support_threshold: float = 0.5) -> nx.DiGraph:
        """
        Derive causal graph from directional satisfaction support strengths.
        """
        derived = nx.DiGraph()
        for node_id in self.nodes:
            derived.add_node(node_id)
        for node_i in self.nodes.values():
            for node_j in self.nodes.values():
                if node_i.id == node_j.id:
                    continue
                support_ij = node_i.satisfaction_links.get(node_j.id, 0.0)
                support_ji = node_j.satisfaction_links.get(node_i.id, 0.0)
                if support_ij >= support_threshold and support_ji < support_threshold:
                    derived.add_edge(node_i.id, node_j.id)
        self.causal_graph = derived
        return derived

    def get_time_partial_order(self) -> List[List[int]]:
        """
        Return layered partial order over causal graph.

        Each inner list is a set of nodes that are incomparable at that layer.
        """
        if len(self.causal_graph.nodes) == 0:
            return []

        # If cycles exist, condense strongly connected components to a DAG first.
        if not nx.is_directed_acyclic_graph(self.causal_graph):
            dag = nx.condensation(self.causal_graph)
            condensed_layers: List[List[int]] = []
            current = [n for n, deg in dag.in_degree() if deg == 0]
            visited = set()
            while current:
                condensed_layers.append(current)
                visited.update(current)
                nxt = []
                for c in current:
                    for succ in dag.successors(c):
                        if succ in visited:
                            continue
                        if all(pred in visited for pred in dag.predecessors(succ)):
                            nxt.append(succ)
                current = sorted(set(nxt))
            return condensed_layers

        # DAG case: standard Kahn-style layering.
        indeg = {n: self.causal_graph.in_degree(n) for n in self.causal_graph.nodes}
        frontier = sorted([n for n, d in indeg.items() if d == 0])
        ordered_layers: List[List[int]] = []
        while frontier:
            ordered_layers.append(frontier)
            next_frontier: List[int] = []
            for n in frontier:
                for succ in self.causal_graph.successors(n):
                    indeg[succ] -= 1
                    if indeg[succ] == 0:
                        next_frontier.append(succ)
            frontier = sorted(next_frontier)
        return ordered_layers

    def compute_relational_potential(
        self, state: np.ndarray, theta: Optional[Dict[str, float]] = None
    ) -> float:
        """
        Compute relational potential Φ_rel(X, Θ) from consistency couplings.
        """
        if len(state) == 0:
            return 0.0
        theta = theta or {}
        coupling_scale = float(theta.get("coupling_scale", 1.0))
        pairwise = 0.0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                pairwise += float(np.abs(state[i] * np.conj(state[j])))
        return float(coupling_scale * pairwise / max(1, len(state)))

    def consistency_path_integral(
        self,
        path: np.ndarray,
        lambda_scale: float = 1.0,
        theta: Optional[Dict[str, float]] = None,
        dt: float = 1.0,
    ) -> complex:
        """
        Compute consistency path integral:
        P[X(t)] = exp(i * λ * ∫ C{X, Xdot, Xddot; Θ} dτ)
        """
        if path.ndim < 2 or len(path) < 2:
            return 1.0 + 0j

        theta = theta or {}
        c_accum = 0.0
        for t in range(1, len(path)):
            x = path[t]
            x_prev = path[t - 1]
            x_dot = (x - x_prev) / dt
            if t > 1:
                x_ddot = (path[t] - 2 * path[t - 1] + path[t - 2]) / (dt * dt)
            else:
                x_ddot = np.zeros_like(x_dot)

            local_c = (
                np.linalg.norm(x)
                + 0.5 * np.linalg.norm(x_dot)
                + 0.25 * np.linalg.norm(x_ddot)
                + self.compute_relational_potential(x, theta=theta)
            )
            c_accum += float(local_c) * dt

        phase = float(lambda_scale * c_accum)
        return complex(np.exp(1j * phase))

    def create_distinction_amplitude_field(
        self, distinctions: List[str], theta: Optional[Dict[str, float]] = None
    ) -> Dict[str, complex]:
        """
        Create distinction amplitude field A({chi}, Theta).
        """
        theta = theta or {}
        base_scale = float(theta.get("base_scale", 1.0))
        self.theta_context = theta
        self.distinction_amplitudes = {}
        for i, d in enumerate(distinctions):
            phase = 2.0 * np.pi * i / max(1, len(distinctions))
            self.distinction_amplitudes[d] = base_scale * np.exp(1j * phase)
        return self.distinction_amplitudes.copy()

    def observation_probability(
        self, distinction: str, relevance: float = 1.0
    ) -> float:
        """
        Compute P(observe d) ∝ |A(d)|^2 * R(d, O).
        """
        if distinction not in self.distinction_amplitudes:
            return 0.0
        weights = {
            d: (abs(a) ** 2) * max(0.0, relevance)
            for d, a in self.distinction_amplitudes.items()
        }
        total = float(sum(weights.values()))
        if total <= 0:
            return 0.0
        return float(weights[distinction] / total)

    def evolve_distinction_field(
        self,
        dt: float = 0.01,
        steps: int = 100,
        coupling: float = 0.05,
    ) -> Dict[str, complex]:
        """
        Evolve distinction field by a non-linear master-constraint approximation:
        i dA/dT = H_MCS[A,Theta] A
        """
        if not self.distinction_amplitudes:
            return {}

        keys = list(self.distinction_amplitudes.keys())
        A = np.array([self.distinction_amplitudes[k] for k in keys], dtype=complex)
        n = len(A)
        H = np.eye(n, dtype=complex)
        for i in range(n):
            for j in range(n):
                if i != j:
                    H[i, j] = 1.0 / (1.0 + abs(i - j))

        for _ in range(max(0, steps)):
            linear = -1j * dt * (H @ A)
            nonlinear = -1j * dt * coupling * (np.abs(A) ** 2) * A
            A = A + linear + nonlinear
            A = A / (np.linalg.norm(A) + 1e-10)

        self.distinction_amplitudes = {k: A[i] for i, k in enumerate(keys)}
        return self.distinction_amplitudes.copy()
