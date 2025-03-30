import time
import signal
import sys
import traceback


class RAG:
    def __init__(self):
        # 设置信号处理器
        self.original_handler = signal.getsignal(signal.SIGINT)
        signal.signal(signal.SIGINT, self._custom_handler)

    def query(self, q, **kwargs):
        # 模拟查询功能
        print(f"Querying with: {q}")
        return self

    def write(self, output_path):
        # 模拟写入功能，包含sleep操作
        print(f"Writing to {output_path}")
        try:
            # 这里的sleep操作是为了给用户时间按Ctrl+C
            time.sleep(6)  # 当用户在这里按Ctrl+C时，会触发自定义的错误信息
            print(f"Successfully wrote to {output_path}")
        except KeyboardInterrupt:
            # 创建自定义的traceback信息
            stack = [
                f'  File "{sys.argv[0]}", Line 2, in <module>\n',
                f'    ret.write("{output_path}")\n',
                f'  File "/root/anaconda3/lib/python3.9/site-packages/mindx/__init__.py", Line 57, in write\n',
                f'    time.sleep(6)\n'
            ]

            # 打印自定义的错误信息
            sys.stderr.write("^CTraceback (most recent call last):\n")
            sys.stderr.write("".join(stack))
            sys.stderr.write("KeyboardInterrupt\n")
            sys.exit(1)

    def _custom_handler(self, sig, frame):
        # 这个函数不会被直接调用，因为KeyboardInterrupt异常会先被引发
        # 但为了完整性，我们仍然实现它
        raise KeyboardInterrupt