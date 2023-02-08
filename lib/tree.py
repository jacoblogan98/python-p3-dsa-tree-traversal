class Tree:
  def __init__(self, root = None):
    self.root = root

  def breadth_first_traversal(self):
    tree_list = []
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      curr_node = nodes_to_visit.pop(0)
      tree_list.append(curr_node['value'])
      nodes_to_visit.extend(curr_node['children'])
    
    return tree_list

  def depth_first_traversal(self):
    tree_list = []
    tree_q = [self.root]

    while tree_q:
      curr_node = tree_q.pop(0)

      tree_list.append(curr_node['value'])
      tree_q = curr_node['children'] + tree_q
  
    return tree_list

  def get_element_by_id(self, id):
    nodes_to_search = [self.root]

    while nodes_to_search:
      curr_node = nodes_to_search.pop(0)

      if curr_node['id'] == id: return curr_node

      nodes_to_search = curr_node['children'] + nodes_to_search
    
    return None



# child_1 = {
#   'value': 2,
#   'children': []
# }

# child_2 = {
#   'value': 3,
#   'children': []
# }

# child_3 = {
#   'value': 4,
#   'children': []
# }

# root = {
#   'value': 1,
#   'children': [child_1, child_2, child_3]
# }

# def breadth_first_traversal(node):
#     tree_list = []
#     nodes_to_visit = [node]

#     while nodes_to_visit:
#       curr_node = nodes_to_visit.pop(0)

#       tree_list.append(curr_node['value'])
#       nodes_to_visit.extend(curr_node['children'])
    
#     return tree_list
  
# print(breadth_first_traversal(root))

# def depth_first_traversal(node):
#   tree_list = []
#   tree_q = [node]

#   while tree_q:
#     curr_node = tree_q.pop(0)

#     tree_list.append(curr_node['value'])
#     tree_q = curr_node['children'] + tree_q
  
#   return tree_list

# print(breadth_first_traversal(root))


