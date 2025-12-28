"""Utility functions for data processing and visualization."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple
import os


def load_lms_data(file_path: str) -> pd.DataFrame:
    """
    Load LMS log data from CSV file.
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        DataFrame with parsed LMS logs
    """
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df


def extract_student_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract features for each student based on their activities.
    
    Args:
        df: DataFrame with LMS logs
        
    Returns:
        DataFrame with student features
    """
    features = []
    
    for student_id in df['student_id'].unique():
        student_data = df[df['student_id'] == student_id]
        
        feature_dict = {
            'student_id': student_id,
            'total_logins': len(student_data[student_data['event_type'] == 'login']),
            'quiz_attempts': len(student_data[student_data['event_type'] == 'quiz_attempt']),
            'forum_posts': len(student_data[student_data['event_type'] == 'forum_post']),
            'assignment_submissions': len(student_data[student_data['event_type'] == 'assignment_submission']),
            'video_watches': len(student_data[student_data['event_type'] == 'video_watch']),
        }
        
        # Calculate average grade
        graded_events = student_data[student_data['grade'].notna()]
        if len(graded_events) > 0:
            feature_dict['avg_grade'] = graded_events['grade'].mean()
        else:
            feature_dict['avg_grade'] = 0
            
        features.append(feature_dict)
    
    return pd.DataFrame(features)


def calculate_correlations(features_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate correlations between activities and performance.
    
    Args:
        features_df: DataFrame with student features
        
    Returns:
        DataFrame with correlation matrix
    """
    activity_cols = ['total_logins', 'quiz_attempts', 'forum_posts', 
                     'assignment_submissions', 'video_watches']
    corr_data = features_df[activity_cols + ['avg_grade']].corr()
    return corr_data


def plot_correlation_heatmap(corr_df: pd.DataFrame, output_path: str = 'reports/correlation_heatmap.png'):
    """
    Create correlation heatmap visualization.
    
    Args:
        corr_df: Correlation matrix DataFrame
        output_path: Path to save the plot
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', center=0, 
                fmt='.2f', square=True, linewidths=1)
    plt.title('Correlation between Activities and Performance', fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Correlation heatmap saved to {output_path}")


def plot_student_performance(features_df: pd.DataFrame, output_path: str = 'reports/student_performance.png'):
    """
    Create student performance visualization.
    
    Args:
        features_df: DataFrame with student features
        output_path: Path to save the plot
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot 1: Average grade distribution
    axes[0, 0].hist(features_df['avg_grade'], bins=10, edgecolor='black', color='skyblue')
    axes[0, 0].set_xlabel('Average Grade', fontsize=12)
    axes[0, 0].set_ylabel('Number of Students', fontsize=12)
    axes[0, 0].set_title('Grade Distribution', fontsize=14)
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Plot 2: Quiz attempts vs Grade
    axes[0, 1].scatter(features_df['quiz_attempts'], features_df['avg_grade'], 
                       alpha=0.6, s=100, color='coral')
    axes[0, 1].set_xlabel('Quiz Attempts', fontsize=12)
    axes[0, 1].set_ylabel('Average Grade', fontsize=12)
    axes[0, 1].set_title('Quiz Attempts vs Performance', fontsize=14)
    axes[0, 1].grid(alpha=0.3)
    
    # Plot 3: Forum posts vs Grade
    axes[1, 0].scatter(features_df['forum_posts'], features_df['avg_grade'], 
                       alpha=0.6, s=100, color='lightgreen')
    axes[1, 0].set_xlabel('Forum Posts', fontsize=12)
    axes[1, 0].set_ylabel('Average Grade', fontsize=12)
    axes[1, 0].set_title('Forum Participation vs Performance', fontsize=14)
    axes[1, 0].grid(alpha=0.3)
    
    # Plot 4: Video watches vs Grade
    axes[1, 1].scatter(features_df['video_watches'], features_df['avg_grade'], 
                       alpha=0.6, s=100, color='plum')
    axes[1, 1].set_xlabel('Video Watches', fontsize=12)
    axes[1, 1].set_ylabel('Average Grade', fontsize=12)
    axes[1, 1].set_title('Video Engagement vs Performance', fontsize=14)
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Student performance visualization saved to {output_path}")


def generate_recommendations(corr_df: pd.DataFrame, features_df: pd.DataFrame) -> List[str]:
    """
    Generate learning path recommendations based on correlations.
    
    Args:
        corr_df: Correlation matrix
        features_df: Student features DataFrame
        
    Returns:
        List of recommendation strings
    """
    recommendations = []
    
    # Get correlations with average grade
    grade_corr = corr_df['avg_grade'].drop('avg_grade').sort_values(ascending=False)
    
    recommendations.append("=" * 60)
    recommendations.append("LEARNING PATH RECOMMENDATIONS")
    recommendations.append("=" * 60)
    recommendations.append("")
    
    recommendations.append("Activity Impact Analysis:")
    recommendations.append("-" * 40)
    for activity, corr in grade_corr.items():
        impact = "High" if abs(corr) > 0.5 else "Medium" if abs(corr) > 0.3 else "Low"
        direction = "positive" if corr > 0 else "negative"
        recommendations.append(f"  • {activity}: {corr:.3f} ({impact} {direction} impact)")
    
    recommendations.append("")
    recommendations.append("Key Recommendations:")
    recommendations.append("-" * 40)
    
    # Find top 3 positive correlations
    top_activities = grade_corr.head(3)
    for i, (activity, corr) in enumerate(top_activities.items(), 1):
        if corr > 0.3:
            recommendations.append(
                f"  {i}. Encourage {activity.replace('_', ' ')} "
                f"(correlation: {corr:.3f})"
            )
    
    # Student performance tiers
    recommendations.append("")
    recommendations.append("Student Performance Tiers:")
    recommendations.append("-" * 40)
    high_performers = len(features_df[features_df['avg_grade'] >= 85])
    mid_performers = len(features_df[(features_df['avg_grade'] >= 70) & (features_df['avg_grade'] < 85)])
    low_performers = len(features_df[features_df['avg_grade'] < 70])
    
    recommendations.append(f"  • High performers (≥85): {high_performers} students")
    recommendations.append(f"  • Mid performers (70-84): {mid_performers} students")
    recommendations.append(f"  • Need support (<70): {low_performers} students")
    
    recommendations.append("")
    recommendations.append("=" * 60)
    
    return recommendations
