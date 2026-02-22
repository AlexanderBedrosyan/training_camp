# Django Модели на База данни - 10 Практически задачи

## Инструкции за настройка за студенти

### Стъпка 1: Инсталиране на Django и създаване на проект
```bash
# Инсталиране на Django (уверете се, че имате Python 3.8+ инсталиран)
pip install django

# Създаване на нов Django проект
django-admin startproject school_management

# Навигиране до папката на проекта
cd school_management

# Създаване на ново приложение
python manage.py startapp students

# Създаване на суперпотребител за администратор
python manage.py createsuperuser
```

### Стъпка 2: Конфигуриране на настройките
Добавете вашето приложение към `INSTALLED_APPS` в `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',  # Добавете този ред
]
```

### Стъпка 3: Копиране на моделите
1. Копирайте съдържанието от `django_practice_models_bg.py` във вашия `students/models.py`
2. Изпълнете миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Стъпка 4: Регистриране на модели в Admin
Добавете в `students/admin.py`:
```python
from django.contrib import admin
from .models import Student, Course, Teacher, Enrollment, Book, Library

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Enrollment)
admin.site.register(Book)
admin.site.register(Library)
```

### Стъпка 5: Стартиране на development сървъра
```bash
python manage.py runserver
```
Посетете: http://127.0.0.1:8000/admin/

---

## 10 Практически задачи

### Задача 1: Основно създаване на модели и миграция
**Цел:** Разбиране на процеса на създаване на модели и миграция на база данни.

**Инструкции:**
1. Създайте нов модел наречен `Subject` в `models.py` със следните полета:
   - `name` (CharField, max_length=100)
   - `code` (CharField, max_length=10, unique=True)
   - `description` (TextField)
   - `is_active` (BooleanField, default=True)

2. Изпълнете миграции за създаване на таблицата в базата данни
3. Създайте 5 примерни предмета използвайки Django admin

**Очакван резултат:** Нова таблица Subject в базата данни с примерни данни

---

### Задача 2: Работа с CharField срещу IntegerField
**Цел:** Разбиране на различията между CharField и IntegerField.

**Инструкции:**
1. Създайте 3 студента използвайки Django shell с различни типове данни:
   - Един студент с възраст като число (правилно)
   - Опитайте се да създадете студент с възраст като текст (наблюдавайте грешката)
   - Създайте студент с много дълго име (тествайте max_length на CharField)

2. Напишете Django shell команди за да:
   - Намерите всички студенти с възраст по-голяма от 16
   - Намерите всички студенти чието име съдържа "Иван"

**Shell команди за практика:**
```python
# Отваряне на Django shell
python manage.py shell

# Импортиране на модели
from students.models import Student

# Създаване на студенти
student1 = Student.objects.create(
    first_name="Алиса", last_name="Иванова", age=17,
    student_id="T001", email="alisa@test.com", grade_level="11"
)

# Опитайте различни заявки
young_students = Student.objects.filter(age__lt=17)
name_search = Student.objects.filter(first_name__icontains="иван")
```

---

### Задача 3: Отношения между модели и Foreign Keys
**Цел:** Научете как да работите с отношения между модели.

**Инструкции:**
1. Създайте 2 учители използвайки Django admin
2. Създайте 3 курса използвайки Django admin
3. Създайте 5 записвания свързвайки различни студенти с курсове
4. Напишете заявки за намиране на:
   - Всички курсове преподавани от определен учител
   - Всички студенти записани в "Въведение в програмирането"
   - Всички записвания за определен студент

**Очаквани заявки:**
```python
# Намиране на курсове по учител
teacher = Teacher.objects.get(id=1)
teacher_courses = Course.objects.filter(enrollment__teacher=teacher)

# Намиране на студенти в курс
course = Course.objects.get(code="CS101")
enrolled_students = Student.objects.filter(enrollment__course=course)
```

---

### Задача 4: Филтриране и заявки за данни
**Цел:** Овладяване на възможностите за филтриране на Django ORM.

**Инструкции:**
1. Създайте поне 10 студента с различни възрасти (15-18)
2. Напишете заявки за намиране на:
   - Всички студенти на 16 години или повече
   - Всички студенти в 12 клас
   - Всички студенти с имейл съдържащ "gmail"
   - Всички студенти чието фамилно име започва с "П"
   - Топ 3 най-възрастни студента

