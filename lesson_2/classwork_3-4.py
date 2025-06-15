from lesson_2_data import courts

# for i in courts:
#     print(i['court_name'])

names = [court['court_name'] for court in courts]
court_mapping = {court['court_code']: court['court_name'] for court in courts}

print (court_mapping)

