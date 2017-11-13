import csv

headers = ['Symbol', 'Price', 'Date', 'Time', 'test']
rows = [
    ('AA', 12, 'abc', '123', 'jj'),
    ('AA', 12, 'abc', '123', 'jj'),
    ('AA', 12, 'abc', '123', 'jj'),
    ('AA', 12, 'abc', '123', 'jj'),
]
path = 'example.csv'

def export_csv(_headers, _rows, _path):
    with open(_path, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(_headers)
        f_csv.writerows(_rows)

export_csv(headers, rows, path)