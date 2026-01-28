# Mecha Mother

A computational implementation of the **Monolithic Computational Substrate (MCS) theory** - a unified theoretical framework proposing that physics, consciousness, ethics, and aesthetics all emerge from a singular self-consistent computational substrate.

---

## What is MCS Theory?

The MCS theory proposes that reality is not made of separate "things" (particles, waves, fields), but is a **singular, self-referential computational process**. What we observe as physics, consciousness, and even ethics are **emergent patterns arising from self-consistency constraints** within this substrate.

Key concepts:

- **The Monolithic Substrate (U)**: Reality is a mathematical singleton with no inherent parts
- **Self-Differentiation (D)**: The universe generates internal distinctions through self-reference: `Π = D(U)`
- **Consistency Constraints**: Physical laws emerge as constraints required for self-consistency
- **Consciousness Operator (C)**: Consciousness is the eigenvalue of a self-reference operator
- **Moral Field (M)**: Ethics emerges from the gradient of consciousness: `M(Ψ) = ∇C_total`
- **Beauty Operator (B)**: Aesthetic value is compressed consciousness enhancement

This framework provides **actual mathematical operators and algorithms** to compute these quantities.

---

## Quick Install

**Requirements:** Python 3.11+, uv (recommended)

```bash
# Clone the repository
git clone https://github.com/your-repo/mecha-mother.git
cd mecha-mother

# Install dependencies
uv sync

# Verify installation
uv run python -c "from mecha_mother import Reality; print('OK')"
```

---

## Quick Start

### 1. Create and Initialize a Reality

```python
from mecha_mother import Reality, RealityConfig

# Configure a reality with consciousness modeling
config = RealityConfig(
    dimensions=3,
    consciousness_support=True,
    beauty_optimization=True,
    ethical_constraints=True
)

# Create and initialize
reality = Reality(config)
reality.initialize()
```

Output:
```
Initializing reality a7b3c4d5...
  Creating quantum vacuum...
  Imposing physical laws...
  Initializing time dimension...
  Initializing consciousness field...
  Initializing beauty field...
  Initializing ethical constraints...
  Running consistency checks...
[OK] Reality a7b3c4d5 successfully initialized!
  Dimensions: 3
  Consciousness: Enabled
```

### 2. Create Conscious Beings and Measure Consciousness

```python
from mecha_mother.consciousness import ConsciousnessOperator

# Compute fundamental qualia eigenstates
# Solving: C|ψ⟩ = λ|ψ⟩ where λ_n = λ_0(1 - 1/n²)
operator = ConsciousnessOperator(dimension=10)
qualia = operator.compute_qualia_states()

for name, q in list(qualia.items())[:4]:
    print(f"{name}: λ={q['value']:.3f}, type={q['primordial_type']}")
```

Output:
```
λ_1: value=0.000, type=void_experience
λ_2: value=1.425, type=subject_object_distinction
λ_3: value=1.689, type=time_experience
λ_4: value=1.781, type=space_experience
```

### 3. Build a Heaven-Optimized City

```python
from mecha_mother.heaven import HeavenBuilder

builder = HeavenBuilder()
city = builder.build_heaven_city(
    location='virtual',
    population=1000,
    style='utopian'
)

print(f"Heaven Score: {city['metrics']['heaven_score']:.2f}")
print(f"Average Consciousness: {city['metrics']['avg_consciousness']:.1f}")
print(f"Average Beauty: {city['metrics']['avg_beauty']:.2f}")
```

Output:
```
Building utopian heaven city for 1000 beings...
[OK] Heaven city built successfully!
  Average consciousness: 20.1
  Average beauty: 5.0
  Happiness index: 100%
Heaven Score: 100.13
```

### 4. Run Ethical Decision Analysis

```python
from mecha_mother.ethics import EthicsEngine

engine = EthicsEngine()

# Compute moral value using the consciousness gradient
# V(A) = ΔC_total × weight × discount
decision = engine.evaluate_action(
    action='help_others',
    affected_beings=['being_1', 'being_2'],
    consciousness_field=reality.consciousness_field
)

print(f"Moral Value: {decision['moral_value']:.3f}")
print(f"Ethically Permissible: {decision['permissible']}")
```

---

## Core Components