**Примери за заявки:**
```python
# Филтриране по възраст
older_students = Student.objects.filter(age__gte=16)
seniors = Student.objects.filter(grade_level='12')

# Текстово филтриране
gmail_users = Student.objects.filter(email__icontains='gmail')
p_names = Student.objects.filter(last_name__startswith='П')

# Подреждане и ограничаване
oldest_students = Student.objects.order_by('-age')[:3]
```

---

### Задача 5: Методи и свойства на модели
**Цел:** Научете да добавяте персонализирани методи и свойства към модели.

**Инструкции:**
1. Добавете персонализиран метод `get_grade_status()` към модела Student който връща:
   - "Първокурсник" за клас 9
   - "Второкурсник" за клас 10  
   - "Третокурсник" за клас 11
   - "Четвъртокурсник" за клас 12

2. Добавете свойство `is_adult` което връща True ако възрастта >= 18

3. Тествайте тези нови методи със съществуващи студенти

**Имплементация:**
```python
# Добавете към модела Student
def get_grade_status(self):
    grade_map = {
        '9': 'Първокурсник',
        '10': 'Второкурсник', 
        '11': 'Третокурсник',
        '12': 'Четвъртокурсник'
    }
    return grade_map.get(self.grade_level, 'Неизвестно')

@property
def is_adult(self):
    return self.age >= 18
```

---

### Задача 6: Масови операции и управление на данни
**Цел:** Научете ефективни начини за работа с множество записи.

**Инструкции:**
1. Създайте 20 студента използвайки bulk_create()
2. Актуализирайте всички студенти в 9 клас да имат is_active=True
3. Изтрийте всички студенти с възраст < 15
4. Пребройте студентите по клас

**Масови операции:**
```python
# Масово създаване
students_list = [
    Student(first_name=f"Студент{i}", last_name=f"Фамилия{i}", 
           age=15+i%4, student_id=f"B{i:03d}", 
           email=f"student{i}@school.com", grade_level=str(9+i%4))
    for i in range(20)
]
Student.objects.bulk_create(students_list)

# Масова актуализация
Student.objects.filter(grade_level='9').update(is_active=True)

# Масово изтриване
Student.objects.filter(age__lt=15).delete()

# Агрегиране
from django.db.models import Count
grade_counts = Student.objects.values('grade_level').annotate(count=Count('id'))
```

---

### Задача 7: Работа с избори и енумерации
**Цел:** Разбиране как да използвате choices в Django модели.

**Инструкции:**
1. Създайте студенти с различни нива на класове използвайки GRADE_CHOICES
2. Създайте курсове с различни катедри използвайки DEPARTMENT_CHOICES
3. Правете заявки и филтрирайте по полета с избори
4. Създайте отчет показващ броя на студенти по класове

**Практика с избори:**
```python
# Създаване на студенти със специфични избори
Student.objects.create(
    first_name="Тест", last_name="Студент",
    age=16, student_id="CH001", 
    email="test@school.com", grade_level='10'
)

# Филтриране по избори
sophomores = Student.objects.filter(grade_level='10')
cs_courses = Course.objects.filter(department='CS')

# Получаване на дисплей стойности на избори
student = Student.objects.first()
print(student.get_grade_level_display())
```

---

### Задача 8: Операции с дата и време
**Цел:** Работа с полета за дата и заявки базирани на време.

**Инструкции:**
1. Създайте учители с различни дати на назначаване (последните 5 години)
2. Намерете учители назначени през последните 2 години
3. Изчислете годините служба за всеки учител
4. Намерете най-новия и най-стария учител по дата на назначаване

**Операции с дата:**
```python
from datetime import date, timedelta

# Филтриране по дата
recent_hire_date = date.today() - timedelta(days=730)  # преди 2 години
recent_teachers = Teacher.objects.filter(hire_date__gte=recent_hire_date)

# Подреждане по дати
newest_teacher = Teacher.objects.order_by('-hire_date').first()
oldest_teacher = Teacher.objects.order_by('hire_date').first()

# Използване на свойството years_of_service
for teacher in Teacher.objects.all():
    print(f"{teacher}: {teacher.years_of_service} години")
```

---

