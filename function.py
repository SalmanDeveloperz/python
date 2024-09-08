# To Define function we might use ====> def Call()
# To calling function we might use =====> Call()

def get_milk():
    print('Hi There I am Chaudhary Slaman')
    print('I am Great')
    print('What\'s about you?')
    print('Would you like to introduce me yourself?')
    print('Regards Chaudhary Slaman')

choice=bool(input('Please enter your choice: (1 for Yes or 0 for No)'))
if(choice==1):
   get_milk()
else:
    print('Sorry you\'re unable to call get milk option')

