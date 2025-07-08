import os

readmes = {
    "README.md": """# 🏫 BYU Software Development Projects

This repository contains all the academic projects developed during my studies at BYU–Idaho / BYU Pathway Worldwide, organized by course and semester.

## 📚 Courses

### ✅ Current Courses
- [CSE 111 – Programming with Functions (Python)](./cse111-programming-functions/)
- [WDD 130 – Web Fundamentals](./wdd130-web-fundamentals/)

### 📦 Previous Courses
- [CSE 110 – Introduction to Programming](./cse110-intro-to-programming/)
- [WDD 100 – Intro to Web Design](./wdd100-intro-to-web/)

---

Each course folder is organized by week and includes assignments, exercises, and final projects.

> 🔄 This repository will be updated throughout my academic progress.
""",
    "cse111-programming-functions/README.md": """# CSE 111 – Programming with Functions (Python)

This course builds on the basics of Python programming with a strong focus on writing and organizing code using functions. It covers logic structures, modular programming, and best practices.

## 📅 Weekly Topics

- Week 01 – Function Basics and Syntax
- Week 02 – Conditionals and Loops
- Week 03 – Lists and Collections
- Week 04 – Custom Functions and Parameters
- Week 05 – Files and Data Structures
- Final Project – Functional Python Application

## 🎯 Objective

To master core programming skills in Python using structured, modular, and reusable code.
""",
    "wdd130-web-fundamentals/README.md": """# WDD 130 – Web Fundamentals

This course introduces the core principles of front-end web development. It includes HTML structure, CSS styling, and basic responsive design techniques.

## 📅 Weekly Topics

- Week 01 – Basic HTML Elements
- Week 02 – Introduction to CSS
- Week 03 – Links, Images, and Lists
- Week 04 – Flexbox, Layout, and Media Queries
- Final Project – Personal Website

## 🎯 Objective

To develop well-structured and visually appealing websites using standard HTML and CSS techniques.
""",
    "cse110-intro-to-programming/README.md": """# CSE 110 – Introduction to Programming

This foundational course teaches the basics of programming using Python. It covers input/output, variables, conditionals, loops, and basic problem-solving.

## 📅 Weekly Topics

- Week 01 – Input, Output, and Variables
- Week 02 – If Statements and Boolean Logic
- Week 03 – Loops: for and while
- Week 04 – Organizing Code
- Weekly Practice Projects

## 🎯 Objective

To develop computational thinking skills and basic programming logic using Python.
""",
    "wdd100-intro-to-web/README.md": """# WDD 100 – Intro to Web Design

An introductory course covering the structure of websites and the fundamentals of web development. Great for those with little or no previous experience.

## 📅 Weekly Topics

- Week 01 – Understanding Web Pages
- Week 02 – HTML Basics
- Week 03 – Basic Design Principles
- Final Project – Simple Personal Web Page

## 🎯 Objective

To understand the foundation of web development and how to create a basic but functional website layout.
"""
}

# Crear los archivos y carpetas si no existen
for path, content in readmes.items():
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ All README.md files created successfully!")
