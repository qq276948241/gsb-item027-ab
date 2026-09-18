import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "散页"))
from 页码 import 读页
from 栏序 import 排栏

def 主():
    原文 = Path("书页").read_text(encoding="utf-8")
    行 = 原文.split("\n")
    if 行 and 行[-1] == "":
        行.pop()
    页 = 读页(行[0].split(" ")[1])
    栏 = 排栏([条.split(" ")[1] for 条 in 行[1:]])
    出 = ["页码 %s" % 页]
    for 序, 文 in enumerate(栏, 1):
        出.append("第%s栏 %s" % (序, 文))
    sys.stdout.write("\n".join(出) + "\n")

if __name__ == "__main__":
    主()
