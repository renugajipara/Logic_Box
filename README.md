🚀 Pattern Generator & Number Analyzer

A menu-driven Python console application that allows users to:

⭐ Generate star patterns

🔢 Analyze numbers within a range

➕ Calculate the sum of numbers

❌ Exit safely

This project demonstrates fundamental Python concepts including loops, conditionals, and the modern match-case statement (Python 3.10+).

📌 Project Overview

This application provides two main functionalities:

1️⃣ Pattern Generator

Generates a right-angled triangle star pattern

User defines number of rows

Uses nested loops for pattern logic



2️⃣ Number Analyzer

Accepts a starting and ending range

Identifies numbers as Even or Odd

Calculates total sum of numbers

Validates range condition (start should not be greater than end)



flowchart TD

A([Start Program]) --> B[Display Welcome Message]
B --> C[Show Menu Options]

C --> D{User Choice}

D -->|1| E[Input Number of Rows]
E --> F[Generate Star Pattern using Nested Loops]
F --> C

D -->|2| G[Input Start and End Range]
G --> H{Is Start > End?}

H -->|Yes| I[Display Error Message]
I --> C

H -->|No| J[Check Each Number]
J --> K[Print Even or Odd]
K --> L[Calculate Sum]
L --> C

D -->|3| M([Exit Program])

D -->|Invalid| N[Display Invalid Input]
N --> C

🧠 Concepts Used

while loop (menu-driven program)

match-case (Python 3.10 switch statement)

Nested for loops

Conditional statements

Modulo operator (%)

Range iteration

Basic input validation

🛠 Technologies

Python 3.10+

VS Code (recommended)

📂 Project Structure
pattern-generator-number-analyzer/
│
├── main.py
└── README.md


👩‍💻 Author

RENU
Aspiring Python Developer
Focused on building strong programming fundamentals.
