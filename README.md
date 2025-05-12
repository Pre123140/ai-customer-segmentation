# AI-Powered Customer Segmentation (Basic Version)

A beginner-friendly machine learning project that applies **K-Means Clustering** to segment mall customers based on their income and spending patterns. Ideal for marketers, analysts, and students learning unsupervised learning, this project builds a complete pipeline from preprocessing to visualization and delivers cluster insights in an actionable format.

---

## Project Objective

* Cluster customers using K-Means to identify hidden patterns
* Explore how annual income and spending score relate to customer behavior
* Analyze and interpret the segments formed for marketing or business strategy
* Export clear and interpretable outputs to drive persona-based insights

---

## Key Features

* **Elbow Method** – Determine optimal number of clusters (K) based on WCSS
* **StandardScaler** – Normalize income and spending data
* **KMeans Clustering** – Segment customers using income and spending score
* **Cluster Labeling** – Assign cluster numbers and interpret behavior
* **Data Export** – Save results as .csv and .xlsx for reuse
* **Visual Table Output** – Tabular summaries embedded into analysis

---

## Conceptual Study

Want to dive deeper into the why and how?
👉 [Explore the Conceptual Study](https://github.com/Pre123140/Customer_Segmentation/blob/main/Customer_Segmentation_Study.pdf) (coming soon)

---

## Tech Stack

* **Python** – Core scripting and modeling
* **Pandas** – Data cleaning and manipulation
* **Matplotlib** – Elbow curve and cluster visuals
* **scikit-learn** – KMeans clustering and preprocessing
* **IPython.display** – Clean table displays in notebooks
* **Excel/CSV** – Export results for analysis

---

## Folder Structure

```
Customer_Segmentation/
├── customer_segmentation.py               # Main script with all steps
├── Mall_Customers.csv                    # Raw input data
├── cluster_counts.csv                    # Output: customer count per cluster
├── cluster_summary.csv                   # Output: average values per segment
├── Customer_Segmentation_Results.xlsx    # Output: labeled customer clusters
├── requirements.txt                      # Python dependencies
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Pre123140/Customer_Segmentation
cd Customer_Segmentation
```

### 2. Set Up the Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Execute the Script

```bash
python customer_segmentation.py
```

All processed cluster insights will be saved in:

* `cluster_summary.csv`
* `cluster_counts.csv`
* `Customer_Segmentation_Results.xlsx`

---

## Project Highlights

* ✅ Full preprocessing pipeline: encode, scale, deduplicate
* ✅ Uses elbow method to choose best K
* ✅ Cluster visualization and statistical summaries
* ✅ Cluster interpretation with labels like "High Earners – Low Spending"
* ✅ Clean export of insights for external analysis or marketing strategy

---
## License

This project is open for educational use only. For commercial deployment, contact the author.

---

## Contact
If you'd like to learn more or collaborate on projects or other initiatives, feel free to connect on [LinkedIn](https://www.linkedin.com/in/prerna-burande-99678a1bb/) or check out my [portfolio site](https://youtheleader.com/).
