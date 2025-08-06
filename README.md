# Winter 2025 Assignment 2
# 📘 GPA Tracker (Command-Line Tool)

A lightweight command-line tool for tracking your course grades, calculating your GPA, and listing passed courses. Built using Python and `argparse`.

---

## 🚀 Features

- ✅ Add a course and grade
- 📊 Calculate GPA
- 🟢 List all passed courses (≥ 50%)
- 💾 Persistent data storage (JSON file)
- 🧩 Easy-to-use CLI with `argparse`

---

## 🧰 Requirements

- Python 3.x  
- No external libraries needed

---

## 📥 Installation

1. Download the script:

   ```bash
   wget https://yourdomain-or-repo.com/gpa_tracker.py
   ```

2. (Optional) Make it executable:

   ```bash
   chmod +x gpa_tracker.py
   ```

---

## 🧪 Usage

### ➕ Add a course

```bash
python3 gpa_tracker.py --add "CourseName" Grade
```

**Example:**

```bash
python3 gpa_tracker.py --add "Math" 80
```

### 🎓 Calculate GPA

```bash
python3 gpa_tracker.py --gpa
```

### ✅ Show passed courses

```bash
python3 gpa_tracker.py --passed
```

---

## 📂 Example Session

```bash
$ python3 gpa_tracker.py --add "Math" 80
✅ Added: Math with grade 80%

$ python3 gpa_tracker.py --add "History" 60
✅ Added: History with grade 60%

$ python3 gpa_tracker.py --gpa
🎓 GPA: 70.00%

$ python3 gpa_tracker.py --passed
✅ Passed Courses:
  - Math (80.0%)
  - History (60.0%)
```

---

## 💾 Data Storage

The script creates a file named `gpa_data.json` in the same directory to store all your courses and grades.

To reset your data:

```bash
rm gpa_data.json
```

---

## 🔧 Future Improvements (Suggestions)

* `--list`: Show all courses and grades
* `--update COURSE NEW_GRADE`: Modify a grade
* `--remove COURSE`: Delete a course
* Convert to 4.0 GPA scale
* Export to CSV

---

## 👨‍💻 Author

Made with 💡 by Aisha Jamal Jeniya

---

## 📝 License

MIT License
