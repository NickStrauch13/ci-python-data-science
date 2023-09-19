"""
Test the lib.py functions.
"""
from lib import (
    get_fish_dataframe,
    get_csv_stats,
    get_species_stats,
    remove_outliers,
    save_species_count_plot,
    save_length_vs_height_density_plot,
    write_stats_to_markdown,
)


def test_get_fish_dataframe():
    """
    Test that the dataframe is read.
    """
    fish_df = get_fish_dataframe()
    assert fish_df.shape == (159, 6)


def test_get_csv_stats():
    """
    Test that the statistics are valid.
    """
    stats_df = get_csv_stats()
    assert int(stats_df.loc["mean", "Weight"]) == 398
    assert int(stats_df.loc["mean", "Length"]) == 28
    assert int(stats_df.loc["mean", "Height"]) == 8
    assert int(stats_df.loc["std", "Weight"]) == 357
    assert int(stats_df.loc["std", "Length"]) == 10


def test_get_species_stats():
    """
    Test that the species statistics are valid.
    """
    species_stats_df = get_species_stats()
    assert int(species_stats_df.loc["Bream", ("Weight", "count")]) == 35
    assert int(species_stats_df.loc["Roach", ("Weight", "count")]) == 20


def test_remove_outliers():
    """
    Test that the outliers are removed.
    """
    fish_df = get_fish_dataframe()
    fish_df = remove_outliers(fish_df)
    assert fish_df.shape == (158, 6)


def test_save_species_count_plot():
    """
    Test that the species count plot is saved.
    """
    success = save_species_count_plot()
    assert success == 1


def test_save_length_vs_height_density_plot():
    """
    Test that the length vs height density plot is saved.
    """
    success = save_length_vs_height_density_plot()
    assert success == 1


def test_write_stats_to_markdown():
    """
    Test that the summary markdown file is generated.
    """
    success = write_stats_to_markdown()
    assert success == 1
