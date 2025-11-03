# Задача 7: Академия за магьосници
# Създай клас MagicAcademy, който следи магьосници и изучените им заклинания.
# Изисквания: Речник {маг: {"spells": [заклинания], "mana": текуща_мана}}
# learn_spell(name, spell, mana_cost)
# use_spell(name, spell) — намаля мана.
# strongest_mage() — връща мага с най-много останала мана.
class MagicAcademy:
    def __init__(self):
        self.dict_mages = {}
    # {маг: {"spells": [заклинания], "mana": текуща_мана}}

    def learn_spell(self, name, spell, mana_cost):
        if name not in self.dict_mages:
            self.dict_mages[name] = {"spells": {}, "mana": 100}
        self.dict_mages[name]["spells"][spell] = mana_cost

    def use_spell(self, name, spell):
        if name not in self.dict_mages:
            print(f"The mage '{name}' does not exist!")
            return
        if spell not in self.dict_mages[name]["spells"]:
            print(f"The mage '{name}' does not know the '{spell}'!")
            return
        mana_cost = self.dict_mages[name]["spells"][spell]
        self.dict_mages[name]["mana"] -= mana_cost

        if self.dict_mages[name]["mana"] < 0:
            self.dict_mages[name]["mana"] = 0  # няма отрицателна мана

    def strongest_mage(self):
        if not self.dict_mages:
            return None
        return max(self.dict_mages, key=lambda n: self.dict_mages[n]["mana"])


# Тест:
m = MagicAcademy()
m.learn_spell("Alaric", "Fireball", 30)
m.learn_spell("Alaric", "Shield", 20)
m.use_spell("Alaric", "Fireball")
print(m.strongest_mage()) # Alaric