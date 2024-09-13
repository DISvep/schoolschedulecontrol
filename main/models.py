from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Class(models.Model):
    name = models.CharField(max_length=3)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    in_class = models.ForeignKey(Class, on_delete=models.CASCADE)


class Schedule(models.Model):
    day_of_week = models.CharField(max_length=100, choices=[("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"), ("Friday", "Friday")])
    start_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    in_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)

