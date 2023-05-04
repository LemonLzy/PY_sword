"""
单例模式:
    1. 考虑多线程
    2. 考虑多线程的效率
    3. python中，考虑单例初始化时，init方法覆盖实例的值的情况
    https://medium.com/analytics-vidhya/how-to-create-a-thread-safe-singleton-class-in-python-822e1170a7f6
"""
import threading


class A:
    # 此变量单纯为了做记录使用，如果初始化过对象，则给此私有变量赋值。通过判断该私有变量是否为None，来确定是否实例化过对象
    _instance = None
    _lock = threading.Lock()

    def __init__(self, name):
        if hasattr(self, 'name'):
            return
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 显示判断_instance是否为None更安全，不建议使用 if not cls._instance 判断方式。
        # 因为如果实现了__bool__方法，则有可能实例存在也返回false
        if cls._instance is None:
            # 锁的开销非常大，建议仅在必要时候使用锁
            with cls._lock:
                # Another thread could have created the instance
                # before we acquired the lock. So check that the
                # instance is still nonexistent.
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return A._instance

    def __bool__(self):
        return False


def create_a(name: str):
    a = A(name)
    print(f"a的地址是{id(a)}, a.name是{a.name}")


if __name__ == '__main__':
    for t in [threading.Thread(create_a("lzy13")), threading.Thread(create_a("lzy6")),
              threading.Thread(create_a("lzy22")),
              threading.Thread(create_a("lzy2")), threading.Thread(create_a("lzy7")),
              threading.Thread(create_a("lzy221")),
              threading.Thread(create_a("lzy3")), threading.Thread(create_a("lzy8")),
              threading.Thread(create_a("lzy23")),
              threading.Thread(create_a("lzy4")), threading.Thread(create_a("lzy9")),
              threading.Thread(create_a("lzy321")),
              threading.Thread(create_a("lzy5")), threading.Thread(create_a("lzy0")),
              threading.Thread(create_a("lzy3"))]:
        t.start()
