import csv

def add_proportions(csv_filename, new_filename):

    with open(csv_filename) as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        header = reader.fieldnames
        data = list(reader)

    count_sum = 0

    for row in data:
        count_sum += int(row['count'])

    for row in data:
        prop = int(row['count']) / count_sum * 100
        row['proportion'] = round(prop, 2)

    new_header = header + ['proportions']

    with open(new_filename, 'w') as new_file:
        writer = csv.DictWriter(new_file, new_header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

