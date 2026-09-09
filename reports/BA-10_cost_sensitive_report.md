# BA-10 Threshold Tuning and Cost-Sensitive Evaluation

## Selected classifier
Random Forest, carried forward from BA-09.

## Cost structure
- False-positive cost: 10
- False-negative cost: 500
- Total cost = 10 × FP + 500 × FN.

## Experimental design
- 60% model-fit partition.
- 20% threshold-tuning partition.
- 20% internal-evaluation partition.
- All partitions stratified.
- Official UCI test set not used.
- Threshold grid: 0.01–0.99 in 0.01 increments.

## Results
- Baseline threshold: 0.50
- Selected threshold: 0.10
- Baseline evaluation cost: 35270
- Selected-threshold evaluation cost: 8830
- Cost reduction: 26440
- Cost reduction (%): 74.96%
- Baseline precision: 0.8280
- Baseline recall: 0.6500
- Baseline F1-score: 0.7283
- Selected-threshold precision: 0.3621
- Selected-threshold recall: 0.9450
- Selected-threshold F1-score: 0.5235
- ROC-AUC: 0.9811

## Interpretation
The selected threshold minimizes the UCI-weighted classification cost on the threshold-tuning partition and is then assessed on a separate internal-evaluation partition. Because false negatives carry a substantially higher cost than false positives, the cost-minimizing threshold may differ from 0.50. The selected threshold is a decision-support parameter and does not authorize autonomous maintenance action.

## Scope limitation
The UCI APS dataset is a public proxy for CGSL. These results demonstrate the analytical method and should not be interpreted as direct evidence of CGSL vessel or equipment performance.