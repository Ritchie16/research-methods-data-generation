# Malawi User Engagement Dataset for App Feature Analysis

## Overview
This dataset contains synthetic user engagement data for 3000 Malawian mobile app users, designed for analyzing user behavior patterns and feature performance in the Malawian context.

## Dataset Details

- **Total Records**: 3,000 users
- **Format**: CSV (Comma-separated values)
- **Generation Date**: 2025-11-27
- **License**: CC0 (Public Domain)

## Features

### User Demographics
- `user_id`: Unique identifier for each user
- `age`: User age (18-64 years)
- `gender`: Gender (M/F with realistic Malawi distribution)
- `location`: Malawi districts and cities (21 locations)

### Device & Network Information
- `device`: Mobile device type (Android, iOS, KaiOS, Feature Phone)
- `network`: Telecom provider (Airtel, TNM, MTL)

### Engagement Metrics
- `clicks`: Number of clicks per session
- `session_duration`: Session duration in seconds (minimum 30s)
- `data_used_mb`: Data consumption in MB

### Experimental & Business Metrics
- `feature_version`: A/B testing group (A/B)
- `feedback_score`: User satisfaction rating (1-5 scale, with some missing values)
- `retention_flag`: User retention indicator (0=churned, 1=retained)

## Context & Realism

### Malawi-Specific Features
- **Locations**: Real Malawian districts and cities including Lilongwe, Blantyre, Mzuzu, Zomba, etc.
- **Telecom Providers**: Airtel (55%), TNM (40%), MTL (5%) - reflecting real market share
- **Device Distribution**: Realistic for Malawi market (predominantly Android)
- **Urban-Rural Engagement**: Different engagement patterns based on location

### Behavioral Patterns
- **Device-based engagement**: Different baseline metrics for Android, iOS, and basic phones
- **Urban multiplier**: 20% higher engagement in urban areas (Lilongwe, Blantyre, Mzuzu)
- **Realistic distributions**: Poisson distribution for clicks, normal distribution for session duration

## Data Generation

### Methodology
- **Synthetic Generation**: Python with Faker and Pandas
- **Random Seed**: 42 for reproducibility
- **Realistic Distributions**: Based on Malawian mobile usage patterns

### Parameters
- Sample size: 3,000 users
- Single day snapshot
- Malawi context with realistic demographics

## Usage

### Potential Applications
- A/B testing analysis for feature versions
- User retention prediction modeling
- Engagement pattern analysis by demographic segments
- Telecom provider performance comparison
- Geographic engagement analysis across Malawi

### Analysis Considerations
- 75% retention rate in the dataset
- Some missing feedback scores (5% of records)
- Realistic data distributions with some outliers

## Files

1. `user_engagement_data.csv` - Main dataset
2. `metadata.json` - Dataset metadata and generation details
3. `requirements.txt` - Python dependencies for reproduction

## Group Members

- Richard Mnthali (BICT1823)
- Praise Mwamlima (BICT2623)
- Ethel Lwinga (BICT1423)
- Blessings Phiri (BICT3223)
- Madalo Zaphuka (BICT1822)
- Kelvin Lackson (BICT1323)

## Contact
**Email**: richardmunthali016@gmail.com

## Notes
This is a synthetic dataset created for academic and research purposes. While it reflects realistic patterns for the Malawian context, it does not represent actual user data. The dataset is suitable for statistical analysis, machine learning experiments, and educational purposes.
