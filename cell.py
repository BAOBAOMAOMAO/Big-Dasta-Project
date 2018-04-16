class Cell():
    # list may change to hashmap
    def __init__(self, val, count = 0, is_leaf_cell = False, children_cell_list = list()):
        self.count = count   
        self.val = val
        self.is_leaf_cell = is_leaf_cell
        self.children_cell_list = children_cell_list

    def add_children_cell(c):
        # check if cell already in the list
        # if in the list, its sum + 1
        # else add cell into the list
        for i in children_cell_list:
            if(i.val == c.val):
                i.count += 1 
                return "dup"
        self.children_cell_list.append(c)
        return "done"

    def get_child_cell(val):
        for i in children_cell_list:
            if(i.val == val):
                return i
        