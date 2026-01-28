# Mecha Mother

**Monolithic Computational Substrate Framework**

A computational simulation framework for exploring the Monolithic Computational Substrate (MCS) theory — a unified theoretical framework that derives physics, consciousness, ethics, and aesthetics from first principles of self-consistency.

---

## Notice

This is a **simulation and modeling framework**, not an implementation of actual reality manipulation. The MCS theory describes a philosophical and metaphysical framework for understanding reality. This codebase provides computational tools to explore, simulate, and experiment with the theory's mathematical structures and concepts.

---

## Quick Install

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/deadcoast/mecha_mother.git
cd mecha-mother
```

### Step 2: Install Dependencies

**Using uv (recommended):**

```bash
uv sync
```

**Using pip:**

```bash
pip install -e .
```

### Step 3: Verify Installation

```bash
python -c "from mecha_mother import Reality; print('Installation successful')"
```

### Development Installation

To install with development dependencies (testing, linting, type checking):

```bash
# Using uv
uv sync --all-extras

# Using pip
pip install -e ".[dev]"
```

---

## Usage

### Basic Reality Simulation

```python
import numpy as np
from mecha_mother import Reality, RealityConfig

# Create a simulated universe
config = RealityConfig(
    dimensions=3,
    consciousness_support=True
)
reality = Reality(config)
reality.initialize()

# Create particles
electron_id = reality.create_particle(
    particle_type='electron',
    position=np.array([0.0, 0.0, 0.0]),
    momentum=np.array([0.1, 0.0, 0.0])
)

# Create simulated conscious beings
human_id = reality.create_conscious_being(
    being_type='human',
    initial_consciousness=15.0,
    properties={'name': 'Alice'}
)

# Optimize for consciousness
results = reality.optimize_for_consciousness(target_c=100.0)
```

### Heaven Builder

```python
from mecha_mother.heaven import HeavenBuilder

builder = HeavenBuilder()

# Build a heaven city
city = builder.build_heaven_city(
    location='virtual',
    population=10000,
    style='utopian'
)

print(f"Heaven Score: {city['metrics']['heaven_score']:.2f}")
print(f"Average Consciousness: {city['metrics']['avg_consciousness']:.1f}")
```

### Running Examples

```bash
# Basic reality demonstration
python src/main.py

# Heaven builder demonstration
python examples/heaven_demo.py
```

---

## Project Structure

```
mecha-mother/
├── src/
│   └── mecha_mother/
│       ├── core/           # Core MCS framework and constraints
│       ├── quantum/        # Quantum reality engine
│       ├── consciousness/  # Consciousness operators and fields
│       ├── ethics/         # Ethics framework and decision engine
│       ├── aesthetics/     # Aesthetics engine and beauty operators
│       ├── reality/        # Reality API and state management
│       └── heaven/         # Heaven builder and optimizer
├── docs/                   # Theoretical documentation
├── examples/               # Example scripts
└── tests/                  # Test suite
```

---

## Core Components

| Component | Description |
|-----------|-------------|
| `Reality` | Main interface for creating and managing simulated realities |
| `RealityConfig` | Configuration for reality parameters |
| `EthicsEngine` | Computes ethical values using MCS formulas |
| `AestheticsEngine` | Calculates beauty metrics |
| `HeavenBuilder` | Tools for optimizing simulated realities |
| `HeavenOptimizer` | Optimization algorithms for consciousness and beauty |

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | >= 1.24.0 | Numerical computations |
| scipy | >= 1.10.0 | Scientific computing |
| matplotlib | >= 3.7.0 | Visualization |
| networkx | >= 3.0 | Graph structures |

---

## Testing

Run the test suite:

```bash
# Using pytest directly
pytest tests/ -v

# With coverage
pytest tests/ -v --cov=src/mecha_mother
```

---

## Documentation

Theoretical documentation is available in the `docs/` directory:

- `docs/001.md` through `docs/010.md` — Core theory documents
- `docs/R01.md` — Reference materials
- `docs/development/` — Development notes

---

## Requirements

- Python >= 3.11
- Operating System: Windows, macOS, or Linux

---

## License

To be determined.

---

## Disclaimer

This software simulates theoretical concepts from the MCS framework. It does not actually manipulate reality, create consciousness, or perform any metaphysical operations. All "beings," "realities," and "consciousness" referenced in the code are computational models and simulations for exploring theoretical concepts.
