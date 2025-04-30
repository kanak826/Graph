import heapq



class Node:
    def __init__(self):
        self.values=[]
        self.neighbours=[]

class weighted_graph:
    def __init__(self):
        self.nodes={}

    def add_node(self,value):
      all_keys = self.nodes.keys()
      if value in all_keys:
        
        self.nodes[value] = new_node
        print("node all ready created")
      else: 
          new_node = Node(value)
          self.nodes[value] = new_node
         
          print("node created")

    def connected_nodes(self,v1,v2,distance):
       if v1 in self.nodes and v2 in self.nodes:
          node1=self.nodes[v1]
          node2=self.nodes[v2]
          node1.neighbour.append((node2,distance))
          node2.neighbour.append((node1,distance))
          print("connected")
       else:
          print("node in graph")  

    def print_graph(self):
       for key in self.nodes:
          node=self.nodes[key]
          print(node.value,end="->")
          for n_node,dis in node.neighbours:
             #n_node=nb[0]
             #dis=nb[1]
              
            print(f"({n_node.value},dis:{dis})",ends=",") 
       print()  
   
    def dijkstras(nodes,start_point):
      distances={}
      visited={}
      for node in nodes:
       distances[node]=float("inf")
       distances=[start_point]
       queue=[]
       queue.append((0,start_point))

       while queue:
         node_tuple=heapq.heappop(queue)
         current_distance=node_tuple[0]
         current_node_val=node_tuple[1]
         current_node=nodes[current_node_val]
         if current_node not in visited:
            for nb,dis in current_node.neighbours:
               new_dis=current_distance+dis
               if new_dis<distances[nb.value]:
                    


    
                
        


# ok=weighted_graph()
# ok.add_node(23) 
# ok.add_node(34)
# ok.add_node(3)
# ok.add_node(5)
# ok.add_node(6)
# ok.add_node(7)
# ok.add_node(9)
# ok.add_node(8)


# ok.connected_nodes(v1=1,v2=2,distance=34)
# ok.print_graph(23)           
