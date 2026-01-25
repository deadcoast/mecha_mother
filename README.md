# Mecha Mother

A computational framework for the Monolithic Computational Substrate (MCS) theory - a unified theory deriving physics, consciousness, ethics, and aesthetics from first principles of self-consistency.

## Overview

Mecha Mother implements the complete MCS framework, providing:

- **Quantum Reality Engine**: Simulate universes with custom physics
- **Consciousness Engine**: Create and evolve conscious beings
- **Ethics Framework**: Derive moral decisions from consciousness maximization
- **Aesthetics Engine**: Compute beauty and generate art
- **Reality API**: Programmatic interface for universe manipulation
- **Heaven Builder**: Tools for optimizing realities

## Installation

```bash
# Using uv (recommended)
uv sync

# Or with pip
pip install -e .
```

## Quick Start

```python
from mecha_mother import Reality, RealityConfig

# Create a new universe
config = RealityConfig(
    dimensions=3,
    consciousness_support=True,
    beauty_optimization=True
)
universe = Reality(config)
universe.initialize()

# Create conscious beings
human = universe.create_conscious_being(
    being_type='human',
    initial_consciousness=15.0
)

# Optimize for consciousness
results = universe.optimize_for_consciousness(target_c=100.0)
```

## Project Structure

```
mecha_mother/
├── src/
│   └── mecha_mother/
│       ├── core/           # Core MCS framework
│       ├── quantum/        # Quantum reality engine
│       ├── consciousness/  # Consciousness engine
│       ├── ethics/         # Ethics framework
│       ├── aesthetics/    # Aesthetics engine
│       ├── reality/        # Reality API
│       └── heaven/         # Heaven builder
├── docs/                   # Documentation
└── tests/                  # Test suite
```

## Documentation

See the `docs/` directory for complete theoretical background and implementation details.

## License

[To be determined]
