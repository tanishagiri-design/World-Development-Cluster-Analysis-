import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🌍 Global Development Clustering Dashboard")

try:
    # Load processed data
    df = pd.read_csv("cluster_results.csv")

    cluster_option = st.selectbox(
        "Select Clustering Method",
        ['KMeans_Cluster', 'Hierarchical_Cluster', 'DBSCAN_Cluster']
    )

    st.write("### Cluster Visualization")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='PC1', y='PC2', hue=cluster_option, data=df, palette='tab10')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

    st.write("### Cluster Summary")

    # Select only numeric columns for mean aggregation
    numeric_cols = df.select_dtypes(include='number').columns
    summary = df.groupby(cluster_option)[numeric_cols].mean()

    st.dataframe(summary)

    st.write("### Cluster Counts")
    counts = df[cluster_option].value_counts().rename_axis(cluster_option).reset_index(name='Counts')
    st.dataframe(counts)

except FileNotFoundError:
    st.error("❌ cluster_results.csv file not found. Please place it in the same folder as app.py.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

