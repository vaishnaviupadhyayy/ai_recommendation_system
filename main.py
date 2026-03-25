import math

print("\n Welcome to your AI Career Guide!")
print("Answer a few questions and get career suggestions tailored for you.\n")

careers = [
    {"name": "Software Developer", "logic": 9, "creativity": 6, "management": 5},
    {"name": "UI/UX Designer", "logic": 5, "creativity": 9, "management": 6},
    {"name": "Data Analyst", "logic": 8, "creativity": 5, "management": 6},
    {"name": "Project Manager", "logic": 6, "creativity": 6, "management": 9},
    {"name": "AI Engineer", "logic": 10, "creativity": 7, "management": 6},
    {"name": "Cybersecurity Analyst", "logic": 9, "creativity": 5, "management": 5},
    {"name": "Game Developer", "logic": 8, "creativity": 9, "management": 4},
    {"name": "Entrepreneur", "logic": 7, "creativity": 8, "management": 10},
    {"name": "Business Analyst", "logic": 7, "creativity": 6, "management": 8},
    {"name": "Cloud Engineer", "logic": 9, "creativity": 5, "management": 6},
    {"name": "Digital Marketer", "logic": 5, "creativity": 9, "management": 7},
    {"name": "Research Scientist", "logic": 10, "creativity": 8, "management": 5},
    {"name": "DevOps Engineer", "logic": 9, "creativity": 6, "management": 7},
    {"name": "Product Manager", "logic": 7, "creativity": 7, "management": 9},
    {"name": "Content Creator", "logic": 4, "creativity": 10, "management": 6},
    {"name": "System Administrator", "logic": 8, "creativity": 5, "management": 6}
]

def take_input(text):
    while True:
        try:
            val = int(input(text))
            if 1 <= val <= 10:
                return val
            else:
                print("Please enter a number between 1 and 10")
        except:
            print("Invalid input, try again")

def get_user_profile():
    print("Rate yourself honestly (1 = low, 10 = high)\n")

    return {
        "logic": take_input("Logical Thinking: "),
        "creativity": take_input("Creativity: "),
        "management": take_input("Management Skills: ")
    }

def calculate_distance(user, career):
    return math.sqrt(
        (user["logic"] - career["logic"])**2 +
        (user["creativity"] - career["creativity"])**2 +
        (user["management"] - career["management"])**2
    )

def get_sorted_careers(user):
    scores = []

    for c in careers:
        dist = calculate_distance(user, c)
        scores.append((c["name"], dist))

    scores.sort(key=lambda x: x[1])
    return scores

def explain_strengths(user):
    reasons = []

    if user["logic"] >= 8:
        reasons.append("you have strong logical thinking")
    if user["creativity"] >= 8:
        reasons.append("you are highly creative")
    if user["management"] >= 8:
        reasons.append("you have good leadership and management skills")

    if reasons:
        return " and ".join(reasons)
    else:
        return "you have a balanced skill set"

def show_results():
    user = get_user_profile()
    sorted_list = get_sorted_careers(user)

    top3 = sorted_list[:3]
    worst2 = sorted_list[-2:]

    print("\n Here are some careers that match your profile:\n")

    for i in range(len(top3)):
        print(i + 1, ".", top3[i][0])

    best = top3[0][0]

    print("\n Best Fit For You:")
    print(f"{best}")

    print("\n Why this suits you:")
    print(f"- Because {explain_strengths(user)}.")

    print("\n You may also explore:")
    for name, _ in top3[1:]:
        print(f"- {name}")

    print("\n You may find these challenging (for now):")
    for name, _ in worst2:
        print(f"- {name}")

    print("\n Tip:")
    print("Skills can always be improved. Don't limit yourself — explore and grow!")

def show_menu():
    while True:
        print("\n===== MENU =====")
        print("1. View Career Options")
        print("2. Get Career Recommendations")
        print("3. Exit")

        choice = input("Enter choice: ")
        
        if choice == "1":
            print("\nAvailable Career Options:\n")
            for i in range(len(careers)):
                print(i + 1, ". ", careers[i]["name"])
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Good luck for your future!")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    show_menu()
