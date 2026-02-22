# models.py - Прости Django модели за начинаещи
# Копирайте това съдържание във файла models.py на вашето Django приложение

from django.db import models

# ============================================================================
# ПРОСТИ МОДЕЛИ ЗА НАЧИНАЕЩИ - ПЪРВА ЛЕКЦИЯ
# ============================================================================

class Student(models.Model):
    """
    Прост модел Student за първа лекция
    Използва само CharField и IntegerField
    """
    name = models.CharField(max_length=100, help_text="Пълното име на студента")
    age = models.IntegerField(help_text="Възраст на студента в години")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенти'


class Book(models.Model):
    """
    Прост модел Book за упражнение
    """
    title = models.CharField(max_length=200, help_text="Заглавие на книгата")
    pages = models.IntegerField(help_text="Брой страници")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Car(models.Model):
    """
    Прост модел Car за допълнително упражнение
    """
    make = models.CharField(max_length=50, help_text="Марка на колата (Toyota, BMW)")
    model = models.CharField(max_length=50, help_text="Модел на колата (Corolla, X5)")
    year = models.IntegerField(help_text="Година на производство")
    
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
    
    class Meta:
        verbose_name = 'Кола'
        verbose_name_plural = 'Коли'


# ============================================================================
# ФУНКЦИИ ЗА СЪЗДАВАНЕ НА ПРИМЕРНИ ДАННИ
# ============================================================================

def create_sample_students():
    """
    Създава примерни студенти за тестване
    Изпълнете в Django shell: from myapp.models import create_sample_students; create_sample_students()
    """
    
    students_data = [
        {'name': 'Иван Петров', 'age': 16},
        {'name': 'Мария Иванова', 'age': 17},
        {'name': 'Георги Стоянов', 'age': 15},
        {'name': 'Анна Димитрова', 'age': 18},
        {'name': 'Петър Николов', 'age': 16},
    ]
    
    for student_data in students_data:
        student, created = Student.objects.get_or_create(
            name=student_data['name'],
            defaults=student_data
        )
        if created:
            print(f"Създаден студент: {student}")


def create_sample_books():
    """
    Създава примерни книги за тестване
    """
    books_data = [
        {'title': 'Под игото', 'pages': 300},
        {'title': 'Железният светилник', 'pages': 150},
        {'title': 'Тютюн', 'pages': 280},
        {'title': 'Бай Ганьо', 'pages': 120},
        {'title': 'Немили-недраги', 'pages': 250},
    ]
    
    for book_data in books_data:
        book, created = Book.objects.get_or_create(
            title=book_data['title'],
            defaults=book_data
        )
        if created:
            print(f"Създадена книга: {book}")


def create_sample_cars():
    """
    Създава примерни коли за тестване
    """
    cars_data = [
        {'make': 'Toyota', 'model': 'Corolla', 'year': 2020},
        {'make': 'BMW', 'model': 'X5', 'year': 2019},
        {'make': 'Mercedes', 'model': 'C-Class', 'year': 2021},
        {'make': 'Volkswagen', 'model': 'Golf', 'year': 2018},
        {'make': 'Audi', 'model': 'A4', 'year': 2022},
    ]
    
    for car_data in cars_data:
        car, created = Car.objects.get_or_create(
            make=car_data['make'],
            model=car_data['model'],
            year=car_data['year'],
            defaults=car_data
        )
        if created:
            print(f"Създадена кола: {car}")


# ============================================================================
# ПРИМЕРИ ЗА ЗАЯВКИ ЗА ПРАКТИКА - ПЪРВА ЛЕКЦИЯ
# ============================================================================

