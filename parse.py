from typing import List

from model import Statement, Bank


class StatementParser:
    def parse(values: List[str]) -> Statement:
        raise NotImplementedError("Parsing not implemented.")


class StatementParserFactory:
    @staticmethod
    def get_parser(bank: Bank) -> StatementParser:
        pass
