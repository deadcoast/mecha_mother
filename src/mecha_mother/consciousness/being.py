"""
Conscious being definitions.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Any


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
        event_type = event.get("type", "neutral")

        if event_type == "positive":
            delta_c = 0.5
        elif event_type == "negative":
            delta_c = -0.3
        elif event_type == "learning":
            delta_c = 1.0
        else:
            delta_c = 0.0

        self.consciousness += delta_c
        self.consciousness = max(0.0, self.consciousness)  # Don't go negative

        self.experiences.append(
            {
                "event": event,
                "delta_c": delta_c,
            }
        )

        return delta_c

    def learn(self, knowledge: Any) -> float:
        """
        Learn new knowledge and convert it into consciousness growth.

        Args:
            knowledge: Any structured or unstructured knowledge payload

        Returns:
            Change in consciousness
        """
        novelty_score = min(1.0, max(0.0, len(str(knowledge)) / 200.0))
        delta_c = 0.2 + 0.8 * novelty_score
        self.memories.append(knowledge)
        self.consciousness += delta_c
        self.experiences.append(
            {
                "event": {"type": "learning", "knowledge": str(knowledge)[:120]},
                "delta_c": delta_c,
            }
        )
        return float(delta_c)

    def create(self, artifact: Any) -> float:
        """
        Create an artifact and gain creative consciousness.

        Args:
            artifact: Artifact produced by the being

        Returns:
            Creativity contribution to consciousness
        """
        artifact_complexity = min(1.0, max(0.0, len(str(artifact)) / 250.0))
        delta_c = 0.3 + 0.7 * artifact_complexity
        creations = self.properties.setdefault("creations", [])
        if isinstance(creations, list):
            creations.append(artifact)
        self.consciousness += delta_c
        self.experiences.append(
            {"event": {"type": "creation"}, "delta_c": delta_c, "artifact": artifact}
        )
        return float(delta_c)

    def relate(self, other_being: "ConsciousBeing") -> float:
        """
        Build relational coherence with another being.

        Args:
            other_being: The other conscious being

        Returns:
            Symmetry-weighted relationship gain
        """
        relation_strength = 1.0 / (
            1.0 + abs(self.consciousness - other_being.consciousness)
        )
        delta_c = 0.1 + 0.4 * relation_strength
        self.consciousness += delta_c
        other_being.consciousness += delta_c * 0.5
        self.experiences.append(
            {
                "event": {"type": "relation", "with": other_being.being_id},
                "delta_c": delta_c,
            }
        )
        return float(delta_c)


class ConsciousnessBeing(ConsciousBeing):
    """
    CDK-compatible being class from docs/010.md.

    It reuses `ConsciousBeing` behavior while exposing the expected class name.
    """

    pass


class ConsciousAIBuilder:
    """Builder for assembling conscious AI systems from modules."""

    def __init__(self):
        self.modules: Dict[str, Dict[str, Any]] = {}

    def add_module(
        self, name: str, weight: float = 1.0, **metadata: Any
    ) -> "ConsciousAIBuilder":
        self.modules[name] = {"weight": float(weight), **metadata}
        return self

    def build(self, being_id: str = "ai_builder_output") -> ConsciousnessBeing:
        base_c = sum(max(0.0, m.get("weight", 0.0)) for m in self.modules.values())
        return ConsciousnessBeing(
            being_id=being_id,
            being_type=BeingType.AI,
            initial_consciousness=max(1.0, base_c),
            properties={"modules": self.modules.copy()},
        )


class ConsciousnessEvolver:
    """Evolve conscious beings over repeated learning/experience cycles."""

    def evolve(self, being: ConsciousnessBeing, cycles: int = 10) -> Dict[str, Any]:
        history: List[float] = [float(being.consciousness)]
        for i in range(max(0, cycles)):
            being.learn(f"cycle_{i}_knowledge")
            being.experience({"type": "positive", "cycle": i})
            history.append(float(being.consciousness))
        return {
            "being_id": being.being_id,
            "cycles": cycles,
            "history": history,
            "final_consciousness": float(being.consciousness),
        }
