import requests
import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define constants
chunk_urls = [f"http://10.8.1.151:{5001 + i}/pi_x" for i in range(63)]
d32 = {1: 1716290000.0, 2: 4052700000.0, 3: 11481400000.0, 4: 34845500000.0,
       5: 58209600000.0, 6: 81573700000.0, 7: 149377000000.0, 8: 383018000000.0,
       9: 616659000000.0, 10: 850300000000.0, 11: 1839400000000.0, 12: 4175810000000.0,
       13: 6512220000000.0, 14: 8848630000000.0, 15: 21850300000000.0, 16: 45214400000000.0,
       17: 205699000000000.0, 18: 439340000000000.0, 19: 672981000000000.0, 20: 906622000000000.0,
       21: 2402620000000000.0, 22: 4739030000000000.0, 23: 7075440000000000.0, 24: 9411850000000000.0,
       25: 27482500000000000.0, 26: 50846600000000000.0, 27: 74210700000000000.0, 28: 97574800000000000.0,
       29: 309388000000000000.0, 30: 543029000000000000.0, 31: 776670000000000000.0, 32: 1e+26}
d16 = {1: 4052710000.0, 2: 34845700000.0, 3: 81574000000.0, 4: 383022000000.0, 5: 850305000000.0,
       6: 4175870000000.0, 7: 8848700000000.0, 8: 45215200000000.0, 9: 439349000000000.0,
       10: 906632000000000.0, 11: 4739140000000000.0, 12: 9411970000000000.0, 13: 5.08479e+16,
       14: 9.75762e+16, 15: 5.43044e+17, 16: 1e+26}
d4 = {1: 83024000000, 2: 45215600000000, 3: 9412030000000000, 4: 1e+26}
d8 = {1: 34845800000.0, 2: 383024000000.0, 3: 4175900000000.0, 4: 45215600000000.0,
      5: 906637000000000.0, 6: 9412030000000000.0, 7: 9.75769e+16, 8: 1e+26}
d2 = {1: 45215700000000, 2: 1e+26}

def find_chunk(x, c):
    if c == 1:
        return 0
    d = {}
    if c == 2:
        d = d2
    elif c == 4:
        d = d4
    elif c == 8:
        d = d8
    elif c == 16:
        d = d16
    else:
        d = d32

    for i in range(1, len(d) + 1):
        if x <= d[i]:
            return i - 1
    return -1

def get_pi_x(x, c):
    chunk_index = find_chunk(x, c)
    if chunk_index < 0 or chunk_index > 32:
        raise ValueError(f"x = {x} is out of range.")
    if c == 32:
        url = 30
    elif c == 16:
        url = 14
    elif c == 8:
        url = 6
    elif c == 4:
        url = 2
    elif c == 2:
        url = 0
    else:
        url = 62
    response = requests.get(chunk_urls[url + chunk_index], params={'x': x, 'chunk_index': chunk_index + 1})
    
    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"Error in fetching π({x}) from {url}: {response.status_code}")

# Streamlit app
st.title("Pi Function Calculator")

st.sidebar.header("Settings")
x_input = st.sidebar.number_input("Enter a value for x:", min_value=1.0, step=0.1)
c = st.sidebar.selectbox("Select cluster size:", [1, 2, 4, 8, 16, 32])

if st.sidebar.button("Calculate"):
    #st.sidebar.write("Calculating...")
    s = time.time()
    try:
        result = get_pi_x(x_input, c)
        elapsed_time = time.time() - s
        st.sidebar.success(f"π({x_input}) = {result}")
        st.sidebar.write(f"Calculation Time: {elapsed_time:.2f} seconds")
        


        
    except Exception as e:
        st.sidebar.write(f"")

st.write("### Instructions")
st.write("1. Enter a value for x in the sidebar.")
st.write("2. Select the cluster size.")
st.write("3. Click 'Calculate' to get the result.")

