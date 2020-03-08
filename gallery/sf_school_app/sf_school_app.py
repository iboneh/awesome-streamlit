"""
## SkillFactor Shooll Projects

DESCRIPTION

Author: [YOUR NAME](https://URL_TO_YOU))\n
Source: [Github](https://github.com/URL_TO_CODE)
"""
import streamlit as st
import pandas as pd
import numpy as np

DATE_COLUMN = 'date'
DATA_URL = ('src/calls.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

def main():
    st.title("SkillFactor Shooll Projects")
    st.markdown("DESCRIPTION")

if __name__ == "__main__":
    main()
