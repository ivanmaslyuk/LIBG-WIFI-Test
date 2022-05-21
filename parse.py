from datetime import datetime
from typing import Dict, Callable

from model import Statement, Bank, TransactionType


def parse_bank1_statement(values: dict) -> Statement:
    return Statement(
        date=datetime.strptime(values["timestamp"], "%b %d %Y").date(),
        transaction=TransactionType(values["type"]),
        amount=float(values["amount"]),
        to=int(values["to"]),
        source=int(values["from"]),
    )


def parse_bank2_statement(values: dict) -> Statement:
    return Statement(
        date=datetime.strptime(values["date"], "%d-%m-%Y").date(),
        transaction=TransactionType(values["transaction"]),
        amount=float(values["amounts"]),
        to=int(values["to"]),
        source=int(values["from"]),
    )


def parse_bank3_statement(values: dict) -> Statement:
    return Statement(
        date=datetime.strptime(values["date_readable"], "%d %b %Y").date(),
        transaction=TransactionType(values["type"]),
        amount=float(values["euro"]) + (float(values["cents"]) / 100),
        to=int(values["to"]),
        source=int(values["from"]),
    )


STATEMENT_PARSERS: Dict[Bank, Callable[[dict], Statement]] = {
    Bank.BANK1: parse_bank1_statement,
    Bank.BANK2: parse_bank2_statement,
    Bank.BANK3: parse_bank3_statement,
}
