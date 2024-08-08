import csv

with open('employeetable.csv', mode='w') as csv_file:
    fieldnames = ['e_id', 'name', 'dep_id','salary','manager_id']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'e_id':'A111','name':'JOHN HELLEN','dep_id':'D01','salary':'15380','manager_id':'A120'})
    writer.writerow({'e_id':'A114','name':'MARTIN TREDEAU','dep_id':'D01','salary':'54497','manager_id':'A120'})
    writer.writerow({'e_id': 'A116', 'name': 'ROBIN WAYNE', 'dep_id': 'D02', 'salary': '20196', 'manager_id': 'A187'})
    writer.writerow({'e_id': 'A120', 'name': 'TIM ARCHER', 'dep_id': 'D01', 'salary': '48834', 'manager_id': 'A298'})
    writer.writerow({'e_id': 'A121', 'name': 'STUART WILLIAM', 'dep_id': 'D02', 'salary': '78629', 'manager_id': 'A187'})
    writer.writerow({'e_id': 'A128', 'name': 'ADAM WAYNE', 'dep_id': 'D05', 'salary': '94324', 'manager_id': 'A165'})
    writer.writerow({'e_id': 'A129', 'name': 'JOSEPH ANGELIN', 'dep_id': 'D05', 'salary': '44280', 'manager_id': 'A165'})
    writer.writerow({'e_id': 'A130', 'name': 'VANESSA PARY', 'dep_id': 'D04', 'salary': '28565', 'manager_id': 'A188'})
    writer.writerow({'e_id': 'A132', 'name': 'PAUL VINCENT', 'dep_id': 'D01', 'salary': '94791', 'manager_id': 'A120'})
    writer.writerow({'e_id': 'A133', 'name': 'STEVE MICHELOS', 'dep_id': 'D02', 'salary': '61215', 'manager_id': 'A187'})
    writer.writerow({'e_id': 'A142', 'name': 'TARA CUMMINGS', 'dep_id': 'D04', 'salary': '99475', 'manager_id': 'A188'})
    writer.writerow({'e_id': 'A143', 'name': 'BRAD MICHAEL', 'dep_id': 'D01', 'salary': '24488', 'manager_id': 'A120'})
    writer.writerow({'e_id': 'A156', 'name': 'NICK MARTIN', 'dep_id': 'D03', 'salary': '50174', 'manager_id': 'A178'})
    writer.writerow({'e_id': 'A165', 'name': 'NATASHA STEVENS', 'dep_id': 'D05', 'salary': '31377', 'manager_id': 'A298'})
    writer.writerow({'e_id': 'A176', 'name': 'EDWARD CANE', 'dep_id': 'D01', 'salary': '89176', 'manager_id': 'A120'})
    writer.writerow({'e_id': 'A178', 'name': 'BRUCE WILLS', 'dep_id': 'D03', 'salary': '66861', 'manager_id': 'A298'})
    writer.writerow({'e_id': 'A187', 'name': 'ADAM JUSTIN', 'dep_id': 'D02', 'salary': '80543', 'manager_id': 'A298'})
    writer.writerow({'e_id': 'A188', 'name': 'ROBERT SWIFT', 'dep_id': 'D04', 'salary': '27700', 'manager_id': 'A298'})
    writer.writerow({'e_id': 'A194', 'name': 'HAROLLD STEVENS', 'dep_id': 'D02', 'salary': '32166', 'manager_id': 'A187'})
    writer.writerow({'e_id': 'A198', 'name': 'TOM HANKS', 'dep_id': 'D02', 'salary': '16879', 'manager_id': 'A187'})
