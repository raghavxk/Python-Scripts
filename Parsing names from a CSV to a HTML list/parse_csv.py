import csv

html_output = ''
names = []

with open('my_csv.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # we don't want csv file header or bad lines to be in html output
    next(csv_data)

    for item in csv_data:
        if(item['FirstName'] == 'No Reward'):
            break
        names.append(f"{item['FirstName' ]} {item['LastName']}")

html_output+=f'<p>There are currently {len(names)} public contributors'
html_output+='\n<ul>'

for name in names:
    html_output+=f'\n\t<li>{name}</li>'

html_output+='\n</ul>'

print(html_output)
