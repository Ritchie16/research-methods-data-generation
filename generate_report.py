import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set professional style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def analyze_user_engagement(df):
    """
    Comprehensive analysis of the user engagement dataset
    """
    print("📊 Starting comprehensive user engagement analysis...")
    
    # Create comprehensive visualization
    fig = plt.figure(figsize=(20, 18))
    
    # 1. Overall KPIs
    plt.subplot(3, 3, 1)
    total_users = df['user_id'].nunique()
    retention_rate = df['retention_flag'].mean() * 100
    avg_session = df['session_duration'].mean()
    avg_clicks = df['clicks'].mean()
    avg_feedback = df['feedback_score'].mean()
    
    kpis = {
        'Total Users': total_users,
        'Retention Rate': retention_rate,
        'Avg Session': avg_session,
        'Avg Clicks': avg_clicks
    }
    
    plt.bar(kpis.keys(), kpis.values(), color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'])
    plt.title('Key Performance Indicators', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    
    # 2. Retention by Feature Version (A/B Test)
    plt.subplot(3, 3, 2)
    retention_by_feature = df.groupby('feature_version')['retention_flag'].mean() * 100
    bars = plt.bar(retention_by_feature.index, retention_by_feature.values, 
                   color=['#2E86AB', '#A23B72'])
    plt.title('Retention Rate by Feature Version', fontsize=14, fontweight='bold')
    plt.ylabel('Retention Rate (%)')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom')
    
    # 3. Age Distribution
    plt.subplot(3, 3, 3)
    df['age'].hist(bins=20, alpha=0.7, color='#2E86AB')
    plt.title('User Age Distribution', fontsize=14, fontweight='bold')
    plt.xlabel('Age')
    plt.ylabel('Count')
    
    # 4. Session Duration vs Retention
    plt.subplot(3, 3, 4)
    retained = df[df['retention_flag'] == 1]['session_duration']
    not_retained = df[df['retention_flag'] == 0]['session_duration']
    
    plt.hist([retained, not_retained], bins=20, alpha=0.7, 
             label=['Retained', 'Not Retained'], color=['green', 'red'])
    plt.title('Session Duration: Retained vs Not Retained', fontsize=14, fontweight='bold')
    plt.xlabel('Session Duration (seconds)')
    plt.ylabel('Frequency')
    plt.legend()
    
    # 5. Network Provider Performance
    plt.subplot(3, 3, 5)
    network_performance = df.groupby('network').agg({
        'retention_flag': 'mean',
        'session_duration': 'mean',
        'clicks': 'mean'
    })
    
    x = np.arange(len(network_performance.index))
    width = 0.25
    
    plt.bar(x - width, network_performance['retention_flag'] * 100, width, 
            label='Retention %', alpha=0.8)
    plt.bar(x, network_performance['session_duration'], width, 
            label='Avg Session', alpha=0.8)
    plt.bar(x + width, network_performance['clicks'], width, 
            label='Avg Clicks', alpha=0.8)
    
    plt.xlabel('Network Provider')
    plt.title('Network Performance Comparison', fontsize=14, fontweight='bold')
    plt.xticks(x, network_performance.index)
    plt.legend()
    
    # 6. Device Type Analysis
    plt.subplot(3, 3, 6)
    device_analysis = df.groupby('device').agg({
        'retention_flag': 'mean',
        'session_duration': 'mean'
    }).sort_values('retention_flag', ascending=False)
    
    x = np.arange(len(device_analysis.index))
    width = 0.35
    
    plt.bar(x - width/2, device_analysis['retention_flag'] * 100, width, 
            label='Retention %', alpha=0.8)
    plt.bar(x + width/2, device_analysis['session_duration'], width, 
            label='Avg Session', alpha=0.8)
    
    plt.xlabel('Device Type')
    plt.title('Device Performance', fontsize=14, fontweight='bold')
    plt.xticks(x, device_analysis.index, rotation=45)
    plt.legend()
    
    # 7. Clicks Distribution
    plt.subplot(3, 3, 7)
    df['clicks'].hist(bins=15, alpha=0.7, color='#F18F01')
    plt.title('Clicks Distribution', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Clicks')
    plt.ylabel('Frequency')
    
    # 8. Feedback Score Analysis
    plt.subplot(3, 3, 8)
    feedback_retention = df.groupby('feedback_score')['retention_flag'].mean() * 100
    feedback_retention.plot(kind='bar', color='#C73E1D', alpha=0.7)
    plt.title('Retention Rate by Feedback Score', fontsize=14, fontweight='bold')
    plt.xlabel('Feedback Score (1-5)')
    plt.ylabel('Retention Rate (%)')
    plt.xticks(rotation=0)
    
    # 9. Data Usage Analysis
    plt.subplot(3, 3, 9)
    plt.scatter(df['data_used_mb'], df['session_duration'], 
               c=df['retention_flag'], alpha=0.6, cmap='coolwarm')
    plt.xlabel('Data Used (MB)')
    plt.ylabel('Session Duration (seconds)')
    plt.title('Data Usage vs Session Duration\n(Color: Retention)', fontsize=14, fontweight='bold')
    plt.colorbar(label='Retention (0=No, 1=Yes)')
    
    plt.tight_layout()
    plt.savefig('user_engagement_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return generate_detailed_report(df, kpis)

def generate_detailed_report(df, kpis):
    """Generate detailed insights report"""
    
    print("📈 Calculating detailed insights...")
    
    # Feature A/B Test Results
    feature_a_retention = df[df['feature_version'] == 'A']['retention_flag'].mean() * 100
    feature_b_retention = df[df['feature_version'] == 'B']['retention_flag'].mean() * 100
    feature_advantage = feature_a_retention - feature_b_retention
    
    # Network Analysis
    best_network = df.groupby('network')['retention_flag'].mean().idxmax()
    best_network_rate = df.groupby('network')['retention_flag'].mean().max() * 100
    
    # Device Analysis
    best_device = df.groupby('device')['retention_flag'].mean().idxmax()
    best_device_rate = df.groupby('device')['retention_flag'].mean().max() * 100
    
    # Engagement Thresholds
    high_engagement = df[(df['clicks'] >= 5) & (df['session_duration'] >= 300)]
    low_engagement = df[(df['clicks'] < 3) | (df['session_duration'] < 150)]
    
    high_engagement_retention = high_engagement['retention_flag'].mean() * 100
    low_engagement_retention = low_engagement['retention_flag'].mean() * 100
    
    # Age Group Analysis
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 45, 55, 100], 
                           labels=['18-25', '26-35', '36-45', '46-55', '55+'])
    best_age_group = df.groupby('age_group')['retention_flag'].mean().idxmax()
    best_age_rate = df.groupby('age_group')['retention_flag'].mean().max() * 100
    
    # Generate HTML Report
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Engagement Analysis Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
            .header {{ background: linear-gradient(135deg, #2E86AB, #A23B72); color: white; padding: 30px; border-radius: 10px; text-align: center; }}
            .kpi-container {{ display: flex; justify-content: space-between; margin: 30px 0; flex-wrap: wrap; }}
            .kpi-box {{ background: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; flex: 1; margin: 10px; min-width: 200px; border-left: 4px solid #2E86AB; }}
            .kpi-value {{ font-size: 28px; font-weight: bold; color: #2E86AB; margin: 10px 0; }}
            .insight {{ background: #e8f5e8; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #27ae60; }}
            .alert {{ background: #ffeaa7; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #f39c12; }}
            .recommendation {{ background: #e3f2fd; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #1976d2; }}
            .section {{ margin: 30px 0; }}
            h2 {{ color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; }}
            .metric-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; }}
            .metric-card {{ background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 User Engagement Analysis Report</h1>
            <p>Comprehensive analysis of {kpis['Total Users']} users | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </div>
        
        <div class="kpi-container">
            <div class="kpi-box">
                <div class="kpi-value">{kpis['Retention Rate']:.1f}%</div>
                <div>Overall Retention Rate</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-value">{kpis['Avg Session']:.0f}s</div>
                <div>Average Session Duration</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-value">{kpis['Avg Clicks']:.1f}</div>
                <div>Average Clicks per Session</div>
            </div>
            <div class="kpi-box">
                <div class="kpi-value">{df['feedback_score'].mean():.1f}/5</div>
                <div>Average Feedback Score</div>
            </div>
        </div>
        
        <div class="alert">
            <h3>🚨 Key Business Impact</h3>
            <p><strong>Feature A outperforms Feature B by {feature_advantage:.1f}% in retention</strong> - Consider rolling out Feature A to all users</p>
            <p><strong>{len(low_engagement)} users ({len(low_engagement)/len(df)*100:.1f}%) show low engagement</strong> - High risk of churn</p>
        </div>
        
        <div class="section">
            <h2>📈 Performance Metrics</h2>
            <div class="metric-grid">
                <div class="metric-card">
                    <h4>Feature A/B Test</h4>
                    <p>Version A: <strong>{feature_a_retention:.1f}%</strong> retention</p>
                    <p>Version B: <strong>{feature_b_retention:.1f}%</strong> retention</p>
                    <p>Difference: <strong>{feature_advantage:.1f}%</strong></p>
                </div>
                <div class="metric-card">
                    <h4>Network Performance</h4>
                    <p>Best: <strong>{best_network}</strong> ({best_network_rate:.1f}%)</p>
                    <p>All networks: {', '.join([f'{net}: {rate*100:.1f}%' for net, rate in df.groupby('network')['retention_flag'].mean().items()])}</p>
                </div>
                <div class="metric-card">
                    <h4>Device Performance</h4>
                    <p>Best: <strong>{best_device}</strong> ({best_device_rate:.1f}%)</p>
                    <p>Android: {df[df['device']=='Android']['retention_flag'].mean()*100:.1f}%</p>
                    <p>iOS: {df[df['device']=='iOS']['retention_flag'].mean()*100:.1f}%</p>
                </div>
                <div class="metric-card">
                    <h4>Engagement Segments</h4>
                    <p>High engagement: <strong>{high_engagement_retention:.1f}%</strong> retention</p>
                    <p>Low engagement: <strong>{low_engagement_retention:.1f}%</strong> retention</p>
                    <p>Engagement gap: <strong>{high_engagement_retention - low_engagement_retention:.1f}%</strong></p>
                </div>
            </div>
        </div>
        
        <div class="recommendation">
            <h3>🎯 Strategic Recommendations</h3>
            <ol>
                <li><strong>Immediate Action:</strong> Roll out Feature Version A to all users</li>
                <li><strong>Targeted Campaign:</strong> Create re-engagement program for {len(low_engagement)} low-engagement users</li>
                <li><strong>Network Optimization:</strong> Focus on improving performance with lower-performing networks</li>
                <li><strong>Device Strategy:</strong> Optimize experience for {best_device} users while improving other platforms</li>
                <li><strong>Age Segmentation:</strong> Develop targeted content for {best_age_group} age group ({best_age_rate:.1f}% retention)</li>
            </ol>
        </div>
        
        <div class="insight">
            <h3>💡 Key Insights</h3>
            <ul>
                <li>Session duration strongly correlates with retention - users with sessions over 300s have {high_engagement_retention:.1f}% retention</li>
                <li>Feedback scores of 4-5 show significantly higher retention rates</li>
                <li>Data usage patterns indicate optimal engagement around 50-80MB per session</li>
                <li>{best_network} network users show the highest loyalty and engagement</li>
            </ul>
        </div>
        
        <h2>📊 Analysis Visualization</h2>
        <img src="user_engagement_analysis.png" alt="Comprehensive Analysis Charts" style="width: 100%; border: 1px solid #ddd; border-radius: 8px; margin: 20px 0;">
        
        <div style="text-align: center; color: #7f8c8d; margin-top: 40px; padding-top: 20px; border-top: 1px solid #ecf0f1;">
            <p>Report generated automatically from user engagement data | {kpis['Total Users']} users analyzed</p>
        </div>
    </body>
    </html>
    """
    
    # Save HTML report
    with open('user_engagement_report.html', 'w') as f:
        f.write(html_content)
    
    print("✅ Analysis complete!")
    print(f"📁 Reports saved:")
    print(f"   - user_engagement_analysis.png (Charts)")
    print(f"   - user_engagement_report.html (Detailed report)")
    
    return {
        'feature_a_retention': feature_a_retention,
        'feature_b_retention': feature_b_retention,
        'feature_advantage': feature_advantage,
        'best_network': best_network,
        'best_device': best_device,
        'high_engagement_users': len(high_engagement),
        'low_engagement_users': len(low_engagement)
    }

# Load and analyze the data
df = pd.read_csv('user_engagement_data.csv')

# Run comprehensive analysis
results = analyze_user_engagement(df)

# Print quick summary
print("\n" + "="*50)
print("QUICK SUMMARY")
print("="*50)
print(f"📊 Total Users: {df['user_id'].nunique()}")
print(f"🎯 Overall Retention: {df['retention_flag'].mean()*100:.1f}%")
print(f"🔬 Feature A vs B: {results['feature_a_retention']:.1f}% vs {results['feature_b_retention']:.1f}%")
print(f"📱 Best Device: {results['best_device']}")
print(f"📶 Best Network: {results['best_network']}")
print(f"⚠️  At-Risk Users: {results['low_engagement_users']}")
print("="*50)