# 📝 Project Statement: Simple Command-Line To-Do List Manager

## 🎯 Problem Statement

In the modern workflow, individuals and teams require a quick, straightforward way to track immediate tasks without relying on complex, feature-heavy applications. The existing project addresses the need for a **minimalist, terminal-based utility** that provides core list management functionality—viewing, adding, and deleting items—enabling users to maintain focus and organization directly from their command line interface.

## 🔭 Scope of the Project

This project is currently scoped as a **standalone, single-file Python application** executed in a terminal environment.

| Component | Description |
| :--- | :--- |
| **Data Storage** | The task list is stored in a simple Python list (`tasks`) and **is not persistent**. Data is lost upon program exit. |
| **User Interface** | Purely command-line driven (CLI) via `print()` and `input()`. |
| **Core Functionality** | Restricted to the essential CRUD operations: Create (Add), Read (Show), and Delete. |
| **Error Handling** | Basic input validation to ensure the user enters a valid menu choice or task number. |

**Out of Scope (Potential Future Enhancements):**
* Data persistence (saving to a file like `.txt` or `.json`).
* Editing or marking tasks as complete.
* Task prioritization or sorting.

## 👤 Target Users

* **Beginner Programmers:** Individuals learning Python who need a simple, self-contained project to understand basic functions, lists, loops, and conditional logic.
* **System Administrators/Developers:** Users who
