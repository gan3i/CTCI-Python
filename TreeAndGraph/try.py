from __future__ import annotations
from typing import List

class foo:
    def __init__(self):
        self._children: List[foo] = []

    def get_children(self) -> List[foo]:
        return self._children

t = foo()




