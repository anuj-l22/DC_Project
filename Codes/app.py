import streamlit as st
import numpy as np
import pandas as pd
import time

def rotate_and_operate_chunked(vec1, vec2, chunk_size=10000, verbose=False):
    n = len(vec1)
    result_vector = np.empty(n * n, dtype='float32')
    for start in range(0, n, chunk_size):
        end = min(start + chunk_size, n)
        chunk_length = end - start
        temp_result = np.empty((chunk_length, n), dtype='float32')
        for i in range(chunk_length):
            rotated_vec1 = np.roll(vec1, start + i)
            temp_result[i, :] = rotated_vec1 - vec2
        result_vector[start*n:(start + chunk_length)*n] = temp_result.flatten()
    return result_vector

# Streamlit user interface
st.title('Data Vector Operation Web App')
st.write('This application processes a CSV file based on user input and returns a sorted result.')

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    num_rows = st.number_input("Enter the number of rows to process:", min_value=1, value=10000)
    
    if st.button('Process'):
        # Read the uploaded file
        df = pd.read_csv(uploaded_file, usecols=[0, 1], nrows=num_rows)
        vec1 = df.iloc[:, 0].values.astype('float32')
        vec2 = df.iloc[:, 1].values.astype('float32')

        start_time = time.time()
        result_vector = rotate_and_operate_chunked(vec1, vec2, verbose=True)
        sorted_vector = np.sort(result_vector)
        end_time = time.time()

        # Convert the sorted array back to DataFrame to display and download
        sorted_df = pd.DataFrame(sorted_vector, columns=['Sorted Results'])
        
        st.write(f"Processed in {end_time - start_time:.2f} seconds.")
        st.download_button(label="Download sorted results as CSV",
                           data=sorted_df.to_csv(index=False).encode('utf-8'),
                           file_name='sorted_results.csv',
                           mime='text/csv')
