# Задача 5: Космическа станция
# Създай клас SpaceStation, който следи астронавти и техните мисии.
# Изисквания:
# Речник {астронавт: {"missions": [мисии], "hours": общо_часове}}
# add_astronaut(name)
# record_mission(name, mission, hours)
# top_astronaut() — връща астронавта с най-много часове в мисии.
# missions_summary() — брои общо мисиите в станцията.

class SpaceStation:
    def __init__(self):
        self.space_station_dict = {}

    def add_astronaut(self, name):
        if name not in self.space_station_dict:
            self.space_station_dict[name] = {"missions": [], "hours": 0}

    def record_mission(self, name, mission, hours):
        if name in self.space_station_dict:
            self.space_station_dict[name]["missions"].append(mission)
            self.space_station_dict[name]["hours"] += hours
        else:
            print("Error")

    def top_astronaut(self):
        return sorted(self.space_station_dict.items(), key=lambda x: -x[1]["hours"])[0][0]

    def missions_summary(self):
        print(list(self.space_station_dict.values()))
        return sum([len(element["missions"]) for element in self.space_station_dict.values()])


# Тест:
s = SpaceStation()
s.add_astronaut("Ivan")
s.record_mission("Ivan", "Mars Alpha", 200)
s.record_mission("Ivan", "Moon Echo", 100)
s.add_astronaut("Georgi")
s.record_mission("Georgi", "GGT", 25)
print(s.top_astronaut()) # Ivan
print(s.missions_summary()) # 2