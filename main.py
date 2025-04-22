# main.py
def say_hello(name):
    return f"你好，{name}！欢迎来到 Python 世界！"

if __name__ == "__main__":
    user = input("请输入你的名字：")
    print(say_hello(user))
