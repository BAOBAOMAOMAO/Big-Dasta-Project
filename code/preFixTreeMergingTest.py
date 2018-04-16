import pandas as pd
from utility import *
from cell import *
from preFixTreeMerging import *
import sys

lll1 = Cell(3,1,True)
lll2 = Cell(4,1,True)
lll5 = Cell(5,1,True)
lll6 = Cell(6,1,True)
lll7 = Cell(7,1,True)
lll8 = Cell(8,1,True)


lll9 = Cell("apple",1,True)
lll10 = Cell("beer",1,True)
lll11 = Cell("cache",1,True)
lll12 = Cell("dad",1,True)


ll1 = Cell(1,children_cell_list=[lll1,lll2])
ll2 = Cell(2,children_cell_list=[lll5,lll6])
ll3 = Cell(2,children_cell_list=[lll7,lll8])
ll4 = Cell(4,children_cell_list=[lll1,lll2])

ll5 = Cell("ear",children_cell_list=[lll1,lll11])
ll6 = Cell("fear",children_cell_list=[lll6,lll12])


l1 = Cell(10, children_cell_list=[ll1, ll2])
l2 = Cell(9, children_cell_list=[ll2, ll3])

mg = prefix_tree_mergeing([ll1,ll2])
mg = prefix_tree_mergeing([ll3,ll4])
mg = prefix_tree_mergeing([ll1,ll4])
mg = prefix_tree_mergeing([ll5,ll6])
print(mg)
for i in mg:
    print("cell val " + str(i.val) +  ", cell count " + str(i.count) + ", cell children list" + str(i.children_cell_list))
    for j in i.children_cell_list:
        print("children name:" + str(j.val))