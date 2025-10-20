#  Задача 9: Финансов отчет
# report = {
#     "January": {"income": 12000, "expenses": 8000},
#     "February": {"income": 15000, "expenses": 9000},
#     "March": {"income": 10000, "expenses": 9500}
# }
# Изисквания:
#
# Изчисли печалбата (income - expenses) за всеки месец.
# Намери месеца с най-голяма печалба.
# Изчисли средна печалба за трите месеца.

class FinancialStatement:
    def __init__(self, curr_report):
        self.curr_report = curr_report

    def profit(self):
        profit_dict = {}
        for month, turnover in self.curr_report.items():
            profit_dict[month] = (list(turnover.values())[0]) - (list(turnover.values())[1])

        return profit_dict

    def best_month(self):
        best_month = None
        most_profit = 0
        for month, profit in self.profit().items():
            if profit >= most_profit:
                most_profit = profit
                best_month = month
        return best_month

    def average_month_profit(self):
        return sum(self.profit().values()) / len(self.profit())

report = {
    "January": {"income": 12000, "expenses": 8000},
    "February": {"income": 15000, "expenses": 9000},
    "March": {"income": 10000, "expenses": 9500}
}

fs = FinancialStatement(report)
print(fs.profit())
print(fs.best_month())
print(fs.average_month_profit())