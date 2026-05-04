import random 
print("__enter your choice__")
print("0. for rock")
print("1. for paper")
print("2. for scissors")
print("3. to quit")

computer=("rock","paper","scissors")
score =0
while True:
    print("your score",score)
    use_inp=int(input("enter here:"))
    if use_inp==3:
        break

    value=computer[use_inp]
    no=random.choice([0,1,2])
    comp_inp=computer[no]

    match use_inp:
        case 0:
            if no == 1:
                print("you loose")
                if score>0:
                    score-=10
            elif no == 2:
                print("you win")
                score+=10
            else:
                print("thats a tie")

        case 1:
            if no == 0:
                print("you win")
                score+=10
            elif no == 2:
                print("you loose")
                if score>0:
                    score-=10
            else:
                print("thats a tie")

        case 2:
            if no==0:
                print("you loose")
                if score>0:
                    score-=10
            elif no== 1:
                print("you win")
                score+=10
            else:
                print("thats a tie")

        case _:
            print("wrong number")

    print("your choice",computer[use_inp])
    print("cpmputer choice",comp_inp)

print("thanks for playing")
print(f"your score was={score}")
        



