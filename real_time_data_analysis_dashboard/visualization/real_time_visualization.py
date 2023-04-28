python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title='Real-time Data Analysis Dashboard - Visualization')

# Load real-time data
data = pd.read_csv('../data/real_time_data.csv')

# Create a line chart
fig, ax = plt.subplots()
ax.plot(data['timestamp'], data['value'])
ax.set_title('Real-time Data Analysis Dashboard')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Value')

# Render the chart using Streamlit
st.pyplot(fig)
