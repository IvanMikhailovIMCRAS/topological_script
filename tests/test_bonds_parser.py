from typing import List

import pytest

from topological_script import bonds_parser


@pytest.mark.parametrize(
    "script, expected_result",
    [
        ("(H)1(O)1(H)1", [(0, 1), (1, 2)]),
        (
            "(A)2[(A)2[(A)2](A)2](A)2",
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (6, 7), (1, 8), (8, 9)],
        ),
        (
            "(Na)1(C0)1[(O)1]((C)1([(H)])2)3(O)1(H)1",
            [
                (0, 1),
                (1, 2),
                (1, 3),
                (3, 4),
                (3, 5),
                (3, 6),
                (6, 7),
                (6, 8),
                (6, 9),
                (9, 10),
                (9, 11),
                (9, 12),
                (12, 13),
            ],
        ),
    ],
)
def test_bonds_parser(script: str, expected_result: List[str]) -> None:
    assert bonds_parser(script) == expected_result
