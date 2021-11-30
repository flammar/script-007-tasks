from typing import List, Callable, Dict


def setpath(my_dict: dict, key: str or List[str], value):
    adeep(my_dict, key, lambda d, k: d.update({k: value}), True)


def getpath(my_dict: dict, key: str or List[str]):
    ret = []
    adeep(my_dict, key, lambda d, k: ret.append(d[k]))
    return ret[0]


def adeep(my_dict: dict, key: str or List[str], action: Callable, create_if_absent: bool = False):
    def my_adeep(my_dict: dict, key: str or List[str]):
        adeep(my_dict, key, action, create_if_absent)

    if isinstance(key, str):
        if '.' in key:
            my_adeep(my_dict, key.split("."))
        else:
            action(my_dict, key)
    elif isinstance(key, list):
        if (len(key)) == 1:
            my_adeep(my_dict, key[0])
        else:
            if '.' in key[0]:
                my_adeep(my_dict, key[0].split(".") + key[1:])
            else:
                if key[0] not in my_dict and create_if_absent:
                    my_dict[key[0]] = {}
                my_adeep(my_dict[key[0]], key[1:])


def keys(my_dict: dict) -> List[str]:
    acc = []

    def my_list_keys(my_dict1: dict, my_acc: List[str], prefix: str = "") -> None:
        for k, v in my_dict1.items():
            pk = k if not prefix else prefix + "." + k
            if isinstance(v, dict):
                my_list_keys(v, my_acc, pk)
            else:
                my_acc.append(pk)

    my_list_keys(my_dict, acc)
    return acc


def get_(l: List or dict, i: int or str, default=None):
    if l is None or (isinstance(l, list) and len(l) <= i or isinstance(l, dict) and i not in l):
        return default
    else:
        return l[i]
