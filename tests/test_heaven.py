"""
Tests for Heaven Builder SDK.
"""

from mecha_mother.heaven import HeavenBuilder, HeavenOptimizer


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
