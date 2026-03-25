# AI Career Recommendation System

## Project Overview
This project presents a simple AI-based Career Recommendation System.

The system suggests suitable career paths based on a user's skill profile, focusing on logical thinking, creativity, and management abilities.

---

## Problem Statement
Choosing the right career path is a common challenge among students. Many lack clarity about which field aligns with their strengths.

This project aims to address this problem by providing personalized career suggestions using a basic AI-driven approach.

---

## Methodology
Each career is represented using three features:
- Logical Thinking
- Creativity
- Management Skills

The user provides their skill levels on the same scale.

The system then:
1. Compares user input with all career profiles
2. Calculates similarity using a distance formula
3. Sorts careers based on closeness
4. Recommends the best matching options

---

## AI Concepts Applied
- **Intelligent Agent**: Takes input and produces output based on logic  
- **State Space Representation**: Each career is a possible state  
- **Search Technique**: Linear search through all options  
- **Feature Vector Representation**: Skills represented numerically  
- **Decision-Making Strategy**: Selecting minimum difference  

---

## Features
- Command-line based interactive system  
- User-friendly input handling  
- Top 3 career recommendations  
- Final best-fit suggestion  
- Basic explanation of results  

---

## Tech Stack
- Python 3

---

## How to Run

1. Clone the repository:
git clone (https://github.com/vaishnaviupadhyayy/ai_recommendation_system)

2. Navigate to the folder:

cd ai-career-recommendation-system

3. Run the program:

python main.py

---

## Sample Output

 Welcome to your AI Career Guide!
Answer a few questions and get career suggestions tailored for you.


===== MENU =====
1. View Career Options
2. Get Career Recommendations
3. Exit
Enter choice: 2
Rate yourself honestly (1 = low, 10 = high)

Logical Thinking: 7
Creativity: 9
Management Skills: 8

Here are some careers that match your profile:

1 . Entrepreneur
2 . Digital Marketer
3 . Product Manager

 Best Fit For You:
Entrepreneur

 Why this suits you:
- Because you are highly creative and you have good leadership and management skills.

 You may also explore:
- Digital Marketer
- Product Manager

 You may find these challenging (for now):
- Cloud Engineer
- Cybersecurity Analyst

 Tip:
Skills can always be improved. Don't limit yourself — explore and grow!

---

## Results
The system successfully provides career recommendations based on user inputs, demonstrating a practical application of AI decision-making techniques.

---

## Future Scope
- Integration with real-world datasets  
- Use of machine learning models (e.g., KNN)  
- Development of a web-based interface  
- Adding more career parameters  

---

## Conclusion
This project demonstrates how fundamental AI concepts can be applied to solve real-world problems in a simple and effective manner.

