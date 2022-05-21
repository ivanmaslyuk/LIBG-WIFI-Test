import csv
from typing import List, Tuple, Iterator

from model import Bank, Statement
from parse import STATEMENT_PARSERS


def combine_statements(files: List[Tuple[str, Bank]]) -> List[Statement]:
    statements = []

    for filename, bank in files:
        statement_parser = STATEMENT_PARSERS[bank]
        for row in _get_rows_from_file(filename):
            statements.append(statement_parser(row))

    statements = list(sorted(statements, key=lambda s: s.date))
    return statements


def _get_rows_from_file(filename: str) -> Iterator[dict]:
    with open(filename) as file:
        csv_reader = csv.reader(file)

        header = next(csv_reader)

        for row in csv_reader:
            if not row:
                continue

            yield {header[idx]: value for idx, value in enumerate(row)}
