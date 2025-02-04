## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
# initial_deposit = float(input("Please enter an intial deposit amount"))
initial_deposit = 1000
months = 36
cost = 800_000.0
down_payment = cost * 0.25
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
high = 1.0
low = 0.0
epsilon = 100
r = (high + low) / 2
amount_saved = initial_deposit * ((1 + (r/12))**months)
count = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while abs(amount_saved - down_payment) >= epsilon:
	if r > 0.99:
		r = None
		count = 0
		break
	count += 1

	if amount_saved > down_payment:
		print(f"{r} is too high")
		high = r
		r = (high + low) / 2
		amount_saved = initial_deposit * ((1 + (r/12))**months)
	elif amount_saved < down_payment:
		print(f"{r} is too low")
		low = r
		r = (high + low) / 2
		amount_saved = initial_deposit * ((1 + (r/12))**months)
	else:
		break



#### Test cases ###
NotImplemented = "Not implemented yet"
print(f"Initial deposit = {initial_deposit} \n \
		Best savings rate = {r} \n \
		Steps in bisection search: {count}")
