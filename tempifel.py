temperature = int(input("Enter todays temperature "))
if temperature > 85:	# comparisons are done in order
    print("it's quite hot outside")
    print('go for a swim!')

elif temperature > 70:
      print('you can go swimming in a heated pool.')
elif temperature > 32: # done only if 1st & 2nd ones fail
      print('it is too cold to go swimming outside.')
else:		        # done only if all of the above fail
      print('you should go ice skating instead!')
