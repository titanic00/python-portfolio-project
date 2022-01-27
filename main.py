import csv
from decimal import Decimal
import math

def smoking_parents(data_list):
    how_much_people_with_baby = 0
    smokers = 0
    non_smokers = 0
    for i in data_list:
        if int(i['children']) != 0:
            how_much_people_with_baby += 1
            if i['smoker'] == 'yes':
                smokers += 1
            else:
                non_smokers += 1
    
    percent_of_non_smokers = (non_smokers / how_much_people_with_baby) * 100
    percent_of_smokers = (smokers / how_much_people_with_baby) * 100

    return math.floor(percent_of_non_smokers), math.ceil(percent_of_smokers)

def the_average_age_who_has_a_kid(data_list):
    the_average_age = 0
    how_much_people_with_baby = 0
    for item in variable_for_insurance_data:
        if int(item['children']) != 0:
            the_average_age = the_average_age + int(item['age'])
            how_much_people_with_baby += 1
    
    return int(the_average_age / how_much_people_with_baby)

#Getting data from insurance.csv in a variable
variable_for_insurance_data = []
with open(r'C:\Users\Vitalik\Desktop\projects\python-portfolio-project\data\insurance.csv') as insurance_data:
    data = csv.DictReader(insurance_data)

    for item in data:
        variable_for_insurance_data.append(item)