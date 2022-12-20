import copy


class Node:
    def __init__(self, name, rate, leads_to):
        self.name = name
        self.rate = rate
        self.leads_to = leads_to
        self.open = False
        self.connections = []
        self.visited = False

    def open_valve(self):
        if self.open:
            return False
        else:
            self.open = True
            return True

    def __repr__(self) -> str:
        return f"Valve {self.name} has flow rate={self.rate}; tunnels lead to valves {[a.name for a in self.connections]}"


class Path:
    def __init__(self, nodes):
        self.nodes = nodes
        self.active = True
        self.remaining_time = 30
        self.current_release = 0
        self.total_release = 0
        self.current_node = self.nodes[0]

    def get_options(self):
        return sorted(self.current_node.connections, key=lambda o: o.rate)

    def visit_node(self, node):
        self.propagate_time()
        self.current_node = node
        # print(f"Moved to {self.current_node.name}")

    def propagate_time(self):
        self.remaining_time -= 1
        self.total_release += self.current_release

    def open_valve(self):
        self.propagate_time()
        self.current_node.open_valve()


with open("test.txt") as f:
    lines = [line.strip() for line in f.readlines()]

nodes = []
for line in lines:
    a, b = line.split(";")
    _, name, _, _, r = a.split()
    rate = int(r.split("=")[1])

    _, v = b.split("to")
    valves = v.split()[1:]

    new_node = Node(name, rate, leads_to=[v.replace(",", "") for v in valves])
    nodes.append(new_node)

# Put the actual nodes into self.connections
for node in nodes:
    for lt in node.leads_to:
        for connection in nodes:
            if connection.name == lt:
                node.connections.append(connection)
                break

# Second try: Find all paths
active_paths = True
paths = [
    Path(copy.copy(nodes)),
]

i_iter = 0
while active_paths and i_iter < 100:
    all_stoped = True
    for path in paths:
        all_stoped = all_stoped and (path.remaining_time == 0)

    if all_stoped:
        active_paths = False
        break

    paths_to_add = list()
    for i_path, path in enumerate(paths):
        print(f"Path {i_path+1}/{len(paths)}")
        if path.remaining_time == 0:
            print("On this path, time is up with {path.total_release=}.")
            continue

        options = path.get_options()

        # Check if it even makes sense to move somewhere and then move
        found_one = False
        for n in reversed(options):
            if not n.open:
                found_one = True
                break

        # If we can't find an open valve, we just decrease the time
        if not found_one:
            path.remaining_time -= 1
            continue
        # Otherwise we go further
        else:
            path_template = copy.deepcopy(path)
            path.visit_node(options[0])
            for option in options[1:]:
                new_path = copy.deepcopy(path_template)
                new_path.visit_node(option)
                paths_to_add.append(new_path)

        if path.current_node.open:
            # If the valve is open, we do nothing and wait for the next move
            pass
        else:
            # If the valve is closed, we can either open it or move on
            new_path = copy.deepcopy(path)
            # Do nothing
            # Open it
            new_path.open_valve()
            paths_to_add.append(new_path)

    for new_path in paths_to_add:
        paths.append(new_path)
    i_iter += 1

print("=" * 100)

for i_path, path in enumerate(paths):
    print(i_path, path.total_release)
