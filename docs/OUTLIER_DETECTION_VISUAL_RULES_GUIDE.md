# Outlier Detection Using Visual Inspection and Simple Rules

## Overview

This guide explains how to detect outliers during exploratory data analysis (EDA).
The focus is detection and interpretation, not automatic removal or modeling.

You will combine:

- visual inspection
- simple rule-based flagging
- contextual reasoning

---

## 1. Understanding Outliers

An outlier is an observation that differs substantially from typical values.
Outliers may occur on the high side, low side, or both.

Outliers are not always errors.
Some are valid extreme events and can contain meaningful insight.

---

## 2. Why Outliers Matter

Outliers can influence key statistics and visual conclusions.

Examples:

- mean can shift upward or downward
- spread can look wider than expected
- trends can appear misleading
- comparisons across groups can be distorted

This is why early outlier detection is part of good EDA.

---

## 3. Visual Detection First

### Boxplots

Boxplots quickly flag potential outliers as points beyond whiskers.
Whiskers commonly extend to:

- $Q_1 - 1.5 \times IQR$
- $Q_3 + 1.5 \times IQR$

Points beyond whiskers are candidates for review.

### Scatter Plots

Scatter plots reveal isolated points far from the main point cloud.
They are especially useful when checking relationships between two numeric variables.

### Histograms

Extreme tails with very low frequency can indicate unusual values.

Visual inspection provides early warnings before applying rules.

---

## 4. Apply Simple Rules

Rules should support visuals, not replace judgment.

### IQR Rule

For a numeric column:

1. Compute quartiles:
- $Q_1$ (25th percentile)
- $Q_3$ (75th percentile)

2. Compute spread:
- $IQR = Q_3 - Q_1$

3. Compute bounds:

$$
\text{Lower Bound} = Q_1 - 1.5 \times IQR
$$

$$
\text{Upper Bound} = Q_3 + 1.5 \times IQR
$$

4. Flag values outside bounds.

### Threshold Rule

If a metric has known practical limits, define simple cutoffs.

Example for survey scores on 1-10 scale:

- low outlier candidate: score < 3
- high outlier candidate: score > 9

Threshold rules are easy to explain and domain-aware.

---

## 5. Compare Rules and Visuals

When reviewing flagged points, compare:

- flagged by IQR only
- flagged by threshold only
- flagged by both

Overlap can increase confidence that points are unusual.
Differences remind you that each method captures different behavior.

---

## 6. Interpreting Carefully

Use a reasoning checklist:

1. Is this value plausible in the real world?
2. Could this be a collection or entry error?
3. Does this point represent a rare but valid case?
4. How much does it affect conclusions?
5. What should be investigated next?

Outlier decisions should be documented, not assumed.

---

## 7. Common Beginner Mistakes

1. Ignoring outliers completely
2. Removing outliers immediately without context
3. Treating all outliers as bad data
4. Using only one method and calling it final
5. Failing to explain outlier decisions

---

## 8. Suggested Milestone Workflow

1. Load dataset and identify numeric columns
2. Create boxplot for one important metric
3. Create scatter plot for two related metrics
4. Apply IQR rule to flag candidates
5. Apply one simple threshold rule
6. Compare flagged records
7. Write interpretation notes

No deletion or transformation is required for this milestone.

---

## 9. Video Walkthrough Checklist (~2 Minutes)

Your recording should include:

1. visual inspection of a numeric column
2. identification of potential outliers
3. one simple rule application (IQR or threshold)
4. brief explanation of why flagged points stand out
5. reminder that detection does not imply automatic removal

---

## Final Reminder

Outlier detection is the question stage:
"Does this value make sense?"

Use visuals plus simple rules to flag unusual points.
Then apply context and reasoning before any treatment.
