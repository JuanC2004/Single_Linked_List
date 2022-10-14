'''
Authiors: Juan Camilo Quintero and Juan Felipe Lopez Sanabria
Date: 11/10/22
Language: Python 3.0
'''

from Single_Linked_List import SingleLinkedList
inst_sll = SingleLinkedList()
inst_sll.prepend_node('B')
inst_sll.prepend_node('A')
inst_sll.append_node('C')
inst_sll.append_node('D')
inst_sll.append_node('E')
inst_sll.show_nodes_list()
inst_sll.insert('a')
inst_sll.insert(7)
inst_sll.insert(2)
inst_sll.show_nodes_list()
inst_sll.remove(2)
''' ['Head', 'A', 'B', 'C', 'D', 'E', 'Tail'] '''
inst_sll.remove(1)
''' ['A', 'B', 'C', 'D', 'E', 'Tail'] '''
inst_sll.remove(6)
''' ['A', 'B', 'C', 'D', 'E'] '''
inst_sll.show_nodes_list()
inst_sll.reverse()
inst_sll.show_nodes_list()