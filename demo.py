import sys
from datetime import datetime

#!/usr/bin/env python3
# demo_print.py - 验证 print 是否可用，并把输出写到当前目录的文件中


def main():
    lines = [
        f"Print demo started at {datetime.now().isoformat()}",
        "Hello, world! This is a print() test.",
        "Printing numbers: " + ", ".join(str(i) for i in range(5)),
        "Print demo finished."
    ]

    # 打印到控制台
    for line in lines:
        print(line)

    # 写入当前目录的文件
    out_file = "print_output.txt"
    try:
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    except Exception as e:
        print(f"Failed to write {out_file}: {e}", file=sys.stderr)
        return 1

    print(f"Wrote output to ./{out_file}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())