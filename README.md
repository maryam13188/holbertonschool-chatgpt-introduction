
# Holberton School ChatGPT Introduction Project

## 📋 Project Overview
This project demonstrates the integration of Artificial Intelligence (ChatGPT) into software development practices, focusing on debugging and automation tasks. Through hands-on exercises, students learn to leverage AI for identifying bugs, documenting code, and implementing error handling.

## 🎯 Learning Objectives

### **Debugging Skills**
- Use ChatGPT to identify and correct coding errors
- Develop problem-solving skills across multiple programming languages
- Understand common programming pitfalls and their solutions

### **Automation Proficiency**
- Generate boilerplate code and documentation with AI assistance
- Automate repetitive coding tasks
- Implement AI-driven solutions for software development challenges

## 📁 Project Structure

| Path | File Name | Description | Status |
|------|-----------|-------------|--------|
| `debugging/` | `factorial.py` | Fixed infinite loop in factorial calculation | ✅ Completed |
| `debugging/` | `print_arguments.py` | Print command line arguments (fixed) | ✅ Completed |
| `debugging/` | `change_background.html` | HTML/JS background color changer (fixed) | ✅ Completed |
| `debugging/` | `mines.py` | Minesweeper with win detection (fixed) | ✅ Completed |
| `debugging/` | `factorial_recursive.py` | Recursive factorial with documentation | ✅ Completed |
| `debugging/` | `checkbook.py` | Checkbook with error handling (fixed) | ✅ Completed |
| `debugging/` | `tic.py` | Tic Tac Toe with multiple bug fixes | ✅ Completed |
| `automation/` | | Automation tasks | ⏳ Future |
| `best_practices/` | | Best practices documentation | ⏳ Future |



## 🛠️ Tasks Completed

### **1. Python Factorial Debugging**
- **File:** `factorial.py`
- **Bug:** Infinite loop in factorial calculation
- **Fix:** Added `n -= 1` inside while loop
- **AI Use:** ChatGPT identified missing decrement operation

### **2. Python Arguments Debugging**
- **File:** `print_arguments.py`
- **Bug:** Printing script name along with arguments
- **Fix:** Changed `range(len(sys.argv))` to `sys.argv[1:]`
- **AI Use:** ChatGPT suggested slicing to skip script name

### **3. HTML/Javascript Debugging**
- **File:** `change_background.html`
- **Bug:** Invalid HTML structure and JavaScript errors
- **Fix:** Added proper HTML tags and fixed color generation
- **AI Use:** ChatGPT provided corrected HTML/JS structure

### **4. Python Minesweeper Debugging**
- **File:** `mines.py`
- **Bug:** No win condition detection
- **Fix:** Added `check_win()` method and win tracking
- **AI Use:** ChatGPT helped implement win detection logic

### **5. Python Factorial Documentation**
- **File:** `factorial_recursive.py`
- **Task:** Add comprehensive documentation
- **Features:** Docstring with parameters, returns, examples
- **AI Use:** ChatGPT generated professional documentation

### **6. Python Checkbook Error Handling**
- **File:** `checkbook.py`
- **Bug:** Program crashes on invalid input
- **Fix:** Added `try-except` blocks and input validation
- **AI Use:** ChatGPT suggested error handling patterns

### **7. Tic Tac Toe Debugging**
- **File:** `tic.py`
- **Bugs:** 
  - Wrong winner announcement
  - No tie detection
  - Crashes on invalid input
  - Board formatting issues
- **Fix:** Multiple corrections including proper win checking and input validation
- **AI Use:** ChatGPT identified all bugs and provided fixes

## 🧪 Testing Commands

```bash
# Test factorial fix
./debugging/factorial.py 5      # Should print: 120

# Test arguments printing
./debugging/print_arguments.py 1 2 3  # Should print only: 1, 2, 3

# Test Tic Tac Toe
./debugging/tic.py              # Play complete game

# Test checkbook
./debugging/checkbook.py        # Test with invalid inputs

# Test minesweeper
./debugging/mines.py            # Try to win the game
```
----
## 🤖 ChatGPT Prompts Used
## For Debugging:

```
"I have this code with a bug: [paste code]
The problem is: [describe issue]
Can you help identify and fix the bug?"
```
## For Documentation:
```
"Please add comprehensive documentation to this Python function:
Include function description, parameters, returns, and examples."
``` 
## For Error Handling:
```
"Add error handling to prevent crashes from invalid user input.
Include try-except blocks and validation for edge cases."
```
## 💡 Key Learnings
AI as Debugging Assistant: ChatGPT excels at identifying common programming errors

Clear Problem Description: The quality of AI help depends on how clearly you describe the problem

Verification is Crucial: Always test AI-suggested solutions

Documentation Matters: AI can generate excellent documentation from well-structured code

Error Prevention: Proactive error handling improves software robustness

## 🚀 Skills Developed
Debugging: Identifying and fixing bugs with AI assistance

Documentation: Creating professional code documentation

Error Handling: Implementing robust input validation

AI Integration: Leveraging ChatGPT for coding tasks

Problem Solving: Breaking down complex problems into manageable tasks

## 📚 Best Practices Demonstrated
Code Testing: Always test after implementing AI suggestions

Version Control: Use Git to track changes and revert if needed

Code Review: Critical evaluation of AI-generated code

Modular Design: Keeping code organized and maintainable

User Experience: Creating friendly error messages and interfaces

 ## Contributor
 Maryam Alessa
