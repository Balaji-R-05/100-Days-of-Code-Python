print("Welcome to Tip Calculator")
print("-------------------------------")
total_bill= float(input("Enter total bill amount: "))
tip_percent = int(input("Enter tip percentge: "))
number_of_people = int(input("Enter number of people: "))
total_per_person = round((total_bill+(total_bill*tip_percent/100))/number_of_people,2)
print("Total per person: ", total_per_person)