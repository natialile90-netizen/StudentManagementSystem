# სტუდენტების მონაცემების შენახვა და ჩატვირთვა

import json
import os

from student import Student


# მონაცემების შენახვის და ჩატვირთვის კლასი
class Storage:

    # ფაილის მისამართის განსაზღვრა
    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "students.json"
        )

    # სტუდენტების მონაცემების შენახვა JSON ფაილში
    def save_students(self, students):
        try:
            data = []

            for student in students:
                student_data = {
                    "name": student.name,
                    "surname": student.surname,
                    "age": student.age,
                    "roll_number": student.roll_number,
                    "course": student.course,
                    "grades": student.grades
                }

                data.append(student_data)

            # მონაცემების ჩაწერა ფაილში
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            print("მონაცემები წარმატებით შეინახა!")
            return True

        # შენახვის დროს შეცდომის დამუშავება
        except (OSError, TypeError, ValueError) as error:
            print("მონაცემების შენახვის შეცდომა:", error)
            return False

    # სტუდენტების მონაცემების ჩატვირთვა JSON ფაილიდან
    def load_students(self):
        try:

            # ფაილის გახსნა და მონაცემების წაკითხვა
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # შემოწმება, რომ მონაცემები სიის სახით იყოს
            if not isinstance(data, list):
                raise ValueError("JSON ფაილში უნდა იყოს სია!")

            loaded_students = []

            # ფაილიდან წაკითხული სტუდენტების დამუშავება
            for index, student_data in enumerate(data, 1):
                roll_number = student_data.get("roll_number")

                # ძველი სტუდენტისთვის ნომრის მინიჭება, თუ არ აქვს
                if not roll_number:
                    roll_number = "OLD-" + str(index)

                # კურსის მიღება ან საწყისი მნიშვნელობის მინიჭება
                course = student_data.get(
                    "course",
                    "არ არის არჩეული"
                )

                # სტუდენტის ობიექტის შექმნა
                student = Student(
                    student_data["name"],
                    student_data["surname"],
                    student_data["age"],
                    str(roll_number),
                    course
                )

                # სტუდენტის შეფასებების ჩატვირთვა
                student.grades = student_data.get("grades", [])

                # სტუდენტის დამატება ჩატვირთულ სიაში
                loaded_students.append(student)

            print("მონაცემები წარმატებით ჩაიტვირთა!")
            return loaded_students

        # თუ JSON ფაილი არ არსებობს
        except FileNotFoundError:
            print("შენახული მონაცემები არ მოიძებნა!")
            return []

        # ჩატვირთვის დროს სხვა შეცდომების დამუშავება
        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
            AttributeError,
            OSError
        ) as error:
            print("მონაცემების ჩატვირთვის შეცდომა:", error)
            return None
