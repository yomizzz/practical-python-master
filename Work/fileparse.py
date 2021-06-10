# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = ',', silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')
    '''   
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        
        # Read the file headers if there are headers in CSV file
        if has_headers:
            headers = next(rows)
        else:
            headers = []
        
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
                
        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:  # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices]
            # Type-conversions
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    # 默认是显示错误信息，只有当调用者要求不显示时，才会跳过打印错误信息
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
                    
            # Making a dictionary if there are headers in CSV file, else Making a tuple
            if has_headers:
                record = dict(zip(headers, row)) # data in dict are all str type
            else:
                record = tuple(row)
                
            records.append(record)
            
    return records
   
