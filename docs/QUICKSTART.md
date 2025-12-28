# Quick Start Guide

## Getting Started in 5 Minutes

### Step 1: Clone and Setup
```bash
git clone <your-repo-url>
cd Learning_Path_Analyzer
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Step 2: Run Analysis
```bash
python -m src.main
```

### Step 3: View Results
Check the `reports/` folder for:
- `correlation_heatmap.png`
- `student_performance.png`
- `recommendations.txt`

## What You Get

✅ Correlation analysis between student activities and grades
✅ Beautiful visualizations
✅ Actionable recommendations for improving learning outcomes

## Next Steps

1. Replace `data/sample.csv` with your own LMS logs
2. Run the analysis again
3. Review recommendations and implement changes
4. Set up GitHub Actions for automatic scheduled analysis

## Need Help?

See the main [README.md](../README.md) for detailed documentation.
