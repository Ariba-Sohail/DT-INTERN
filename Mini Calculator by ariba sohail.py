print('mini calculator by Ariba Sohail')

num1 = float(input('enter 1st num:'))
num2 = float(input('enter 2nd num:'))

print('press 1 for additon \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division')

choice = int(input('enter your choice 1-4:'))

if choice == 1:
    print ('the addition of given numbers is:',num1 + num2)
elif choice == 2:
    print ('the subtraction of given numbers is:',num1 - num2)
elif choice == 3:
    print ('the multiplication of given numbers is:',num1 * num2)
elif choice == 4:
    print ('the division of given numbers is:',num1 / num2)
else:
    print('invalid input')