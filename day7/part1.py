class Node:
    def __init__(self, name, parent, is_dir=False, size=0):
        self.is_dir = is_dir
        self.children = list()
        self.size = size
        self.name = name
        self.parent = parent

    def __str__(self) -> str:
        if self.is_dir:
            return f"{self.name} has {len(self.children)} elements ({self.size})"
        else:
            return f"{self.name} ({self.size})"

    def check_exists(self, name):
        for item in self.children:
            if item.name == name:
                return True
        return False

    def add_child(self, new_node):
        if not self.check_exists(new_node.name):
            self.children.append(new_node)
        else:
            pass
            # print(f"{new_node.name} already exists")

    def print_children(self):
        if len(self.children) > 0:
            for item in self.children:
                print(item)
        else:
            print("No children")

    def print_tree(self, indent=0):
        print(" " * indent + str(self))
        for item in self.children:
            if item.is_dir:
                item.print_tree(indent=indent + 4)
            else:
                print(" " * (indent + 4) + str(item))

    def go_to(self, name):
        for item in self.children:
            if item.name == name:
                return item

        print(f"Error, couldn't find {name}")


root = Node("/", is_dir=True, parent=None)

# testfile = Node("b.txt", size=1000)
# root.add_child(testfile)

# testfolder = Node("nested", is_dir=True)
# root.add_child(testfolder)

# print(root)
# root.print_children()


with open("input.txt") as f:
    lines = f.readlines()

in_ls_output = False
current_node = root
# Build the tree
for line in lines[1:]:
    # print(f"{line=}")

    if line.startswith("$ "):
        in_ls_output = False
        command = line[2:4]
        if command == "cd":
            directory = line.split()[2]
            if current_node is not None:
                if directory == "..":
                    if current_node.parent is not None:
                        current_node = current_node.parent
                    else:
                        print("Error, we want to go up from root")
                else:
                    new_directory = Node(directory, is_dir=True, parent=current_node)
                    current_node.add_child(new_directory)
                    current_node = current_node.go_to(directory)

            # print(f"root: {root}")
            # print("Children: ")
            # root.print_children()

            # print("Current node: ", current_node)
            # print()
        elif command == "ls":
            in_ls_output = True
            continue

    if in_ls_output:
        size_is_dir, name = line.split()
        if size_is_dir == "dir":
            new_node = Node(name, is_dir=True, parent=current_node)
        else:
            new_node = Node(name, size=int(size_is_dir), parent=current_node)

        current_node.add_child(new_node)


solution = 0


def calculate_folder_size(node):
    global solution
    for item in node.children:
        if not item.is_dir:
            node.size += item.size
        else:
            node.size += calculate_folder_size(item)

    if node.size <= 100000:
        solution += node.size

    return node.size


calculate_folder_size(root)
root.print_tree()

print(f"{solution=}")
print("=" * 50)

disk_space = 70000000
needed = 30000000
free_now = disk_space - root.size
to_free = needed - free_now

possible = list()


def check_if_large_enough(node, to_free):
    global possible
    for item in node.children:
        if item.is_dir:
            if item.size >= to_free:
                possible.append(item)
            check_if_large_enough(item, to_free)


check_if_large_enough(root, to_free)
print(sorted(possible, key=lambda x: x.size)[0])