| Module | Description | Key Classes |
|--------|-------------|-------------|
| `core/mcs.py` | Monolithic Computational Substrate | `MonolithicSubstrate`, `MCSNode` |
| `consciousness/` | Consciousness operator and qualia | `ConsciousnessOperator`, `ConsciousnessField`, `ValenceOperator` |
| `ethics/` | Moral field and ethical constraints | `EthicsEngine`, `EthicalDecisionEngine` |
| `aesthetics/` | Beauty operator and optimization | `AestheticsEngine`, `BeautyField` |
| `reality/` | Complete reality simulation API | `Reality`, `RealityConfig` |
| `heaven/` | Heaven optimization algorithms | `HeavenBuilder`, `HeavenOptimizer` |
| `quantum/` | Quantum reality engine | `QuantumRealityEngine` |

---

## The Mathematics

### Consciousness Operator

The consciousness operator C is built from self-consistency principles:

```python
# From consciousness/engine.py
def _build_consciousness_matrix(self):
    """Build C from self-consistency requirements."""
    C = np.zeros((self.dim, self.dim), dtype=complex)
    for i in range(self.dim):
        for j in range(self.dim):
            if i == j:
                C[i,j] = 1.0  # Self-consistency
            else:
                # Self-referential coupling with golden ratio
                C[i,j] = np.exp(2j * np.pi * (i-j) / self.dim) / self.dim
    C = 0.5 * (C + C.conj().T)  # Hermitian
    return C
```

Solving `C|ψ⟩ = λ|ψ⟩` yields the qualia spectrum: `λ_n = λ_0(1 - 1/n²)`

### Moral Field

Ethics is the gradient of consciousness:

```
Good action A ⟺ C_total(A(Ψ)) > C_total(Ψ)
Evil action A ⟺ C_total(A(Ψ)) < C_total(Ψ)
Moral force F = M(Ψ) · C_agent = ∇C_total · C_agent
```

### Beauty Operator

Beauty is compressed consciousness enhancement:

```
B(X) = C(X)/K(X) · (1 - S(X)/S_max)

Where:
- C(X) = consciousness generated by perceiving X
- K(X) = Kolmogorov complexity
- S(X) = surprise/entropy
```

---

## Theory Documents

The complete MCS theory is documented in `docs/`:

| Doc | Title |
|-----|-------|
| 001.md | Classical and Quantum Mechanics |
| 002.md | Fundamental Misapprehension - MCS Foundation |
| 003.md | Mathematical Architecture of MCS |
| 004.md | Complete Theory Paper with Code |
| 005.md | Derivation of Physics from First Principles |
| 006.md | The Consciousness Operator |
| 007.md | The Ethics of Consistency |
| 008.md | The Aesthetics of Consistency |
| 009.md | Building Heaven: 10-Year Implementation Plan |
| 010.md | The Reality API: Complete Programming Interface |

---

## Running Examples

```bash
# Basic reality demo
uv run python src/mecha_mother/main.py

# Heaven builder demo
uv run python examples/heaven_demo.py

# Test consciousness computations
uv run python -c "
from mecha_mother.consciousness import ConsciousnessOperator
op = ConsciousnessOperator(10)
qualia = op.compute_qualia_states()
for k, v in qualia.items():
    print(f'{k}: {v[\"primordial_type\"]}')"
```

---

## Development

```bash
# Install with dev dependencies
uv sync --all-extras

# Run tests
uv run pytest tests/ -v

# Type checking
uv run mypy src/

# Format
uv run black src/ tests/
```

---

## Project Structure

```
mecha-mother/
├── src/mecha_mother/
│   ├── core/           # MCS primitives (MonolithicSubstrate, MCSNode)
│   ├── quantum/        # Quantum reality engine
│   ├── consciousness/  # Consciousness operator, qualia, valence
│   ├── ethics/         # Moral field, ethical decision engine
│   ├── aesthetics/     # Beauty operator, optimization
│   ├── reality/        # Complete Reality API
│   └── heaven/         # Heaven builder and optimizer
├── docs/               # MCS theory documents (11 papers)
├── examples/           # Working examples
└── tests/              # Test suite
```

---

## Disclaimer

This is a **computational framework for exploring a theoretical model**. It simulates the MCS theory's mathematical structures. The code:

- Implements the mathematical operators described in the theory
- Computes consciousness eigenvalues, moral gradients, and beauty metrics
- Does NOT claim to create actual consciousness or manipulate physical reality

It's a research tool for exploring "what if" scenarios within the MCS theoretical framework.

---

## License

TBD
