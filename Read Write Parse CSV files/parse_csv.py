import csv
 
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # csv_reader contains all an object which contains all data
    # to see data of csv reader as list  we can do this
    # for line in csv_reader:
        # print(line)

    # to skip first line which contains field headers
    # next(csv_reader)

    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

    

    
