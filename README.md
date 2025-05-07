# customer_segmentation
Customer segmentation using RFM analysis in Python
# 🧠 Customer Segmentation Project (RFM Analysis)

This project applies **RFM (Recency, Frequency, Monetary)** analysis to segment customers based on their purchasing behavior using a real-world sales dataset.

## 📌 Objective
Identify valuable customer segments (e.g., Champions, Loyal Customers, At Risk, etc.) for targeted marketing strategies.

## 🛠 Tools & Libraries
- Python
- Pandas
- Matplotlib & Seaborn
- RFM (Recency, Frequency, Monetary) Framework

## 📊 RFM Metrics
- **Recency**: Days since last purchase
- **Frequency**: Number of purchases
- **Monetary**: Total amount spent

## 🔍 Steps Performed
1. Data Cleaning & Preprocessing
2. RFM Metric Calculation
3. Quartile Assignment for RFM values
4. RFM Scoring (e.g., 111, 234, etc.)
5. Customer Segmentation based on RFM Score
6. Data Visualization using bar plots and pie chart
7. Exported segmented data to CSV

## 📂 Output Sample

| CustomerID | RFM_Score | Segment               |
|------------|-----------|------------------------|
| 12346      | 113       | Others                 |
| 12347      | 323       | Champion               |
| 12350      | 111       | Lost Customer          |

- RFM table with scores and segments
- Bar plot of customer segments
- pie chart of customer segments

## 📌 Key Segments
- **Champion**: Recently purchased, frequent, high spending
- **Loyal Customer**: Frequent buyers, good spending
- **Potential Loyalist**: Not very recent but engaged
- **At Risk / Lost**: Long since last purchase

## 📈 Visual Insights
Includes plots for:
- Count of Customers per Segment
- Frequency & Monetary distributions

## 💡 Business Use Case
This segmentation can help businesses:
- Improve retention through personalized offers
- Reactivate at-risk or lost customers
- Focus promotions on loyal and champion buyers

---

## 👩‍💻 Author
Shweta Ashok Swain


