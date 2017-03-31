class Project:
    def __init__(self, name):
        self.name = name
        self.incomings = set()
        self.outgoings = set()

    def add_incoming(self, incoming):
        self.incomings.add(incoming)

    def add_outgoing(self, outgoing):
        self.outgoings.add(outgoing)

def initialize_node(projects):
    result = {}
    for p in projects:
        result[p] = Project(p)

    return result

def build_dependencies(projects_map, dependencies):
    for dep in dependencies:
        from_project = dep[0]
        to_project = dep[1]
        projects_map[from_project].add_outgoing(to_project)
        projects_map[to_project].add_incoming(from_project)

def build_order(projects, dependencies):
    projects_map = initialize_node(projects)
    build_dependencies(projects_map, dependencies)

    result = []
    changed = True
    while len(result) != len(projects):
        if not changed:
            return None
        changed = False
        for [name, project] in projects_map.iteritems():
            try:
                result.index(name)
            except ValueError:
                if not project.incomings:
                    changed = True
                    result.append(name)
                    for outgoing in project.outgoings:
                        projects_map[outgoing].incomings.remove(project.name)

    return result

print build_order(
    ['a', 'b'],
    []
)

print build_order(
    ['a', 'b', 'c', 'd', 'e', 'f'],
    [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]
)
