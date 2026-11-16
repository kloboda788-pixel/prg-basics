###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = float(input("Enter the father's income: "))
mother_income = float(input("Enter the mother's income: "))
family_members = int(input("Enter the number of family members: "))
total_income = father_income + mother_income
income_per_person = total_income / family_members
print(f'Total family income is {total_income}, and income per person is {income_per_person:.2f}.')