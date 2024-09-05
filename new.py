import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Gradebook Form")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
        self.student_id_field = tk.Entry(self)
        self.student_id_field.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Student Name:").grid(row=1, column=0, padx=10, pady=10)
        self.student_name_field = tk.Entry(self)
        self.student_name_field.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Grade:").grid(row=2, column=0, padx=10, pady=10)
        self.grade_field = tk.Entry(self)
        self.grade_field.grid(row=2, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def submit_data(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='mydatabase',
                user='root',
                password='Raunit@123'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                sql = "INSERT INTO students (student_id, student_name, grade) VALUES (%s, %s, %s)"
                values = (
                    self.student_id_field.get(),
                    self.student_name_field.get(),
                    self.grade_field.get()
                )
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                connection.close()
                messagebox.showinfo("Success", "Data submitted successfully!")
        except Error as e:
            messagebox.showerror("Error", f"Error submitting data: {e}")

if __name__ == "__main__":
    app = Login()
    app.mainloop()
