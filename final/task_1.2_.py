_ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
_SUB_PAIRS = {"IV", "IX", "XL", "XC", "CD", "CM"}

def roman_to_int(s: str) -> int:
    if not isinstance(s, str) or not s:
        raise ValueError("ожидается непустая строка")
    s = s.upper()
    if any(ch not in _ROMAN for ch in s):
        raise ValueError("недопустимые символы")

    repeat = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            repeat += 1
            if s[i] in "VLD" or repeat > 3:
                raise ValueError("слишком много повторов")
        else:
            repeat = 1

    total = 0
    i = 0
    while i < len(s):
        cur = _ROMAN[s[i]]
        if i + 1 < len(s) and cur < _ROMAN[s[i + 1]]:
            pair = s[i] + s[i + 1]
            if pair not in _SUB_PAIRS:
                raise ValueError("неверная пара")
            total += _ROMAN[s[i + 1]] - cur
            i += 2
        else:
            total += cur
            i += 1
    return total


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Roman → Int")
    p.add_argument("s", help="Римское число (например, MCMXCIV)")
    args = p.parse_args()
    print(roman_to_int(args.s))
