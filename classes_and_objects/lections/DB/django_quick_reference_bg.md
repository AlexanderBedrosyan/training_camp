# Django Модели на База данни - Бърз справочник

## Общи Django команди

### Настройка на проект
```bash
# Създаване на проект
django-admin startproject myproject

# Създаване на приложение
python manage.py startapp myapp

# Създаване на миграции
python manage.py makemigrations

# Прилагане на миграции
python manage.py migrate

# Създаване на суперпотребител
python manage.py createsuperuser

# Стартиране на сървър
python manage.py runserver

# Отваряне на Django shell
python manage.py shell
```

## Бърз справочник за типове полета

| Тип поле | Предназначение | Пример |
|----------|---------------|---------|
| `CharField` | Къс текст | `models.CharField(max_length=100)` |
| `TextField` | Дълъг текст | `models.TextField()` |
| `IntegerField` | Цели числа | `models.IntegerField()` |
| `DecimalField` | Точни десетични числа | `models.DecimalField(max_digits=5, decimal_places=2)` |
| `BooleanField` | True/False | `models.BooleanField(default=True)` |
| `DateField` | Дати | `models.DateField()` |
| `DateTimeField` | Дата + Час | `models.DateTimeField(auto_now_add=True)` |
| `EmailField` | Имейл адреси | `models.EmailField()` |
| `ForeignKey` | Един-към-много | `models.ForeignKey(OtherModel, on_delete=models.CASCADE)` |

## Общи опции за полета

| Опция | Предназначение | Пример |
|-------|---------------|---------|
| `max_length` | Максимум символи (задължително за CharField) | `max_length=100` |
| `null=True` | Позволява NULL в базата данни | `null=True` |
| `blank=True` | Позволява празно във форми | `blank=True` |
| `default` | Стойност по подразбиране | `default=True` |
| `unique=True` | Трябва да е уникално | `unique=True` |
| `choices` | Ограничава до специфични стойности | `choices=MY_CHOICES` |
| `help_text` | Помощен текст за admin | `help_text="Въведете име"` |

## Помагало за заявки

### Основни заявки
```python
# Импортиране на вашите модели
from myapp.models import Student

# Взимане на всички записи
Student.objects.all()

# Взимане на един запис
Student.objects.get(id=1)
Student.objects.get(student_id="S001")

# Взимане на първи/последен запис
Student.objects.first()
Student.objects.last()

# Броене на записи
Student.objects.count()
```

### Филтриране
```python
# Филтриране по точна стойност
Student.objects.filter(age=16)
Student.objects.filter(grade_level='10')

# Филтриране по множество условия (AND)
Student.objects.filter(age=16, grade_level='10')

# Изключване на записи
Student.objects.exclude(age=15)

# Заявки за диапазон
Student.objects.filter(age__gte=16)  # възраст >= 16
Student.objects.filter(age__lt=18)   # възраст < 18
Student.objects.filter(age__range=[15, 17])  # 15 <= възраст <= 17
```

### Текстови заявки
```python
# Съдържа (без значение от главни/малки букви)
Student.objects.filter(first_name__icontains='иван')

# Започва с / Завършва с
Student.objects.filter(last_name__startswith='П')
Student.objects.filter(email__endswith='gmail.com')

# Точно съвпадение (с значение от главни/малки букви)
Student.objects.filter(first_name__exact='Иван')
```

### Подреждане
```python
# Подреждане по едно поле
Student.objects.order_by('age')
Student.objects.order_by('-age')  # Низходящо

# Подреждане по множество полета
Student.objects.order_by('grade_level', 'last_name')

# Взимане на определен брой записи
Student.objects.order_by('age')[:5]  # Първите 5
Student.objects.order_by('-age')[:3]  # Топ 3
```

### Създаване на записи
```python
# Метод 1: Създаване и запазване
student = Student(first_name="Иван", last_name="Иванов", age=16)
student.save()

# Метод 2: Директно създаване
student = Student.objects.create(
    first_name="Мария",
    last_name="Петрова", 
    age=17
)

# Масово създаване
students_list = [
    Student(first_name="Алиса", last_name="Димитрова", age=16),
    Student(first_name="Георги", last_name="Стоянов", age=17),
]
Student.objects.bulk_create(students_list)
```

