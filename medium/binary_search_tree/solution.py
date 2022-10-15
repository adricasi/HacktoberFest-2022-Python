class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert_list(self, list_of_values):
        for value in list_of_values:
            self.insert(value)

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value,self.root)

    def _insert(self, value, current_node):
        # Left child
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = node(value)
            else:
                self._insert(value,current_node.left_child)
        # Right child
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = node(value)
            else:
                self._insert(value,current_node.right_child)
        else:
            print("Value already in tree.")

    def search(self, value=None):
        # Check valid inputs
        if not isinstance(value, int):
            return -1

        if self.root != None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        return False