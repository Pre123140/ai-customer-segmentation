import pandas as pd

# Load the dataset
file_path = "Mall_Customers.csv"  # Ensure this matches your file name
df = pd.read_csv(file_path)

# Display first few rows
print(df.head())
# Basic info about the dataset
print(df.info())

# Check for missing values
print("\nMissing values in each column:\n", df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:\n", df.describe())

# Display column names
print("\nColumn Names:", df.columns)
df = df.drop(columns=["CustomerID"])  # Drop CustomerID since it's not useful for clustering
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
df = df.drop_duplicates()
print("Duplicates removed!")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 6.1: Select relevant features
features = ["Annual Income (k$)", "Spending Score (1-100)"]  # Modify if needed
X = df[features]

# Step 6.2: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6.3: Find the optimal K using the Elbow Method
wcss = []
for k in range(1, 11):  # Testing K values from 1 to 10
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method to Find Optimal K")
plt.show()
from sklearn.preprocessing import StandardScaler

# Select only the numeric columns for clustering
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
data = df[numeric_columns]

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)  # This creates 'scaled_data'
# Import KMeans
from sklearn.cluster import KMeans

# Apply K-Means with the optimal number of clusters (replace 'k' with the number from the elbow method)
k = 3  # Change this based on your elbow plot
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize the clusters using a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(scaled_data[:, 0], scaled_data[:, 1], c=df['Cluster'], cmap='viridis', alpha=0.5)
plt.xlabel(numeric_columns[0])
plt.ylabel(numeric_columns[1])
plt.title("Customer Segmentation")
plt.colorbar(label="Cluster")
plt.show()
# Analyze the cluster centers
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=numeric_columns)
cluster_centers
# Add cluster labels to the original dataset
df['Cluster'] = kmeans.labels_

# Compute average values per cluster
cluster_summary = df.groupby('Cluster').mean()
cluster_summary
# Create a summary table with mean values per cluster
cluster_summary = df.groupby('Cluster').mean()
cluster_summary
# Count the number of customers in each cluster
cluster_counts = df['Cluster'].value_counts().reset_index()
cluster_counts.columns = ['Cluster', 'Number of Customers']
cluster_counts
# Format the table for readability
cluster_summary.round(2)
print(df.head())  # Show first few rows
print(df.groupby('Cluster').mean())  # Summary table
print(df['Cluster'].value_counts())  # Count per cluster
from IPython.display import display  # Only needed for Jupyter Notebook

# Display cluster summary with mean values
display(df.groupby('Cluster').mean())

# Display count of customers per cluster
display(df['Cluster'].value_counts().to_frame().rename(columns={'Cluster': 'Number of Customers'}))
df.groupby('Cluster').mean().to_csv("cluster_summary.csv")
df['Cluster'].value_counts().to_csv("cluster_counts.csv")
cluster_summary = pd.DataFrame({
    "Cluster": ["Older Budget-Conscious", "High Earners - Low Spending", "Young & High Spenders"],
    "Avg Age": [52, 40, 28],
    "Avg Income ($K)": [46, 91, 59],
    "Avg Spending Score": [39, 20, 69]
})

# Display table in VS Code
print(cluster_summary)

# Plot the cluster summary for better understanding
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('tight')
ax.axis('off')
table_data = cluster_summary.values
table = ax.table(cellText=table_data, colLabels=cluster_summary.columns, cellLoc='center', loc='center')

plt.show()
# Convert the cluster summary to a DataFrame
cluster_summary.to_excel("Customer_Segmentation_Results.xlsx", index=True)

print("Excel file saved successfully!")  