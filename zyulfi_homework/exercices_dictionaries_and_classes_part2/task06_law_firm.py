# Задача 6: Адвокатска кантора
# Създай клас LawFirm, който управлява адвокати и техните дела.
# Изисквания:
# Речник {адвокат: {"cases": [дела], "won": спечелени}}
# add_lawyer(name)
# add_case(name, case, won)
# win_rate(name) — връща % на спечелени дела.
# best_lawyer() — връща адвоката с най-висок win rate.



class LawFirm:
    def __init__(self):
        self.lawyers_dict = {}

    def add_lawyer(self, name_lawyer):
        if name_lawyer not in self.lawyers_dict:
            self.lawyers_dict[name_lawyer] = {}
            self.lawyers_dict[name_lawyer]["cases"] = []
            self.lawyers_dict[name_lawyer]["won"] = []

    def add_case(self, name_lawyer, case, won):
        if name_lawyer not in self.lawyers_dict:
            self.add_lawyer(name_lawyer)
        self.lawyers_dict[name_lawyer]["cases"].append(case)
        self.lawyers_dict[name_lawyer]["won"].append(won)

    def win_rate(self, name_lawyer):
        try:
            wins = self.lawyers_dict[name_lawyer]["won"].count(True)
            return wins / len(self.lawyers_dict[name_lawyer]["won"]) * 100
        except KeyError:
            print("Error")

    def best_lawyer(self):
        return max(self.lawyers_dict, key=lambda x: self.win_rate(x))

            # sorted(self.win_rate(self.lawyers_dict[name_laver]) ))


# Тест:
l = LawFirm()
l.add_lawyer("Petar")
l.add_case("Petar", "Case A", True)
l.add_case("Petar", "Case B", False)
l.add_case("Petar", "Case C", True)
l.add_case("Ivan", "Case AB", False)
l.add_case("Ivan", "Case CC", True)
l.add_case("Ivan", "Case VC", True)
l.add_case("Ivan", "Case FC", True)


print(l.lawyers_dict)
print(round(l.win_rate("Petar"), 2)) # 66.67
print(l.best_lawyer())
print(l.win_rate("Ivan"))