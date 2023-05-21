
import random



d_min=1
d_max=6

roll='y'or'yes'

while roll=='y' or roll=='yes':

    print(random.randint(d_min,d_max),random.randint(d_min,d_max))
    
    roll=input('do u want roll again? ')
