import dataclasses
import datetime
import enum
from types import TracebackType


class TransactionType(enum.Enum):
    ADD = "ADD"
    REMOVE = "remove"


@dataclasses.dataclass
class Statement:
    date: datetime.date
    transaction: TracebackType
    amount: float
    to: int
    source: int
