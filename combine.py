import csv
from typing import List, Tuple, Generator

from model import Bank, Statement
from parse import StatementParserFactory


class StatementsCombiner:
    def combine(self, files: List[Tuple[str, Bank]]) -> List[Statement]:
        statements = []

        for filename, bank in files:
            statement_parser = StatementParserFactory.get_parser(bank)
            for row in self._get_rows_from_file(filename):
                statements.append(statement_parser.parse(row))
        
        statements = list(sorted(statements, key=lambda s: s.date))
        return statements

    def _get_rows_from_file(self, filename: str) -> Generator[List[str], None, None]:
        with open(filename) as file:
            csv_reader = csv.reader(file)

            next(csv_reader) # Skip header

            for row in csv_reader:
                yield row
