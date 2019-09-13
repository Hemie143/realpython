import csv
import os
import argparse

def file_exists(filename):
    if os.path.exists(filename):
        return True
    return False

def valid_rows(filename, rows):
    with open(filename, "r") as f:
        out = f.readlines()
        if len(out) > rows:
            return True
    return False

parser = argparse.ArgumentParser(description='Split a CSV file.')
parser.add_argument('-i', dest='input', action='store', default='samples.csv')
parser.add_argument('-o', dest='output', action='store', default='output')
parser.add_argument('-r', dest='row_limit', action='store', type=int, default=25)
args = parser.parse_args()

input_file = args.input
output = args.output
row_limit = args.row_limit

if not (file_exists(input_file) and valid_rows(input_file, row_limit)):
    print('Invalid data')
    exit()


with open(input_file, "r") as csv_file:
    file_reader = csv.reader(csv_file)
    header = next(file_reader)
    chunk_number = 0
    while True:
        chunk = []
        chunk_number += 1
        out_filename = f'{output}_{chunk_number:03d}.csv'
        for _ in range(row_limit):
            try:
                row = next(file_reader)
                chunk.append(row)
            except:
                pass
        if len(chunk) > 0:
            with open(out_filename, 'w') as out_file:
                file_writer = csv.writer(out_file)
                file_writer.writerow(header)
                file_writer.writerows(chunk)
                print(f'{out_filename}: {len(chunk)} rows')
                if len(chunk) < row_limit:
                    break
        if len(chunk) < row_limit:
            break
            # print(f'Chunk length: {len(chunk)}')
        # print(f'i: {i}')
