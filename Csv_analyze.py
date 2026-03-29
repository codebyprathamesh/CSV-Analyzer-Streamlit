import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="CSV Analyzer", layout="wide")

st.title("📊 CSV Analyzer")
st.markdown("Upload your dataset and explore insights automatically 🚀")

uploaded_csv = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    with st.expander("⚠️ Missing Values"):
        ser = df.isnull().sum()
        for i in range(len(ser)):
            if ser.iloc[i] > 0:
                st.write(f"{ser.index[i]} → {ser.iloc[i]} missing values")

    with st.expander("📈 Statistical Description"):
        st.dataframe(df.describe())

    threshold = 10
    categorical = []
    numerical = []

    for col in df.columns:
        if df[col].dtype == 'object':
            categorical.append(col)
        else:
            if df[col].nunique() > threshold:
                numerical.append(col)
            else:
                categorical.append(col)

    new_numerical = []
    for col in numerical:
        if df[col].nunique() != len(df):
            new_numerical.append(col)
    numerical = new_numerical

    st.subheader("📊 Categorical Analysis")

    cols = st.columns(2)

    for i in range(len(categorical)):
        if df[categorical[i]].nunique() <= 10:
            with cols[i % 2]:
                plt.figure()
                sns.countplot(x=df[categorical[i]])
                plt.title(f"{categorical[i]}")
                plt.xticks(rotation=45)
                st.pyplot(plt)
                plt.close()

    st.subheader("📉 Numerical Analysis")

    cols = st.columns(2)

    for i in range(len(numerical)):
        if df[numerical[i]].nunique() == len(df):
            continue

        if pd.api.types.is_numeric_dtype(df[numerical[i]]):
            with cols[i % 2]:
                plt.figure()
                sns.histplot(x=df[numerical[i]])
                plt.title(f"{numerical[i]}")
                st.pyplot(plt)
                plt.close()

    st.subheader("🔗 Bivariate Analysis")

    col1, col2 = st.columns(2)

    with col1:
        selected_cat = st.selectbox("Categorical", categorical)

    with col2:
        selected_num = st.selectbox("Numerical", numerical)

    plt.figure()
    sns.boxplot(x=df[selected_cat], y=df[selected_num])
    plt.title(f"{selected_cat} vs {selected_num}")
    st.pyplot(plt)
    plt.close()

    st.subheader("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['number'])
    target = numeric_df.columns[-1]

    plt.figure(figsize=(8,6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    st.pyplot(plt)
    plt.close()

    st.subheader("💡 Insights")

    if target in numeric_df.columns:
        corr = numeric_df.corr()[target].sort_values(ascending=False)

        for col in corr.index:
            if col == target:
                continue

            if df[col].nunique() == len(df):
                continue

            value = corr[col]

            if abs(value) > 0.2:
                if value > 0:
                    st.success(f"{col} increases {target}")
                else:
                    st.error(f"{col} decreases {target}")
    else:
        st.warning("Target column is not numeric. Cannot generate insights.")