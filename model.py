import dataclasses
import datetime
import enum


class Bank(enum.Enum):
    BANK1 = "bank1"
    BANK2 = "bank2"
    BANK3 = "bank3"


class TransactionType(enum.Enum):
    ADD = "add"
    REMOVE = "remove"


@dataclasses.dataclass
class Statement:
    date: datetime.date
    transaction: TransactionType
    amount: float
    to: int
    source: int
