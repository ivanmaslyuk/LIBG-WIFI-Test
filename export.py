import csv
from typing import List

from model import Statement

CSV_HEADER = ["date", "transaction", "amount", "to", "from"]


def export_statements_to_csv(filename, results: List[Statement]):
    with open(filename, "w") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(CSV_HEADER)

        for statement in results:
            csv_writer.writerow([
                statement.date.strftime("%d %b %Y"),
                statement.transaction.value,
                "%00.2f" % statement.amount,
                statement.to,
                statement.source,
            ])
