from destination import Destination


def create_destiantion(path: dict, source: str, dest: str, distance: float, morning: int, noon: int, evening:int):
    new_destination = Destination(dest, distance, morning, noon, evening)
    if source in path:
        path[source].append(new_destination)
    else:
        new_paths_list = [new_destination]
        path[source] = new_paths_list


def calculate_dijkstra_distance(map:dict, start_location: str, final_location: str):
    pass