class Project:
    def __init__(self):
        _children: List[Project] = []
        _map: dict[str, Project] = {}
        _name: str = None
        _dependencies: int = 0

    def add_neighbor(node: Project) -> None:
        if not node.get_name() in map:
            self._children.append(node)
            self._map[node.get_name()] = node
            node.increase_dependencies()

    def increase_dependencies(self) -> None:
        self._dependencies += 1
    
    def decrease_dependencies(self) -> None:
        self._dependencies -= 1

    def get_name(self) -> str:
        return self._name

    def get_children(self) -> List[Project]:
        return self._children

    def get_number_of_dependencies(self) -> int:
        return self._dependencies