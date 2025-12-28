# 📊 Learning Path Analyzer

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🎯 Description

**Learning Path Analyzer** is an intelligent system for analyzing student learning paths based on LMS (Learning Management System) logs from platforms like Moodle, Canvas, and others. The system identifies which types of educational activities are most effective for different students and provides data-driven recommendations for optimizing learning paths.

### Key Features

- 📝 **CSV Log Parsing** - Automatic parsing of LMS activity logs
- 🔍 **Event Analysis** - Extraction of key events (logins, assignments, forum posts, quizzes)
- 📈 **Correlation Analysis** - Statistical analysis of relationships between activities and performance
- 📊 **Visualizations** - Beautiful charts and heatmaps using matplotlib and seaborn
- 💡 **Smart Recommendations** - AI-driven suggestions for improving learning outcomes
- 🤖 **CI/CD Automation** - Scheduled analysis and automatic report generation

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Input Data Format](#input-data-format)
- [Output Examples](#output-examples)
- [Project Structure](#project-structure)
- [CI/CD Pipeline](#cicd-pipeline)
- [Development](#development)
- [Testing](#testing)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Learning_Path_Analyzer.git
cd Learning_Path_Analyzer
```

2. **Create virtual environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

Run the analyzer with the default sample data:

```bash
python -m src.main
```

### Custom Data File

Analyze your own LMS log file:

```bash
python -m src.main --data path/to/your/data.csv --output reports
```

### Command Line Options

```
Options:
  --data PATH     Path to CSV file with LMS logs (default: data/sample.csv)
  --output DIR    Directory to save reports (default: reports)
  -h, --help      Show help message
```

### Example Output

```
============================================================
LEARNING PATH ANALYZER
============================================================

Loading data from data/sample.csv...
Loaded 47 log entries for 6 students

Extracting student features...
Extracted features for 6 students

Calculating correlations...

Generating visualizations...
Correlation heatmap saved to reports/correlation_heatmap.png
Student performance visualization saved to reports/student_performance.png

Generating recommendations...
============================================================
LEARNING PATH RECOMMENDATIONS
============================================================

Activity Impact Analysis:
----------------------------------------
  • video_watches: 0.985 (High positive impact)
  • quiz_attempts: 0.976 (High positive impact)
  • forum_posts: 0.945 (High positive impact)
...
```

## 📊 Input Data Format

The system expects CSV files with the following columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `student_id` | string | Unique student identifier | S001 |
| `timestamp` | datetime | Event timestamp | 2024-01-15 09:00:00 |
| `event_type` | string | Type of activity | login, quiz_attempt, forum_post, assignment_submission, video_watch |
| `event_detail` | string | Additional event info | Math_Quiz_1 |
| `grade` | float | Grade (if applicable) | 85.0 |

### Sample Data

```csv
student_id,timestamp,event_type,event_detail,grade
S001,2024-01-15 09:00:00,login,morning_session,
S001,2024-01-15 09:15:00,quiz_attempt,Math_Quiz_1,85
S001,2024-01-15 10:30:00,forum_post,Discussion_Topic_A,
S001,2024-01-15 14:00:00,assignment_submission,Essay_Assignment_1,78
```

See `data/sample.csv` for a complete example.

## 📈 Output Examples

The analyzer generates three main outputs:

### 1. Correlation Heatmap
![Correlation Heatmap Example](docs/example_heatmap.png)

Shows correlations between different activities and student performance.

### 2. Performance Visualizations
![Performance Charts](docs/example_performance.png)

Includes:
- Grade distribution histogram
- Quiz attempts vs performance scatter plot
- Forum participation vs performance
- Video engagement vs performance

### 3. Recommendations Report

Text file with detailed analysis and actionable recommendations:
- Activity impact rankings
- Student performance tiers
- Specific improvement suggestions

## 📁 Project Structure

```
Learning_Path_Analyzer/
├── .github/
│   └── workflows/
│       └── analysis.yml       # CI/CD pipeline configuration
├── data/
│   └── sample.csv            # Sample LMS log data
├── docs/                     # Documentation and examples
├── reports/                  # Generated reports (auto-created)
├── scripts/                  # Utility scripts
├── src/
│   ├── __init__.py
│   ├── main.py              # Main analysis script
│   └── utils.py             # Helper functions
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Unit tests
├── .gitignore
├── README.md
└── requirements.txt
```

## 🤖 CI/CD Pipeline

This project includes a comprehensive GitHub Actions workflow that:

### Features

✅ **Code Quality Checks**
- Black code formatting validation
- Flake8 linting for PEP 8 compliance

✅ **Automated Testing**
- Pytest unit tests with coverage reports
- Codecov integration

✅ **Scheduled Analysis** (Unique Feature! 🌟)
- Runs automatically every day at 9:00 AM UTC
- Analyzes latest data and generates fresh reports

✅ **Manual Triggers**
- Workflow dispatch with custom data file parameter
- On-demand report generation

✅ **Artifact Management**
- Automatic upload of generated reports
- 30-day retention for historical analysis
- Commits results to `reports/` branch

✅ **Summary Reports**
- GitHub Actions summary with key recommendations
- Quick insights without downloading artifacts

### Trigger the Workflow

1. **Automatic** - Pushes to main branch
2. **Scheduled** - Daily at 9:00 AM UTC
3. **Manual** - Go to Actions → Learning Path Analysis CI/CD → Run workflow

## 🛠 Development

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/test_main.py -v
```

### Code Formatting

```bash
# Check formatting
black --check src/ tests/

# Auto-format code
black src/ tests/
```

### Linting

```bash
# Run flake8
flake8 src/ tests/ --max-line-length=100
```

## 📊 Example Analysis Workflow

1. **Collect Data** - Export LMS logs to CSV
2. **Run Analysis** - Execute `python -m src.main --data your_data.csv`
3. **Review Reports** - Check generated visualizations and recommendations
4. **Implement Changes** - Apply suggested learning path optimizations
5. **Monitor Results** - Re-run analysis periodically to track improvements

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Inspired by educational data mining research
- Built for AI in Education course
- Thanks to all contributors

## 📞 Support

For questions or issues, please open an issue on GitHub.

---

**Made with ❤️ for better education through data analysis**
