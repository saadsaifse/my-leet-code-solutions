class Test:
    field = "blabla"
    def __init__(self, f):
        self.field = f

if __name__ == "__main__":
    i = Test()
    print(i.field)