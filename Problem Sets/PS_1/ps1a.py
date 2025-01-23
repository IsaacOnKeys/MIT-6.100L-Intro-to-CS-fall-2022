## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
# yearly_salary = float(input("Enter your yearly salary\n"))
# portion_saved = float(input("What percentage of your salary do want to save? (ex.50% = 0.5)\n"))
# cost_of_dream_home = float(input("Enter how much your dream home costs\n"))
yearly_salary = float(350000)
portion_saved = float(0.3)
cost_of_dream_home = float(10000000)

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################
def savings_calc(yearly_salary, portion_saved, cost_of_dream_home):
    amount_saved = 0
    portion_down_payment = cost_of_dream_home * 0.25
    r = 0.05
    global months
    months = 0
    while portion_down_payment > amount_saved:
        amount_saved += amount_saved * (r / 12)
        amount_saved += (yearly_salary / 12) * portion_saved
        months += 1
    return months


savings_calc(yearly_salary, portion_saved, cost_of_dream_home)
print(
    f"It will take {months} months to save for the down payment. That is {(months // 12)} years"
)
