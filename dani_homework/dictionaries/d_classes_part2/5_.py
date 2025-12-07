# Задача 5: Космическа станция
# Създай клас SpaceStation, който следи астронавти и техните мисии.
# Изисквания: Речник {астронавт: {"missions": [мисии], "hours": общо_часове}}
# add_astronaut(name)
# record_mission(name, mission, hours)
# top_astronaut() — връща астронавта с най-много часове в мисии.
# missions_summary() — брои общо мисиите в станцията.
class SpaceStation:
    def __init__(self):
        self.dict_astronauts = {}

    def add_astronaut(self, name):
        if name not in self.dict_astronauts:
            self.dict_astronauts[name] = {"missions": [], "hours": 0}

    def record_mission(self, name, mission, hours):
        if name not in self.dict_astronauts:
            print(f"The astronaut '{name}' does not exist!")
            return
        astronaut = self.dict_astronauts[name]

        if mission not in astronaut["missions"]:
            astronaut["missions"].append(mission)
        astronaut["hours"] += hours

    def top_astronaut(self):
        if not self.dict_astronauts:
            return None
        return max(self.dict_astronauts, key=lambda n: self.dict_astronauts[n]["hours"])

    def missions_summary(self):
        return sum(len(a["missions"]) for a in self.dict_astronauts.values())


# Тест:
s = SpaceStation()
s.add_astronaut("Ivan")
s.record_mission("Ivan", "Mars Alpha", 200)
s.record_mission("Ivan", "Moon Echo", 100)
print(s.top_astronaut()) # Ivan
print(s.missions_summary()) # 2