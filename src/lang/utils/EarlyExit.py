from typing import Literal
from src.lang.generated.ignoreParser import ignoreParser

EarlyExitTag = Literal["Return"] | Literal["Break"]
class EarlyExit[T](Exception):
    # This is a hack to traverse whole stack and wrap return value of a function.
    # This is similar to how python handles iterators internally tho.
    def __init__(self, value: T, tag: EarlyExitTag = "Return"):
        super().__init__()
        self.value = value
        self.tag = tag

    def __str__(self):
        return f"Early Exit signalizer with {self.value=}"

    @staticmethod
    def return_with(value: T) -> None:
        raise EarlyExit(value)

    @staticmethod
    def break_from_loop() -> None:
        raise EarlyExit(None, "Break")