"""W00D3 练习：Python 变量 / 类型 / 条件 / 循环 —— 5 道题

怎么用：
    1. 打开终端，运行  cd ~/learn/learn-log
    2. 在 VS Code 里打开这个文件： code ex_w00d3.py
    3. 每道题只填 TODO 下面的函数体，不要改测试部分
    4. 每填完一题，运行一次：  python3 ex_w00d3.py
    5. 全部显示 "全部通过" 就算完成，然后提交：
       ~/learn/d.sh "feat: 完成 W00D3 的 5 道 Python 基础题"
"""
import sys


# ---------------------------------------------------------------- 第 1 题
# 输入一个整数 n，返回 n 的绝对值。
# 提示：可以用 if，也可以用内置函数 abs()（两种都写一遍试试）
# 例子： -3 -> 3 ； 5 -> 5 ； 0 -> 0
def q1_abs(n):
    # TODO: 把下面的 pass 替换成你的代码
    pass


# ---------------------------------------------------------------- 第 2 题
# 输入一个整数 score（0-100），返回等级字符串：
#   >= 90 -> "A"，80-89 -> "B"，60-79 -> "C"，否则 "D"
# 提示：用 if / elif / else，注意条件从上往下判断
def q2_grade(score):
    # TODO
    pass


# ---------------------------------------------------------------- 第 3 题
# 输入一个字符串 s，返回它里面有多少个元音字母（a e i o u，不分大小写）。
# 提示：for 循环遍历每个字符；可以用  c.lower()  把字符转小写
# 例子： "Hello World" -> 3
def q3_count_vowels(s):
    # TODO
    pass


# ---------------------------------------------------------------- 第 4 题
# 输入一个整数 n，返回 1+2+...+n 的和（用 for 循环写，不要用公式）
# 例子： n=5 -> 15 ； n=0 -> 0
def q4_sum_to_n(n):
    # TODO
    pass


# ---------------------------------------------------------------- 第 5 题
# 输入一个列表 xs（里面是整数），返回一个新列表：
# 只保留偶数，并且每个数乘以 2。
# 例子： [1, 2, 3, 4] -> [4, 8]
# 提示：先写下 for 循环 + if 版本，再用列表推导式 [ ... for x in xs if ...] 写一遍
def q5_even_double(xs):
    # TODO
    pass


# =================================================================
# 下面是测试代码，不要修改，直接运行本文件即可
# =================================================================
def _run():
    cases = [
        ("第1题 abs(-3)", q1_abs(-3), 3),
        ("第1题 abs(5)", q1_abs(5), 5),
        ("第1题 abs(0)", q1_abs(0), 0),
        ("第2题 grade(95)", q2_grade(95), "A"),
        ("第2题 grade(85)", q2_grade(85), "B"),
        ("第2题 grade(60)", q2_grade(60), "C"),
        ("第2题 grade(59)", q2_grade(59), "D"),
        ("第3题 vowels('Hello World')", q3_count_vowels("Hello World"), 3),
        ("第3题 vowels('xyz')", q3_count_vowels("xyz"), 0),
        ("第4题 sum(5)", q4_sum_to_n(5), 15),
        ("第4题 sum(0)", q4_sum_to_n(0), 0),
        ("第5题 even_double([1,2,3,4])", q5_even_double([1, 2, 3, 4]), [4, 8]),
    ]
    failed = 0
    for name, got, want in cases:
        if got == want:
            print("  [ok]  %s  ->  %r" % (name, got))
        else:
            failed += 1
            print("  [XX]  %s  期望 %r，实际 %r" % (name, want, got))
    print()
    if failed == 0:
        print("全部通过！可以提交了：~/learn/d.sh \"feat: 完成 W00D3 的 5 道 Python 基础题\"")
    else:
        print("还有 %d 处不对，回去改 TODO 部分再运行。" % failed)
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run() else 0)
