# 以这份为准
import sys
from pathlib import Path

数字 = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}


def 失败(消息):
    sys.stderr.write(消息 + "\n")
    raise SystemExit(1)


def 读页(文本):
    数 = 0
    for 字 in 文本:
        if 字 not in 数字:
            失败("页写错")
        数 += 数字[字]
    return 数


def 主():
    路径 = Path("书页")
    if not 路径.is_file():
        失败("没有书页")
    原文 = 路径.read_text(encoding="utf-8")
    行 = 原文.split("\n")
    if 行 and 行[-1] == "":
        行.pop()
    首 = 行[0].split(" ")
    栏 = [条.split(" ")[1] for 条 in 行[1:]]
    页 = 读页(首[1])
    出 = ["页码 %s" % 页]
    for 序, 文 in enumerate(栏, 1):
        出.append("第%s栏 %s" % (序, 文))
    sys.stdout.write("\n".join(出) + "\n")


if __name__ == "__main__":
    主()
