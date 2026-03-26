import math

print("\nHey there! Welcome to your Career Helper thingy!")
print("Just answer a few questions and I'll suggest something cool for you.\n")

careers = [
 {"name":"Software Developer","logic":9,"creativity":6,"management":5},
 {"name":"UI/UX Designer","logic":5,"creativity":9,"management":6},
 {"name":"Data Analyst","logic":8,"creativity":5,"management":6},
 {"name":"Project Manager","logic":6,"creativity":6,"management":9},
 {"name":"AI Engineer","logic":10,"creativity":7,"management":6},
 {"name":"Cybersecurity Analyst","logic":9,"creativity":5,"management":5},
 {"name":"Game Developer","logic":8,"creativity":9,"management":4},
 {"name":"Entrepreneur","logic":7,"creativity":8,"management":10},
 {"name":"Business Analyst","logic":7,"creativity":6,"management":8},
 {"name":"Cloud Engineer","logic":9,"creativity":5,"management":6},
 {"name":"Digital Marketer","logic":5,"creativity":9,"management":7},
 {"name":"Research Scientist","logic":10,"creativity":8,"management":5},
 {"name":"DevOps Engineer","logic":9,"creativity":6,"management":7},
 {"name":"Product Manager","logic":7,"creativity":7,"management":9},
 {"name":"Content Creator","logic":4,"creativity":10,"management":6},
 {"name":"System Administrator","logic":8,"creativity":5,"management":6}
]

def get_number(msg):
    while True:
        try:
            x = int(input(msg))
            if x >=1 and x <=10:
                return x
            else:
                print("Oop! Number should be 1 to 10. Try again.")
        except:
            print("That's not a number...try again.")

def get_user_skills():
    print("\nRate yourself 1 to 10 (1=low,10=high)\n")
    temp = {}
    temp["l"] = get_number("How logical are you? ")
    temp["c"] = get_number("How creative are you? ")
    temp["m"] = get_number("How good are you at managing stuff? ")
    return temp

def distance(u, career):
    # Euclidean distance 
    d = math.sqrt( (u["l"]-career["logic"])**2 + (u["c"]-career["creativity"])**2 + (u["m"]-career["management"])**2 )
    return d

def rank_careers(u):
    lst = []
    for c in careers:
        d = distance(u,c)
        lst.append( (c["name"], d) )
    lst.sort(key=lambda x:x[1])
    return lst

def explain_skills(u):
    r = []
    if u["l"]>=8: r.append("You are really logical")
    if u["c"]>=8: r.append("You are super creative")
    if u["m"]>=8: r.append("You have leadership vibes")
    if len(r) > 0:
        return " and ".join(r)
    else:
        return "You seem to have a balanced skill set"

def show_results():
    user = get_user_skills()
    ranking = rank_careers(user)
    top3 = ranking[:3]
    bottom2 = ranking[-2:]

    print("\nHere are some career ideas for you:\n")
    for i in range(len(top3)):
        print(str(i+1)+". "+top3[i][0])

    print("\nYour BEST fit seems to be:")
    print(top3[0][0])

    print("\nWhy it fits you:")
    print("- Because "+explain_skills(user)+".") 

    print("\nOther options you can try:")
    for x in top3[1:]:
        print("- "+x[0])

    print("\nHmm...these might be tough for you:")
    for x in bottom2:
        print("- "+x[0])

    print("\nTip:")
    print("Keep learning and practicing! You got this!")

def menu():
    while True:
        print("\n-------MENU-------")
        print("1. See all careers")
        print("2. Get career suggestion")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice=="1":
            print("\nAll available careers:\n")
            for i in range(len(careers)):
                print(str(i+1)+". "+careers[i]["name"])
        elif choice=="2":
            show_results()
        elif choice=="3":
            print("Bye! Good luck out there :)")
            break
        else:
            print("Invalid choice lol, try again.")

if __name__=="__main__":
    menu()
