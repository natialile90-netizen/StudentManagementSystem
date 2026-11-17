#სტუდენტების მართვის პროგრამის მთავარი ფაილი

from student_manager import StudentManager
from grades import GradeManager
from storage import Storage


# პროგრამის მთავარი კლასი
class StudentManagementSystem:

    #ობიექტების შექმნა:მონაცემების შესანახად, სტუდენტების სამართავად,შეფასების სამართავად
    def __init__(self):
        self.storage = Storage()

        self.student_manager = StudentManager(self.storage)

        self.grade_manager = GradeManager(self.student_manager)

    # არჩეული მოქმედების შესრულება
    def show_result(self, title, function):
        print("\n" + "=" * 45)
        print(title.center(45))
        print("=" * 45)

        # შეცდომის შემთხვევაში შეტყობინების ჩვენება
        try:
            function()

        except (ValueError, TypeError, IndexError) as error:
            print("მოქმედების შესრულების შეცდომა:", error)

        print("=" * 45 + "\n")

    # მთავარი მენიუს ჩვენება
    def show_menu(self):
        print("\n===== IT აკადემიის მართვის სისტემა =====")
        print("1. სტუდენტის დამატება")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. სტუდენტის ძებნა")
        print("4. სტუდენტის წაშლა")
        print("5. სტუდენტის მონაცემების შეცვლა")
        print("6. შეფასების დამატება")
        print("7. საშუალო შეფასების ნახვა")
        print("8. სტუდენტების ნახვა კურსის მიხედვით")
        print("9. შეფასების შეცვლა")
        print("10. შეფასების წაშლა")
        print("11. სტუდენტების საერთო რაოდენობა")
        print("12. საუკეთესო სტუდენტი")
        print("13. კურსების სტატისტიკა")
        print("0. გამოსვლა")

    # პროგრამის მუშაობის დაწყება
    def run(self):

        # შენახული სტუდენტების ჩატვირთვა
        loaded_students = self.storage.load_students()

        # თუ ჩატვირთვისას შეცდომაა, პროგრამა ჩერდება
        if loaded_students is None:
            print("პროგრამა შეჩერდა მონაცემების დასაცავად!")
            return

        self.student_manager.students = loaded_students

        # მენიუ მეორდება, სანამ მომხმარებელი არ გამოვა
        while True:
            self.show_menu()

            # მომხმარებლის არჩევანის მიღება
            try:
                choice = input("აირჩიეთ მოქმედება: ").strip()

            except (EOFError, KeyboardInterrupt):
                print("\nპროგრამის შეწყვეტის მოთხოვნა.")
                print("გამოსასვლელად აირჩიეთ 0.")
                continue

            # არჩევანის მიხედვით მოქმედების შესრულება
            if choice == "1":
                self.show_result(
                    "სტუდენტის დამატება",
                    self.student_manager.add_student
                )

            elif choice == "2":
                self.show_result(
                    "სტუდენტების სია",
                    self.student_manager.show_students
                )

            elif choice == "3":
                self.show_result(
                    "სტუდენტის ძებნა",
                    self.student_manager.search_student
                )

            elif choice == "4":
                self.show_result(
                    "სტუდენტის წაშლა",
                    self.student_manager.delete_student
                )

            elif choice == "5":
                self.show_result(
                    "სტუდენტის განახლება",
                    self.student_manager.update_student
                )

            elif choice == "6":
                self.show_result(
                    "შეფასების დამატება",
                    self.grade_manager.add_grade
                )

            elif choice == "7":
                self.show_result(
                    "საშუალო შეფასება",
                    self.grade_manager.average_grade
                )

            elif choice == "8":
                self.show_result(
                    "სტუდენტები კურსის მიხედვით",
                    self.student_manager.show_students_by_course
                )

            elif choice == "9":
                self.show_result(
                    "შეფასების შეცვლა",
                    self.grade_manager.edit_grade
                )

            elif choice == "10":
                self.show_result(
                    "შეფასების წაშლა",
                    self.grade_manager.delete_grade
                )

            elif choice == "11":
                self.show_result(
                    "სტუდენტების რაოდენობა",
                    self.student_manager.total_students
                )

            elif choice == "12":
                self.show_result(
                    "საუკეთესო სტუდენტი",
                    self.student_manager.top_student
                )

            elif choice == "13":
                self.show_result(
                    "კურსების სტატისტიკა",
                    self.student_manager.course_statistics
                )

            # პროგრამიდან გამოსვლა და მონაცემების შენახვა
            elif choice == "0":
                if self.storage.save_students(
                    self.student_manager.students
                ):
                    print("ნახვამდის!")
                    break

                else:
                    print("მონაცემები ვერ შეინახა!")
                    print("სცადეთ თავიდან.")

            # თუ მომხმარებელმა არასწორი ნომერი შეიყვანა
            else:
                print("\nარასწორი არჩევანი! სცადეთ თავიდან.")


# პროგრამის გაშვება
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
