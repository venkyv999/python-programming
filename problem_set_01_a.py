annual_salary = int(input("Enter your annual salary:"))
month_salary = annual_salary/12
save_per = float(
    input("Enter the percent of your salary to save,as a decimal:"))
portion_saved = month_salary*save_per
total_cost = int(input("Enter cost of your dream home:"))
down_payment = total_cost*0.25
current_saving = 0
i = 1
while True:
    if current_saving >= down_payment:
        break
    current_saving += portion_saved
    current_saving += (current_saving*0.04)/12
    i += 1
print("Number of months:", i)
