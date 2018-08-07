import csv

def read(File):
    open(File, 'rb') as csvfile:
        List = csv.reader(csvfile, delimiter = ';', quotechar = '"')
        return List

def write(File:)
    open(File, 'w+') as csvfile
        