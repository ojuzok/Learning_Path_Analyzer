"""Main module for Learning Path Analyzer."""

import argparse
import sys
from pathlib import Path
from src.utils import (
    load_lms_data,
    extract_student_features,
    calculate_correlations,
    plot_correlation_heatmap,
    plot_student_performance,
    generate_recommendations,
)


def analyze_learning_path(data_path: str, output_dir: str = "reports"):
    """
    Analyze learning path from LMS logs and generate recommendations.

    Args:
        data_path: Path to CSV file with LMS logs
        output_dir: Directory to save reports and visualizations
    """
    print("=" * 60)
    print("LEARNING PATH ANALYZER")
    print("=" * 60)
    print()

    # Load data
    print(f"Loading data from {data_path}...")
    df = load_lms_data(data_path)
    print(f"Loaded {len(df)} log entries for {df['student_id'].nunique()} students")
    print()

    # Extract features
    print("Extracting student features...")
    features_df = extract_student_features(df)
    print(f"Extracted features for {len(features_df)} students")
    print()

    # Calculate correlations
    print("Calculating correlations...")
    corr_df = calculate_correlations(features_df)
    print()

    # Generate visualizations
    print("Generating visualizations...")
    plot_correlation_heatmap(corr_df, f"{output_dir}/correlation_heatmap.png")
    plot_student_performance(features_df, f"{output_dir}/student_performance.png")
    print()

    # Generate recommendations
    print("Generating recommendations...")
    recommendations = generate_recommendations(corr_df, features_df)

    # Print recommendations
    for line in recommendations:
        print(line)

    # Save recommendations to file
    rec_path = Path(output_dir) / "recommendations.txt"
    rec_path.parent.mkdir(parents=True, exist_ok=True)
    with open(rec_path, "w", encoding="utf-8") as f:
        f.write("\n".join(recommendations))
    print(f"\nRecommendations saved to {rec_path}")
    print()

    # Display summary statistics
    print("Summary Statistics:")
    print("-" * 40)
    print(features_df.describe())
    print()

    print("=" * 60)
    print("Analysis complete!")
    print("=" * 60)


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Analyze student learning paths from LMS logs"
    )
    parser.add_argument(
        "--data",
        type=str,
        default="data/sample.csv",
        help="Path to CSV file with LMS logs (default: data/sample.csv)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="reports",
        help="Directory to save reports (default: reports)",
    )

    args = parser.parse_args()

    # Check if data file exists
    if not Path(args.data).exists():
        print(f"Error: Data file '{args.data}' not found!")
        sys.exit(1)

    # Run analysis
    analyze_learning_path(args.data, args.output)


if __name__ == "__main__":
    main()
