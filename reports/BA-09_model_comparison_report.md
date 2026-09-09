# BA-09 Classifier Comparison Report

## Purpose
Compare Logistic Regression, Random Forest and Gradient Boosting using five-fold stratified cross-validation on the prepared UCI APS training data.

## Experimental controls
- Final feature count: 334
- Cross-validation: StratifiedKFold, 5 folds, shuffled, random state 42
- Official test set used for selection/tuning: No
- Baseline threshold: 0.5
- Threshold tuning: No; reserved for BA-10

## Cross-validation summary

```
              Model  Precision_Mean  Precision_SD  Recall_Mean  Recall_SD  F1_Mean    F1_SD  ROC_AUC_Mean  ROC_AUC_SD
      Random Forest        0.883831      0.013267        0.655   0.048088 0.751680 0.034080      0.986330    0.004061
Logistic Regression        0.366171      0.007107        0.910   0.032210 0.522151 0.011503      0.964928    0.016348
  Gradient Boosting        0.244126      0.006128        0.960   0.011726 0.389236 0.008240      0.982841    0.005132
```

## Provisional comparison result
The classifier with the highest mean F1-score in this run is **Random Forest** with mean F1-score **0.7517**.

This is a comparison-stage result only. Final model and threshold decisions should also consider recall, precision, ROC-AUC, stability across folds, and the business cost of false negatives versus false positives.

## Scope limitation
The UCI APS dataset is a public proxy for the CGSL project. These results demonstrate analytical methodology and should not be interpreted as direct evidence of CGSL vessel or equipment performance.
