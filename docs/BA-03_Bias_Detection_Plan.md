# Bias Detection Plan

## Current proxy
- Measure target-class representation because the source is highly imbalanced.
- Record that protected-group fairness assessment is not defensible when no protected/sensitive attributes exist.

## Future CGSL data
- Define approved sensitive/group variables with governance.
- Use Fairlearn `MetricFrame` for subgroup metrics when valid group labels exist.
- Monitor recall, precision, false-positive rate, false-negative rate, selection rate and support size.
- Set minimum subgroup sample thresholds and document exceptions.
- Escalate material disparities for review rather than automatically changing model behavior.
