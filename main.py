import pyfiglet
import winsound

design = pyfiglet.figlet_format("Confirm Jannati") 
print(design)

print("Hello ! This Is Confirm Jannati Team,\nWe Are Helping You To Test Your Iman In A Halal Way.\nJust Answer The Following Questions.\n")

proceed = input("Do You Want To Proceed Sir/Mam (yes/no): ")

#Starting Code With Error Handling

while True:
    if proceed=="yes":
        print("\nLets Start,")
        break
    if proceed=="no":
        print("Thaks, Visit Again.")
        break
    else:
        print("You Entered a Wrong Value, Restart. ")
        break
       
list = ["\nWho Is Your Creator ?\nAns: ", "Who Is The Last Prophet in Accordance with Quran & Hadith ?\nAns: ", "Have You Ever Read The Holy Quran ?\nAns: "]

# Question 1

while True:
    question1 = input(list[0])
    print(question1)
    if question1=="yes":
        print("Anything")
    else:
        print("\nYou Are Correct !\n")
        break
    
# Question 2

while True:
    question2 = input(list[1])
    print(question2)
    if question2=="yes":
        print("Anything")
    else:
        print("\nYou Are Correct !\n")
        break

# Question 2

while True:
    question3 = input(list[2])
    print(question3)
    if question3=="yes":
        print("Anything")
    else:
        print("\nYou Are Correct !\n")
        print("No. Of Questions You Attempted = 3")
        print("Correct No Of Answers = 3\n")
        break    

print("\nOk You Gave Right Answer Of All Of The Questions,\n")
reward = input("Do You Want To Check Your Reward (yes or no): ")

if reward=="yes":
    print("\nActually This Was A Prank Game . Anyone Cannot Define Your Iman Level.\nBut Allah Knows You Better.\nDont Wait For A Reward Just Repent Before Its Too Late.\n\nThanks,\nConfimJannati Team.")
    winsound.PlaySound('C:\music.wav',0)
else:
    print("\nActually This Was A Prank Game . Anyone Cannot Define Your Iman Level.\nBut Allah Knows You Better.\nDont Wait For A Reward Just Repent Before Its Too Late.\n\nThanks,\nConfimJannati Team.")
    winsound.PlaySound('C:\music.wav',0)
