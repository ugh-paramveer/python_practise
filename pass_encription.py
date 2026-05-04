pws=input("Enter master key:")

def add():
    name=input("enter the account name:")
    passw=input("enter the account password:")
    with open('password.txt','a') as f:
        f.write(f"{name}|{passw}")


def veiw():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,pws=data.split("|")
            print(f"name={user},password={pws}")

while True:
    mode=input("would you like to add new passsword or view the existing one(add/veiw).press q to quit:".lower())
    if mode == "q":
        break
    elif mode=="add":
        add()
    elif mode=="veiw":
        veiw()
    else:
        print("invalid input")