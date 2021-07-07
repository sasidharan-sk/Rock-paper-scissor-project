import random

while True:
    print('here the choices : \n 1.Rock \n 2.Paper \n 3.Scissor \n ')

    user_choice = int(input('enter the choice: '))

    while user_choice>3 or user_choice<1:
        user_choice = int(input('enter validate input: '))
        
    if user_choice==1:
        choice_name = 'Rock'
    elif user_choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print(f'\n user choice is : {choice_name}')
        
    com_choice = random.randint(1,3)

    if com_choice==1:
       com_name = 'Rock'
    elif com_choice == 2:
       com_name = 'Paper'
    else:
       com_name = 'Scissor'

    print(f'\n cpu choice is : {com_name}')

    print(f'\n {choice_name} v/s {com_name}')

    if ((user_choice==1 and com_choice ==2) or
       (user_choice==2and com_choice==1)):
           print('\n Paper wins')
           result = 'Paper'
        
    elif((user_choice==2 and com_choice==3)or
        (user_choice==3 and com_choice==2)):
            print('\n Scissor wins')
            result = 'Scissor'
        
    elif(user_choice == com_choice):
            pass

    else:
            print('\n Rock wins ')
            result = 'Rock'

    if result == choice_name:
        print('\n -- user wins --')

    elif result == com_name:
        print('\n -- cpu wins --')

    else:
        print('\n It\'s tie')

    print('DO YOU WANT TO PLAY AGAIN? : (Y/N)')

    ans = input()

    if ans == 'n' or ans == 'N':
        
        break

print('\n ** Thank you **')






    




