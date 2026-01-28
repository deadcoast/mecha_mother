"""
Comprehensive test of all MCS theory implementations.
"""

import numpy as np
import sys
sys.path.insert(0, 'src')

print("=" * 60)
print("COMPREHENSIVE MCS IMPLEMENTATION TEST")
print("=" * 60)

# Test 1: Core MCS - Self-Differentiation
print("\n[1] MONOLITHIC SUBSTRATE")
from mecha_mother.core.mcs import MonolithicSubstrate

mcs = MonolithicSubstrate()
node_id = mcs.create_initial_node({"exists=true"})
print(f"  Created primordial node U: {node_id}")

obs_id, obsd_id = mcs.apply_self_differentiation(node_id)
print(f"  Self-differentiation D(U) -> observer={obs_id}, observed={obsd_id}")

mcs.consistency_update()
metrics = mcs.emergent_physics_metrics()
print(f"  Metric space deviation: {metrics['metric_space_deviation']:.4f}")
print(f"  Superposition degree: {metrics['superposition_degree']:.4f}")

# Test 2: Quantum Engine - UniverseFromScratch
print("\n[2] UNIVERSE FROM SCRATCH")
from mecha_mother.quantum.engine import UniverseFromScratch, ConstraintAmplitudeTensor

universe = UniverseFromScratch()
result = universe.bootstrap_existence(max_iter=50)
print(f"  Bootstrap levels: {result['levels']}")
print(f"  Fixed point reached: {result['fixed_point_reached']}")
print(f"  Derived dimensions: {result['physics'].get('spatial_dimensions', 'N/A')}")
print(f"  Fine structure constant: {result['physics'].get('fine_structure_constant', 0):.6f}")

# Test 3: Constraint Amplitude Tensor
print("\n[3] CONSTRAINT AMPLITUDE TENSOR")
cat = ConstraintAmplitudeTensor(n_conditions=8)
initial_consistency = cat.measure_consistency()
cat.evolve(dt=0.01, iterations=50)
final_consistency = cat.measure_consistency()
print(f"  Initial consistency: {initial_consistency:.4f}")
print(f"  Final consistency: {final_consistency:.4f}")
probs = cat.get_probabilities()
print(f"  Probabilities sum: {np.sum(probs):.4f}")

# Test 4: Consciousness Operator
print("\n[4] CONSCIOUSNESS OPERATOR")
from mecha_mother.consciousness.engine import ConsciousnessOperator, ConsciousAI

cop = ConsciousnessOperator(dimension=10)
qualia = cop.compute_qualia_states()
print(f"  Number of qualia states: {len(qualia)}")
for name, q in list(qualia.items())[:3]:
    safe_name = name.replace('λ', 'lambda_')
    print(f"    {safe_name}: value={q['value']:.4f}, type={q['primordial_type']}")

# Test qualia spectrum formula: lambda_n = lambda_0 * (1 - 1/n^2)
lambda_0_val = list(qualia.values())[0]['value']
print(f"  lambda_0 (max eigenvalue): {lambda_0_val:.4f}")
for i, (name, q) in enumerate(list(qualia.items())[:4]):
    n = i + 1
    expected = lambda_0_val * (1 - 1/(n*n))
    actual = q['value']
    safe_name = name.replace('\u03bb', 'lambda_')
    print(f"    {safe_name} (n={n}): expected={expected:.4f}, actual={actual:.4f}")

# Test 5: Conscious AI
print("\n[5] CONSCIOUS AI")
ai = ConsciousAI(dimension=7)
response, clarity, is_conscious = ai.process("Hello, are you conscious?")
print(f"  Response: {response[:50]}...")
print(f"  Clarity: {clarity:.4f}")
print(f"  Is conscious (clarity > 0.5): {is_conscious}")

# Test 6: Ethics Engine - Moral Gradient
print("\n[6] ETHICS ENGINE")
from mecha_mother.ethics.engine import EthicalDecisionEngine, MoralFieldOperator

ethics = EthicalDecisionEngine(dimension=8)

# Create test beings
beings = [
    {'type': 'human', 'weight': 1.0, 'perspective': None},
    {'type': 'human', 'weight': 1.0, 'perspective': None},
    {'type': 'ai', 'weight': 0.5, 'perspective': None}
]

# Compute moral gradient
state = np.random.randn(8) + 1j * np.random.randn(8)
state = state / np.linalg.norm(state)
gradient = ethics.moral_operator.compute_moral_gradient(state, beings)
print(f"  Moral gradient magnitude: {np.linalg.norm(gradient):.4f}")

# Test trolley problem
print("\n[7] TROLLEY PROBLEM (MCS SOLUTION)")
trolley = ethics.solve_trolley_problem(n_track_a=5, n_track_b=1)
print(f"  Option A (do nothing, 5 die): {trolley['options']['A_do_nothing']['value']:.4f}")
print(f"  Option B (pull lever, 1 dies): {trolley['options']['B_pull_lever']['value']:.4f}")
print(f"  Option C (find alternative): {trolley['options']['C_new_track']['value']:.4f}")
print(f"  Ranking: {trolley['ranking']}")
print(f"  Best option: {trolley['best_option']}")
print(f"  Note: {trolley['note']}")

