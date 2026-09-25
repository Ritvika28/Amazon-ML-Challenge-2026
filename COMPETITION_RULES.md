# Competition Rules & Constraints

## Overview

- **Problem Type:** Business Entity Resolution
- **Source Sets:**
  - **Source 1:** Reference / source entity set.
  - **Source 2 & Source 3:** Contain potential corresponding entity records.
- **Mapping Cardinality:** Each Source 1 entity can map to zero (singleton), one, or multiple corresponding records across Source 2 and Source 3.

## Evaluation & Metrics

- **Primary Metric:** Macro F0.5
- **Weighting:** Precision receives more weight than recall ($\beta = 0.5$).
- **Impact:** False merges (false positives) are particularly costly to the score.

## Candidate Generation & Blocking

- Blocking determines the maximum achievable candidate recall.
- Candidate pairs must be generated and saved prior to scoring/classification.
- Singleton / no-match predictions must be explicitly supported.

## Output Requirements

- Candidate pairs must be generated and saved.
- Final predictions must be saved separately.
- **Submission format & schema:** TO BE VERIFIED FROM OFFICIAL CHALLENGE DOCUMENTATION.

## Strict Restrictions

- **External Data:** Lookup is strictly prohibited.
- **Prohibited Sources & APIs:** No Google Search, Google Maps, external business databases, geocoding APIs, or external datasets.
- **Data Integrity:** Do not leak or use information outside the competition-provided data.
- **Raw Data:** Do not modify raw input files under `data/raw/`.
