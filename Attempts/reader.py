import csv

def read_csv_as_dicts(filename, type_conversions):
    """
    Create a new file reader.py. In that file, define a utility function 
    read_csv_as_dicts() that reads a file of CSV data into a list of dictionaries
    where the user specifies the type conversions for each column.

    see ex2_6.md for how this works
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {headers:func(val) for headers, func, val in zip(headers, type_conversions, row) }
            records.append(record)
    return records