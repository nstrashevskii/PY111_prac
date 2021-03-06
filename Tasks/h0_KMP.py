from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    pi = [0] * len(prefix_str)  # префикс таблица
    j = 0  # граница префикса
    i = 1  # граница сцффикса

    while i < len(prefix_str):
        if prefix_str[i] != prefix_str[j]:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j - 1]
        else:
            pi[i] = j + 1
            j += 1
            i += 1
    return pi


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    # 1. Сравниваем `i-й` элемент строки и `j-й` элемент шаблона
    # 2. Если они равны - увеличиваем оба счетчика (и проверяем условие выхода)
    # 3. Если не равны – значит мы нашли несовпадение где-то в середине шаблона,
    # нужно вычислить, с какого символа шаблона нужно продолжать. `j = pi(j-1)`
    pref_fun = _prefix_fun(substr)  # префикс таблица
    i = j = 0  # индексы элементов строки и подстроки
    while i < len(inp_string) and j < len(substr):
        if substr[j] == inp_string[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = pref_fun[j - 1]
    else:
        if j == len(substr):
            return i - j
    return None
