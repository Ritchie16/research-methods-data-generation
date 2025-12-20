import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style but limit complexity
plt.style.use('default')
sns.set_palette("husl")

def optimized_complete_analysis(df):
    print("Starting OPTIMIZED complete analysis...")
    
    # 1. Calculate all metrics first
    print("Calculating metrics...")
    
    total_users = df['user_id'].nunique()
    retention_rate = df['retention_flag'].mean() * 100
    avg_session = df['session_duration'].mean()
    avg_clicks = df['clicks'].mean()
    avg_feedback = df['feedback_score'].mean()
    
    # Feature A/B Test
    feature_a_retention = df[df['feature_version'] == 'A']['retention_flag'].mean() * 100
    feature_b_retention = df[df['feature_version'] == 'B']['retention_flag'].mean() * 100
    feature_advantage = feature_a_retention - feature_b_retention
    
    # Network Analysis
    network_performance = df.groupby('network').agg({
        'retention_flag': 'mean',
        'session_duration': 'mean', 
        'clicks': 'mean'
    })
    best_network = network_performance['retention_flag'].idxmax()
    
    # Device Analysis
    device_performance = df.groupby('device').agg({
        'retention_flag': 'mean',
        'session_duration': 'mean'
    })
    best_device = device_performance['retention_flag'].idxmax()
    
    # Engagement Segments
    high_engagement = df[(df['clicks'] >= 5) & (df['session_duration'] >= 300)]
    low_engagement = df[(df['clicks'] < 3) | (df['session_duration'] < 150)]
    
    # Age Groups
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 45, 55, 100], 
                           labels=['18-25', '26-35', '36-45', '46-55', '55+'])
    age_retention = df.groupby('age_group')['retention_flag'].mean()
    best_age_group = age_retention.idxmax()
    
    # Location Analysis
    top_locations = df.groupby('location')['retention_flag'].mean().nlargest(5)
    
    print("Metrics calculated!")
    
    # 2. Create SIMPLIFIED but complete visualizations
    print("Generating charts...")
    
    fig = plt.figure(figsize=(18, 16))
    
    # Chart 1: KPIs
    plt.subplot(4, 4, 1)
    kpis = {'Total Users': total_users, 'Retention': retention_rate, 
            'Avg Session': avg_session, 'Avg Clicks': avg_clicks}
    plt.bar(kpis.keys(), kpis.values())
    plt.title('Key Performance Indicators')
    plt.xticks(rotation=45)
    
    # Chart 2: Feature A/B Test
    plt.subplot(4, 4, 2)
    plt.bar(['Feature A', 'Feature B'], [feature_a_retention, feature_b_retention])
    plt.title('A/B Test: Retention Rate')
    plt.ylabel('Retention (%)')
    
    # Chart 3: Network Performance
    plt.subplot(4, 4, 3)
    network_performance['retention_flag'].plot(kind='bar')
    plt.title('Retention by Network')
    plt.ylabel('Retention Rate')
    
    # Chart 4: Device Performance
    plt.subplot(4, 4, 4)
    device_performance['retention_flag'].plot(kind='bar')
    plt.title('Retention by Device')
    plt.ylabel('Retention Rate')
    
    # Chart 5: Age Group Analysis
    plt.subplot(4, 4, 5)
    age_retention.plot(kind='bar')
    plt.title('Retention by Age Group')
    plt.ylabel('Retention Rate')
    
    # Chart 6: Session Duration Distribution
    plt.subplot(4, 4, 6)
    plt.hist(df['session_duration'], bins=20, alpha=0.7)
    plt.title('Session Duration Distribution')
    plt.xlabel('Seconds')
    
    # Chart 7: Clicks Distribution
    plt.subplot(4, 4, 7)
    plt.hist(df['clicks'], bins=15, alpha=0.7)
    plt.title('Clicks Distribution')
    plt.xlabel('Number of Clicks')
    
    # Chart 8: Feedback Scores
    plt.subplot(4, 4, 8)
    df['feedback_score'].value_counts().sort_index().plot(kind='bar')
    plt.title('Feedback Score Distribution')
    plt.xlabel('Score (1-5)')
    
    # Chart 9: Retention vs Session Duration
    plt.subplot(4, 4, 9)
    retained = df[df['retention_flag'] == 1]['session_duration']
    not_retained = df[df['retention_flag'] == 0]['session_duration']
    plt.hist([retained, not_retained], bins=20, alpha=0.7, label=['Retained', 'Not Retained'])
    plt.title('Session Duration: Retained vs Not')
    plt.xlabel('Seconds')
    plt.legend()
    
    # Chart 10: Data Usage
    plt.subplot(4, 4, 10)
    plt.scatter(df['data_used_mb'], df['session_duration'], alpha=0.5)
    plt.xlabel('Data Used (MB)')
    plt.ylabel('Session Duration (s)')
    plt.title('Data Usage vs Engagement')
    
    # Chart 11: Top Locations
    plt.subplot(4, 4, 11)
    top_locations.plot(kind='bar')
    plt.title('Top 5 Locations by Retention')
    plt.ylabel('Retention Rate')
    plt.xticks(rotation=45)
    
    # Chart 12: Feature Version Comparison
    plt.subplot(4, 4, 12)
    feature_metrics = df.groupby('feature_version').agg({
        'retention_flag': 'mean',
        'session_duration': 'mean',
        'clicks': 'mean'
    })
    x = np.arange(3)
    plt.bar(x - 0.2, feature_metrics.loc['A'], 0.4, label='Version A')
    plt.bar(x + 0.2, feature_metrics.loc['B'], 0.4, label='Version B')
    plt.xticks(x, ['Retention', 'Duration', 'Clicks'])
    plt.title('Feature Version Comparison')
    plt.legend()
    
    # Chart 13: Engagement Segments
    plt.subplot(4, 4, 13)
    engagement_data = [
        high_engagement['retention_flag'].mean() * 100,
        low_engagement['retention_flag'].mean() * 100
    ]
    plt.bar(['High Engagement', 'Low Engagement'], engagement_data)
    plt.title('Retention by Engagement Level')
    plt.ylabel('Retention (%)')
    
    # Chart 14: Gender Analysis
    plt.subplot(4, 4, 14)
    gender_retention = df.groupby('gender')['retention_flag'].mean()
    gender_retention.plot(kind='bar')
    plt.title('Retention by Gender')
    plt.ylabel('Retention Rate')
    
    # Chart 15: Age Distribution
    plt.subplot(4, 4, 15)
    df['age'].hist(bins=20)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    
    # Chart 16: Network Engagement
    plt.subplot(4, 4, 16)
    df.groupby('network')['session_duration'].mean().plot(kind='bar')
    plt.title('Avg Session by Network')
    plt.ylabel('Seconds')
    
    plt.tight_layout()
    plt.savefig('complete_analysis.png', dpi=150, bbox_inches='tight')
    print("Charts saved as complete_analysis.png")
    
    # 3. Generate COMPREHENSIVE HTML report (FIXED - no emojis)
    print("Generating comprehensive report...")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Complete User Engagement Analysis</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ background: #2E86AB; color: white; padding: 20px; border-radius: 10px; }}
            .section {{ margin: 25px 0; padding: 20px; background: #f8f9fa; border-radius: 8px; }}
            .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }}
            .kpi-card {{ background: white; padding: 15px; border-radius: 6px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            .kpi-value {{ font-size: 24px; font-weight: bold; color: #2E86AB; }}
            .insight {{ background: #e8f5e8; padding: 15px; border-radius: 6px; margin: 10px 0; }}
            .alert {{ background: #ffeaa7; padding: 15px; border-radius: 6px; margin: 10px 0; }}
            table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
            th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
            th {{ background: #2E86AB; color: white; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Complete User Engagement Analysis</h1>
            <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Users: {total_users} | Records: {len(df)}</p>
        </div>
        
        <div class="section">
            <h2>Executive Summary</h2>
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-value">{retention_rate:.1f}%</div>
                    <div>Overall Retention</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{avg_session:.0f}s</div>
                    <div>Avg Session</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{avg_clicks:.1f}</div>
                    <div>Avg Clicks</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{avg_feedback:.1f}/5</div>
                    <div>Avg Feedback</div>
                </div>
            </div>
        </div>
        
        <div class="alert">
            <h3>Critical Business Insight</h3>
            <p><strong>Feature A outperforms Feature B by {feature_advantage:.1f}% in user retention</strong></p>
            <p>Feature A: {feature_a_retention:.1f}% vs Feature B: {feature_b_retention:.1f}%</p>
        </div>
        
        <div class="section">
            <h2>Performance Analysis</h2>
            
            <h3>Feature A/B Test Results</h3>
            <table>
                <tr><th>Metric</th><th>Feature A</th><th>Feature B</th><th>Difference</th></tr>
                <tr><td>Retention Rate</td><td>{feature_a_retention:.1f}%</td><td>{feature_b_retention:.1f}%</td><td>{feature_advantage:+.1f}%</td></tr>
                <tr><td>Avg Session Duration</td><td>{df[df['feature_version']=='A']['session_duration'].mean():.0f}s</td><td>{df[df['feature_version']=='B']['session_duration'].mean():.0f}s</td><td>{df[df['feature_version']=='A']['session_duration'].mean() - df[df['feature_version']=='B']['session_duration'].mean():+.0f}s</td></tr>
                <tr><td>Avg Clicks</td><td>{df[df['feature_version']=='A']['clicks'].mean():.1f}</td><td>{df[df['feature_version']=='B']['clicks'].mean():.1f}</td><td>{df[df['feature_version']=='A']['clicks'].mean() - df[df['feature_version']=='B']['clicks'].mean():+.1f}</td></tr>
            </table>
            
            <h3>Network Performance</h3>
            <table>
                <tr><th>Network</th><th>Retention Rate</th><th>Avg Session</th><th>Avg Clicks</th></tr>
                {"".join([f"<tr><td>{net}</td><td>{row['retention_flag']*100:.1f}%</td><td>{row['session_duration']:.0f}s</td><td>{row['clicks']:.1f}</td></tr>" for net, row in network_performance.iterrows()])}
            </table>
            
            <h3>Device Performance</h3>
            <table>
                <tr><th>Device</th><th>Retention Rate</th><th>Avg Session</th></tr>
                {"".join([f"<tr><td>{device}</td><td>{row['retention_flag']*100:.1f}%</td><td>{row['session_duration']:.0f}s</td></tr>" for device, row in device_performance.iterrows()])}
            </table>
        </div>
        
        <div class="section">
            <h2>User Segmentation</h2>
            
            <h3>Age Group Performance</h3>
            <table>
                <tr><th>Age Group</th><th>Retention Rate</th><th>User Count</th></tr>
                {"".join([f"<tr><td>{age}</td><td>{rate*100:.1f}%</td><td>{df[df['age_group']==age].shape[0]}</td></tr>" for age, rate in age_retention.items()])}
            </table>
            
            <h3>Engagement Segments</h3>
            <table>
                <tr><th>Segment</th><th>User Count</th><th>Retention Rate</th><th>Description</th></tr>
                <tr><td>High Engagement</td><td>{len(high_engagement)}</td><td>{high_engagement['retention_flag'].mean()*100:.1f}%</td><td>5+ clicks & 300s+ sessions</td></tr>
                <tr><td>Low Engagement</td><td>{len(low_engagement)}</td><td>{low_engagement['retention_flag'].mean()*100:.1f}%</td><td>Under 3 clicks or 150s sessions</td></tr>
                <tr><td>At Risk</td><td>{len(low_engagement[low_engagement['retention_flag'] == 0])}</td><td>0%</td><td>Low engagement + not retained</td></tr>
            </table>
            
            <h3>Top Performing Locations</h3>
            <table>
                <tr><th>Location</th><th>Retention Rate</th><th>User Count</th></tr>
                {"".join([f"<tr><td>{loc}</td><td>{rate*100:.1f}%</td><td>{df[df['location']==loc].shape[0]}</td></tr>" for loc, rate in top_locations.items()])}
            </table>
        </div>
        
        <div class="insight">
            <h3>Strategic Recommendations</h3>
            <ol>
                <li><strong>Immediate Rollout:</strong> Deploy Feature A to all users (+{feature_advantage:.1f}% retention gain)</li>
                <li><strong>Targeted Intervention:</strong> Create re-engagement campaign for {len(low_engagement)} low-engagement users</li>
                <li><strong>Network Optimization:</strong> Focus on improving {network_performance['retention_flag'].idxmin()} network performance</li>
                <li><strong>Device Strategy:</strong> Optimize experience for {best_device} users while addressing gaps in other platforms</li>
                <li><strong>Demographic Focus:</strong> Develop content tailored for {best_age_group} age group (highest retention)</li>
            </ol>
        </div>
        
        <div class="section">
            <h2>Complete Analysis Visualization</h2>
            <img src="complete_analysis.png" alt="Complete Analysis Charts" style="width: 100%; border: 1px solid #ddd; border-radius: 8px;">
        </div>
        
        <div style="text-align: center; color: #7f8c8d; margin-top: 40px; padding-top: 20px; border-top: 1px solid #ecf0f1;">
            <p>Complete analysis of {total_users} users across {len(df)} engagement sessions</p>
        </div>
    </body>
    </html>
    """
    
    # FIX: Specify UTF-8 encoding to handle special characters
    with open('complete_analysis_report.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Complete report saved as complete_analysis_report.html")
    
    return {
        'feature_a_retention': feature_a_retention,
        'feature_b_retention': feature_b_retention, 
        'feature_advantage': feature_advantage,
        'total_users': total_users,
        'retention_rate': retention_rate,
        'best_network': best_network,
        'best_device': best_device,
        'best_age_group': best_age_group,
        'high_engagement': len(high_engagement),
        'low_engagement': len(low_engagement)
    }

# RUN THE OPTIMIZED COMPLETE ANALYSIS
df = pd.read_csv('user_engagement_data.csv')
results = optimized_complete_analysis(df)

print("\n" + "="*60)
print("COMPLETE ANALYSIS RESULTS")
print("="*60)
print(f"Total Users Analyzed: {results['total_users']}")
print(f"Overall Retention Rate: {results['retention_rate']:.1f}%")
print(f"Feature A Performance: {results['feature_a_retention']:.1f}%")
print(f"Feature B Performance: {results['feature_b_retention']:.1f}%")
print(f"Performance Advantage: {results['feature_advantage']:+.1f}%")
print(f"Best Performing Network: {results['best_network']}")
print(f"Best Performing Device: {results['best_device']}")
print(f"Best Age Group: {results['best_age_group']}")
print(f"Low Engagement Users: {results['low_engagement']}")
print(f"High Engagement Users: {results['high_engagement']}")
print("="*60)
print("All data preserved! Check complete_analysis.png and complete_analysis_report.html")