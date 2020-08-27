import pandas as pd
import argparse

# Code to add the command line interface
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--datafile", required=True, help="data file ")
args = vars(parser.parse_args())

#Catching the user defined data file
data_file = args['datafile']

#Logic to make sure it is a data file.A data file ends with .dat extension

if data_file.endswith(".dat"):
    
    #Storing the name of the file
    file_name = data_file.split(".")[0]

    #Collecting data of the file in a pandas object
    data_of_the_file = pd.read_csv(data_file, sep="\s+")

    #Converting the pandas object into a csv
    data_of_the_file.to_csv(file_name+".csv", index=False)
    print("Your csv file has been created successfully!!!")
else:
    print("Invalid data file")

#Sample Input-Output:

#Input(At the command line): python dat_to_csv -l awesome.dat
#Output: awesome.csv
