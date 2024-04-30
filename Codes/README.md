# Repository Overview

This repository contains the code for the vector operations project, focusing on photon correlation for a two-qubit system using a one-dimensional detector. The code is divided into several Jupyter notebooks detailing different stages of the development process, as well as a deployment script for local testing.

## Repository Structure

- **DC_initial_approach.ipynb**: 
  - This notebook includes the initial approach to the problem, which involves basic vector operations without optimizations.

- **DC_improved.ipynb**: 
  - This notebook presents an improved version of the initial code, incorporating chunked processing to enhance performance and reduce computational time overhead.

- **DC_final.ipynb**: 
  - This notebook contains the final, optimized code that is ready for deployment. It includes all the enhancements and final touches needed for efficient operation.

- **app.py**: 
  - This Python script is set up for deploying the application on a localhost. It serves the final model and allows for interaction via a simple web interface.

# Deployment Instructions for Streamlit Application

To deploy the Streamlit application on your local machine, please follow these specific steps:

1. **Clone the Repository**:
   - If you haven't already, clone the repository to your local machine using:
     ```
     git clone https://github.com/your-github-username/your-repository-name.git
     ```
   - Navigate to the repository directory:
     ```
     cd your-repository-name
     ```

2. **Install Required Packages**:
   - Ensure that you have Python installed by running `python --version` in your command line or terminal. If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).
   - Install Streamlit and other necessary packages using pip:
     ```
     pip install streamlit numpy pandas matplotlib
     ```

3. **Run the Streamlit Application**:
   - Start the application by running the following command in your terminal:
     ```
     streamlit run app.py
     ```
   - This command will start the Streamlit server and typically opens your default web browser automatically. If it does not, it will provide a local URL you can visit, typically `http://localhost:8500`.

4. **Access the Application**:
   - If your browser does not open automatically, open a web browser and go to `http://localhost:8500` to access the application.
   - Interact with the application through the Streamlit interface.



