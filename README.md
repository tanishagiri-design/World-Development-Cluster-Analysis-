🌍 World Development Cluster Analysis
This project performs clustering on global socio-economic development data using multiple machine learning techniques. The goal is to group countries based on key development indicators and uncover meaningful global patterns.
🚀 Project Overview
The dataset contains 2,708 observations and 25 development metrics, including birth rate, GDP, CO₂ emissions, healthcare spending, energy usage, internet penetration, and business environment factors.
The workflow involves:
Exploratory Data Analysis (EDA)
Handling missing values
Feature scaling
Dimensionality reduction (PCA)
Clustering with K-Means, DBSCAN & Hierarchical Clustering
Evaluation using Silhouette Score
Deployment on Streamlit
📊 Techniques Used
🔹 Preprocessing
Handled 12,203 missing values
Heatmap visualization of missing data
Mean/median imputation based on distribution
Standard scaling of features
🔹 Dimensionality Reduction
Used PCA, selecting 15 components explaining 95%+ variance.
🔹 Clustering Models
Model	Notes	Best Silhouette Score
K-Means	Tried 2–4 clusters & PCA variants	~0.38
DBSCAN	Used nearest-neighbor for eps	~0.23
Hierarchical	Dendrogram + scatter visualization	~0.40
🛠️ Tech Stack
Python
Pandas, NumPy, Scikit-learn
Seaborn, Matplotlib
Streamlit
PCA, K-Means, DBSCAN, Hierarchical Models
🖥️ Deployment
A fully interactive Streamlit app is built to:
✔ Visualize clusters
✔ Explore country-level development patterns
✔ Understand what defines each cluster
📚 Learnings
Preprocessing large socio-economic datasets
Understanding multi-variable relationships
Applying and comparing clustering algorithms
Evaluating performance with silhouette scores
Deploying ML models for real-time exploration
🔮 Future Scope
Add time-series development indicators
Include governance & environmental metrics
Explore Gaussian Mixture Models & Spectral Clustering
Build supervised ML for development predictio
