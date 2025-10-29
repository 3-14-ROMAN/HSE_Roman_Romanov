import sys, ast, re

def is_monotonic(nums: list[int]) -> bool:
    n = len(nums)
    if n <= 2:
        return True
    inc = all(nums[i] <= nums[i + 1] for i in range(n - 1))
    if inc:
        return True
    dec = all(nums[i] >= nums[i + 1] for i in range(n - 1))
    return dec

# Находим ОДИН список в строке (с optional 'nums =')
_SINGLE_RE = re.compile(r"^\s*(?:nums\s*=\s*)?(\[[^\]]*\])\s*$")
# Находим ВСЕ списки в строке (несколько подряд, даже без разделителей)
_MULTI_RE = re.compile(r"(?:nums\s*=\s*)?(\[[^\]]*\])")

def parse_one(s: str) -> list[int]:
    m = _SINGLE_RE.match(s)
    if not m:
        raise ValueError
    lst = ast.literal_eval(m.group(1))
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        raise ValueError
    return lst

def parse_many(s: str) -> list[list[int]]:
    items = []
    for g in _MULTI_RE.findall(s):
        lst = ast.literal_eval(g)
        if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
            raise ValueError
        items.append(lst)
    return items

def handle_line(line: str) -> None:
    # Сначала пробуем выцепить несколько списков в одной строке
    many = parse_many(line)
    if many:
        for lst in many:
            print("true" if is_monotonic(lst) else "false")
        return
    # Иначе — одиночный формат
    try:
        lst = parse_one(line)
        print("true" if is_monotonic(lst) else "false")
    except Exception:
        print("format: nums = [1,2,3]")

def main():
    if len(sys.argv) > 1:
        handle_line(" ".join(sys.argv[1:]))
        return

    print("format: nums = [1,2,3]  |  exit для выхода")
    while True:
        try:
            line = input("nums> ")
        except EOFError:
            break
        if not line:
            continue
        t = line.strip().lower()
        if t in {"exit", "quit", "q"}:
            break
        handle_line(line)

if __name__ == "__main__":
    main()
