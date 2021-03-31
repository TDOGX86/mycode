#!/usr/bin/ python3

life = 3
answer = ""


def level1():
        global life # use gloabl variable to manage lives
        global answer
        print("World 1-1")

        while answer != "Mario":
            answer = input('This character has his own day in March?') #Ask first question

            if answer.lower() == "mario": #  checks for erro with lower
                print("Correct the answer was Mario, but your princess is in another Castle")
                level2()# moves to next level when correct
            elif life == 1:#gives hint on last life
                print("Here is a hint the quiz is named after him")
            elif life == 0:
                print("Sorry the answer was Mario looks like Bowser won")
                break

            elif answer.lower() == "1UP": #extra life secret
                print("You found a 1UP mushroom")
                life +=1

            elif answer == "":
                print("Let's a go! enter an answer")
            
            
            else:
                print("Mama mia! Thats not right try again")
                life -=1
            

def level2():
        global life 
        global answer

        print("World 2-1")

        while answer != "Luigi":
            answer = input('Which charcter got their own year in 2013')

            if answer.lower() == "luigi": 
                print("Correct the answere was Luigi, but your princess is in another castle")
                level3()
            elif life == 1: 
                print("Here is a hint he wears green")    
            elif life == 0:
                print("Sorry the answer was Luigi looks like Bowser won")
                break

            elif answer.lower() == "1UP":
                print("You found a 1UP mushroom")
                life +=1
          
            else:
                print("Mama mia! Thats not right try again")
                life -=1
def level3():
        global life
        global answer

        print("World 3-1")
        while answer != "Mario":

            life -=1 
            answer = input('Which character\'s game is where Mario made his debut')

            if answer.lower() == "donkey kong": 
                print("Correct! Congratulations you saved the Princess")
            elif life == 1:
                break
                print("Here is a hint he likes bananas")    
            elif life == 0:
                print("Sorry the answer was Donkey Kong looks like Bowser won")
                break
            elif answer.lower() == "1UPm":
                print("You found a 1UP mushroom")
                life +=1
            elif answer == "":
                print("Let's a go! enter an answer")
            
            else:
                print("Mama mia! Thats not right try again")
                life -=1

level1()
