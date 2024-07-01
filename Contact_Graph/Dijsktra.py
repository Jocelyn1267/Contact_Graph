import numpy as np
from CRP import crp
from CSP import csp

class Contact:
    def __init__(self, id, start, end, sender, receiver, owlt):
        """
        Initializes the Contact class

        Args:
            id -- i (the id for a specific contact)
            start -- ci.start (a float representing the start time)
            end -- ci.end (a float representing the end time)
            sender -- ci.sender (the sending vertex)
            receiver -- ci.receiver (the receiving vertex).
            owlt -- ci.owlt.
        """
        self.id = id
        self.start = start
        self.end = end
        self.sender = sender
        self.receiver = receiver
        self.owlt = owlt
        self.visited = False  # Flag to indicate if the contact has been visited
        self.visited_n = set()  # Set of visited nodes
        self.pred = None  # Predecessor contact in the shortest path
        self.arr_time = np.inf  # Arrival time at the contact(cost)

    def __lt__(self, other):
        return self.arr_time < other.arr_time

def dijkstra_contact_search(G, Croot, Cdest):
    # Initializations
    path = []               # Initialize the path to be returned
    Cfin = None            # Initialize the earliest contact found so far
    BDT = np.inf            # Initialize the earliest arrival time found so far
    Croot.arr_time = 0     # Set the arrival time of the source contact to 0

    Ccurr = Croot         # Set the current contact to the source contact

    while True:
        Cfin, BDT = crp(G, Ccurr, Cfin, BDT, Cdest)
        Cnext = csp(G, BDT)

        if Cnext == None:
            break
        else:
            Ccurr = Cnext

    # Construct the path from back to front
    if Cfin != None:
        C = Cfin
        while C != Croot:
            path.append(C)
            C = C.pred
        path.reverse()
    return path, BDT


if __name__ == '__main__':
    contact_graph = []

    # Read the contact graph from the file
    with open('ContactList.txt', 'r') as f:
        for line in f:
            id, start, end, sender, receiver, owlt = map(float, line.split())
            contact = Contact(id, start, end, sender, receiver, owlt)
            contact_graph.append(contact)

    # Run the search algorithm to find an optimal path from node 8 to node 5
    candidate_source = []
    candidate_destination = []
    for contact in contact_graph:
        if contact.sender == 8:
            candidate_source.append(contact)
        if contact.receiver == 5:
            candidate_destination.append(contact)

    # candidate_source_ids = [contact.id for contact in candidate_source]
    # candidate_destination_ids = [contact.id for contact in candidate_destination]
    #
    # print("The ids of the possible source node:", candidate_source_ids)
    # print("The ids of the possible destination node candidate:", candidate_destination_ids)

    min_cost = np.inf
    fin_path = []
    for s in candidate_source:
        for d in candidate_destination:
            path, cost = dijkstra_contact_search(contact_graph, contact_graph[int(s.id)], contact_graph[int(d.id)])
            if cost < min_cost:
                min_cost = cost
                fin_path = path

    # path, cost = dijkstra_contact_search(contact_graph, contact_graph[7], contact_graph[4])

    print("\nOutput:\n")
    if not fin_path:
        print("No path found")
    else:
        print("Optimal path:")
        for i, C in enumerate(fin_path):
            if i == 0:
                print(f"  {C.sender} => {C.receiver}  Contact {C.id}")
            else:
                print(f"  {fin_path[i - 1].receiver} => {C.receiver}  Contact {C.id}")

        print("\nNodes visited :", [C.sender for C in fin_path] + [fin_path[-1].receiver])
        print("Optimal path is", [C.id for C in fin_path])
        print("Best arrival time = ", format(min_cost, ".2f"))

