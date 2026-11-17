# სტუდენტების შეფასებების მართვა

from validation import Validation


# შეფასებების მართვის კლასი
class GradeManager:

    # საჭირო ობიექტების შექმნა
    def __init__(self, student_manager):
        self.student_manager = student_manager
        self.validation = Validation()

    # სტუდენტისთვის შეფასების დამატება
    def add_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        # სტუდენტის მოძებნა
        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        grade = input("შეიყვანეთ შეფასება (0-100): ").strip()

        # შეფასების შემოწმება
        if not self.validation.validate_grade(grade):
            print("შეფასება უნდა იყოს 0-დან 100-მდე!")
            return

        # შეფასების დამატება და შენახვა
        try:
            student.grades.append(int(grade))

            if self.student_manager.save():
                print("შეფასება წარმატებით დაემატა!")
            else:
                print("შეფასება დაემატა, მაგრამ ფაილში ვერ შეინახა!")

        except (ValueError, TypeError) as error:
            print("შეფასების დამატების შეცდომა:", error)

    # შეფასების მიხედვით შედეგის განსაზღვრა
    def grade_category(self, grade):
        if grade >= 91:
            return "შესანიშნავი"
        elif grade >= 81:
            return "ძალიან კარგი"
        elif grade >= 71:
            return "კარგი"
        elif grade >= 61:
            return "დამაკმაყოფილებელი"
        elif grade >= 51:
            return "ჩაბარებული"
        else:
            return "არადამაკმაყოფილებელი"

    # სტუდენტის საშუალო შეფასების ნახვა
    def average_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        # სტუდენტის მოძებნა
        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        # შემოწმება, აქვს თუ არა სტუდენტს შეფასებები
        if not student.grades:
            print("სტუდენტს შეფასებები არ აქვს!")
            return

        # საშუალო შეფასების გამოთვლა
        try:
            average = student.get_average()

            print("სტუდენტი:", student.name, student.surname)
            print("კურსი:", student.course)
            print("შეფასებები:", student.grades)
            print("საშუალო შეფასება:", round(average, 2))
            print("შედეგი:", self.grade_category(average))

            # შემოწმება, ჩააბარა თუ არა სტუდენტმა
            if average >= 51:
                print("სტატუსი: ჩაბარებული")
            else:
                print("სტატუსი: ჩაჭრილი")

        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("საშუალო შეფასების გამოთვლის შეცდომა:", error)

    # სტუდენტის შეფასების შეცვლა
    def edit_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        # სტუდენტის მოძებნა
        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        if not student.grades:
            print("სტუდენტს შეფასებები არ აქვს!")
            return

        # სტუდენტის შეფასებების ჩვენება ნომრებით
        for index, grade in enumerate(student.grades, 1):
            print(index, "-", grade)

        choice = input(
            "აირჩიეთ შესაცვლელი შეფასების ნომერი: "
        ).strip()

        # არჩეული ნომრის შემოწმება
        if not choice.isdigit():
            print("არასწორი ნომერი!")
            return

        choice = int(choice)

        if choice < 1 or choice > len(student.grades):
            print("არასწორი ნომერი!")
            return

        new_grade = input(
            "შეიყვანეთ ახალი შეფასება (0-100): "
        ).strip()

        # ახალი შეფასების შემოწმება
        if not self.validation.validate_grade(new_grade):
            print("შეფასება უნდა იყოს 0-დან 100-მდე!")
            return

        # ძველი შეფასების ახლით შეცვლა
        try:
            student.grades[choice - 1] = int(new_grade)

            if self.student_manager.save():
                print("შეფასება წარმატებით შეიცვალა!")
            else:
                print("შეფასება შეიცვალა, მაგრამ ფაილში ვერ შეინახა!")

        except (ValueError, TypeError, IndexError) as error:
            print("შეფასების შეცვლის შეცდომა:", error)

    # სტუდენტის შეფასების წაშლა
    def delete_grade(self):
        roll_number = input(
            "შეიყვანეთ სტუდენტის ნომერი: "
        ).strip()

        # სტუდენტის მოძებნა
        student = self.student_manager.find_student(roll_number)

        if not student:
            print("სტუდენტი ვერ მოიძებნა!")
            return

        if not student.grades:
            print("სტუდენტს შეფასებები არ აქვს!")
            return

        # შეფასებების ჩვენება ნომრებით
        for index, grade in enumerate(student.grades, 1):
            print(index, "-", grade)

        choice = input(
            "აირჩიეთ წასაშლელი შეფასების ნომერი: "
        ).strip()

        # არჩეული ნომრის შემოწმება
        if not choice.isdigit():
            print("არასწორი ნომერი!")
            return

        choice = int(choice)

        if choice < 1 or choice > len(student.grades):
            print("არასწორი ნომერი!")
            return

        # შეფასების წაშლა და ცვლილების შენახვა
        try:
            student.grades.pop(choice - 1)

            if self.student_manager.save():
                print("შეფასება წარმატებით წაიშალა!")
            else:
                print("შეფასება წაიშალა, მაგრამ ფაილში ვერ შეინახა!")

        except (IndexError, TypeError) as error:
            print("შეფასების წაშლის შეცდომა:", error)
