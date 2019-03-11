#!/usr/bin/env python3

import datetime

def age_to_time():
    age_input =int(input('How old are you? '))
    age_in_months = str(age_input*12)
    print('months: ' + age_in_months)
    age_in_days = str(int(age_in_months) * 30)
    print('days: ' + age_in_days)
    age_in_hours = str(int(age_in_days) * 24)
    print('hours: ' + age_in_hours)
    age_in_minutes = str(int(age_in_hours) * 60)
    print('minutes: ' + age_in_minutes)


def age_to_time2():
    age_input = (input('when were you born? '))
    age_in_months = datetime.age_input.month
    print(age_in_months)

if __name__=='__main__':
    age_to_time2()
