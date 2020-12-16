import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices=[rock,paper,scissors]
pc=int(input ("type 0 for rock , type 1 for paper , type 2 for scissors \n")) 
player =print(choices[pc])
random_num=random.randint(0,2)
computer=print(choices[random_num])
if pc ==0 and random_num==2 :
  print("you win ")
elif random_num ==0 and pc==2 :
  print("you lose ")
elif random_num > pc :
  print("you lose")
elif random_num < pc :
  print("you win")
elif random_num == pc :
  print("it's a draw")

