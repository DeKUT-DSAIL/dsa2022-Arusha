# IoT Data Processing - DSA 2022

This repo contains material to be used for the DSAIL session at DSA 2022. During the session we will discuss the acquisition and processing of data from internet of things (IoT) devices. In particular we will focus on:
* Camera trap image processing
* Outlier detection for time series data

## Instructions on installing requirements for windows.

### A. Using anaconda 
1. Download and install [Anaconda](https://www.anaconda.com/products/distribution) for your machine.

2. Open Anaconda prompt

3. Clone this repository and cd into it

4.  Create enviroment `conda create --name iot-env`

5. Access environment `conda activate iot-env`

6. Installl requirements `pip install -r requirements.txt`

7. Launch jupyter `jupyter notebook`

### B. Using pip 
1. Clone this repository and cd into it
2. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
 `python -m venv iot-env`
3. Activate it
`.\iot-env\Scripts\activate.bat`
4. Update pip `pip install --upgrade pip`
5. Install the requirements
`pip install -r requirements.txt`
6. Launch `jupyter notebook`

