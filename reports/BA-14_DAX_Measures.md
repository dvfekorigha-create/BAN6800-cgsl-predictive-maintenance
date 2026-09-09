# BA-14 Power BI DAX Measures

Total Observations = COUNTROWS('RiskData')

Critical Count = CALCULATE([Total Observations], 'RiskData'[Risk_Category] = "Critical")

High Count = CALCULATE([Total Observations], 'RiskData'[Risk_Category] = "High")

Lower Count = CALCULATE([Total Observations], 'RiskData'[Risk_Category] = "Lower")

P1 Count = CALCULATE([Total Observations], 'RiskData'[Priority_Level] = "P1")

P2 Count = CALCULATE([Total Observations], 'RiskData'[Priority_Level] = "P2")

P3 Count = CALCULATE([Total Observations], 'RiskData'[Priority_Level] = "P3")

Average Risk Score = AVERAGE('RiskData'[Risk_Score])

Maximum Risk Score = MAX('RiskData'[Risk_Score])

High Plus Critical = [Critical Count] + [High Count]

High Plus Critical % = DIVIDE([High Plus Critical], [Total Observations], 0)

Critical % = DIVIDE([Critical Count], [Total Observations], 0)

Human Review Required % = DIVIDE(CALCULATE([Total Observations], 'RiskData'[Human_Review_Flag] = 1), [Total Observations], 0)

Autonomous Control Count = CALCULATE([Total Observations], 'RiskData'[Autonomous_Control_Flag] = 1)

Top 10 Risk Score = MAXX(TOPN(10, 'RiskData', 'RiskData'[Risk_Score], DESC), 'RiskData'[Risk_Score])