### Актуализиране на записи
```python
# Актуализиране на един запис
student = Student.objects.get(id=1)
student.age = 17
student.save()

# Масова актуализация
Student.objects.filter(grade_level='9').update(is_active=True)
```

### Изтриване на записи
```python
# Изтриване на един запис
student = Student.objects.get(id=1)
student.delete()

# Масово изтриване
Student.objects.filter(age__lt=15).delete()
```

## Заявки за отношения

### Предни отношения (ForeignKey)
```python
# Взимане на свързан обект
enrollment = Enrollment.objects.get(id=1)
student = enrollment.student
course = enrollment.course

# Филтриране по свързано поле
Enrollment.objects.filter(student__age__gt=16)
Enrollment.objects.filter(course__department='CS')
```

### Обратни отношения
```python
# Взимане на всички записвания за студент
student = Student.objects.get(id=1)
enrollments = student.enrollment_set.all()

# Филтриране на обратни отношения
Student.objects.filter(enrollment__course__code='CS101')
```

## Общи шаблони

### Проверка дали запис съществува
```python
if Student.objects.filter(student_id='S001').exists():
    print("Студентът съществува")
```

### Вземи или създай
```python
student, created = Student.objects.get_or_create(
    student_id='S001',
    defaults={'first_name': 'Иван', 'last_name': 'Иванов', 'age': 16}
)
```

### Агрегация
```python
from django.db.models import Count, Avg, Max, Min

# Броене на свързани обекти
Student.objects.annotate(course_count=Count('enrollment'))

# Изчисляване на средни стойности
Student.objects.aggregate(avg_age=Avg('age'))
```

### Сложни филтри с Q обекти
```python
from django.db.models import Q

# OR условия
Student.objects.filter(Q(age=16) | Q(age=17))

# NOT условия
Student.objects.filter(~Q(grade_level='12'))
```

## Добри практики за модели

### Основна структура на модел
```python
from django.db import models

class MyModel(models.Model):
    # Полета
    name = models.CharField(max_length=100)
    
    # Meta клас
    class Meta:
        ordering = ['name']
        verbose_name = 'Моят модел'
        verbose_name_plural = 'Моите модели'
    
    # Низово представяне
    def __str__(self):
        return self.name
    
    # Персонализирани методи
    def my_method(self):
        return "нещо"
    
    # Свойства
    @property
    def my_property(self):
        return "изчислена стойност"
```

## Съвети за отстраняване на грешки

### Общи грешки и решения

**Грешка:** `django.db.utils.IntegrityError`
**Решение:** Проверете за уникални ограничения или задължителни полета

**Грешка:** `RelatedObjectDoesNotExist`
**Решение:** Използвайте `hasattr()` или `try/except` за проверка дали свързаният обект съществува

**Грешка:** `MultipleObjectsReturned`
**Решение:** Използвайте `filter()` вместо `get()`, или добавете по-специфични филтри

### Полезни команди за отстраняване на грешки
```python
# Отпечатване на SQL заявка
queryset = Student.objects.filter(age=16)
print(queryset.query)

# Проверка дали queryset е празен
if queryset.exists():
    print("Има записи")

# Вземане на чист SQL за сложни заявки
from django.db import connection
print(connection.queries)
```

## Тестване на знанията ви

### Бързи въпроси за самопроверка:
1. Каква е разликата между `null=True` и `blank=True`?
2. Кога трябва да използвате `CharField` срещу `TextField`?
3. Какво е предназначението на метода `__str__`?
4. Как филтрирате записи където възрастта НЕ е равна на 16?
5. Каква е разликата между `filter()` и `get()`?

### Отговори:
1. `null=True` позволява NULL в базата данни; `blank=True` позволява празно във форми
2. `CharField` за къс текст (с max_length); `TextField` за дълъг текст
3. Предоставя четимо от човек низово представяне на обекта
4. `Student.objects.exclude(age=16)` или `Student.objects.filter(~Q(age=16))`
5. `filter()` връща queryset (множество резултати); `get()` връща един обект

## Следващи стъпки

След овладяване на тези основи, научете:
- Персонализиране на Django Admin
- Валидация на модели
- Персонализирани мениджъри и queryset-ове
- Django REST Framework
- Напреднали отношения (Many-to-Many)
- Оптимизация на база данни и индексиране