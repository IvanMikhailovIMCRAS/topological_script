from typing import List, Tuple


def bonds_parser(script: str) -> List[Tuple[int, int]]:
    """_summary_

    Args:
        script (str): topological script defining the molecule,
        sample: "(Na)1(C0)1[(O)1]((C)1([(H)])2)3(O)1(H)1"

    Returns:
        List[Tuple[int, int]]: list of connected pairs of beads,
        sample: [(0,1), (1,2), (1,3), (3,4), (3,5), (3,6), (6,7), (6,8), (6,9), (9,10), (9,11), (9,12), (12,13)]
    """

    pass
