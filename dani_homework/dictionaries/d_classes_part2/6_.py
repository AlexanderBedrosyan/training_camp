#  Задача 6: Адвокатска кантора
# Създай клас LawFirm, който управлява адвокати и техните дела.
# Изисквания: Речник {адвокат: {"cases": [дела], "won": спечелени}}
# add_lawyer(name)
# add_case(name, case, won)
# win_rate(name) — връща % на спечелени дела.
# best_lawyer() — връща адвоката с най-висок win rate.
class LawFirm:
    def __init__(self):
# {адвокат: {"cases": [дело 1, дело 2], "won": спечелени}}
        self.dict_lawyers = {}

    def add_lawyer(self, l_name):
        if l_name not in self.dict_lawyers:
            self.dict_lawyers[l_name] = {"cases": [], "won": 0}

    def add_case(self, name, case, won):
        if name not in self.dict_lawyers:
            print(f"The lawyer '{name}' does not exist!")
            return
        lawyer = self.dict_lawyers[name]

        if case not in lawyer["cases"]:
            lawyer["cases"].append(case)
            if won:
                lawyer["won"] += 1

    def win_rate(self, name):
        if name not in self.dict_lawyers:
            print(f"The lawyer '{name}' does not exist!")
            return 0
        total_cases = len(self.dict_lawyers[name]["cases"])
        if total_cases == 0:
            return 0
        return (self.dict_lawyers[name]["won"] / total_cases) * 100

    def best_lawyer(self):
        if not self.dict_lawyers:
            return None
        return max(self.dict_lawyers, key=lambda n: self.win_rate(n))


# Тест:
l = LawFirm()
l.add_lawyer("Petar")
l.add_case("Petar", "Case A", True)
l.add_case("Petar", "Case B", False)
l.add_case("Petar", "Case C", True)
print(round(l.win_rate("Petar"), 2)) # 66.67