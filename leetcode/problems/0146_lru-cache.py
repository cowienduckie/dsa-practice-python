class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.front = None
        self.rear = None

    def append(self, node: Node) -> None:
        # New node is a normal node
        if self.front and self.rear:
            self.rear.next, node.prev = node, self.rear
            self.rear = node
        # New node is the first node
        else:
            self.front = node
            self.rear = node

    def remove(self, node: Node) -> Node:
        # Remove node is a normal node
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        # Remove node is the front node (no prev)
        elif node.next:
            self.front = node.next
            self.front.prev = None
        # Remove node is the rear node (no next)
        elif node.prev:
            self.rear = node.prev
            self.rear.next = None
        node.prev, node.next = None, None
        return node

    def pop_front(self) -> Node:
        return self.remove(self.front)

    def move_to_back(self, node: Node) -> None:
        self.append(self.remove(node))


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.used_list = LinkedList()

    def get(self, key: int) -> int:
        node = self.cache_dict.get(key)
        if node:
            self.used_list.move_to_back(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Update cache node if key exists and mark it as most recently used
        node = self.cache_dict.get(key)
        if node:
            node.value = value
            self.used_list.move_to_back(node)
        else:
            # Otherwise, add new node
            node = Node(key, value)
            self.cache_dict[key] = node
            self.used_list.append(node)

            # If number of nodes is reach capacity, remove the front node of used list as LRU item
            if len(self.cache_dict) > self.capacity:
                removed_node = self.used_list.pop_front()
                del self.cache_dict[removed_node.key]
