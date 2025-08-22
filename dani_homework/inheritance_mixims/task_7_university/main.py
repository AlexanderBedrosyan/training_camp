from professor import Professor

p = Professor("Dr. Boris", "P123")
p.teach("Math")
p.teach("Physics")
print(p.list_courses())  # ['Math', 'Physics']