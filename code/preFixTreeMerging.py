import pandas as pd
from utility import *
from cell import *
import sys

def prefix_tree_mergeing(toMerge):
    '''
    Input: Merge    list of Node(val + list(Cell))
    Output: MergedNode  list of Node(val + list(Cell))
    '''
    mergedNode = list()
    if len(toMerge) == 1:
        mergedNode.append(toMerge[0])
        return mergedNode
    else:
        node_val_set = set()
        val_cell_dict = dict()

        for cell in toMerge:
            if cell.val not in val_cell_dict.keys():
                tmp = list()
                tmp.append(cell)
                val_cell_dict[cell.val] = tmp
            else:
                val_cell_dict[cell.val].append(cell)

        for val in val_cell_dict.keys():
            new_cell = Cell(val)
            cell_list = val_cell_dict.get(val)
            for cell in cell_list:
                new_cell = Cell(val)
                # if cells are leaves
                if cell.is_leaf_cell:
                    new_cell.count = len(cell_list)
                # not leaves, do recursion on children
                else:
                    particalSet = list()
                    for sub_cell in cell_list:
                        particalSet += sub_cell.children_cell_list
                    new_cell.children_cell_list = prefix_tree_mergeing(particalSet)
            mergedNode.append(new_cell)
        return mergedNode   