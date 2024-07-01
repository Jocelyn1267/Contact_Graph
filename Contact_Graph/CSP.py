import heapq


def csp(G, BDT):
    queue = []
    for C in G:
        # Skip C condition
        # The unvisited contacta with arrival time less than BDT
        if C.arr_time > BDT or C.visited:
            continue

        # Use Priority Queue instead
        heapq.heappush(queue, (C.arr_time, C))
    if queue:
        # Pop the contact with the shortest arrival time in the heap
        return heapq.heappop(queue)[1]
    else:
        # if heap is empty, return None
        return None

