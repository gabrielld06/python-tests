class SimpleTests:
    def __init__(self, string: str) -> None:
        self.string = string

    def hello(self) -> str:
        return "Hello World!"

    def setString(self, string: str) -> None:
        self.string = string

    def getString(self) -> str:
        return self.string
