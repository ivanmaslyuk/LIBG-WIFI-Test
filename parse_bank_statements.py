from combine import combine_statements
from export import export_statements_to_csv
from model import Bank


if __name__ == "__main__":
    files = [
        ("bank1.csv", Bank.BANK1),
        ("bank2.csv", Bank.BANK2),
        ("bank3.csv", Bank.BANK3),
    ]

    statements = combine_statements(files)
    export_statements_to_csv("results.csv", statements)
