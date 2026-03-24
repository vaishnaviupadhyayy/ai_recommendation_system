# AI Recommendation & Decision System

## Overview:

Welcome to the AI Recommendation & Decision System! This project is a simple yet powerful command-line application built using Python that simulates how intelligent systems make decisions.

It was designed to solve a common real-world problem: confusion while choosing the right career path. The system acts like a smart assistant — it takes user preferences as input, analyzes them against a dataset, and recommends the most suitable career option.

This project demonstrates how basic AI concepts like decision-making, similarity calculation, and recommendation systems work in practice.

---

## Features

Intelligent Recommendation:
The system compares your skills (logic, creativity, management) with predefined career data and suggests the best match.

Real Dataset:
Includes multiple career options such as Software Developer, AI Engineer, Data Analyst, Entrepreneur, and more.

Feature-Based Matching:
Instead of random suggestions, the system uses similarity scoring to find the closest match.

Menu-Driven Interface:
Simple and user-friendly menu system for smooth interaction.

Dynamic Output:
Displays the best career option along with a similarity score.

Lightweight & Fast:
Runs instantly in the terminal without requiring any external libraries.

---

## AI Concepts Used

- Intelligent Agent (takes input → processes → gives decision)
- Decision Making System
- Recommendation System
- Feature-Based Similarity
- Basic Machine Learning (Rule-Based Approach)

---

## Technologies/Tools Used

Python 3:
The entire system is implemented using clean and structured Python code.

Core Python Concepts:
- Dictionaries (to store dataset)
- Functions (modular design)
- Loops & Conditions (logic building)

No External Libraries:
The project runs using only built-in Python features.

---

## How the System Works

1. The system stores a dataset of career options.
2. Each option has features like:
   - Logical Thinking
   - Creativity
   - Management Skills
3. The user enters their own skill ratings.
4. The system compares user input with dataset values.
5. It calculates similarity using difference scoring.
6. The closest match is selected and displayed.

---

## Steps to Install & Run the Project

### Prerequisites:
- Python 3 installed on your system

### Run the Program:

1. Save the code in a file named:
   main.py

2. Open terminal / command prompt

3. Run the program.


---

## Instructions for Testing

Follow these steps to verify the system works correctly:

### 1. Normal Recommendation

- Choose option 2 (Get Recommendation)
- Enter:
  - Logical Thinking: 8
  - Creativity: 6
  - Management Skills: 5

Expected Result:
System should suggest a career like Software Developer or Data Analyst.

---

### 2. Different Input Test

- Try different values like:
  - Logic: 5
  - Creativity: 9
  - Management: 7

Expected Result:
System should suggest creative roles like UI/UX Designer or Digital Marketer.

---

### 3. Menu Navigation Test

- Try all menu options:
  - View dataset
  - Get recommendation
  - Explanation

Expected Result:
System should work smoothly without crashing.

---

## Example Output
Best Career Option: Software Developer
Similarity Score: 1



