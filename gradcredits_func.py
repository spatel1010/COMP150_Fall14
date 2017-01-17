def needed_credits(credits):	
    GRADCREDITS = 120		# number required
    return GRADCREDITS - credits	# number still needed

def main():
    credits = int(input('enter your current LUC credits: '))
    needed = needed_credits(credits)
    if needed <= 0: # number needed is 0 or negative
	print("You have enough credits to graduate!")
    else:   # a positive number is still needed
	print("You need {} more credits.".format(needed))

main()
