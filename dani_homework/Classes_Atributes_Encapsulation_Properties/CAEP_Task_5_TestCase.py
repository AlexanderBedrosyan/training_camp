# Създай клас с:
#
# protected атрибут _name
# private атрибут __status (по подразбиране "Not Run")
# метод run() – променя __status на "Passed"
# @property за status
# Примерен вход:
#
# t = TestCase("Check sum")
# print(t.status)  # Not Run
# t.run()
# print(t.status)  # Passed
#--------------------------------------------------------