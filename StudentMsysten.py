import tkinter as tk
from tkinter import messagebox

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")


        self.title_label = tk.Label(self.root, text="Student Management System", font=("Helvetica", 24), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.frame1 = tk.Frame(self.root, bg="#d9d9d9", padx=10, pady=10)
        self.frame1.pack(fill="x", padx=20, pady=5)

        self.frame2 = tk.Frame(self.root, bg="#d9d9d9", padx=10, pady=10)
        self.frame2.pack(fill="x", padx=20, pady=5)

        self.frame3 = tk.Frame(self.root, bg="#d9d9d9", padx=10, pady=10)
        self.frame3.pack(fill="both", expand=True, padx=20, pady=5)

        self.label2 = tk.Label(self.frame1, text="Name:", bg="#d9d9d9", font=("Helvetica", 14))
        self.label2.pack(side="left", padx=10, pady=10)

        self.name_entry = tk.Entry(self.frame1, width=20, font=("Helvetica", 14))
        self.name_entry.pack(side="left", padx=10, pady=10)
        
        self.label1 = tk.Label(self.frame1, text="Roll No:", bg="#d9d9d9", font=("Helvetica", 14))
        self.label1.pack(side="left", padx=10, pady=10)

        self.roll_no_entry = tk.Entry(self.frame1, width=20, font=("Helvetica", 14))
        self.roll_no_entry.pack(side="left", padx=10, pady=10)


        self.buttons_frame = tk.Frame(self.frame2, bg="#d9d9d9")
        self.buttons_frame.pack(anchor="center", pady=10)

        self.add_button = tk.Button(self.buttons_frame, text="➕ Add", font=("Helvetica", 14), command=self.add_student, bg="#4CAF50", fg="white")
        self.add_button.pack(side="left", padx=10)

        self.update_button = tk.Button(self.buttons_frame, text="✏️ Update", font=("Helvetica", 14), command=self.update_student, bg="#2196F3", fg="white")
        self.update_button.pack(side="left", padx=10)

        self.delete_button = tk.Button(self.buttons_frame, text="❌ Delete", font=("Helvetica", 14), command=self.delete_student, bg="#f44336", fg="white")
        self.delete_button.pack(side="left", padx=10)

        self.view_button = tk.Button(self.buttons_frame, text="👁️ View", font=("Helvetica", 14), command=self.view_students, bg="#9C27B0", fg="white")
        self.view_button.pack(side="left", padx=10)

        self.listbox_frame = tk.Frame(self.frame3, bg="#d9d9d9")
        self.listbox_frame.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(self.listbox_frame, width=50, font=("Helvetica", 14))
        self.listbox.pack(side="left", fill="both", expand=True, pady=10)

        self.scrollbar = tk.Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.students = []

    def add_student(self):
        roll_no = self.roll_no_entry.get()
        name = self.name_entry.get()

        if roll_no and name:
            self.students.append({"roll_no": roll_no, "name": name})
            self.listbox.insert("end", f"Roll No: {roll_no}, Name: {name}")
            self.roll_no_entry.delete(0, "end")
            self.name_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def update_student(self):
        roll_no = self.roll_no_entry.get()
        name = self.name_entry.get()

        if roll_no and name:
            for student in self.students:
                if student["roll_no"] == roll_no:
                    student["name"] = name
                    self.listbox.delete(0, "end")
                    for student in self.students:
                        self.listbox.insert("end", f"Roll No: {student['roll_no']}, Name: {student['name']}")
                    self.roll_no_entry.delete(0, "end")
                    self.name_entry.delete(0, "end")
                    return
            messagebox.showerror("Error", "Student not found")
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def delete_student(self):
        roll_no = self.roll_no_entry.get()

        if roll_no:
            for student in self.students:
                if student["roll_no"] == roll_no:
                    self.students.remove(student)
                    self.listbox.delete(0, "end")
                    for student in self.students:
                        self.listbox.insert("end", f"Roll No: {student['roll_no']}, Name: {student['name']}")
                    self.roll_no_entry.delete(0, "end")
                    self.name_entry.delete(0, "end")
                    return
            messagebox.showerror("Error", "Student not found")
        else:
            messagebox.showerror("Error", "Please fill roll no field")

    def view_students(self):
        self.listbox.delete(0, "end")
        for student in self.students:
            self.listbox.insert("end", f"Roll No: {student['roll_no']}, Name: {student['name']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
