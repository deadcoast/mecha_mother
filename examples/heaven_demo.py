"""
Demonstration of Heaven Builder capabilities.
"""

import numpy as np
from mecha_mother.heaven import HeavenBuilder


def demo_heaven_city():
    """Demonstrate building a heaven city."""
    print("=" * 70)
    print("HEAVEN BUILDER - CITY DEMONSTRATION")
    print("=" * 70)

    builder = HeavenBuilder()

    # Build a small heaven city
    city = builder.build_heaven_city(
        location="virtual", population=10000, style="utopian"
    )

    print("\nCity Summary:")
    print(f"  Population: {city['population']:,}")
    print(f"  Style: {city['style']}")
    print(f"  Heaven Score: {city['metrics']['heaven_score']:.2f}")
    print(f"  Average Consciousness: {city['metrics']['avg_consciousness']:.1f}")
    print(f"  Average Beauty: {city['metrics']['avg_beauty']:.2f}")
    print(f"  Happiness Index: {city['metrics']['happiness']:.2%}")

    print("\n" + "=" * 70)


def demo_heaven_planet():
    """Demonstrate building a heaven planet."""
    print("=" * 70)
    print("HEAVEN BUILDER - PLANET DEMONSTRATION")
    print("=" * 70)

    builder = HeavenBuilder()

    # Build a heaven planet
    planet = builder.build_heaven_planet(planet_type="earthlike", population=1000000)

    print("\nPlanet Summary:")
    print(f"  Type: {planet['planet_type']}")
    print(f"  Population: {planet['population']:,}")
    print(f"  Planet Consciousness: {planet['metrics']['planet_consciousness']:.1f}")
    print(f"  Total Consciousness: {planet['metrics']['total_consciousness']:.1f}")
    print(f"  Beauty: {planet['metrics']['beauty']:.2f}")
    print(f"  Heaven Score: {planet['metrics']['heaven_score']:.2f}")

    print("\n" + "=" * 70)


def demo_heaven_civilization():
    """Demonstrate building a heaven civilization."""
    print("=" * 70)
    print("HEAVEN BUILDER - CIVILIZATION DEMONSTRATION")
    print("=" * 70)

    builder = HeavenBuilder()

    # Build a Type 1 civilization
    civilization = builder.build_heaven_civilization(
        scale="type1", values=["consciousness", "beauty", "ethics", "exploration"]
    )

    print("\nCivilization Summary:")
    print(f"  Scale: {civilization['scale']}")
    print(f"  Values: {', '.join(civilization['values'])}")
    print(
        f"  Civilization Consciousness: {civilization['metrics']['civilization_consciousness']:.1f}"
    )
    print(
        f"  Total Consciousness: {civilization['metrics']['total_consciousness']:.1f}"
    )
    print(f"  Beauty: {civilization['metrics']['beauty']:.2f}")
    print(f"  Heaven Score: {civilization['metrics']['heaven_score']:.2f}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    demo_heaven_city()
    print("\n")
    demo_heaven_planet()
    print("\n")
    demo_heaven_civilization()
