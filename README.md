# Max Flow

This is a implementation of maximum flow algorithm.

### in terminal
First load a json file typing open {path}. Then type start {initial_vertex finish_vertex} execute the algorithm. Type help for more instructions.

the structure of the node must be:

{
    "node1":{"next_node1":flow,"next_node2:flow"},
    "node2":{"next_node1":flow,"next_node2:flow"}
}

example

{
    "1":{"2":8,"3":14,"5":4},
    "2":{"1":0,"3":5,"4":7,"5":6},
    "3":{"1":0,"2":10,"4":9,"5":10},
    "4":{"2":6,"3":7,"5":5},
    "5":{"1":0,"2":0,"3":0,"4":0}
}