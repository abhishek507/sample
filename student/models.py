from django.db import models

# Create your models here.

class student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=100)
    stu_age = models.IntegerField()
    stu_class = models.CharField(max_length=20)
    sut_dept = models.CharField(max_length=20,choices=(('cse','CSE'),('ece','ECE'),('eee','EEE'),('mech','MECH')))
    address = models.TextField()

    def __str__(self):
        return self.stu_name

    class Meta:
        db_table ='student'

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    staff_count = models.IntegerField()
    hod = models.CharField(max_length=20)
    total_subjects = models.IntegerField()


    def __str__(self):
        return self.dept_name

    class Meta:
        db_table ='dept'

class Subject(models.Model):
    sub_code = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=100)
    author = models.CharField(max_length=20,null=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name

    class Meta:
        db_table = 'subject'

class Examination(models.Model):
    sub_code = models.ForeignKey(Subject,on_delete=models.CASCADE)
    duration = models.FloatField(default=180)
    total_marks = models.FloatField(default=100)

    def __str__(self):
        return self.sub_code.sub_name

    class Meta:
        db_table = 'exam'


