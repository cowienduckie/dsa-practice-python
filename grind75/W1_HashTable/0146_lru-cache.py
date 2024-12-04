from typing import Tuple


class Node:
    def __init__(self, data: Tuple[int, int], prev_node=None, next_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def append(self, node: Node) -> Node:
        """
        Append a node to the linked list
        """
        if not self.head:
            self.head = node
            self.rear = node
            node.prev = None
            node.next = None
        else:
            node.prev = self.rear
            node.next = None
            self.rear.next = node
            self.rear = node

        return node

    def remove(self, node: Node) -> None:
        """
        Remove a node from the linked list
        """
        prev_node = node.prev
        next_node = node.next

        if prev_node and next_node:
            # Update the pointers of the previous and next nodes
            prev_node.next = node.next
            next_node.prev = node.prev
        elif prev_node:
            # If the node is the rear node, update the rear node
            self.rear = prev_node
            self.rear.next = None
        elif next_node:
            # If the node is the head node, update the head node
            self.head = next_node
            self.head.prev = None
        else:
            # If the node is the only node in the linked list
            self.head = None
            self.rear = None

        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_dict = dict()
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if not key in self.num_dict:
            return -1

        # Move the node to the rear of the linked list
        self.linked_list.remove(self.num_dict[key])
        self.linked_list.append(self.num_dict[key])

        return self.num_dict[key].data[1]

    def put(self, key: int, value: int) -> None:
        if key in self.num_dict:
            # If the key is in the dictionary, update the value
            self.linked_list.remove(self.num_dict[key])
            self.linked_list.append(self.num_dict[key])

            self.num_dict[key].data = (key, value)
        else:
            # If the key is not in the dictionary but the capacity is full, remove the head node
            if self.capacity == 0:
                removed_key = self.linked_list.remove(self.linked_list.head).data[0]
                del self.num_dict[removed_key]
            else:
                self.capacity -= 1

            self.num_dict[key] = self.linked_list.append(Node((key, value)))


# Test cases
commands = [
    "LRUCache",
    "put",
    "put",
    "put",
    "put",
    "get",
    "get",
    "get",
    "get",
    "put",
    "get",
    "get",
    "get",
    "get",
    "get",
]
values = [
    [3],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [4],
    [3],
    [2],
    [1],
    [5, 5],
    [1],
    [2],
    [3],
    [4],
    [5],
]
lru_cache = None
for i, command in enumerate(commands):
    if command == "LRUCache":
        lru_cache = LRUCache(values[i][0])
        print(None)
    elif command == "put":
        lru_cache.put(values[i][0], values[i][1])
        print(None)
    elif command == "get":
        print(lru_cache.get(values[i][0]))