### Задача 9: Сложни заявки с множество условия
**Цел:** Комбиниране на множество филтри и условия.

**Инструкции:**
1. Намерете всички активни студенти в клас 11 или 12 с възраст >= 17
2. Намерете всички CS курсове с повече от 3 кредита
3. Намерете всички записвания където възрастта на студента > 16 И курсът е от CS катедра
4. Намерете студенти записани в повече от 2 курса

**Сложни заявки:**
```python
from django.db.models import Q, Count

# Множество условия с AND
senior_active = Student.objects.filter(
    is_active=True,
    grade_level__in=['11', '12'],
    age__gte=17
)

# Използване на Q обекти за OR условия
cs_or_math = Course.objects.filter(
    Q(department='CS') | Q(department='MATH')
)

# Филтриране през модели
complex_enrollments = Enrollment.objects.filter(
    student__age__gt=16,
    course__department='CS'
)

# Агрегиране с филтриране
busy_students = Student.objects.annotate(
    course_count=Count('enrollment')
).filter(course_count__gt=2)
```

---

### Задача 10: Персонализиране на Admin интерфейс и анализ на данни
**Цел:** Персонализиране на Django admin и извършване на анализ на данни.

**Инструкции:**
1. Персонализирайте Student admin да показва first_name, last_name, age, и grade_level в списъчния изглед
2. Добавете функционалност за търсене по имена на студенти и student_id
3. Добавете филтри за grade_level и is_active
4. Създайте отчет за анализ на данни показващ:
   - Общ брой студенти по клас
   - Средна възраст по клас
   - Най-популярни курсове (по брой записвания)

**Персонализиране на Admin:**
```python
# В admin.py
from django.contrib import admin
from .models import Student, Course, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'grade_level', 'is_active']
    search_fields = ['first_name', 'last_name', 'student_id']
    list_filter = ['grade_level', 'is_active']
    ordering = ['last_name', 'first_name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'credits', 'is_active']
    list_filter = ['department', 'is_active']
    search_fields = ['name', 'code']
```

**Анализ на данни:**
```python
# Заявки за анализ
from django.db.models import Count, Avg

# Студенти по клас
grade_distribution = Student.objects.values('grade_level').annotate(
    count=Count('id')
).order_by('grade_level')

# Средна възраст по клас
age_by_grade = Student.objects.values('grade_level').annotate(
    avg_age=Avg('age')
).order_by('grade_level')

# Популярни курсове
popular_courses = Course.objects.annotate(
    enrollment_count=Count('enrollment')
).order_by('-enrollment_count')
```

---

## Допълнителни предизвикателства

### Предизвикателство A: Създайте ваша собствена функция за управление на училище
Проектирайте и имплементирайте модел `Classroom` който включва:
- Номер на стая
- Капацитет
- Оборудване (проектор, компютри, и др.)
- Име на сграда
- Отношение с курсове

### Предизвикателство B: Система за управление на оценки
Създайте модел `Grade` който следи:
- Име на задание
- Спечелени точки
- Общо възможни точки
- Дата на подаване
- Отношение със Student и Course

### Предизвикателство C: Система за посещаемост  
Проектирайте модел `Attendance` за следене на:
- Дата
- Студент
- Курс
- Статус (Присъства, Отсъства, Закъснял)

---

## Контролен списък за оценка

**Основно ниво (Задачи 1-5):**
- [ ] Може да създава модели с различни типове полета
- [ ] Разбира различията между CharField и IntegerField
- [ ] Може да изпълнява миграции успешно
- [ ] Може да създава и заявява основни данни
- [ ] Разбира отношения между модели

**Средно ниво (Задачи 6-8):**
- [ ] Може да извършва масови операции
- [ ] Разбира полета с избори
- [ ] Може да работи с полета за дата/време
- [ ] Може да пише сложни заявки

**Напреднало ниво (Задачи 9-10):**
- [ ] Може да комбинира множество условия за заявки
- [ ] Може да персонализира Django admin
- [ ] Може да извършва анализ на данни с Django ORM
- [ ] Разбира агрегация и анотация

**Следващи стъпки:**
След завършване на тези задачи, студентите ще бъдат готови да учат:
- Напреднали отношения (Many-to-Many)
- Django REST API разработка
- Работа с форми в Django
- Шаблонна система и изгледи