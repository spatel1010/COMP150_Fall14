GRADCREDITS = 120	# this is a global constant
credits = int(input('enter your current LUC credits: '))
if credits >= GRADCREDITS:
    print("You have enough credits to graduate!")
else:
    needed = GRADCREDITS - credits
    print("You need {} more credits.".format(needed))
