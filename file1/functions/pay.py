#!/usr/bin/env python3


def prompt_hours():
    hours_worked = float(input('How many hours did you work? '))
    return hours_worked

def prompt_rate():
    pay_rate = float(input('what is your hourly rate? '))
    return pay_rate

def compute_pay(hours, rate):
    if hours > 40:
        return (float((40 * rate) + ((hours - 40)* (rate * 1.5))))
    if hours <= 40:
        return ((float(hours * rate)))


hours = prompt_hours()
rate = prompt_rate()
pay = compute_pay(hours, rate)

print('You will be paid ${:.2f}.'.format(pay))

#    if hours < 40:
#        print(hours * rate)
#    return hours,rate
 #   if hours > 40:
 #       return ((40 * rate) + ((hours - 40) * (rate * 1.5))

