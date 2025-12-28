"""Unit tests for Learning Path Analyzer."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import (
    load_lms_data,
    extract_student_features,
    calculate_correlations,
    generate_recommendations
)


@pytest.fixture
def sample_data():
    """Create sample LMS data for testing."""
    data = {
        'student_id': ['S001', 'S001', 'S001', 'S002', 'S002'],
        'timestamp': [
            '2024-01-15 09:00:00',
            '2024-01-15 09:15:00',
            '2024-01-15 10:30:00',
            '2024-01-15 10:00:00',
            '2024-01-15 10:30:00'
        ],
        'event_type': ['login', 'quiz_attempt', 'forum_post', 'login', 'quiz_attempt'],
        'event_detail': ['morning', 'Math_Quiz_1', 'Topic_A', 'morning', 'Math_Quiz_1'],
        'grade': [np.nan, 85, np.nan, np.nan, 65]
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_csv_file(tmp_path, sample_data):
    """Create a temporary CSV file for testing."""
    csv_path = tmp_path / "test_data.csv"
    sample_data.to_csv(csv_path, index=False)
    return str(csv_path)


def test_load_lms_data(sample_csv_file):
    """Test loading LMS data from CSV."""
    df = load_lms_data(sample_csv_file)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert 'timestamp' in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df['timestamp'])


def test_extract_student_features(sample_data):
    """Test feature extraction from LMS data."""
    sample_data['timestamp'] = pd.to_datetime(sample_data['timestamp'])
    features_df = extract_student_features(sample_data)
    
    assert isinstance(features_df, pd.DataFrame)
    assert len(features_df) == 2  # Two unique students
    assert 'student_id' in features_df.columns
    assert 'total_logins' in features_df.columns
    assert 'quiz_attempts' in features_df.columns
    assert 'forum_posts' in features_df.columns
    assert 'avg_grade' in features_df.columns
    
    # Check S001 features
    s001_features = features_df[features_df['student_id'] == 'S001'].iloc[0]
    assert s001_features['total_logins'] == 1
    assert s001_features['quiz_attempts'] == 1
    assert s001_features['forum_posts'] == 1
    assert s001_features['avg_grade'] == 85


def test_calculate_correlations():
    """Test correlation calculation."""
    features_data = {
        'student_id': ['S001', 'S002', 'S003'],
        'total_logins': [5, 3, 7],
        'quiz_attempts': [4, 2, 6],
        'forum_posts': [3, 1, 5],
        'assignment_submissions': [2, 1, 3],
        'video_watches': [4, 2, 6],
        'avg_grade': [85, 65, 95]
    }
    features_df = pd.DataFrame(features_data)
    
    corr_df = calculate_correlations(features_df)
    
    assert isinstance(corr_df, pd.DataFrame)
    assert 'avg_grade' in corr_df.columns
    assert 'total_logins' in corr_df.index
    
    # Correlation matrix should be symmetric
    assert corr_df.shape[0] == corr_df.shape[1]


def test_generate_recommendations():
    """Test recommendation generation."""
    # Create sample correlation data
    features_data = {
        'student_id': ['S001', 'S002', 'S003'],
        'total_logins': [5, 3, 7],
        'quiz_attempts': [4, 2, 6],
        'forum_posts': [3, 1, 5],
        'assignment_submissions': [2, 1, 3],
        'video_watches': [4, 2, 6],
        'avg_grade': [85, 65, 95]
    }
    features_df = pd.DataFrame(features_data)
    corr_df = calculate_correlations(features_df)
    
    recommendations = generate_recommendations(corr_df, features_df)
    
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0
    assert any('RECOMMENDATIONS' in line for line in recommendations)


def test_student_features_with_no_grades(sample_data):
    """Test feature extraction when student has no graded activities."""
    # Remove all grades
    sample_data['grade'] = np.nan
    sample_data['timestamp'] = pd.to_datetime(sample_data['timestamp'])
    
    features_df = extract_student_features(sample_data)
    
    # Should still work, but avg_grade should be 0
    assert all(features_df['avg_grade'] == 0)


def test_empty_dataframe():
    """Test handling of empty DataFrame."""
    empty_df = pd.DataFrame(columns=['student_id', 'timestamp', 'event_type', 'event_detail', 'grade'])
    
    features_df = extract_student_features(empty_df)
    
    assert isinstance(features_df, pd.DataFrame)
    assert len(features_df) == 0
