"""W01D1 练习：把"能跑但很乱"的代码重构成函数 + 类

这是第 1 天我给你的那 3 个练习里的第 1 个，这次配好了完整测试。
用法：python3 ex_w01d1.py

题目背景：下面这个类 TodoList 里塞了所有逻辑，而且没有任何错误处理。
你现在的活：把它拆开、补上边界情况的处理，让测试全绿。

⚠️ 这是一个「改代码」的练习，不是「填 TODO」。函数签名已经定好，
   你只需要改函数体（可以随便加 helper 函数）。
"""
import json
import os
import sys


# ---------------------------------------------------------------- 第 1 题
# 把  todo.py 里 "算平均" 的代码重构成函数：
#   输入一个列表 xs，返回平均值；如果 xs 是空列表，返回 None（不要报错！）
def mean(xs):
    pass


# ---------------------------------------------------------------- 第 2 题
# 标准差（总体标准差，除以 n 而不是 n-1）。
# 空列表返回 None。长度 1 返回 0.0。
# 提示：先调用 mean(xs)，再对每个 x 求 (x - m)**2 求和，开根号（用  ** 0.5）
def std(xs):
    pass


# ---------------------------------------------------------------- 第 3 题
# 给一个 todos 列表（元素 {"title": str, "done": bool}），
# 返回 "还剩 2 项未完成" 这样的字符串
def summary(todos):
    pass


# ---------------------------------------------------------------- 第 4 题
# 错误处理练习：把字符串 s 转成 int 并返回；转不了（比如 "abc"）返回 -1
# 提示：try / except ValueError
def safe_int(s):
    pass


# ---------------------------------------------------------------- 第 5 题
# 把 TodoList 改到测试全绿。要求：
#   - add(title)：title 是空字符串时 抛 ValueError
#   - complete(title)：title 不存在时 抛 KeyError
#   - to_json()：返回能 json.dumps 的列表
#   - from_json(s)：从字符串恢复（是类方法）
class TodoList:
    def __init__(self):
        self._items = []

    def add(self, title):
        # TODO
        pass

    def complete(self, title):
        # TODO
        pass

    def pending_count(self):
        # TODO 返回未完成的数量
        pass

    def to_json(self):
        # TODO 返回 self._items 本身也是可以的（列表里是 dict）
        pass

    @classmethod
    def from_json(cls, s):
        # TODO
        pass


# =================================================================
def _run():
    failed = 0

    def check(name, fn, want):
        nonlocal failed
        try:
            got = fn()
        except Exception as e:
            got = "<异常 %s: %s>" % (type(e).__name__, e)
        if got == want or (isinstance(got, float) and isinstance(want, float) and abs(got - want) < 1e-9):
            print("  [ok]  %s" % name)
        else:
            failed += 1
            print("  [XX]  %s  期望 %r，实际 %r" % (name, want, got))

    check("mean([1,2,3])", lambda: mean([1, 2, 3]), 2.0)
    check("mean([]) 不报错", lambda: mean([]), None)
    check("mean([5])", lambda: mean([5]), 5.0)
    check("std([2,4,4,4,5,5,7,9])", lambda: std([2, 4, 4, 4, 5, 5, 7, 9]), 2.0)
    check("std([]) ", lambda: std([]), None)
    check("std([3])", lambda: std([3]), 0.0)
    check("summary 0 项", lambda: summary([]), "全部完成")
    check("summary 2 项",
          lambda: summary([{"title": "a", "done": True}, {"title": "b", "done": False},
                           {"title": "c", "done": False}]), "还剩 2 项未完成")
    check("safe_int('42')", lambda: safe_int("42"), 42)
    check("safe_int('abc')", lambda: safe_int("abc"), -1)

    t = TodoList()
    check("add 正常", lambda: (t.add("买菜"), len(t._items))[1], 1)
    try:
        t.add("   ")
        print("  [XX]  add 空字符串应该抛 ValueError")
        failed += 1
    except ValueError:
        print("  [ok]  add 空字符串抛 ValueError")
    try:
        t.complete("不存在")
        print("  [XX]  complete 不存在的项应该抛 KeyError")
        failed += 1
    except KeyError:
        print("  [ok]  complete 不存在的项抛 KeyError")
    t.add("跑步")
    t.complete("跑步")
    check("pending_count", lambda: t.pending_count(), 1)
    check("json 往返",
          lambda: [x["title"] for x in TodoList.from_json(t.to_json())._items], ["买菜", "跑步"])

    print()
    if failed == 0:
        print("全部通过！提交：~/learn/d.sh \"feat: 完成 W01D1 重构与错误处理\"")
    else:
        print("还有 %d 处不对。" % failed)
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run() else 0)
