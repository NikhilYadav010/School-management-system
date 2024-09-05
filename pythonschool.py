import mysql.connector
from mysql.connector import Error

class Gradebook:
    JDBC_URL = "localhost"
    DATABASE = "author_01"
    USERNAME = "root"
    PASSWORD = "Raunit@123"

    @staticmethod
    def connect():
        try:
            connection = mysql.connector.connect(
                host=Gradebook.JDBC_URL,
                database=Gradebook.DATABASE,
                user=Gradebook.USERNAME,
                password=Gradebook.PASSWORD
            )
            return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    @staticmethod
    def disconnect(connection, cursor):
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    @staticmethod
    def insert_student_record(student_id, student_name, grade):
        connection = None
        cursor = None
        try:
            connection = Gradebook.connect()
            if connection is None:
                return

            query = "INSERT INTO stu_d (student_id, student_name, grade) VALUES (%s, %s, %s)"
            cursor = connection.cursor()
            cursor.execute(query, (student_id, student_name, grade))
            connection.commit()

            if cursor.rowcount > 0:
                print("Student record inserted successfully.")
            else:
                print("Failed to insert student record.")
        except Error as e:
            print(f"Error while inserting student record: {e}")
        finally:
            Gradebook.disconnect(connection, cursor)

    @staticmethod
    def get_student_grades():
        connection = None
        cursor = None
        try:
            connection = Gradebook.connect()
            if connection is None:
                return

            query = "SELECT student_id, student_name, grade FROM stu_d"
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()

            for row in records:
                student_id = row[0]
                student_name = row[1]
                grade = row[2]
                print(f"Student ID: {student_id}, Name: {student_name}, Grade: {grade}")
        except Error as e:
            print(f"Error while fetching student grades: {e}")
        finally:
            Gradebook.disconnect(connection, cursor)

if __name__ == "__main__":
    import sys
    student_id = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")
    grade = float(input("Enter Grade: "))
    Gradebook.insert_student_record(student_id, student_name, grade)
    print("\nStudent Records: \n")
    Gradebook.get_student_grades()
