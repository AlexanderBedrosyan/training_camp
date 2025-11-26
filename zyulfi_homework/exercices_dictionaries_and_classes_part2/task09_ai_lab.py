# Задача 9: Изкуствен интелект лаборатория
# Създай клас AILab, който управлява проекти и техните метрики.
# Изисквания:
# Речник {проект: {"accuracy": %, "models": брой}}
# add_project(name, accuracy, models)
# improve_project(name, delta) — увеличава точността.
# best_project() — връща името на най-точния проект.
# average_accuracy() — средна точност на всички.

class AILab:
    def __init__(self):
        self.project_dict = {}

    def add_project(self, name, accuracy, models):
        if name not in self.project_dict:
            self.project_dict[name] = {
                "accuracy": accuracy,
                "models": models
            }

    def improve_project(self, name, delta):
        if name in self.project_dict:
            self.project_dict[name]["accuracy"] += delta
        else:
            print(f"The {name} not in project")

    def best_project(self):
        return sorted(self.project_dict.items(), key=lambda x: -x[1]["accuracy"])[0][0]

    def average_accuracy(self):
        average_project = 0
        for name, details in self.project_dict.items():
            for name_details, value_details in details.items():
                if name_details == "accuracy":
                    average_project += value_details

        return average_project / len(self.project_dict)


# Тест:
ai = AILab()
ai.add_project("VisionX", 92, 3)
ai.add_project("SpeechPro", 88, 2)
ai.add_project("VisionX", 88, 5)
ai.improve_project("SpeechPro", 5)
print(ai.project_dict)
print(ai.best_project()) # SpeechPro

print(ai.average_accuracy())