class Node:
    def __init__(self, name, rate, leads_to):
        self.name = name
        self.rate = rate
        self.leads_to = leads_to
        self.open = False
        self.total_release = 0
        self.connections = []
        self.visited = False

    def potential(self, remaining_time, depth):
        # Get also the connections
        total = 0
        if depth > 0 and remaining_time > 0:
            for node in self.connections:
                total += node.potential(remaining_time - 2, depth - 1)

        if self.open:
            return total
        else:
            return remaining_time * self.rate + total

    def open_valve(self, remaining_time):
        if self.open:
            return False
        else:
            self.open = True
            self.total_release = remaining_time * self.rate
            return True

    def __repr__(self) -> str:
        return f"Valve {self.name} has flow rate={self.rate}; tunnels lead to valves {[a.name for a in self.connections]}"


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

released_pressure = 0.0
remaining_time = 30
current_node = nodes[0]
depth = 3

# First try: Always greedily find the immediate best step
while remaining_time > 0:
    current_node.visited = True
    options = sorted(
        current_node.connections, key=lambda o: o.potential(remaining_time, depth)
    )

    found_one = False
    for n in reversed(options):
        if not n.visited:
            current_node = options[-1]
            remaining_time -= 1
            found_one = True
            break

    if not found_one:
        print("All nodes were already visisted")
        remaining_time -= 1
    print()
    print(f"Minute {30-remaining_time}")
    print(f"Options: {[(o.name, o.potential(remaining_time, depth)) for o in options]}")
    print(f"Moved to {current_node.name}")

    if current_node.open_valve(remaining_time):
        remaining_time -= 1
        print()
        print(f"Minute {30-remaining_time}")
        print(
            f"Opened valve {current_node.name} releasing {current_node.total_release}"
        )
    else:
        print(f"Valve was already open")

    total = 0
    for node in nodes:
        total += node.total_release

    print(f"{total=}")
