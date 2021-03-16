from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

COURSE_CHOISES = [
		('alg1', 'Algebra 1'),
		('alg2', 'Algebra 2'),
		('clc1', 'Calculus 1'),
		('clc2', 'Calculus 2'),
		('prb1', 'Probability'),
		('dsc1', 'Descrete 1'),
		('dsc2', 'Descrete 2'),
		('psc1', 'Physics 1'),
		('psc2', 'Physics 2'),
		('psc3', 'Physics 3'),
		('defo', 'Default'),
]

PROGRAM_REQUEST = [
		('per', 'Perach'),
		('ifk', 'Ifak'),
		('def', 'None'),

]

DAYS_CHOICES = [
		('sun', 'Sunday'),
		('mon', 'Monday'),
		('tue', 'Tuesday'),
		('wed', 'Wednesday'),
		('thu', 'Thursday'),
		('def', 'None'),

]
DEPARTMENT_CHOICES = [
		('sof', 'Software'),
		('ele', 'Electricity'),
		('mac', 'Machines'),
		('mat', 'Mathematics'),
		('iam', 'Industry and managment'),
		('bio', 'Bio technology'),
		('def', 'Default'),

]


HOURS_CHOICES = [
		('1', '8:00'),
		('2', '9:00'),
		('3', '10:00'),
		('4', '11:00'),
		('5', '12:00'),
		('6', '13:00'),
		('7', '14:00'),
		('8', '15:00'),
		('9', '16:00'),
		('10', '17:00'),
		('11', '18:00'),
		('12', '19:00'),

]

# Create your models here.

#mapping data onto the database
class User(models.Model):
	name = models.CharField(max_length = 20,default = "Enter name")
	lastName = models.CharField(max_length = 20, default = "Enter last name")
	userType = models.CharField(max_length = 20 ,default= "Student")
	userStatus = models.CharField(max_length = 20, default = "ACTIVE")
	phoneNumber = PhoneNumberField(default = "Enter phone number")
	email = models.EmailField(max_length=254, default = "Enter email")
	department = models.CharField(max_length = 20, choices = DEPARTMENT_CHOICES, default = 'def')
	password = models.CharField(max_length = 20, default="Enter password") #users password for logging in
	programRequest = models.CharField(max_length = 3, choices = PROGRAM_REQUEST, default = 'defo')
	academicYear = models.PositiveSmallIntegerField(default = 0)
	gradeSheet = models.FileField(upload_to='uploads/%Y/%m/%d/', default="null")

class Student(User):
	coursesRequired = models.CharField(max_length = 4, choices = COURSE_CHOISES, default = 'defo')
	hoursRequiredSunday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursRequiredMonday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursRequiredTuesday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursRequiredWednesday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursRequiredThursday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")

class Tutor(User):
	coursesProvide = models.CharField(max_length = 4, choices = COURSE_CHOISES, default = 'defo')
	hoursProvideSunday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursProvidedMonday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursProvideTuesday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursProvideWednesday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")
	hoursProvideThursday = MultiSelectField(choices = HOURS_CHOICES, max_choices = 12, max_length= 12, default = "def")

'''
my_field2 = MultiSelectField(choices=MY_CHOICES2,
                                 max_choices=3,
                                 max_length=3)
'''