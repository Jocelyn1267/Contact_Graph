import heapq

def crp(G, Ccurr, Cfin, BDT, D):

    for C in G:

        # Skip C condition:
        # Matching source
        if C.sender != Ccurr.receiver:
            continue
        # Not ending before current's arrival time
        if C.end <= Ccurr.arr_time:
            continue
            # With a destination not visited in current's path
        if C.visited:
            continue
        if C.receiver in Ccurr.visited_n:
            continue

        # Calculate the arrival time in C via Ccurr
        if C.start < Ccurr.arr_time:
            arr_time = Ccurr.arr_time + C.owlt
        else:
            arr_time = C.start + C.owlt

        if arr_time < C.arr_time:
            C.arr_time = arr_time
            C.pred = Ccurr
            C.visited_n = Ccurr.visited_n.union({C.receiver})

            if C.receiver == D.sender and C.arr_time < BDT:
                BDT = C.arr_time
                Cfin = C



    Ccurr.visited = True

    return Cfin, BDT
