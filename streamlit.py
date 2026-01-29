import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="(Change this)Dashboard", layout="wide")
st.title("Online Transactions Dashboard")

@st.cache_data
def load_dataset():
    df = pd.read_csv("datasets/clean_dataset.csv")
    return df

df = load_dataset()

### Side bar START
st.sidebar.header("Filters")


### Side bar END

###


###

### Tabs Start
tab1, tab2, tab3, tab4, tab5 = st.tabs(["EDA","Revenue Analysis", "Customer Behaviour Analysis", "Purchase Analysis", "Findings"])

### Tabs End

### Raw DataFrame Start
with st.expander("Show Raw data"):
    st.dataframe(df, use_container_width=True)


### Raw DataFrame End