"""
Практикувайте тези заявки в Django shell (python manage.py shell):

# Импортиране на модели
from myapp.models import Student, Book, Car

# === РАБОТА СЪС СТУДЕНТИ ===

# Създаване на нов студент
new_student = Student.objects.create(name="Тодор Живков", age=17)

# Намиране на всички студенти
all_students = Student.objects.all()
print(f"Общо студенти: {all_students.count()}")

# Намиране на конкретен студент по име
student = Student.objects.get(name="Иван Петров")
print(f"Намерen студент: {student}")

# Намиране на студенти на определена възраст
sixteen_year_olds = Student.objects.filter(age=16)
print(f"Студенти на 16 години: {sixteen_year_olds.count()}")

# Намиране на студенти по-стари от определена възраст
older_students = Student.objects.filter(age__gt=16)
for student in older_students:
    print(f"{student.name} е на {student.age} години")

# Намиране на най-възрастния студент
oldest_student = Student.objects.order_by('-age').first()
print(f"Най-възрастният студент е: {oldest_student}")

# Промяна на възрастта на студент
student = Student.objects.get(name="Мария Иванова")
student.age = 18  # Мария вече е пълнолетна
student.save()

# === РАБОТА С КНИГИ ===

# Създаване на нова книга
new_book = Book.objects.create(title="Нова книга", pages=200)

# Намиране на книги с повече от 200 страници
thick_books = Book.objects.filter(pages__gt=200)
print(f"Дебели книги: {thick_books.count()}")

# Намиране на най-дебелата книга
thickest_book = Book.objects.order_by('-pages').first()
print(f"Най-дебелата книга: {thickest_book} - {thickest_book.pages} страници")

# === РАБОТА С КОЛИ ===

# Създаване на нова кола
new_car = Car.objects.create(make="Ford", model="Focus", year=2023)

# Намиране на всички коли от определена марка
toyota_cars = Car.objects.filter(make="Toyota")

# Намиране на най-новата кола
newest_car = Car.objects.order_by('-year').first()
print(f"Най-новата кола: {newest_car}")

# Намиране на коли произведени след 2020
modern_cars = Car.objects.filter(year__gt=2020)
"""


class Course(models.Model):
    """
    Модел Course за учебни курсове
    """
    name = models.CharField(max_length=200, help_text="Име на курса")
    code = models.CharField(max_length=10, unique=True, help_text="Код на курса (напр. CS101)")
    description = models.TextField(help_text="Подробно описание на курса")
    credits = models.IntegerField(help_text="Брой кредитни часове")
    max_students = models.IntegerField(default=30, help_text="Максимален брой студенти")
    
    # Избори за катедра
    DEPARTMENT_CHOICES = [
        ('CS', 'Компютърни науки'),
        ('MATH', 'Математика'),
        ('ENG', 'Английски език'),
        ('SCI', 'Природни науки'),
        ('HIST', 'История'),
        ('ART', 'Изкуство'),
    ]
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES)
    
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['department', 'code']
    
    def __str__(self):
        return f"{self.code}: {self.name}"


