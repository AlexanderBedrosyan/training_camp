# Задача 9: Изкуствен интелект лаборатория
# Създай клас AILab, който управлява проекти и техните метрики.
# Изисквания: Речник {проект: {"accuracy": %, "models": брой}}
# add_project(name, accuracy, models)
# improve_project(name, delta) — увеличава точността.
# best_project() — връща името на най-точния проект.
# average_accuracy() — средна точност на всички.
class AILab:
    def __init__(self):
        self.ai_projects = {}
# {проект: {"accuracy": %, "models": брой}}

    def add_project(self, name, accuracy, models):
        if name not in self.ai_projects:
            self.ai_projects[name] = {"accuracy": accuracy, "models": models}

    def improve_project(self, name, delta):
        if name not in self.ai_projects:
            print(f"The project '{name}' does not exist!")
            return
        self.ai_projects[name]["accuracy"] += delta

    def best_project(self):
        if not self.ai_projects:
            return None
        return max(self.ai_projects, key=lambda n: self.ai_projects[n]["accuracy"])

    def average_accuracy(self):
        if not self.ai_projects:
            return 0
        total = sum(p["accuracy"] for p in self.ai_projects.values())
        return total / len(self.ai_projects)


# Тест:
ai = AILab()
ai.add_project("VisionX", 92, 3)
ai.add_project("SpeechPro", 88, 2)
ai.improve_project("SpeechPro", 5)
print(ai.best_project()) # SpeechPro