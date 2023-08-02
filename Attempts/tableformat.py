def print_table(records, fields):
    '''
    Create a new module called tableformat.py. In that program, write a function 
    print_table() that takes a sequence (list) of objects, a list of attribute 
    names, and prints a nicely formatted table. For example:
    '''
    print(' '.join('%10s' % fieldname for fieldname in fields))
    print(('-'*10 + ' ')*len(fields))
    for record in records:
        print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))