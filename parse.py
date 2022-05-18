from datetime import datetime, date

from model import Statement, Bank, TransactionType


class StatementParser:
    def parse(self, values: dict) -> Statement:
        raise NotImplementedError("Parsing not implemented.")


class Bank1StatementParser(StatementParser):
    def parse(self, values: dict) -> Statement:
        return Statement(
            date=datetime.strptime(values["timestamp"], "%b %d %Y").date(),
            transaction=TransactionType(values["type"]),
            amount=float(values["amount"]),
            to=int(values["to"]),
            source=int(values["from"]),
        )


class Bank2StatementParser(StatementParser):
    def parse(self, values: dict) -> Statement:
        return Statement(
            date=datetime.strptime(values["date"], "%d-%m-%Y").date(),
            transaction=TransactionType(values["transaction"]),
            amount=float(values["amounts"]),
            to=int(values["to"]),
            source=int(values["from"]),
        )


class Bank3StatementParser(StatementParser):
    def parse(self, values: dict) -> Statement:
        return Statement(
            date=datetime.strptime(values["date_readable"], "%d %b %Y").date(),
            transaction=TransactionType(values["type"]),
            amount=float(values["euro"]) + (float(values["cents"]) / 100),
            to=int(values["to"]),
            source=int(values["from"]),
        )


class StatementParserFactory:
    @staticmethod
    def get_parser(bank: Bank) -> StatementParser:
        if bank == Bank.BANK1:
            return Bank1StatementParser()
        elif bank == Bank.BANK2:
            return Bank2StatementParser()
        elif bank == Bank.BANK3:
            return Bank3StatementParser()
        else:
            raise Exception("Unknown bank.")
