# სტუდენტის მონაცემების და შეფასებების მართვა


# ძირითადი მონაცემები
class Person:

    #ადამიანის სახელის, გვარის და ასაკის შენახვა
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # ადამიანის ინფორმაციის ჩვენება
    def show_info(self):
        print("სახელი:", self.name)
        print("გვარი:", self.surname)
        print("ასაკი:", self.age)


# სტუდენტის კლასი, რომელიც Person კლასის მონაცემებს იყენებს
class Student(Person):

    # სტუდენტის მონაცემების შექმნა
    def __init__(self, name, surname, age, roll_number, course):
        super().__init__(name, surname, age)

        self.roll_number = roll_number
        self.course = course
        self._grades = []

    # სტუდენტის შეფასებების მიღება
    @property
    def grades(self):
        return self._grades

    # ახალი შეფასებების შემოწმება და შენახვა
    @grades.setter
    def grades(self, new_grades):
        if not isinstance(new_grades, list):
            raise ValueError("შეფასებები უნდა იყოს სიაში!")

        # ყველა შეფასების შემოწმება
        for grade in new_grades:
            if type(grade) != int or grade < 0 or grade > 100:
                raise ValueError("შეფასება უნდა იყოს 0-დან 100-მდე!")

        self._grades = new_grades

    # საშუალო შეფასების გამოთვლა
    def get_average(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    # სტუდენტის სრული ინფორმაციის ჩვენება
    def show_info(self):
        print("სტუდენტის ნომერი:", self.roll_number)

        super().show_info()

        print("კურსი:", self.course)
        print("შეფასებები:", self.grades)

        # საშუალო შეფასების ჩვენება, თუ სტუდენტს შეფასებები აქვს
        if self.grades:
            print("საშუალო შეფასება:", round(self.get_average(), 2))
        else:
            print("საშუალო შეფასება: შეფასებები არ აქვს")

        print("-" * 45)