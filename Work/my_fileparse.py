# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(input, types=None, select=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    rows = csv.reader(input, delimiter=delimiter)
    
    if has_headers:
        # Read the file headers
        headers = next(rows)
    
    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        if not has_headers:
            raise RuntimeError("select argument requires column headers")
        indices = [ headers.index(colname) for colname in select ]
        headers = select
    else:
        indices = []
    
    records = []
    for rowno, row in enumerate(rows, 1):
        if not row: # Skip rows with no data
            continue
        
        try:
            if indices:
                row = [ row[index] for index in indices ]
            
            if types:
                row = [ func(val) for func, val in zip(types, row) ]
                
            # Make a dictionary, but only if there are column names
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
        except ValueError as e:
            if not silence_errors:
                print(f"Row {rowno}: Couldn't convert {row}")
                print(f"Row {rowno}: Reason {e}")
        
        records.append(record)
            
    return records