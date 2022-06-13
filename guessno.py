# PROJECT 


print("\n\n\n")
print("\t \t \t \t \t \t \t \t' GUESS THE NUMBER '\n\n\t \t \t \t \t \t Instruction: \n\t \t \t \t \t \t    >> You will have to guess the number through the clues provided!\n\t \t \t \t \t \t    >> Guessing number is between 1 and 20 \n\t \t \t \t \t \t    >> Four chance for each play!\n\n\t \t \t \t \t \t \t \t    BEST OF LUCK !!\n")             

print("\t \t \t \t \t \t Secret number should be between 1 and 10")                                                                                                                                                                            
count=0                                                                                                                                                                                                                     
secret_num=int(input("\t \t \t \t \t \t Enter the secret number: "))                                                                                                                                                                             
x=secret_num*2-5+3                                                                                                                                                                                                                   

def guess(a,b):                                                                                                                                                                                                                        
        if x==y:                                                                                                                                                                                                                 
            print("\t \t \t \t \t \t You have guessed the right number!\n\n\t \t \t \t \t \t YOU WON THE GAME \n\n\t \t \t \t \t \t \t \t    CONGRATULATION !!")                                                                                                                                
        elif x<y:                                                                                                                                                                                                        
             print("\t \t \t \t \t \t Your guess is greater than actual number")                                                                                                                                                               
        else:                                                                                                                                                                                                               
             print("\t \t \t \t \t \t Your guess is lower than actual number")                                                                                                                                                                   
        return guess                                                 

for i in range(1,5):                                                                                                                                                                                                 
        print("\n")
        y=int(input("\t \t \t \t \t \t Guess the number:"))                                          
        z=guess(x,y)                          
        if x==y:                                                                                                                                                                                                           
            break                                                                                                                                                                                                     
        count=count+1                                                                                                                                                                                                       

if count==4:                                 
    print("\n \t \t \t \t \t \t Oops you have used all your chances!\n\t \t \t \t \t \t Try again\n\t \t \t \t \t \t \t \t    GAME OVER !!")     
