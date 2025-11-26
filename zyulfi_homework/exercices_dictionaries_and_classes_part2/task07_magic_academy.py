# Задача 7: Академия за магьосници
# Създай клас MagicAcademy, който следи магьосници и изучените им заклинания.
# Изисквания:
# Речник {маг: {"spells": [заклинания], "mana": текуща_мана}}
# learn_spell(name, spell, mana_cost)
# use_spell(name, spell) — намаля мана.
# strongest_mage() — връща мага с най-много останала мана.

class MagicAcademy:
    def __init__(self):
        self.magic_dict = {}

    def learn_spell(self, name, spell, mana_cost):
        if name not in self.magic_dict:
            self.magic_dict[name] = {
                "spells": [],
                "mana": 0
            }
        self.magic_dict[name]["spells"].append(spell)
        self.magic_dict[name]["mana"] += mana_cost

    def use_spell(self, name, spell):
        if name in self.magic_dict:
            if spell in self.magic_dict[name]["spells"]:
                self.magic_dict[name]["mana"] -= 1
        else:
            print("Error")

    def strongest_mage(self):
        return sorted(self.magic_dict.items(), key=lambda x: -len(x[1]["spells"]))[0][0]


# Тест:
m = MagicAcademy()
m.learn_spell("Alaric", "Fireball", 30)
m.learn_spell("Alaric", "Shield", 20)
m.use_spell("Alaric", "Fireball")
print(m.strongest_mage()) # Alaric