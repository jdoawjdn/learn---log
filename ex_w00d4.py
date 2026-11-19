"""W00D4 练习：函数 / 列表字典推导 / 文件读写 —— 3 道题

用法：python3 ex_w00d4.py
（和第1天一样，只填 TODO，不要改测试部分）
"""
import json
import os
import sys


# ---------------------------------------------------------------- 第 1 题
# 用列表推导式，返回 1 到 100 之间所有能被 3 整除、且不能被 5 整除的数。
# 提示：range(1, 101)
def q1_numbers():
    # TODO: 一行代码 + return
    pass


# ---------------------------------------------------------------- 第 2 题
# 输入一段文本 text，返回一个字典：每个单词出现次数（只统计小写化后的单词，用 text.split() 切）
# 例子： "a b a" -> {"a": 2, "b": 1}
# 提示：先 dict 初始化为空，遍历单词，用 d.get(w, 0) + 1
def q2_word_count(text):
    # TODO
    pass


# ---------------------------------------------------------------- 第 3 题
# 读 JSON 文件 + 写 JSON 文件（这就是计划里 todo.py 的核心）
# 要求：读取 path 处的 json 列表（元素是 {"title": str, "done": bool}），
#       返回其中 done 为 True 的所有 title 组成的列表。
# 文件不存在时，返回空列表 []（用 os.path.exists 判断）
# 提示：with open(path, encoding="utf-8") as f:  data = json.load(f)
def q3_read_todos(path):
    # TODO
    pass


# =================================================================
# 测试部分，不要修改
# =================================================================
def _run():
    failed = 0

    def check(name, got, want):
        nonlocal failed
        if got == want:
            print("  [ok]  %s" % name)
        else:
            failed += 1
            print("  [XX]  %s  期望 %r，实际 %r" % (name, want, got))

    check("第1题", q1_numbers(), [3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48,
                                  51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99])
    check("第2题", q2_word_count("a b a"), {"a": 2, "b": 1})

    tmp = "_tmp_todos.json"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump([{"title": "买菜", "done": True},
                   {"title": "写作业", "done": False},
                   {"title": "跑步", "done": True}], f, ensure_ascii=False)
    check("第3题(有文件)", q3_read_todos(tmp), ["买菜", "跑步"])
    os.remove(tmp)
    check("第3题(没文件)", q3_read_todos("_不存在的文件.json"), [])

    print()
    if failed == 0:
        print("全部通过！提交：~/learn/d.sh \"feat: 完成 W00D4 函数/推导/文件读写\"")
    else:
        print("还有 %d 处不对。" % failed)
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run() else 0)
