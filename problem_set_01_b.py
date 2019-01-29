annual_salary = int(input("Enter your annual salary:"))
month_salary = annual_salary/12
save_per = float(
    input("Enter the percent of your salary to save,as a decimal:"))

total_cost = int(input("Enter cost of your dream home:"))
semi_inc = float(input("Enter semi annual inc:"))
down_payment = total_cost*0.25
current_saving = 0
for i in range(1, 999):
    if current_saving >= down_payment:
        break
    if i % 6 == 0:
        month_salary += month_salary*semi_inc
    current_saving += (month_salary*save_per)
    current_saving += (current_saving*0.04)/12
print("Number of months:", i)
