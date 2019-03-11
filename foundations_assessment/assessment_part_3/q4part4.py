

import csv


def flight_csv():
    flight_list = []
    with open('airtravel.csv', 'r') as air_file:
        for lines in air_file:
            lines = lines.split()
            print(lines)
            
            
        #     lines = list(lines)
        #     flight_list = flight_list.extend(lines)
        # print(flight_list)
            



flight_csv()
