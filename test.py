
import csv;

#reader = csv.reader(['1997,Ford,E350,"Super, luxurious truck"'], skipinitialspace=True)
#for r in reader:
#    print(r)

with open('data/test.csv') as csvf:
    reader = csv.reader(csvf, skipinitialspace=True)
    for r in reader:
        r[6] = ''.join(' ' if c == '\n' or c == '\t' else c for c in r[6])
        print(len(r))
        print(r)
