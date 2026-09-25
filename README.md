# Amazon ML Challenge 2026

## Project Overview

This repository contains the system structure for the **Amazon ML Challenge 2026: Business Entity Resolution**.

The objective of this challenge is to build a high-quality Business Entity Resolution system. For each business record in **Source 1**, the system must identify its corresponding entity records in **Source 2** and **Source 3**.

## Core Pipeline

```
Raw Data
  │
  ▼
Data Validation
  │
  ▼
Normalization
  │
  ▼
Blocking
  │
  ▼
Candidate Generation
  │
  ▼
Feature Engineering
  │
  ▼
Match Classification
  │
  ▼
Threshold Optimization
  │
  ▼
Singleton Detection
  │
  ▼
Cross-Source Consistency
  │
  ▼
Final Predictions
  │
  ▼
Submission
```

## Primary Evaluation Metric

- **Macro F0.5**
- Precision receives more weight than recall (Precision is more important than recall).

## Important Competition Considerations

- A Source 1 entity may have **zero** matches (singleton/no-match).
- A Source 1 entity may have **one** match.
- A Source 1 entity may have **multiple** matches.
- False matches (false positives) are costly due to the F0.5 metric weighting.
- Blocking must maintain high candidate recall.
- Singleton / no-match handling is critical.
- Decision thresholds must eventually be optimized specifically for F0.5.
- External data is strictly **prohibited**.
- Only competition-provided data may be used.

## Development Philosophy

Build and validate the system incrementally:

1. **EDA**
2. **Normalization**
3. **Baseline**
4. **Blocking**
5. **Feature engineering**
6. **Hard-negative generation**
7. **ML model**
8. **Threshold optimization**
9. **Singleton detection**
10. **Cross-source consistency**
11. **Error analysis**
12. **Final submission**

*Do not claim that any particular model or threshold is optimal until experiments prove it.*
