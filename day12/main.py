import art
import random



def game():
    print(art.logo)
    ans=int(input("guess the num "))
    
    num=random.randint(1,100)
    turn = 0
    hard=5
    easy=10
    print('select hard or easy')
    level=input()
    
    if level=='hard':
        while ans!=num and turn<hard:
            turn+=1
            if ans>num:
                print('too high')
            elif ans<num:
                print('too low')
            ans=int(input('guess again '))
            
    if level=='easy':
        while ans!=num and turn<easy:
            turn+=1
            if ans>num:
                print('too high')
            elif ans<num:
                print('too low')
            ans=int(input('guess again '))

        
    if num==ans:
        print("you win")
    else:
        print("you lose")
    
    
    
    

game()
