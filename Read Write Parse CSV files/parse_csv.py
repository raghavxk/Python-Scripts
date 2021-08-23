import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # to read contents of csv file as dictionary rather than list use this
    # csv_reader = csv.DictReader(csv_file)

    # csv_reader contains all an object which contains all data
    # to see data of csv reader as list  we can do this
    # for line in csv_reader:
    # print(line)

    # to skip first line which contains field headers
    # next(csv_reader)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        # follwing code can be used to write to csv files as dictionaries
        # field_names = ['first_name','second_name','email']
        # csv_writer=csv.DictWriter(new_file,fieldnames=field_names,delimiter="\t")
        
        # to write field headers in csv file following line can be added
        # csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)
