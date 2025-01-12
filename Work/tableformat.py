# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
        
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print('<tr><th>' + '</th><th>'.join(headers) + '</th></tr>')
    
    def row(self, rowdata):
        print('<tr><td>' + '</td><td>'.join(rowdata) + '</td></tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Create a formatter object as specified
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')

def print_table(portfolio, columns, formatter):
    formatter.headings(columns)
    
    for s in portfolio:
        rowdata = [ str(getattr(s, colname)) for colname in columns ]
        formatter.row(rowdata)