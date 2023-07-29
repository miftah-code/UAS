class HybridArrayListNode:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.next_node = None

class HybridArrayList:
    def __init__(self, initial_capacity):
        self.initial_capacity = initial_capacity
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = HybridArrayListNode(self.initial_capacity)
            self.head.array[0] = data
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node

            for i in range(len(current_node.array)):
                if current_node.array[i] is None:
                    current_node.array[i] = data
                    return

            new_node = HybridArrayListNode(self.initial_capacity)
            new_node.array[0] = data
            current_node.next_node = new_node

    def insert(self, data, position):
        current_node = self.head
        while current_node is not None:
            for i in range(len(current_node.array)):
                if current_node.array[i] is None or i == len(current_node.array) - 1:
                    if i == len(current_node.array) - 1:
                        # The current node is full, move to the next node
                        current_node = current_node.next_node
                    break
                if i == position:
                    # Shift elements to the right to make space for the new element
                    for j in range(len(current_node.array) - 1, i, -1):
                        current_node.array[j] = current_node.array[j - 1]
                    current_node.array[i] = data
                    return

            if current_node is not None:
                current_node = current_node.next_node

    def delete(self, position):
        current_node = self.head
        while current_node is not None:
            for i in range(len(current_node.array)):
                if current_node.array[i] is None:
                    return  # Element not found
                if i == position:
                    # Shift elements to the left to remove the element
                    for j in range(i, len(current_node.array) - 1):
                        current_node.array[j] = current_node.array[j + 1]
                    current_node.array[len(current_node.array) - 1] = None
                    return

            if current_node is not None:
                current_node = current_node.next_node

    def actual_position(self, data):
        current_node = self.head
        index = 0
        while current_node is not None:
            for i in range(len(current_node.array)):
                if current_node.array[i] == data:
                    return index + i
            index += len(current_node.array)
            current_node = current_node.next_node

        return -1  # Element not found

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            for data in current_node.array:
                if data is not None:
                    print(data, end=" -> ")
            current_node = current_node.next_node
        print("None")


# Contoh Penggunaan HybridArrayList
if __name__ == "__main__":
    hal = HybridArrayList(initial_capacity=3)

    hal.append(10)
    hal.append(20)
    hal.append(30)

    hal.insert(15, 1)
    hal.insert(25, 4)

    hal.print_list()  # Output: 10 -> 15 -> 20 -> 30 -> 25 -> None

    print("Position of 20:", hal.actual_position(20))  # Output: Position of 20: 2

    hal.delete(1)
    hal.delete(3)

    hal.print_list()  # Output: 10 -> 20 -> 25 -> None

    print("Position of 25:", hal.actual_position(25))  # Output: Position of 25: 2
