# Importing the required libraries
import xml.etree.ElementTree as ET
import pandas as pd
import os

""" Defining main variables """

#Head
cols = ["Write the heads of your CSV File separatad to commas"]

# Rows of my csv file
rows = []

# Files Dir
dir = os.chdir(r"files")

# List with the files that are inside my directory
listFiles = os.listdir(dir)

# Parsing the XML files in loop
for a in listFiles:
	tree = ET.parse(a)
	root = tree.getroot()

	#Get Variables
	variables = root["Put here the index that you need"].text

	#Print Values
	print("Waiting while i'm getting values of xml: " + {a})

	#Append Rows in CSV
	rows.append({"Header[1]": variables})

	#Create a dataframe
	df = pd.DataFrame(rows, columns=cols)

	#Writing dataframe to csv
	df.to_csv('xml-to-csv.csv')


