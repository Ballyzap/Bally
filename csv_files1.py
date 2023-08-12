import csv
with open('employees.csv') as f:
    csv_reader = csv.reader(f, delimiter = ',')
    love = 0
    for benz in csv_reader:
        if love == 0:
            print(f'Column names are {", "}.join(benz)')
            love += 1
        else:
            print(f'\t{benz[0]} works in the {benz[1]} departments, and was born in {benz[2]}.')
            love += 1
    print(f'processed {love} lines.')