from main.models import Subject, Teacher, Class, Student, Schedule, Grade


def add_subject():
    print('======= додавання предмету ========')

    name = input("Введіть назву предмету: ")

    if not Subject.objects.filter(name=name).exists():
        Subject.objects.create(name=name)
        print("Предмет додано.")
    else:
        print("Такий предмет вже існує.")

    print('===================================')


def add_teacher():
    print('======= додавання вчителя =======')

    first_name = input("Ім'я вчителя: ")
    last_name = input("Прізвище вчителя: ")
    subject_name = input("Назва предмету: ")
    subject = Subject.objects.filter(name=subject_name).first()

    if subject:
        Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
        print("Вчителя додано.")
    else:
        print("Предмет не знайдено.")

    print('=================================')


def add_class():
    print('======== додавання класу =======')

    name = input("Назва класу (наприклад: 11Б):")

    if not Class.objects.filter(name=name).exists():
        Class.objects.create(name=name)
        print("Клас додано.")
    else:
        print("Такий клас вже існує.")

    print('================================')


def add_student():
    print('======= додавання учня =======')

    first_name = input("Ім'я учня: ")
    last_name = input("Прізвище учня: ")
    class_name = input("Назва класу: ")
    in_class = Class.objects.filter(name=class_name).first()

    if in_class:
        Student.objects.create(first_name=first_name, last_name=last_name, in_class=in_class)
        print("Учня додано.")
    else:
        print("Клас не знайдено.")

    print("==============================")


def add_schedule():
    print("======= додавання заняття =======")

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print("Доступні дні: ", ', '.join(days_of_week))

    day_of_week = input("Виберіть день тижня: ")

    if day_of_week not in days_of_week:
        print("Неправильний вибір дня тижня.")
        return

    start_time = input("Час початку (HH:MM): ")

    subject_name = input("Назва предмету: ")
    subject = Subject.objects.filter(name=subject_name).first()

    if not subject:
        print("Предмет не знайдено.")
        return

    class_name = input("Назва класу: ")
    in_class = Class.objects.filter(name=class_name).first()

    if not in_class:
        print("Клас не знайдено.")
        return

    first_name = input("Ім'я вчителя: ")
    last_name = input("Прізвище вчителя: ")
    teacher = Teacher.objects.filter(first_name=first_name, last_name=last_name).first()

    if not teacher:
        print("Вчителя не знайдено.")
        return

    Schedule.objects.create(
        day_of_week=day_of_week,
        start_time=start_time,
        subject=subject,
        in_class=in_class,
        teacher=teacher
    )

    print("Заняття успішно додано до розкладу.")
    print("=================================")


def add_grade():
    print("======= додавання оцінки =======")

    student_first = input("Ім'я учня: ")
    student_last = input("Прізвище учня: ")

    subject_name = input("Назва предмету: ")

    grade_value = int(input("Оцінка: "))

    student = Student.objects.filter(first_name=student_first, last_name=student_last).first()
    subject = Subject.objects.filter(name=subject_name).first()

    if not student:
        print("Учня не знайдено.")
        return

    if not subject:
        print("Предмет не знайдено.")
        return

    Grade.objects.create(student=student, subject=subject, grade=grade_value)

    print("Оцінку успішно додано.")
    print("================================")

