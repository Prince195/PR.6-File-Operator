# PR.6-File-Operator
 Project: File Operator (Personal Journal System)

 Overview

This project is a Python-based Personal Journal Management System that allows users to create, store, manage, and maintain journal entries using text file handling. The application is designed using Object-Oriented Programming (OOP) principles and demonstrates proper use of file operations along with exception handling to ensure smooth and safe execution.

The system stores all journal data in a single text file and provides a menu-driven interface for user interaction.



 Objectives

To understand and implement file handling operations in Python.

To demonstrate the use of different file opening modes such as read, write, append, and exclusive creation.

To apply Object-Oriented Programming (OOP) concepts using classes and objects.

To handle runtime errors gracefully using exception handling.

To build a menu-driven application for better user interaction.

---

System Design (OOP Structure)

The entire application is encapsulated inside a single class.

All functionalities such as adding, viewing, searching, and deleting journal entries are implemented using instance methods.

This approach ensures encapsulation, modularity, and better code organization.

No external or user-defined functions are used outside the class structure.

 File Handling Description

The application works only with text files (.txt).

All journal entries are stored in a file named journal.txt.

Each journal entry includes:

A timestamp (date and time)

User-provided content

File Modes Used:

Read (r): Used to display or search journal entries.

Append (a): Used to add new entries without removing existing data.

Write (w): Used when recreating the file after deletion.

Exclusive Creation (x): Demonstrates safe file creation logic.

---

 Application Features

1. Add New Entry

Allows the user to write a new journal entry.

The entry is appended to the journal file.

Automatically creates the file if it does not exist.

Each entry is saved with a timestamp.


2. View All Entries

Displays all journal entries stored in the file.

Handles the case where the file does not exist or is empty.


3. Search for an Entry

Allows users to search journal entries using a keyword or date.

Displays all matching entries from the file.

Shows a clear message if no match is found.


4. Delete All Entries

Deletes the entire journal by removing the file.

Requires user confirmation before deletion.

Prevents accidental data loss.


5. Exit Program

Allows the user to safely exit the application from the main menu.

 Exception Handling

Handles errors such as:

File not found

Invalid file access

Permission-related issues

Prevents the program from crashing due to unexpected input or file errors.

Displays clear and user-friendly error messages.


---
