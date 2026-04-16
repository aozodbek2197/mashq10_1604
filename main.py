# 1-mashq
class Old:
    def old_method(self):
        return "old"

class Adapter:
    def __init__(self, obj):
        self.obj = obj

    def new_method(self):
        return self.obj.old_method()
# 2-mashq
class CPU:
    def start(self): print("CPU start")

class RAM:
    def load(self): print("RAM load")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()

    def start(self):
        self.cpu.start()
        self.ram.load()
# 3-mashq
class Real:
    def request(self):
        print("Real request")

class Proxy:
    def __init__(self):
        self.real = Real()

    def request(self):
        print("Checking access...")
        self.real.request()
# 4-mashq
class StateA:
    def handle(self):
        print("State A")

class StateB:
    def handle(self):
        print("State B")

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle()
# 5-mashq
class Base:
    def process(self):
        self.step1()
        self.step2()

    def step1(self): pass
    def step2(self): pass
