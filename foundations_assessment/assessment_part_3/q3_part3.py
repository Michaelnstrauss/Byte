import json




def open_appl():
    appl_dict = {}
    with open('aapl.json', 'r') as appl_file:
        data = json.load(appl_file)
        appl_dict['companyName'] = data['companyName']
        appl_dict['latestPrice'] = data['latestPrice']
        appl_dict['marketCap'] = data['marketCap']
        print(appl_dict)
    with open('AAPLprice.json', 'w+') as applprice_file:
        json.dump(appl_dict, applprice_file)

#         for line in appl_file:
# #           appl_dict['companyName'] = line['companyName'][1]
#             print(line)
#             print(type(line))
            
            
            
            
        # new_dict = {'companyName': lines[0], 'latestPrice': lines[0], 'marketCap': lines[0]}
        # print(new_dict)



        #     lines['companyName'] = 'Apple Inc.'
        #     appl_dict['companyName'] = lines
        # print(lines)
            

open_appl()