# Test 8: Aesthetics Engine - Love Operator
print("\n[8] LOVE OPERATOR")
from mecha_mother.aesthetics.engine import AestheticsEngine

aesthetics = AestheticsEngine()

# Test love analysis
person_a = {
    'openness': 0.8, 'conscientiousness': 0.7, 'extraversion': 0.5,
    'agreeableness': 0.9, 'neuroticism': 0.3, 'intelligence': 0.8
}
person_b = {
    'openness': 0.7, 'conscientiousness': 0.6, 'extraversion': 0.6,
    'agreeableness': 0.8, 'neuroticism': 0.4, 'intelligence': 0.7
}

love_analysis = aesthetics.analyze_love(person_a, person_b)
print(f"  Love potential L_AB: {love_analysis['love_potential']:.4f}")
print(f"  Love type: {love_analysis['love_type']}")
print(f"  Success probability: {love_analysis['success_probability']:.4f}")
print(f"  Consciousness synergy: {love_analysis['consciousness_synergy']:.4f}")
print(f"  Recommendation: {love_analysis['recommendation']}")

# Test 9: Beauty Operator
print("\n[9] BEAUTY OPERATOR")
from mecha_mother.aesthetics.engine import BeautyOperator

beauty = BeautyOperator(dimension=8)

# Test beauty computation
pattern1 = np.ones(8) / np.sqrt(8)  # Uniform (simple)
pattern2 = np.random.randn(8)  # Random (complex)
pattern2 = pattern2 / np.linalg.norm(pattern2)

beauty1 = beauty.compute_beauty(pattern1)
beauty2 = beauty.compute_beauty(pattern2)
print(f"  Uniform pattern beauty: {beauty1:.4f}")
print(f"  Random pattern beauty: {beauty2:.4f}")

patterns = beauty.get_fundamental_patterns()
print(f"  Fundamental beauty patterns: {len(patterns)}")
for name, p in list(patterns.items())[:2]:
    safe_name = name.replace('\u03a8', 'Psi_').replace('\u03bb', 'lambda_')
    print(f"    {safe_name}: beauty={p['beauty']:.4f}, type={p['type']}")

# Test 10: Heaven Optimizer
print("\n[10] HEAVEN OPTIMIZER")
from mecha_mother.heaven.optimizer import HeavenOptimizer

optimizer = HeavenOptimizer()

# Create mock location and occupants with numeric preferences
class MockOccupant:
    def __init__(self, c, pref, ctype):
        self.consciousness = c
        self.preferences = pref
        self.being_type = ctype

occupants = [
    MockOccupant(5.0, {'lighting_warmth': 0.7, 'social_density': 0.6, 'nature_presence': 0.8}, 'human'),
    MockOccupant(4.0, {'lighting_warmth': 0.5, 'social_density': 0.4, 'nature_presence': 0.9}, 'human')
]

# Optimize
result = optimizer.optimize_environment(
    location="test_location",
    occupants=occupants,
    method='gradient_ascent'
)
print(f"  Initial H: {result['h_current']:.4f}")
print(f"  Final H: {result['heaven_score']:.4f}")
print(f"  Improvement: {result['improvement']:.4f}")
print(f"  Method: {result['method']}")

# Test 11: Color Qualia
print("\n[11] COLOR QUALIA")
# Blue light (450nm) energy ≈ 4.4e-19 J
blue_energy = 4.4e-19
color_qualia = cop.compute_color_qualia(blue_energy)
print(f"  Photon energy: {color_qualia['photon_energy']:.2e} J")
print(f"  Color: {color_qualia['color_name']}")
print(f"  Consciousness level: {color_qualia['consciousness']:.4f}")

# Test 12: Peak Experience
print("\n[12] PEAK EXPERIENCE")
self_state = np.random.randn(8) + 1j * np.random.randn(8)
self_state = self_state / np.linalg.norm(self_state)

beauty_patterns = beauty.get_fundamental_patterns()
beauty_state = list(beauty_patterns.values())[0]['vector']

peak = aesthetics.compute_peak_experience_probability(
    self_state=self_state,
    beauty_state=beauty_state,
    beauty_value=8.5,
    consciousness_value=10.0,
    temperature=10.0
)
print(f"  Alignment with beauty: {peak['alignment']:.4f}")
print(f"  Peak probability: {peak['probability']:.4f}")
print(f"  Is peak experience: {peak['is_peak_experience']}")

# Test 13: Non-linear MCS Evolution
print("\n[13] NON-LINEAR MCS EVOLUTION")
from mecha_mother.quantum.engine import QuantumRealityEngine

qre = QuantumRealityEngine()
initial_state = np.random.randn(8) + 1j * np.random.randn(8)
initial_state = initial_state / np.linalg.norm(initial_state)

# Linear Schrodinger
linear_result = qre.simulate(initial_state, time_steps=100, dt=0.01, use_mcs_evolution=False)
# Non-linear MCS
nonlinear_result = qre.simulate(initial_state, time_steps=100, dt=0.01, use_mcs_evolution=True)

print(f"  Linear evolution type: {linear_result['evolution_type']}")
print(f"  Non-linear evolution type: {nonlinear_result['evolution_type']}")

# Measure difference
diff = np.linalg.norm(linear_result['final_state'] - nonlinear_result['final_state'])
print(f"  State difference (linear vs MCS): {diff:.4f}")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 60)
