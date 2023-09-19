"""
Common functions between the script and notebook.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame


def get_fish_dataframe() -> DataFrame:
    """
    Read a CSV file from a URL and return its DataFrame.
    """
    return pd.read_csv("https://github.com/rickiepark/hg-mldl/raw/master/fish.csv")


def get_csv_stats() -> DataFrame:
    """
    Read a CSV file from a URL and return its statistics.
    """
    fish_df = get_fish_dataframe()
    stats = fish_df.describe()
    return stats


def get_species_stats() -> DataFrame:
    """
    Read a CSV file from a URL and return its statistics.
    """
    fish_df = get_fish_dataframe()
    species_stats = fish_df.groupby("Species").describe()
    return species_stats


def remove_outliers(fish_df: DataFrame) -> DataFrame:
    """
    Read a CSV file from a URL and remove outliers.
    """
    fish_df = fish_df[fish_df["Weight"] < 2000]
    fish_df = fish_df[fish_df["Weight"] > 0.001]
    return fish_df


def save_species_count_plot() -> int:
    """Save a bar plot of the species counts."""
    plt.clf()
    fish_df = get_fish_dataframe()
    species_counts = fish_df["Species"].value_counts()
    custom_palette = sns.color_palette("Set3", len(species_counts))
    _, ax = plt.subplots(figsize=(8, 6))
    species_counts.plot(kind="bar", ax=ax, color=custom_palette)
    ax.set_title("Distribution of Species")
    ax.set_xlabel("Species")
    ax.set_ylabel("Count")
    ax.set_xticklabels(species_counts.index, rotation=45, ha="right")
    for i, v in enumerate(species_counts):
        ax.text(
            i, v + 5, str(v), ha="center", va="bottom", fontsize=12, fontweight="bold"
        )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    dest = os.path.join(
        os.path.dirname(__file__), "..", "img", "species_distribution.png"
    )
    plt.savefig(dest)
    return 1


def save_length_vs_height_density_plot() -> int:
    """Plot the relationship between length and height, colored by density."""
    plt.clf()
    fish_df = get_fish_dataframe()
    fish_df = remove_outliers(fish_df)
    fish_df["Density"] = fish_df["Weight"] / (
        fish_df["Length"] * fish_df["Height"] * fish_df["Width"]
    )
    norm = plt.Normalize(fish_df["Density"].min(), fish_df["Density"].max())
    colors = plt.cm.viridis(norm(fish_df["Density"]))
    plt.scatter(fish_df["Length"], fish_df["Height"], c=colors)
    plt.colorbar(label="Density")
    plt.xlabel("Length")
    plt.ylabel("Height")
    plt.title("Length vs Height (Color by Density)")
    dest = os.path.join(
        os.path.dirname(__file__), "..", "img", "density_relationship.png"
    )
    plt.savefig(dest)
    return 1


def write_stats_to_markdown() -> int:
    """Write the statistics to a Markdown file."""
    stats = get_csv_stats()
    # Save the summary stats to a markdown file
    dest = os.path.join(os.path.dirname(__file__), "..", "output", "summary_stats.md")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(stats.to_markdown())
    return 1