class Teacher(models.Model):
    """
    Модел Teacher
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, help_text="Годишна заплата")
    
    # Катедра - същите избори както в Course
    DEPARTMENT_CHOICES = [
        ('CS', 'Компютърни науки'),
        ('MATH', 'Математика'),
        ('ENG', 'Английски език'),
        ('SCI', 'Природни науки'),
        ('HIST', 'История'),
        ('ART', 'Изкуство'),
    ]
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Проф. {self.first_name} {self.last_name}"
    
    @property
    def years_of_service(self):
        return (date.today() - self.hire_date).days // 365


# ============================================================================
# МОДЕЛИ С ОТНОШЕНИЯ
# ============================================================================

class Enrollment(models.Model):
    """
    Enrollment свързва студенти с курсове (Many-to-Many отношение чрез този модел)
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    # Избори за статус
    STATUS_CHOICES = [
        ('ENROLLED', 'Записан'),
        ('COMPLETED', 'Завършен'),
        ('DROPPED', 'Отписан'),
        ('FAILED', 'Неуспешен'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ENROLLED')
    
    class Meta:
        unique_together = ['student', 'course']  # Студент не може да се запише два пъти в същия курс
    
    def __str__(self):
        return f"{self.student} записан в {self.course}"


# ============================================================================
# ДОПЪЛНИТЕЛНИ МОДЕЛИ ЗА ПРАКТИКА
# ============================================================================

class Book(models.Model):
    """
    Модел Book за библиотечни книги за допълнителна практика
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    # Избори за жанр
    GENRE_CHOICES = [
        ('FIC', 'Художествена литература'),
        ('NONFIC', 'Нехудожествена литература'),
        ('SCIFI', 'Научна фантастика'),
        ('MYSTERY', 'Мистерия'),
        ('ROMANCE', 'Романтика'),
        ('HISTORY', 'История'),
        ('TECH', 'Технология'),
    ]
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} от {self.author}"


class Library(models.Model):
    """
    Модел Library който може да има много книги
    """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    books = models.ManyToManyField(Book, through='BookCopy')
    
    def __str__(self):
        return self.name


class BookCopy(models.Model):
    """
    Междинен модел за отношението Library-Book
    """
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_number = models.CharField(max_length=20)
    condition = models.CharField(max_length=20, choices=[
        ('EXCELLENT', 'Отлично'),
        ('GOOD', 'Добро'),
        ('FAIR', 'Задоволително'),
        ('POOR', 'Лошо'),
    ])
    date_acquired = models.DateField()
    
    def __str__(self):
        return f"{self.book.title} - Копие {self.copy_number} в {self.library.name}"


# ============================================================================
# ФУНКЦИИ ЗА СЪЗДАВАНЕ НА ПРИМЕРНИ ДАННИ
# ============================================================================

def create_sample_data():
    """
    Функция за създаване на примерни данни за тестване
    Изпълнете това в Django shell: python manage.py shell
    След това: from myapp.models import create_sample_data; create_sample_data()
    """
    
    # Създаване на примерни студенти
    students_data = [
        {'first_name': 'Иван', 'last_name': 'Иванов', 'age': 16, 'student_id': 'S001', 'email': 'ivan.ivanov@school.com', 'grade_level': '10'},
        {'first_name': 'Мария', 'last_name': 'Петрова', 'age': 17, 'student_id': 'S002', 'email': 'maria.petrova@school.com', 'grade_level': '11'},
        {'first_name': 'Георги', 'last_name': 'Георгиев', 'age': 15, 'student_id': 'S003', 'email': 'georgi.georgiev@school.com', 'grade_level': '9'},
        {'first_name': 'Анна', 'last_name': 'Димитрова', 'age': 18, 'student_id': 'S004', 'email': 'anna.dimitrova@school.com', 'grade_level': '12'},
        {'first_name': 'Петър', 'last_name': 'Стоянов', 'age': 16, 'student_id': 'S005', 'email': 'petar.stoyanov@school.com', 'grade_level': '10'},
    ]
    
    for student_data in students_data:
        student, created = Student.objects.get_or_create(
            student_id=student_data['student_id'],
            defaults=student_data
        )
        if created:
            print(f"Създаден студент: {student}")
    
    # Създаване на примерни курсове
    courses_data = [
        {'name': 'Въведение в програмирането', 'code': 'CS101', 'credits': 3, 'department': 'CS', 'description': 'Основни концепции на програмирането'},
        {'name': 'Алгебра II', 'code': 'MATH201', 'credits': 4, 'department': 'MATH', 'description': 'Напреднали алгебрични концепции'},
        {'name': 'Българска литература', 'code': 'ENG101', 'credits': 3, 'department': 'ENG', 'description': 'Класическа и модерна литература'},
        {'name': 'Биология', 'code': 'SCI101', 'credits': 4, 'department': 'SCI', 'description': 'Въведение в биологичните науки'},
    ]
    
    for course_data in courses_data:
        course, created = Course.objects.get_or_create(
            code=course_data['code'],
            defaults=course_data
        )
        if created:
            print(f"Създаден курс: {course}")
    
    # Създаване на примерни учители
    teachers_data = [
        {'first_name': 'Д-р Мария', 'last_name': 'Николова', 'email': 'maria.nikolova@school.com', 
         'phone': '555-0101', 'hire_date': '2020-08-15', 'salary': 65000, 'department': 'CS'},
        {'first_name': 'Проф. Стефан', 'last_name': 'Петров', 'email': 'stefan.petrov@school.com', 
         'phone': '555-0102', 'hire_date': '2018-08-20', 'salary': 70000, 'department': 'MATH'},
    ]
    
    for teacher_data in teachers_data:
        teacher, created = Teacher.objects.get_or_create(
            email=teacher_data['email'],
            defaults=teacher_data
        )
        if created:
            print(f"Създаден учител: {teacher}")


# ============================================================================
# ПРИМЕРИ ЗА ЗАЯВКИ ЗА ПРАКТИКА
# ============================================================================

"""
Практикувайте тези заявки в Django shell (python manage.py shell):

# Импортиране на модели
from myapp.models import Student, Course, Teacher, Enrollment

# Основни заявки
all_students = Student.objects.all()
first_student = Student.objects.first()
student_by_id = Student.objects.get(id=1)

# Филтриране
young_students = Student.objects.filter(age__lt=17)
seniors = Student.objects.filter(grade_level='12')
active_students = Student.objects.filter(is_active=True)

# Сложно филтриране
cs_courses = Course.objects.filter(department='CS')
high_credit_courses = Course.objects.filter(credits__gte=4)

# Подреждане
students_by_age = Student.objects.order_by('age')
students_by_name = Student.objects.order_by('last_name', 'first_name')

# Броене
total_students = Student.objects.count()
senior_count = Student.objects.filter(grade_level='12').count()

# Актуализиране
Student.objects.filter(age__lt=16).update(is_active=True)

# Създаване
new_student = Student.objects.create(
    first_name='Тест',
    last_name='Студент',
    age=16,
    student_id='S999',
    email='test@school.com',
    grade_level='10'
)

# Отношения
enrollments = Enrollment.objects.filter(student__age__gt=17)
courses_for_student = Course.objects.filter(enrollment__student_id=1)
"""