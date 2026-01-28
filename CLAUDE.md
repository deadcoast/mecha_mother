# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Mecha Mother is a computational simulation framework for the Monolithic Computational Substrate (MCS) theory. It provides tools to simulate quantum mechanics, consciousness, ethics, and aesthetics based on mathematical models derived from first principles.

**Important**: This is a simulation framework, not actual reality manipulation.

## Commands

### Setup
```bash
uv sync                    # Install dependencies (recommended)
pip install -e .           # Alternative: pip install
```

### Testing
```bash
pytest                     # Run all tests
pytest tests/test_basic.py # Run a single test file
pytest -k "test_name"      # Run tests matching pattern
pytest --cov               # Run with coverage
```

### Code Quality
```bash
ruff check src/            # Linting
black src/ tests/          # Formatting
mypy src/                  # Type checking
```

### Running
```bash
python -m mecha_mother.main           # Run demo
python examples/heaven_demo.py        # Run heaven builder demo
```

## Architecture

### Core Layer (`src/mecha_mother/core/`)
- `mcs.py`: `MonolithicSubstrate` - the foundational substrate implementing self-differentiation and consistency constraints. `MCSNode` represents discrete points in the substrate.
- `constraints.py`: `ConstraintResolver` - verifies and repairs consistency across MCS, quantum, and physical constant changes.

### Simulation Engines
Each engine operates on a specific domain:

- **quantum/**: `QuantumRealityEngine` manages particles, physical constants, vacuum states, and spacetime. `PhysicalConstants` dataclass holds fundamental constants.
- **consciousness/**: `ConsciousnessEngine` creates consciousness fields and beings. `ConsciousnessOperator` computes qualia states. `ValenceOperator` handles pain/pleasure computation. `ConsciousBeing` represents entities with consciousness levels.
- **ethics/**: `EthicsEngine` computes moral values and constraints. `MoralFieldOperator` calculates moral gradients and forces.
- **aesthetics/**: `AestheticsEngine` manages beauty fields and generates art. `BeautyOperator` computes beauty metrics. Also contains love dynamics computation.

### High-Level API (`src/mecha_mother/reality/`)
- `reality.py`: `Reality` class - main entry point. Orchestrates all engines together. Handles initialization, particle/being creation, optimization, merging realities, and import/export.
- `RealityConfig` dataclass configures dimensions, consciousness support, and beauty optimization.
- `SafetyProtocols` and `ParadoxPreventer` handle safety constraints.

### Heaven Builder (`src/mecha_mother/heaven/`)
- `builder.py`: `HeavenBuilder` constructs optimized cities, planets, and civilizations.
- `optimizer.py`: `HeavenOptimizer` optimizes environments for consciousness/beauty metrics.

### Data Flow
```
Reality (orchestrator)
  ├── MonolithicSubstrate (foundation)
  ├── QuantumRealityEngine (physics)
  ├── ConsciousnessEngine → ConsciousnessField → ConsciousBeing
  ├── EthicsEngine → MoralFieldOperator
  └── AestheticsEngine → BeautyOperator
```

## Key Patterns

- Engines are initialized by `Reality` and stored as instance attributes (`reality.quantum_engine`, `reality.consciousness_engine`, etc.)
- Dataclasses are used extensively for configuration and state objects
- NumPy arrays represent positions, momenta, and field states
- Optimization methods accept target values and return result dictionaries

## Dependencies
- numpy, scipy: numerical computation
- matplotlib: visualization
- networkx: graph structures for substrate nodes
