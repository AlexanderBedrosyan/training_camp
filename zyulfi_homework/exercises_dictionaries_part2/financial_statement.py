# ЗАДАЧА 4: Финансов отчет
# ---------------------------------------------------------------
# История:
# Фирма анализира месечните си приходи и разходи.
# Условие:
# Напиши функция profit_report(finances), която връща
# {месец: печалба} и най-печелившия месец.
# data = {"Януари":{"приходи":2000,"разходи":1500}, "Февруари":{"приходи":2500,"разходи":2600},
#          "Март":{"приходи":3000,"разходи":2000}}
# print(profit_report(data))
# Очакван изход: ({'Януари':500,'Февруари':-100,'Март':1000}, 'Март')


class FinancialStatement:
    def __init__(self, curr_data):
        self.curr_data = curr_data

    def report(self):
        report_dict = {}
        for month, turnover in self.curr_data.items():
            report_dict[month] = (turnover["приходи"] - turnover["разходи"])
        return report_dict

    def best_month(self):
        return sorted(self.report().items(), key=lambda item: - item[1])[0][0]

    def profit_report(self):
        return self.report(), self.best_month()


data = {"Януари":{"приходи":2000,"разходи":1500}, "Февруари":{"приходи":2500,"разходи":2600}, "Март":{"приходи":3000,"разходи":2000}}

financial = FinancialStatement(data)
print(financial.profit_report())

# Очакван изход: ({'Януари':500,'Февруари':-100,'Март':1000}, 'Март')