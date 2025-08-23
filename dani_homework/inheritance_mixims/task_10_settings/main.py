from config import Config

c = Config("dark", "bg")
c.set_attr("theme", "light")
print(c.get_attr("theme"))  # light