import pandas as pd

# Load data
df = pd.read_excel('Online Retail.xlsx')

# Show first few rows
print(df.head())

# Drop rows with missing CustomerID (very important!)
df = df[pd.notnull(df['CustomerID'])]

# Remove negative/zero quantities (these are returns or invalid)
df = df[df['Quantity'] > 0]

# Remove negative unit prices (refunds or errors)
df = df[df['UnitPrice'] > 0]

# Create a new column for total spend
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print(df[['Quantity', 'UnitPrice', 'TotalPrice']].head())
print("Cleaned data shape:", df.shape)

import datetime as dt

# Set reference date for recency calculation (day after last transaction)
ref_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Group by customer
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (ref_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                              # Frequency
    'TotalPrice': 'sum'                                  # Monetary
})

# Rename columns
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
}, inplace=True)

print(rfm.head())

print(df[['Quantity', 'UnitPrice', 'TotalPrice']].head(10))  # shows 10 rows

# Recency quartile
r_bins = pd.qcut(rfm['Recency'], 4, duplicates='drop')
rfm['R_Quartile'] = pd.qcut(rfm['Recency'], q=r_bins.unique().size - 1, labels=range(r_bins.unique().size - 1, 0, -1), duplicates='drop')

# Frequency quartile
f_bins = pd.qcut(rfm['Frequency'], 4, duplicates='drop')
rfm['F_Quartile'] = pd.qcut(rfm['Frequency'], q=f_bins.unique().size - 1, labels=range(1, f_bins.unique().size), duplicates='drop')

# Monetary quartile
m_bins = pd.qcut(rfm['Monetary'], 4, duplicates='drop')
rfm['M_Quartile'] = pd.qcut(rfm['Monetary'], q=m_bins.unique().size - 1, labels=range(1, m_bins.unique().size), duplicates='drop')

rfm['RFM_Score'] = (
    rfm['R_Quartile'].astype(str) +
    rfm['F_Quartile'].astype(str) +
    rfm['M_Quartile'].astype(str)
)

print(rfm.head())  # Shows the first few rows with R_Quartile, F_Quartile, M_Quartile, and RFM_Score
print("\nUnique RFM Scores:\n", rfm['RFM_Score'].value_counts())


# Define a function to map RFM_Score to customer segments
def segment_customer(rfm):
    score = rfm['RFM_Score']
    if score == '111':
        return 'Lost Customer'
    elif score[0] == '3' and score[1] in '23' and score[2] in '23':
        return 'Champion'
    elif score[0] in '23' and score[1] in '23':
        return 'Loyal Customer'
    elif score[0] in '12' and score[1] in '23':
        return 'Potential Loyalist'
    elif score[0] == '3' and score[1] == '1':
        return 'Recent but Low Frequency'
    elif score[0] == '1' and score[1] == '3':
        return 'Need Attention'
    else:
        return 'Others'

# Apply the function
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# Display sample and segment distribution
print(rfm[['RFM_Score', 'Segment']].head(10))
print("\nSegment counts:\n", rfm['Segment'].value_counts())

import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")

# Bar chart: Segment counts
plt.figure(figsize=(10, 6))
sns.countplot(data=rfm, x='Segment', order=rfm['Segment'].value_counts().index, palette='viridis')
plt.title('Customer Segments Distribution', fontsize=16)
plt.xlabel('Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart (optional)
segment_counts = rfm['Segment'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(segment_counts)))
plt.title('Customer Segment Distribution')
plt.axis('equal')
plt.show()

# Save the final segmented data to CSV
rfm.to_csv('rfm_customer_segments.csv')
print("Segmented customer data saved successfully as 'rfm_customer_segments.csv'")



