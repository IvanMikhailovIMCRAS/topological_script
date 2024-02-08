from typing import List, Tuple


def bonds_parser(script: str) -> List[Tuple[int, int]]:
    """_summary_

    Args:
        script (str): topological script defining the molecule,
        sample: "(Na)1(C0)1[(O)1]((C)1([(H)1])2)3(O)1(H)1"

    Returns:
        List[Tuple[int, int]]: list of connected pairs of beads,
        sample: [(0,1), (1,2), (1,3), (3,4), (3,5), (3,6), (6,7), (6,8), (6,9), (9,10), (9,11), (9,12), (12,13)]
    """
    indexes = list()
    index_br_close = None
    index_br_open = None

    for i, symbol in enumerate(script):
        if symbol == "(":
            index_br_open = i

        if symbol == ")" and index_br_open is not None:
            indexes.append((index_br_open, i))
            index_br_open = None
    list_script = list(script)
    for i in indexes:
        for j in range(i[0], i[1] + 1):
            list_script[j] = " "

    list_script = "".join(list_script)
    list_new = []
    for el in list_script:
        # print(el)
        if el == " ":
            label = False
            continue
        elif el in "()[]":
            label = False
            list_new.append(el)
        elif el.isdigit:
            if label:
                list_new[-1] += el
            else:
                list_new.append(el)
            label = True

    index_br_open = None
    tmp_list = []
    indexes_open = []
    indexes_close = []
    # print(list_new)
    while ")" in list_new:
        for i, symbol in enumerate(list_new):
            if symbol == "(":
                index_br_open = i

            if symbol == ")" and index_br_open is not None:
                if len(list_new) >= i + 2:
                    list_new = (
                        list_new[0:index_br_open]
                        + list_new[index_br_open + 1 : i] * int(list_new[i + 1])
                        + list_new[i + 2 :]
                    )
                else:
                    list_new = list_new[0:index_br_open] + list_new[
                        index_br_open + 1 : i
                    ] * int(list_new[i + 1])
                # print(list_new)
                index_br_open = None
    tmp_list = [""]

    for i in range(len(list_new)):
        print(list_new[i].isdigit())
        if tmp_list[-1].isdigit() and list_new[i].isdigit():
            tmp_list[-1] = str(int(tmp_list[-1]) + int(list_new[i]))
        else:
            tmp_list.append(list_new[i])
    del tmp_list[0]
    print(tmp_list)

    # print(list_new)


if __name__ == "__main__":
    print(bonds_parser("(Na)100(C0)1[(O)1]((C)1([(H)1])2)3(O)1(H)1"))
