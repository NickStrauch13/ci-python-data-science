"""
Test the descriptive statistics script.
"""
from descriptive_stats import (
    get_descriptive_stats,
    get_species_stats,
    generate_plots,
    generate_markdown,
)


def test_stat_validity():
    """
    Test that the descriptive statistics are valid.
    """
    stats_dict = get_descriptive_stats()
    assert int(stats_dict["Weight"]["mean"]) == 398
    assert int(stats_dict["Length"]["mean"]) == 28
    assert int(stats_dict["Height"]["mean"]) == 8
    assert int(stats_dict["Weight"]["std"]) == 357
    assert int(stats_dict["Length"]["std"]) == 10


def test_species_stats():
    """
    Test that the species statistics are valid.
    """
    species_stats_dict = get_species_stats()
    assert int(species_stats_dict[("Weight", "count")]["Bream"]) == 35
    assert int(species_stats_dict[("Weight", "count")]["Roach"]) == 20


def test_plots():
    """
    Test that the plots are generated.
    """
    success = generate_plots()
    assert success == 1


def test_markdown():
    """
    Test that the markdown file is generated.
    """
    success = generate_markdown()
    assert success == 1
