# შეყვანილი მონაცემების შემოწმება


# მონაცემების შემოწმების კლასი
class Validation:

    # სახელის და გვარის შემოწმება
    def validate_name(self, name):
        name = name.strip()

        # ცარიელი სახელის შემოწმება
        if not name:
            return False

        # შემოწმება, რომ სახელი მხოლოდ ასოებისგან შედგებოდეს
        return all(
            part.isalpha()
            for part in name.split()
        )

    # ასაკის შემოწმება
    def validate_age(self, age):

        # შემოწმება, რომ ასაკი მხოლოდ ციფრებით იყოს შეყვანილი
        if not age.isdigit():
            return False

        age = int(age)

        # ასაკი უნდა იყოს 16-დან 70 წლამდე
        return 16 <= age <= 70

    # სტუდენტის ნომრის შემოწმება
    def validate_roll_number(self, roll_number):

        # სტუდენტის ნომერი მხოლოდ ციფრებს უნდა შეიცავდეს
        return roll_number.isdigit()

    # შეფასების შემოწმება
    def validate_grade(self, grade):

        # შემოწმება, რომ შეფასება მხოლოდ ციფრებით იყოს შეყვანილი
        if not grade.isdigit():
            return False

        grade = int(grade)

        # შეფასება უნდა იყოს 0-დან 100-მდე
        return 0 <= grade <= 100
