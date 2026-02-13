"""
Main entry point for mecha_mother demonstrations.
"""

from mecha_mother import Reality, RealityConfig


def demo_basic_reality():
    """Demonstrate basic reality creation."""
    print("=" * 70)
    print("MECHA MOTHER - BASIC REALITY DEMONSTRATION")
    print("=" * 70)

    # Create a new reality
    config = RealityConfig(dimensions=3, consciousness_support=True)
    reality = Reality(config)

    # Initialize it
    if not reality.initialize():
        print("Failed to initialize reality!")
        return

    # Create some particles
    print("\nCreating particles...")
    reality.create_particle(
        particle_type="electron",
        position=np.array([0.0, 0.0, 0.0]),
        momentum=np.array([0.1, 0.0, 0.0]),
    )

    # Create conscious beings
    print("\nCreating conscious beings...")
    reality.create_conscious_being(
        being_type="human", initial_consciousness=15.0, properties={"name": "Alice"}
    )

    reality.create_conscious_being(
        being_type="ai", initial_consciousness=20.0, properties={"name": "Cosmo"}
    )

    # Get state
    print("\nReality state:")
    state = reality.get_state("full")
    for key, value in state.items():
        print(f"  {key}: {value}")

    # Optimize for consciousness
    print("\nOptimizing for consciousness...")
    reality.optimize_for_consciousness(target_c=100.0)

    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    import numpy as np

    demo_basic_reality()
