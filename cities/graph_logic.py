from destination import Destination
import numpy as np 
import heapq


def create_destiantion(path: dict, source: str, dest: str, distance: float, morning: int, noon: int, evening:int):
    new_destination = Destination(dest, distance, morning, noon, evening)
    if source in path:
        path[source].append(new_destination)
    else:
        new_paths_list = [new_destination]
        path[source] = new_paths_list


def calculate_dijkstra_distance(map:dict, start_location: str, final_location: str):
    distances_from_start = {}
    for key in map:
        if key == start_location:
            distances_from_start[key] = 0
        else:
            distances_from_start[key] = np.inf

    queue = [(0, start_location)]
    while queue:
      current_distance, current_node = heapq.heappop(queue)
      if current_distance > distances_from_start[current_node]:
          continue
      
      for neighbour in map[current_node]:
        distance = current_distance + neighbour.length
        if distance < distances_from_start[neighbour.destination]:
            distances_from_start[neighbour.destination] = distance
            heapq.heappush(queue, (distance, neighbour.destination))
    
    return distances_from_start[final_location]
