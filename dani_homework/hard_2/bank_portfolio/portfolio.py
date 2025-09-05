#Portfolio: списък от Accounts и Investments; методи total_value(), projected_value(years)

from __future__ import annotations
from typing import List
from account import Account
from investment import Investment

class Portfolio:
    def __init__(self) -> None:
        self.__accounts: List[Account] = []
        self.__investments: List[Investment] = []

    def add_account(self, account: Account) -> None:
        self.__accounts.append(account)

    def add_investment(self, investment: Investment) -> None:
        self.__investments.append(investment)

    def total_value(self) -> float:

        total_accounts = sum(a.balance for a in self.__accounts)
        total_invests_now = sum(inv.amount for inv in self.__investments)
        return total_accounts + total_invests_now

    def projected_value(self, years: int) -> float:
        if years < 0:
            raise ValueError("Years cannot be negative.")
        total_accounts = sum(a.balance for a in self.__accounts)
        total_invests_future = sum(inv.calculate_return(years) for inv in self.__investments)
        return total_accounts + total_invests_future

    def __str__(self) -> str:
        return (f"Portfolio(accounts={len(self.__accounts)}, "
                f"investments={len(self.__investments)})")