## Import Things
import pandas as pd
import numpy as np

## Get Data
years = [0]*(2022-1918)
for i in range(1918, 2022):
    years[i-1918] = i 

years