from flask import Flask, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = './attendance_data'
EXCEL_FILE = os.path.join(UPLOAD_FOLDER, 'attendance.xlsx')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize the Excel file if it doesn't exist
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Student ID", "Name", "Date", "Status"])
    df.to_excel(EXCEL_FILE, index=False)

# Simulate a database of registered students
STUDENT_DB = {
    "12345": "Alice",
    "67890": "Bob",
    "11121": "Charlie"
}

# Route for Laptop Fingerprint Authentication
@app.route('/laptop-auth', methods=['POST'])
def laptop_auth():
    data = request.json
    student_id = data.get("studentId")
    if not student_id or student_id not in STUDENT_DB:
        return jsonify({"message": "Authentication failed"}), 403

    student_name = STUDENT_DB[student_id]
    mark_attendance(student_id, student_name, "Present")
    return jsonify({"message": f"{student_name} marked as present"}), 200

# Route for Hardware Fingerprint Authentication
@app.route('/hardware-auth', methods=['POST'])
def hardware_auth():
    data = request.json
    student_id = data.get("studentId")
    if not student_id or student_id not in STUDENT_DB:
        return jsonify({"message": "Authentication failed"}), 403

    student_name = STUDENT_DB[student_id]
    mark_attendance(student_id, student_name, "Present")
    return jsonify({"message": f"{student_name} marked as present"}), 200

def mark_attendance(student_id, student_name, status):
    """Update attendance in the Excel file."""
    date_today = datetime.now().strftime("%Y-%m-%d")
    new_entry = {"Student ID": student_id, "Name": student_name, "Date": date_today, "Status": status}
    try:
        df = pd.read_excel(EXCEL_FILE)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
    except Exception as e:
        print(f"Error updating Excel: {e}")

if __name__ == '__main__':
    app.run(debug=True)
