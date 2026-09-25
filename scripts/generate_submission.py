"""Script to generate final submission artifacts for Amazon ML Challenge 2026."""

import argparse


def main() -> None:
    """Run full pipeline inference on test data and export final submission files."""
    parser = argparse.ArgumentParser(description="Generate final submission files.")
    parser.add_argument("--config", type=str, default="configs/config.yaml", help="Path to config file.")
    args = parser.parse_args()

    print(f"Generating submission output using config: {args.config}")
    # TODO: Load test data, generate candidates, compute features, predict matches, format matching_results.tsv and candidate_pairs.tsv.
    print("Submission generation completed (Placeholder).")


if __name__ == "__main__":
    main()
