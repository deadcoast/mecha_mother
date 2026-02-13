"""
Tests for Heaven Builder SDK.
"""

import numpy as np

from mecha_mother.heaven import HeavenBuilder, HeavenOptimizer
from mecha_mother.heaven.optimizer import CScanner


def test_heaven_optimizer():
    """Test heaven optimizer."""
    optimizer = HeavenOptimizer()

    # Test environment optimization
    location = "test_location"
    occupants = []
    result = optimizer.optimize_environment(location, occupants)

    assert "c_increase" in result
    assert "b_increase" in result
    assert "heaven_score" in result
    assert result["heaven_score"] >= 0


def test_heaven_optimizer_city():
    """Test city optimization."""
    optimizer = HeavenOptimizer()

    result = optimizer.optimize_city("test_city", population=100000)

    assert "city_id" in result
    assert "c_increase" in result
    assert "b_increase" in result
    assert "heaven_score" in result
    assert result["population"] == 100000


def test_heaven_optimizer_city_population_validation():
    """City optimization should reject non-positive populations."""
    optimizer = HeavenOptimizer()
    try:
        optimizer.optimize_city("bad_city", population=0)
        assert False, "Expected ValueError for zero population"
    except ValueError:
        pass


def test_cscanner_integrated_information_nontrivial_state():
    """Integrated information should be finite and positive for nontrivial states."""
    scanner = CScanner()
    state = (np.array([1.0, 0.5, 0.25, 0.1], dtype=float) + 0j).astype(complex)
    phi = scanner.compute_integrated_information(state)
    assert 0.0 <= phi <= 1.0
    assert phi > 0.0


def test_heaven_compute_h_handles_empty_preferences():
    """Heaven score computation should be stable with empty preference maps."""
    optimizer = HeavenOptimizer()
    params = np.array([1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5], dtype=float)
    h = optimizer._compute_h(10.0, 5.0, params, {})
    assert np.isfinite(h)
    assert h >= 0.0


def test_heaven_compute_h_pref_alignment_increases_score():
    """Better preference alignment should increase computed heaven score."""
    optimizer = HeavenOptimizer()
    c = 10.0
    b = 8.0
    prefs = {
        "lighting_warmth": 0.8,
        "sound_level": 0.2,
        "space_openness": 0.9,
        "nature_presence": 0.7,
        "social_density": 0.4,
    }
    well_aligned = np.array([1.0, 1.0, 0.8, 0.2, 0.9, 0.7, 0.4], dtype=float)
    misaligned = np.array([1.0, 1.0, 0.1, 0.9, 0.1, 0.1, 0.9], dtype=float)

    h_good = optimizer._compute_h(c, b, well_aligned, prefs)
    h_bad = optimizer._compute_h(c, b, misaligned, prefs)
    assert h_good > h_bad


def test_heaven_builder_city():
    """Test building a heaven city."""
    builder = HeavenBuilder()

    city = builder.build_heaven_city(location="test", population=1000, style="utopian")

    assert "reality" in city
    assert "beings" in city
    assert "metrics" in city
    assert "layout" in city

    metrics = city["metrics"]
    assert "avg_consciousness" in metrics
    assert "avg_beauty" in metrics
    assert "happiness" in metrics
    assert "heaven_score" in metrics

    assert metrics["heaven_score"] >= 0
    assert 0 <= metrics["happiness"] <= 1


def test_heaven_builder_city_population_scaling():
    """Large populations should use representative cohorts with scaled metrics."""
    builder = HeavenBuilder()
    city = builder.build_heaven_city(location="test", population=20000, style="utopian")

    assert city["population"] == 20000
    assert city["represented_population"] < city["population"]
    assert city["population_scale"] > 1.0

    metrics = city["metrics"]
    assert metrics["num_beings"] == 20000
    assert metrics["represented_population"] == city["represented_population"]
    assert metrics["population_scale"] == city["population_scale"]


def test_heaven_builder_planet():
    """Test building a heaven planet."""
    builder = HeavenBuilder()

    planet = builder.build_heaven_planet(planet_type="earthlike", population=10000)

    assert "reality" in planet
    assert "planet_being" in planet
    assert "metrics" in planet

    metrics = planet["metrics"]
    assert "planet_consciousness" in metrics
    assert "total_consciousness" in metrics
    assert "beauty" in metrics
    assert "heaven_score" in metrics


def test_heaven_builder_civilization():
    """Test building a heaven civilization."""
    builder = HeavenBuilder()

    civ = builder.build_heaven_civilization(
        scale="type1", values=["consciousness", "beauty"]
    )

    assert "reality" in civ
    assert "civilization_being" in civ
    assert "metrics" in civ
    assert "scale" in civ

    metrics = civ["metrics"]
    assert "civilization_consciousness" in metrics
    assert "total_consciousness" in metrics
    assert "heaven_score" in metrics
    assert metrics["scale"] == "type1"


def test_heaven_decade_protocol():
    """Test decade transformation and singularity protocol scaffolding."""
    builder = HeavenBuilder()
    result = builder.run_decade()
    assert result["years"] == 10
    assert "reports" in result
    assert len(result["reports"]) == 10
    assert result["technology_level"] > 1.0
