import csv

headers = ['Symbol', 'Price', 'Date', 'Time', 'test']
rows = [
    ('AA', 12, 'abc', '123', 'jj'),
    ('Ad', 12, 'abc', '123', 'jj'),
    ('Ac', 12, 'abc', '123', 'jj'),
    ('Ab', 12, 'abc', '123', 'jj'),
]
path = 'example.csv'


def export_csv(_headers, _rows, _path):
    """
        export_csv with headers rows and path
    """
    with open(_path, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(_headers)
        f_csv.writerows(_rows)


def read_csv(_path):
    """
        read_csv from _path
    """
    rows = []
    with open(_path) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            rows.append(row)
    return rows

# export_csv(headers, rows, path)
# print(read_csv(path)[1]['Symbol'])
