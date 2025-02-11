## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary=float(350000)
portion_saved=float(.3)
cost_of_dream_home=float(10000000)
semi_annual_raise = 1.05
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

amount_saved = 0
portion_down_payment = cost_of_dream_home * 0.25
r = 0.05
months = 0
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while portion_down_payment > amount_saved:
	amount_saved += (amount_saved * (r/12))
	amount_saved += ((yearly_salary/12) * portion_saved)
	months += 1
	if months % 6 == 0:
		yearly_salary *= semi_annual_raise

print(f"Number of months: {months}")