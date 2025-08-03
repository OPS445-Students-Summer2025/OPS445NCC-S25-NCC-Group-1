import argparse
import json
import os

DATA_FILE = 'gpa_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_course(course, grade):
    data = load_data()
    data.append({"course": course, "grade": grade})
    save_data(data)
    print(f"✅ Added: {course} with grade {grade}%")

def calculate_gpa():
    data = load_data()
    if not data:
        print("📭 No courses found.")
        return

    total = 0
    for item in data:
        total += item["grade"]

    gpa = total / len(data)
    print(f"🎓 GPA: {gpa:.2f}%")

def show_passed_courses():
    data = load_data()
    passed = [item for item in data if item["grade"] >= 50]

    if not passed:
        print("❌ No passed courses found.")
        return

    print("✅ Passed Courses:")
    for item in passed:
        print(f"  - {item['course']} ({item['grade']}%)")

def main():
    parser = argparse.ArgumentParser(description="📘 Command-line GPA Tracker")

    parser.add_argument('--add', nargs=2, metavar=('COURSE', 'GRADE'),
                        help='Add a course with its grade (e.g., --add Math 85)')

    parser.add_argument('--gpa', action='store_true',
                        help='Calculate and display GPA')

    parser.add_argument('--passed', action='store_true',
                        help='List all passed courses')

    args = parser.parse_args()

    if args.add:
        course, grade_str = args.add
        try:
            grade = float(grade_str)
            if 0 <= grade <= 100:
                add_course(course, grade)
            else:
                print("⚠️ Grade must be between 0 and 100.")
        except ValueError:
            print("⚠️ Invalid grade format. Use a number.")
    elif args.gpa:
        calculate_gpa()
    elif args.passed:
        show_passed_courses()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
