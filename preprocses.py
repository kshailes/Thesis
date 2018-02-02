import re
import pandas as pd
import numpy as np
directory = '/home/shailesh/mission'

def preprocess():

	#reading file
	dir_name = directory + '/emailscandals/'
	raw_data = pd.DataFrame()
	