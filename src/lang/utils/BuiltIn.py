from dataclasses import dataclass
from typing import Any


@dataclass
class BuiltIn:
    # wrapper around built ins. No type safety included.
    value: Any

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.value(*args, **kwargs)
