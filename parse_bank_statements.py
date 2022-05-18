from combine import StatementsCombiner
from model import Bank


if __name__ == "__main__":
    files = [
        ("bank1.csv", Bank.BANK1),
        ("bank2.csv", Bank.BANK2),
        ("bank3.csv", Bank.BANK3),
    ]

    combiner = StatementsCombiner()
    statements = combiner.combine(files)