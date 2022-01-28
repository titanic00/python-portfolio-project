import csv
import math

#--------------------------------------------------------------------------------------------------------

#8% above 60, 61% between 30 and 60, 31% below 30
def the_number_of_smokers_depending_on_age(data_list):
    how_much_smokers = 0
    smokers_above_60 = 0
    smokers_between_30_and_60 = 0
    smokers_below_30 = 0

    for i in data_list:
        if i['smoker'] == 'yes':
            how_much_smokers += 1
            if int(i['age']) > 60:
                smokers_above_60 += 1
                continue
            elif int(i['age']) >= 30 and int(i['age']) <= 60:
                smokers_between_30_and_60 += 1
                continue
            else:
                smokers_below_30 += 1
                continue

    percent_of_smokers_above_60 = (smokers_above_60 / how_much_smokers) * 100
    percent_of_smokers_between_30_and_60 = (smokers_between_30_and_60 / how_much_smokers) * 100
    percent_of_smokers_below_30 = (smokers_below_30 / how_much_smokers) * 100

    return math.floor(percent_of_smokers_above_60), math.ceil(percent_of_smokers_between_30_and_60), math.floor(percent_of_smokers_below_30)

#32050$ average charges for smokers and 8435$ average charges for non-smokers
def difference_in_charges(data_list):
    how_much_smokers = 0
    how_much_non_smokers = 0
    the_average_charges_of_smokers = 0
    the_average_charges_of_non_smokers = 0

    for item in data_list:
        if item['smoker'] == 'yes':
            the_average_charges_of_smokers += float(item['charges'])
            how_much_smokers += 1
        elif item['smoker'] == 'no':
            the_average_charges_of_non_smokers += float(item['charges'])
            how_much_non_smokers += 1
    
    the_average_charges_of_smokers /= how_much_smokers
    the_average_charges_of_non_smokers /= how_much_non_smokers

    return math.floor(the_average_charges_of_smokers), math.ceil(the_average_charges_of_non_smokers)

#BMI is almost the same
def the_average_bmi_of_smokers_and_non_smokers(data_list):
    how_much_smokers = 0
    how_much_non_smokers = 0
    the_average_bmi_of_smokers = 0
    the_average_bmi_of_non_smokers = 0

    for item in data_list:
        if item['smoker'] == 'yes':
            the_average_bmi_of_smokers += float(item['bmi'])
            how_much_smokers += 1
            continue
        else:
            the_average_bmi_of_non_smokers += float(item['bmi'])
            how_much_non_smokers += 1
            continue

#--------------------------------------------------------------------------------------------------------

#What a surprise! Smokers have more baby!
def how_much_children_smoking_and_non_smoking_people_have(data_list):
    how_much_smoking_people_with_baby = 0
    how_much_non_smoking_people_with_baby = 0
    kids_of_smoking_parents = 0
    kids_of_non_smoking_parents = 0

    for i in data_list:
        if int(i['children']) != 0 and i['smoker'] == 'yes':
            how_much_smoking_people_with_baby += 1
            kids_of_smoking_parents += float(i['children'])
        else:
            how_much_non_smoking_people_with_baby += 1
            kids_of_non_smoking_parents += float(i['children'])
    
    the_average_amount_of_kids_of_smoking_parents = kids_of_smoking_parents / how_much_smoking_people_with_baby
    the_average_amount_of_kids_between_of_non_smoking_parents = kids_of_non_smoking_parents / how_much_non_smoking_people_with_baby

    return math.ceil(the_average_amount_of_kids_of_smoking_parents), math.ceil(the_average_amount_of_kids_between_of_non_smoking_parents)

#Smokers are paying one tousand dollars more
def how_much_smoking_and_non_smoking_parents_pay_for_insurance(data_list):
    how_much_smoking_people_with_baby = 0
    how_much_non_smoking_people_with_baby = 0
    calculated_charges_smokers = 0
    calculated_charges_non_smokers = 0

    for i in data_list:
        if int(i['children']) != 0 and i['smoker']:
            how_much_smoking_people_with_baby += 1
            calculated_charges_smokers += float(i['charges'])
        else:
            how_much_non_smoking_people_with_baby += 1
            calculated_charges_non_smokers += float(i['charges'])
    
    the_average_amount_of_charges_between_smoking_parents = calculated_charges_smokers / how_much_smoking_people_with_baby
    the_average_amount_of_charges_between_non_smoking_parents = calculated_charges_non_smokers / how_much_non_smoking_people_with_baby

    return the_average_amount_of_charges_between_smoking_parents, the_average_amount_of_charges_between_non_smoking_parents

#Non-smoking parents are more than smoking parents (79% against 21%)
#they have kids they pay less though
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

#The average age is 39
def the_average_age_who_has_a_kid(data_list):
    the_average_age = 0
    how_much_people_with_baby = 0
    for item in variable_for_insurance_data:
        if int(item['children']) != 0:
            the_average_age = the_average_age + int(item['age'])
            how_much_people_with_baby += 1
    
    return int(the_average_age / how_much_people_with_baby)

#--------------------------------------------------------------------------------------------------------

#Getting data from insurance.csv in a variable
variable_for_insurance_data = []
with open(r'C:\Users\Vitalik\Desktop\projects\python-portfolio-project\data\insurance.csv') as insurance_data:
    data = csv.DictReader(insurance_data)

    for item in data:
        variable_for_insurance_data.append(item)