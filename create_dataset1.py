import csv
with open("depttable.csv",mode="w") as csv_file:
    fieldnames = ['dep_id', 'dep_name', 'dep_manager']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'dep_id': 'D01', 'dep_name': 'HEALTH', 'dep_manager': 'TIM ARCHER'})
    writer.writerow({'dep_id': 'D02', 'dep_name': 'COMMUNICATIONS', 'dep_manager': 'ADAM JUSTIN'})
    writer.writerow({'dep_id': 'D03', 'dep_name': 'PRODUCT', 'dep_manager': 'BRUCE WILLS'})
    writer.writerow({'dep_id': 'D04', 'dep_name': 'INSURANCE', 'dep_manager': 'ROBERT SWIFT'})
    writer.writerow({'dep_id': 'D05', 'dep_name': 'FINANCE', 'dep_manager': 'NATASHA STEVENS'})
