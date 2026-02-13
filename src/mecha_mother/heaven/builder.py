"""
Heaven Builder - constructs heaven-optimized realities.
"""

import numpy as np
from typing import Dict, List, Optional, Any
from mecha_mother import Reality, RealityConfig
from mecha_mother.heaven.optimizer import HeavenOptimizer


class HeavenBuilder:
    """
    Build heaven-optimized realities, cities, and civilizations.
    """

    def __init__(self):
        """Initialize heaven builder."""
        self.optimizer = HeavenOptimizer()
        self.templates: Dict[str, Any] = {}

    def build_heaven_city(
        self, location: str = "earth", population: int = 1000000, style: str = "utopian"
    ) -> Dict[str, Any]:
        """
        Build a heaven-optimized city.

        Args:
            location: Location for the city
            population: Target population
            style: City style ('utopian', 'transcendent', 'minimalist')

        Returns:
            Dictionary with city details and metrics
        """
        # Create base reality
        config = RealityConfig(
            dimensions=3,
            consciousness_support=True,
            beauty_optimization=True,
            ethical_constraints=True,
        )
        reality = Reality(config)
        reality.initialize()

        print(f"Building {style} heaven city for {population:,} beings...")

        # Create beings
        beings = []
        for i in range(min(population, 1000)):  # Limit for demo
            being = reality.create_conscious_being(
                being_type="human",
                initial_consciousness=np.random.normal(20, 5),
                properties={
                    "name": f"Citizen_{i}",
                    "role": self._assign_role(i),
                    "happiness": 0.8,
                },
            )
            beings.append(being)

        # Optimize city layout
        print("Optimizing city layout...")
        layout = self.optimizer._create_optimal_layout(population)

        # Optimize for beauty
        print("Optimizing for beauty...")
        reality.optimize_for_beauty(target_b=8.5, preserve_consciousness=True)

        # Optimize for consciousness
        print("Optimizing for consciousness...")
        target_c = population * 0.1  # Target: 0.1 consciousness per person
        reality.optimize_for_consciousness(target_c=target_c)

        # Measure results
        print("Measuring heaven metrics...")
        metrics = self._calculate_heaven_metrics(reality, beings)

        print("[OK] Heaven city built successfully!")
        print(f"  Average consciousness: {metrics['avg_consciousness']:.1f}")
        print(f"  Average beauty: {metrics['avg_beauty']:.1f}")
        print(f"  Happiness index: {metrics['happiness']:.2f}")
        print(f"  Heaven score: {metrics['heaven_score']:.2f}")

        return {
            "reality": reality,
            "beings": beings,
            "metrics": metrics,
            "layout": layout,
            "style": style,
            "population": population,
        }

    def build_heaven_planet(
        self, planet_type: str = "earthlike", population: int = 1000000000
    ) -> Dict[str, Any]:
        """
        Build a heaven-optimized planet.

        Args:
            planet_type: Type of planet ('earthlike', 'ocean', 'desert', etc.)
            population: Target population

        Returns:
            Dictionary with planet details
        """
        # Create reality for planet
        config = RealityConfig(
            dimensions=3,
            consciousness_support=True,
            beauty_optimization=True,
            ethical_constraints=True,
        )
        reality = Reality(config)
        reality.initialize()

        print(f"Building {planet_type} heaven planet for {population:,} beings...")

        # Create planetary consciousness
        planet_being_id = reality.create_conscious_being(
            being_type="custom",
            initial_consciousness=population * 0.01,
            properties={
                "name": f"{planet_type}_planet",
                "type": planet_type,
                "scale": "planetary",
            },
        )

        # Get the actual being object
        beings: List[Any] = []
        total_consciousness: float = 0.0
        if reality.consciousness_field is not None:
            beings = reality.consciousness_field.get_beings()
            total_consciousness = reality.consciousness_field.total_consciousness()
        planet_being = next((b for b in beings if b.being_id == planet_being_id), None)

        # Optimize planet-wide
        print("Optimizing planet-wide systems...")
        target_c = population * 0.15
        reality.optimize_for_consciousness(target_c=target_c)
        reality.optimize_for_beauty(target_b=9.0)

        planet_consciousness = (
            planet_being.consciousness if planet_being else population * 0.01
        )
        metrics = {
            "planet_consciousness": planet_consciousness,
            "total_consciousness": total_consciousness,
            "beauty": reality.aesthetics_engine.average_beauty(),
            "heaven_score": np.sqrt(
                total_consciousness * reality.aesthetics_engine.average_beauty()
            ),
        }

        print("[OK] Heaven planet built successfully!")
        print(f"  Planet consciousness: {metrics['planet_consciousness']:.1f}")
        print(f"  Total consciousness: {metrics['total_consciousness']:.1f}")
        print(f"  Beauty: {metrics['beauty']:.2f}")

        return {
            "reality": reality,
            "planet_being": planet_being,
            "metrics": metrics,
            "planet_type": planet_type,
            "population": population,
        }

    def build_heaven_civilization(
        self, scale: str = "type1", values: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Build a heaven-optimized civilization.

        Args:
            scale: Kardashev scale ('type1', 'type2', 'type3')
            values: Core values of the civilization

        Returns:
            Dictionary with civilization details
        """
        # Map scale to population
        scale_map = {
            "type1": 1e10,  # Planetary
            "type2": 1e15,  # Stellar
            "type3": 1e20,  # Galactic
        }

        population = scale_map.get(scale, 1e10)

        # Create reality
        config = RealityConfig(
            dimensions=3,
            consciousness_support=True,
            beauty_optimization=True,
            ethical_constraints=True,
        )
        reality = Reality(config)
        reality.initialize()

        print(f"Building {scale} heaven civilization...")

        # Create civilization-level consciousness
        civ_being_id = reality.create_conscious_being(
            being_type="custom",
            initial_consciousness=population * 0.02,
            properties={
                "name": f"{scale}_civilization",
                "scale": scale,
                "values": values or ["consciousness", "beauty", "ethics"],
            },
        )

        # Get the actual being object
        beings: List[Any] = []
        total_consciousness: float = 0.0
        if reality.consciousness_field is not None:
            beings = reality.consciousness_field.get_beings()
            total_consciousness = reality.consciousness_field.total_consciousness()
        civ_being = next((b for b in beings if b.being_id == civ_being_id), None)

        # Optimize at civilization scale
        target_c = population * 0.2
        reality.optimize_for_consciousness(target_c=target_c)
        reality.optimize_for_beauty(target_b=9.5)

        civ_consciousness = civ_being.consciousness if civ_being else population * 0.02
        metrics = {
            "civilization_consciousness": civ_consciousness,
            "total_consciousness": total_consciousness,
            "beauty": reality.aesthetics_engine.average_beauty(),
            "heaven_score": np.sqrt(
                total_consciousness * reality.aesthetics_engine.average_beauty()
            ),
            "scale": scale,
        }

        print("[OK] Heaven civilization built successfully!")
        print(f"  Scale: {scale}")
        print(
            f"  Civilization consciousness: {metrics['civilization_consciousness']:.1f}"
        )
        print(f"  Heaven score: {metrics['heaven_score']:.2f}")

        return {
            "reality": reality,
            "civilization_being": civ_being,
            "metrics": metrics,
            "scale": scale,
            "values": values,
        }

    def _assign_role(self, index: int) -> str:
        """Assign a role to a citizen."""
        roles = [
            "artist",
            "scientist",
            "teacher",
            "healer",
            "explorer",
            "philosopher",
            "engineer",
            "gardener",
            "musician",
            "builder",
        ]
        return roles[index % len(roles)]

    def _calculate_heaven_metrics(
        self, reality: Reality, beings: List[Any]
    ) -> Dict[str, float]:
        """
        Calculate heaven metrics for a reality.

        Args:
            reality: Reality instance
            beings: List of beings

        Returns:
            Dictionary of metrics
        """
        if not reality.consciousness_field:
            return {
                "avg_consciousness": 0.0,
                "avg_beauty": 0.0,
                "happiness": 0.0,
                "heaven_score": 0.0,
            }

        total_c = reality.consciousness_field.total_consciousness()
        num_beings = len(beings)
        avg_c = total_c / num_beings if num_beings > 0 else 0.0

        avg_b = (
            reality.aesthetics_engine.average_beauty() if reality.beauty_field else 5.0
        )

        # Happiness = function of consciousness and beauty
        happiness = np.sqrt(avg_c * avg_b) / 10.0
        happiness = np.clip(happiness, 0.0, 1.0)

        # Heaven score = geometric mean of consciousness and beauty
        heaven_score = np.sqrt(total_c * avg_b)

        return {
            "avg_consciousness": avg_c,
            "avg_beauty": avg_b,
            "happiness": happiness,
            "heaven_score": heaven_score,
            "total_consciousness": total_c,
            "num_beings": num_beings,
        }
