"""参考答案（不要提前看！先自己写 40 分钟再打开）

对应 ex_w00d3.py / ex_w00d4.py / ex_w00d5.py / ex_w01d1.py
"""
import json, os, numpy as np

# ---------------- W00D3
def q1_abs(n):
    return n if n >= 0 else -n

def q2_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 60: return "C"
    else: return "D"

def q3_count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

def q4_sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def q5_even_double(xs):
    return [x * 2 for x in xs if x % 2 == 0]

# ---------------- W00D4
def q1_numbers():
    return [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]

def q2_word_count(text):
    d = {}
    for w in text.split():
        d[w.lower()] = d.get(w.lower(), 0) + 1
    return d

def q3_read_todos(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [x["title"] for x in data if x["done"]]

# ---------------- W00D5
def q1_zeros(): return np.zeros((3, 4))
def q2_arange(): return np.arange(5)
def q3_transpose(a): return a.T
def q4_row(a): return a[1]
def q5_slice(a): return a[0:2, 2:4]
def q6_broadcast(a, b): return a + b
def q7_outer(a, b): return a + b
def q8_mean(a): return a.mean(axis=-1)

# ---------------- W01D1
def mean(xs):
    if not xs: return None
    return sum(xs) / len(xs)

def std(xs):
    if not xs: return None
    m = mean(xs)
    return (sum((x - m) ** 2 for x in xs) / len(xs)) ** 0.5

def summary(todos):
    n = sum(1 for t in todos if not t["done"])
    return "全部完成" if n == 0 else "还剩 %d 项未完成" % n

def safe_int(s):
    try: return int(s)
    except ValueError: return -1

class TodoList:
    def __init__(self): self._items = []
    def add(self, title):
        if not title.strip(): raise ValueError("title 不能为空")
        self._items.append({"title": title, "done": False})
    def complete(self, title):
        for it in self._items:
            if it["title"] == title:
                it["done"] = True
                return
        raise KeyError(title)
    def pending_count(self):
        return sum(1 for it in self._items if not it["done"])
    def to_json(self):
        return self._items
    @classmethod
    def from_json(cls, s):
        obj = cls()
        obj._items = s if isinstance(s, list) else json.loads(s)
        return obj
