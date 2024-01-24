from typing import List


def types_parser(script: str) -> List[str]:
    """_summary_

    Args:
        script (str): topological script defining the molecule,
        sample: "(Na)1(C0)1[(O)1]((C)1([(H)])2)3(O)1(H)1"

    Returns:
        List[str]: list of beads (atoms) types,
        sample: ['Na', 'C0', 'O', 'C', 'H', 'H', 'C', 'H', 'H', 'C', 'H', 'H', 'O', 'H']
    """

    pass
