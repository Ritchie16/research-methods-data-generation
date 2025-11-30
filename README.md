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
  
## Dependencies

| Package    | Version   | Purpose                                    |
|------------|-----------|--------------------------------------------|
| **pandas** | >= 2.3.3  | Data manipulation and CSV export           |
| **numpy**  | >= 2.2.6  | Numerical computations and random sampling |
| **faker**  | >= 38.2.0 | Synthetic data generation                  |


### What Makes This Project Reproducible 

1. **Deterministic Random Seeds** - Both numpy and Faker use seed 42
   - Line 7-8 in `generate_data.py`: `np.random.seed(42)` and `Faker.seed(42)`
   - Guarantees identical output every time the script runs

2. **Pinned Dependencies** - Exact versions in `requirements.txt`
   - Ensures consistent behavior across all environments
   - Use: `pip install -r requirements.txt`

3. **Complete Parameter Documentation** - All parameters saved in `metadata.json`
   - Number of users: 3,000
   - Random seed: 42
   - Locations: 21 Malawi districts
   - Device distribution: Android 65%, iOS 20%, KaiOS 8%, Feature Phone 7%
   - Network distribution: Airtel 55%, TNM 40%, MTL 5%

4. **Reproducible Data Characteristics**
   - Urban engagement multiplier: 1.2x (Lilongwe, Blantyre, Mzuzu)
   - Rural engagement multiplier: 0.8x (all other locations)
   - Gender ratio: 52% Male, 48% Female
   - Age range: 18-65 years
   - Retention rate: 75%


### Setup Environment
1. Clone the repository: 
   ```bash
   git clone https://github.com/Ritchie16/research-methods-data-generation.git
   cd research-methods-data-generation
   ```

2. Install dependencies this is recommended for reproducibility:
   ```bash
   pip install -r requirements.txt

### Run Script:
```bash

python generate_data.py

```
**
Expected output:
- File `user_engagement_data.csv` with 3,001 lines (header + 3,000 records)
- File `metadata.json` with generation parameters
- Console output showing sample data and distribution summaries

**Verification**

Check that:
- `user_engagement_data.csv` has exactly 3,000 data rows
- First few rows match expected values (download and compare)
- `metadata.json` contains all expected generation parameters

### Verifying Identical Output

To confirm your generated data is identical to any previous run:

1. **Row count**: Should be exactly 3,000 rows + 1 header
   ```bash
   # On Linux/Mac:
   wc -l user_engagement_data.csv 

   # On Windows:
    Get-Content user_engagement_data.csv | Measure-Object -Line

   ```

2. **Column count**:Should be exactly 12 columns and headers
   ```bash
   # on linux/mac
    head -1 user_engagement_data.csv 

   # on windows:
   Get-Content user_engagement_data.csv -TotalCount 1 
   
   # Should have these headers: user_id, age, gender, location, device, network, clicks, session_duration, data_used_mb, feature_version, feedback_score, retention_flag
   
   ```


3. **Data integrity**: Check first row matches
   ```bash
   #on windows:
   (Get-Content user_engagement_data.csv)[1]

   #on Linux/mac:
   head -n 1 user_engagement_data.csv

   # Should start with: 0,39,M,Mzuzu,Android,TNM,6,404,A,,1,70.21...

   ```

4. **Metadata parameters**: Verify seed is 42
   ```bash
   #on Windows:
   Select-String -Path metadata.json -Pattern "seed"
   
   #on Linux:
   cat metadata.json | grep -i seed

   # "seed": 42
   ```

## Metadata

- **Date Generated**: 2025-11-27
- **Seed**: 42 (for reproducibility)
- **License**: CC0
- **Contact**: richardmunthali016@gmail.com



## Notes and limitations
This is a synthetic dataset created for academic and research purposes. While it reflects realistic patterns for the Malawian context, it does not represent actual user data. The dataset is suitable for statistical analysis, machine learning experiments, and educational purposes.
