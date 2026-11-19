"""W00D5 练习：NumPy 形状、广播、切片 —— 8 道题（这是后面 Tensor 形状的地基）

用法：python3 ex_w00d5.py
规则：只填 TODO，不要用 for 循环（NumPy 的意义就是不用循环）
"""
import numpy as np
import sys


# 1. 创建一个形状为 (3, 4) 的全零矩阵
def q1_zeros():
    pass


# 2. 创建一个 (5,) 的数组，值为 0,1,2,3,4
def q2_arange():
    pass


# 3. 输入 (3,4) 的矩阵 a，返回它的转置，形状应为 (4,3)
#    提示：a.T   或   a.transpose()
def q3_transpose(a):
    pass


# 4. 输入 a 形状 (3,4)，返回第 2 行（索引 1），形状 (4,)
def q4_row(a):
    pass


# 5. 输入 a 形状 (3,4)，返回前两行、后两列的子矩阵，形状 (2,2)
#    提示：切片 a[0:2, 2:4]
def q5_slice(a):
    pass


# 6. 广播：输入形状 (3,4) 的矩阵 a 和形状 (4,) 的向量 b，返回 a 的每一行都加上 b
def q6_broadcast(a, b):
    pass


# 7. 广播规则验证：a 形状 (3,1)，b 形状 (1,4)，相加后形状是 (3,4)
#    返回 a + b
def q7_outer(a, b):
    pass


# 8. 输入 a 形状 (2,3,4)，返回最后一维的平均值，结果形状应为 (2,3)
#    提示：a.mean(axis=-1)
def q8_mean(a):
    pass


# =================================================================
def _run():
    failed = 0

    def check(name, got, want):
        nonlocal failed
        ok = isinstance(got, np.ndarray) and np.array_equal(np.asarray(got), np.asarray(want))
        if ok:
            print("  [ok]  %s" % name)
        else:
            failed += 1
            print("  [XX]  %s  期望 %r，实际 %r" % (name, want, got))

    a34 = np.arange(12).reshape(3, 4)
    b4 = np.array([10, 20, 30, 40])

    check("1 zeros (3,4)", q1_zeros(), np.zeros((3, 4)))
    check("2 arange", q2_arange(), np.arange(5))
    _t = q3_transpose(a34)
    if hasattr(_t, "shape") and _t.shape == (4, 3):
        print("  [ok]  3 transpose shape")
    else:
        failed += 1
        print("  [XX]  3 transpose shape  期望 (4, 3)，实际 %r" % (getattr(_t, "shape", _t),))
    check("4 row", q4_row(a34), np.array([4, 5, 6, 7]))
    check("5 slice", q5_slice(a34), np.array([[2, 3], [6, 7]]))
    check("6 broadcast", q6_broadcast(a34, b4), a34 + b4)
    check("7 outer", q7_outer(np.array([[1], [2], [3]]), np.array([[10, 20, 30, 40]])),
          np.array([[11, 21, 31, 41], [12, 22, 32, 42], [13, 23, 33, 43]]))
    check("8 mean", q8_mean(np.arange(24).reshape(2, 3, 4)),
          np.arange(24).reshape(2, 3, 4).mean(axis=-1))

    print()
    if failed == 0:
        print("全部通过！提交：~/learn/d.sh \"feat: 完成 W00D5 NumPy 形状练习\"")
    else:
        print("还有 %d 处不对。" % failed)
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run() else 0)
