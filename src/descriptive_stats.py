"""
A script utilizing the descriptive statistics functions in the lib.py module.
"""
import lib


def get_descriptive_stats() -> dict:
    """Return the descriptive statistics for the fish dataset."""
    stats_df = lib.get_csv_stats()
    stats_dict = stats_df.to_dict()
    return stats_dict


def get_species_stats() -> dict:
    """Return the descriptive statistics for the fish dataset by species."""
    species_stats_df = lib.get_species_stats()
    species_stats_dict = species_stats_df.to_dict()
    return species_stats_dict


def generate_plots() -> int:
    """Generate a plot of the species counts and of length vs height density."""
    lib.save_species_count_plot()
    lib.save_length_vs_height_density_plot()
    return 1


def generate_markdown() -> int:
    """Generate a markdown file with the descriptive statistics."""
    lib.write_stats_to_markdown()
    return 1


if __name__ == "__main__":
    print("Descriptive Statistics")
    stats = get_descriptive_stats()  # pragma: no cover
    print("   Feature Averages")
    for key in stats:
        print(f"     {key}: {round(stats[key]['mean'], 2)}")

    print("Species Statistics")
    species_stats = get_species_stats()  # pragma: no cover
    print("   Species Counts")
    count_data = species_stats[("Weight", "count")]
    for key in count_data:
        print(f"     {key}: {int(count_data[key])}")

    generate_plots()  # pragma: no cover
    generate_markdown()  # pragma: no cover
