import sys
from pathlib import Path

数字 = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}


def 失败(消息):
    sys.stderr.write(消息 + "\n")
    raise SystemExit(1)


def 读页(文本):
    if 文本 == "十":
        return 10
    if 文本.startswith("十") and len(文本) == 2 and 文本[1] in 数字:
        return 10 + 数字[文本[1]]
    if "十" in 文本:
        左, 右 = 文本.split("十")
        if 左 not in 数字:
            失败("页码不对")
        数 = 数字[左] * 10
        if 右 == "":
            return 数
        if len(右) == 1 and 右 in 数字:
            return 数 + 数字[右]
        失败("页码不对")
    if len(文本) == 1 and 文本 in 数字:
        return 数字[文本]
    失败("页码不对")


def 主():
    路径 = Path("书页")
    if not 路径.is_file():
        失败("找不到书页")
    原文 = 路径.read_text(encoding="utf-8")
    if 原文 == "":
        失败("书页不对")
    行 = 原文.split("\n")
    if 行 and 行[-1] == "":
        行.pop()
    if not 行:
        失败("书页不对")
    首 = 行[0].split(" ")
    if len(首) != 2 or 首[0] != "页" or 首[1] == "":
        失败("书页不对")
    栏 = []
    for 条 in 行[1:]:
        段 = 条.split(" ")
        if len(段) != 2 or 段[0] != "栏" or 段[1] == "":
            失败("书页不对")
        栏.append(段[1])
    if len(栏) < 1 or len(栏) > 8:
        失败("书页不对")
    页 = 读页(首[1])
    顺序 = list(reversed(栏))
    出 = ["页码 %s" % 页]
    for 序, 文 in enumerate(顺序, 1):
        出.append("第%s栏 %s" % (序, 文))
    sys.stdout.write("\n".join(出) + "\n")


if __name__ == "__main__":
    主()
