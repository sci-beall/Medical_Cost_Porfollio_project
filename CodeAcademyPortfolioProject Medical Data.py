import csv

with open('insurance.csv') as insurance_data:
    reader = csv.DictReader(insurance_data, delimiter = ',')
    clients = 0
    client_dict = {}
    for row in reader:
        clients+=1
        client_dict[clients] = dict(row)
        

#print(client_dict)

#store the number of people in each region northwest, northeast, southwest, southest
num_in_nw = 0
num_in_ne = 0
num_in_sw = 0
num_in_se = 0

num_of_smokers = 0

for client in client_dict.values():
    if client['region'].lower() == 'northwest':
        num_in_nw += 1
    elif client['region'].lower() == 'northeast':
        num_in_ne += 1
    elif client['region'].lower() == 'southwest':
        num_in_sw += 1
    elif client['region'].lower() == 'southeast':
        num_in_se += 1
    if client['smoker'].lower() == 'yes':
        num_of_smokers += 1

print('Northwest: {nw}, Northeast: {ne}, Southwest: {sw}, Southeast: {se}'.format(nw = num_in_nw, ne = num_in_ne, sw = num_in_sw, se = num_in_se))
print('Number of smokers: {}'.format(num_of_smokers))
print(f'Percentage of smokers: {(num_of_smokers/clients)*100}')


#create a dictionary of each client that smokes based on region
regions_smokers_dictionary = {'northwest': [],
                      'northeast': [],
                      'southwest': [],
                      'southeast': []}

def update_regions_dict(dictionary):
    for client, info in dictionary.items():
        if info['smoker'].lower() == 'yes':
            regions_smokers_dictionary[info['region']].append(client) 
update_regions_dict(client_dict)
#print(regions_smokers_dictionary)

#store the number of smokers in each region
num_smokers_nw = len(regions_smokers_dictionary['northwest'])
num_smokers_ne = len(regions_smokers_dictionary['northeast'])
num_smokers_sw = len(regions_smokers_dictionary['southwest'])
num_smokers_se = len(regions_smokers_dictionary['southeast'])

print(f'The number of smokers in each region: Northwest => {num_smokers_nw}, Northeast => {num_smokers_ne}, Southwest => {num_smokers_sw}, Southeast => {num_smokers_se}')
# IT SEEMS THE REGION WITH THE MOST SMOKERS IS THE SOUTHEAST WITH A LEAD OF 14 PEOPLE

#to see if bmi has a corrolation with number of children we will first make a dicitonary with number of children
#as the key and a list of bmis as the value
children_vs_bmi_dict = {}
def update_children_v_bmi(dit):
    for info in dit.values():
        if info['children'] not in children_vs_bmi_dict:
            children_vs_bmi_dict[info['children']] = []
        children_vs_bmi_dict[info['children']].append(float(info['bmi'])) #add the bmi to the category and convert it to a float
update_children_v_bmi(client_dict)
#check to see min and max number of children
#for keys in children_vs_bmi_dict.keys():
#    print(keys)

#AVERAGE THE BMIs FOR EACH CHILD AMOUNT
def average_dictionary(dit):
    averages = []
    for cat, info in dit.items():
        average = sum(info)/len(info)
        averages.append((cat, average))
    return averages
bmi_averages = average_dictionary(children_vs_bmi_dict)
bmi_averages.sort()
for bmi in bmi_averages:
    print('People with {kids} kids have an average bmi of {bm}.'.format(kids = bmi[0], bm = bmi[1]))
#THERE DOES NOT SEEM TO BE A LINK TO NUMBER OF CHILDREN AND BMI





