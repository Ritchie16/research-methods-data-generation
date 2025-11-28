import pandas as pd
import numpy as np
from faker import Faker
import json

# Set random seeds for reproducibility
np.random.seed(42)
Faker.seed(42)

print("Starting data generation...")

# Initialize Faker with Malawi locale
# British English often works better for African countries
fake = Faker(['en_GB'])  

# Malawi-specific locations (districts and cities)
malawi_locations = [
    "Lilongwe", "Blantyre", "Mzuzu", "Zomba", "Kasungu", "Mangochi", "Karonga", 
    "Salima", "Nkhotakota", "Liwonde", "Dedza", "Mchinji", "Mulanje", "Thyolo",
    "Balaka", "Mwanza", "Ntcheu", "Rumphi", "Chitipa", "Nsanje", "Chikhwawa"
]

# Realistic device distribution for Malawi (based on market share)
devices = ["Android", "Android", "Android", "iOS", "KaiOS", "Feature Phone"]

# Generate user base with MALAWI context
users = []
# Simulate 3000 users
for i in range(3000):
    users.append({
        'user_id': i,
        'age': np.random.randint(18, 65),
        'gender': np.random.choice(['M', 'F'], p=[0.52, 0.48]),  # Realistic Malawi gender ratio
        'location': np.random.choice(malawi_locations),
        'device': np.random.choice(devices, p=[0.65, 0.20, 0.08, 0.05, 0.01, 0.01]),  # Fixed: probabilities match 6 devices
        'network': np.random.choice(['Airtel', 'TNM', 'MTL'], p=[0.55, 0.40, 0.05])  # Malawi telecom providers
    })

# Expand to daily interactions for 30 days
data = []
for user in users:
    for day in range(30):
        # Realistic user behavior patterns
        if user['device'] == 'Android':
            base_clicks = np.random.poisson(lam=6)
            base_duration = np.random.normal(320, 60)
        elif user['device'] == 'iOS':
            base_clicks = np.random.poisson(lam=7)
            base_duration = np.random.normal(350, 50)
        else:  # Basic phones
            base_clicks = np.random.poisson(lam=3)
            base_duration = np.random.normal(180, 40)
        
        # Urban vs rural engagement differences
        urban_areas = ["Lilongwe", "Blantyre", "Mzuzu"]
        if user['location'] in urban_areas:
            engagement_multiplier = 1.2
        else:
            engagement_multiplier = 0.8
        
        data.append({
            **user,
            'date': f'2025-11-{day+1:02d}',
            'clicks': max(0, int(base_clicks * engagement_multiplier)),
            'session_duration': max(30, int(base_duration * engagement_multiplier)),  # Minimum 30 seconds
            'feature_version': np.random.choice(['A', 'B'], p=[0.5, 0.5]),
            'feedback_score': np.random.choice([1, 2, 3, 4, 5, None], p=[0.05, 0.1, 0.25, 0.35, 0.2, 0.05]),
            'retention_flag': np.random.choice([0, 1], p=[0.25, 0.75]),  # 75% retention
            'data_used_mb': max(0, np.random.normal(50, 20))  # Data usage in MB
        })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('user_engagement_data.csv', index=False)
print("dataset saved: user_engagement_data.csv")
print(f"Dataset shape: {df.shape}")

# Create proper metadata
metadata = {
    "title": "Malawi User Engagement Dataset for App Feature Analysis",
    "group": [
        {
            "name": "Richard Mnthali",
            "registration_number": "BICT1823"
        },
        {
            "name": "Praise Mwamlima",
            "registration_number": "BICT2623"
        },
        {
            "name": "Ethel Lwinga",
            "registration_number": "BICT1423"
        },
        {
            "name": "Blessings Phiri",
            "registration_number": "BICT3223"
        },
        {
            "name": "Madalo Zaphuka",
            "registration_number": "BICT1822"
        },
        {
            "name": "Kelvin Lackson",
            "registration_number": "BICT1323"
        }
    ],  
    "date": "2025-11-27",
    "generation_method": "Synthetic (Python/Faker+Pandas)",
    "parameters": {
        "n_users": 3000,
        "n_days": 30, 
        "seed": 42,
        "total_records": len(df),
        "locations": "Malawi districts and cities",
        "devices": "Realistic Malawi market distribution"
    },
    "source": "synthetic - Malawi context",
    "license": "CC0",
    "contact": "richardmunthali016@gmail.com",
    "context": "Simulated Malawian mobile user behavior with realistic demographics"
}

with open('metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print("Metadata saved: metadata.json")

# Show realistic sample of the data
print("\nREALISTIC Sample of generated data:")
print(df.head(10))

# Show distribution summary
print(f"\nDevice Distribution:")
print(df['device'].value_counts())
print(f"\nLocation Distribution (top 10):")
print(df['location'].value_counts().head(10))
print(f"\nNetwork Distribution:")
print(df['network'].value_counts())