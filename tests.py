from datetime import date

from parse import (
    parse_bank1_statement,
    parse_bank2_statement,
    parse_bank3_statement,
)
from model import Statement, TransactionType


def test_bank1_parsing():
    expected = Statement(
        date=date(2019, 10, 1),
        transaction=TransactionType.REMOVE,
        amount=99.1,
        to=182,
        source=198,
    )

    actual = parse_bank1_statement({
        "timestamp": "Oct 1 2019",
        "type": "remove",
        "amount": "99.10",
        "to": "182",
        "from": "198",
    })

    assert expected == actual


def test_bank2_parsing():
    expected = Statement(
        date=date(2019, 10, 4),
        transaction=TransactionType.ADD,
        amount=2123.99,
        to=198,
        source=188,
    )

    actual = parse_bank2_statement({
        "date": "04-10-2019",
        "transaction": "add",
        "amounts": "2123.99",
        "to": "198",
        "from": "188",
    })

    assert expected == actual


def test_bank3_parsing():
    expected = Statement(
        date=date(2019, 10, 6),
        transaction=TransactionType.ADD,
        amount=1060.44,
        to=198,
        source=188,
    )

    actual = parse_bank3_statement({
        "date_readable": "6 Oct 2019",
        "type": "add",
        "euro": "1060",
        "cents": "44",
        "to": "198",
        "from": "188",
    })

    assert expected == actual
