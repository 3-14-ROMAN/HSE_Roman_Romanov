from lesson_2_data import respondents, courts

# # for i in courts:
# # print(i['court_name'])

# names = [court['court_name'] for court in courts]
# court_mapping = {court['court_code']: court['court_name'] for court in courts}

# print (court_mapping)


def gen_court_header(court):
    header = f"В {court['court_name']}\n" \
             f"Адрес: {court['court_address']} \n"
    print(header)

def gen_respondent_header(respondent):
    header = f"Ответчик: {respondent['short_name']}\n" \
             f"ИНН: {respondent['inn']}, ОГРН: {respondent['ogrn']}\n" \
             f"Адрес: {respondent['address']} \n"
    print(header)


def main():
    print ('start')
    court_mapping = {i['court_code']: i for i in courts}
    for i in respondents:
        try:
            code = i ['case_number'][:3]
            court = court_mapping[code]
            gen_court_header(court=court)
            gen_respondent_header(respondent=i)
        except Exception:
            print('error')
            continue
    print ('stop')

if __name__ == "__main__":
    main()