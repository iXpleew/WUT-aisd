from destination import Destination
import numpy as np 
import heapq
import random


def create_destiantion(path: dict, source: str, dest: str, distance: float, morning: int, noon: int, evening:int):
    new_destination = Destination(dest, distance, morning, noon, evening)
    if source in path:
        path[source].append(new_destination)
    else:
        new_paths_list = [new_destination]
        path[source] = new_paths_list


#tutaj bedzie sparsowana kategoria
def define_dijkstra_type(category: int, city: Destination) -> float:
    if category < 0:
        return city.length
    elif 7 <= category < 10:
        return city.morning_time
    elif 10 <= category < 16:
        return city.noon_time
    elif 16 <= category <= 20:
        return city.evening_time
    else:
        return city.night_time()

# make this method calculate time 
def calculate_proper_time(current_time: str, add_time: float):
    hour_time = int(current_time[:2])
    minutes_time = int(current_time[3:])
    while add_time > 0:
        minutes_to_full_hour = 60 - minutes_time
        if add_time > minutes_to_full_hour:
            if hour_time == 23:
                hour_time = 0
            else:
                hour_time += 1
            add_time -= minutes_to_full_hour
            minutes_time = 0
        else:
            minutes_time += add_time
    return f"{hour_time:02d}:{minutes_time:02d}"


def return_int_hour_value(time: str) -> int:
    hour = int(time[:2])
    minutes = int(time[3:])
    hour *= 1000
    return hour+minutes
    

def calculate_dijkstra_distance(map: dict, start_location: str, final_location: str):
    distances_from_start = {}
    for key in map:
        if key == start_location:
            distances_from_start[key] = 0.0
        else:
            distances_from_start[key] = float('inf')

    queue = [(0.0, start_location)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances_from_start[current_node]:
            continue
        
        for neighbour in map[current_node]:
            distance = current_distance + neighbour.lenght
            if distance < distances_from_start[neighbour.destination]:
                distances_from_start[neighbour.destination] = distance
                heapq.heappush(queue, (distance, neighbour.destination))
    
    return distances_from_start[final_location]


def calculate_dijkstra_time(map:dict, start: str, final: str, current_time: str):
    hours_from_start = {}
    for key in map:
        if key == start:
            hours_from_start[key] = 0.0
        else:
            hours_from_start[key] = float("inf")
    
    queue = [(current_time, start)]
    while queue:
        current_time, current_node = heapq.heappop(queue)

        if return_int_hour_value(current_time) > hours_from_start[current_node]:
            pass
    pass


def get_dijsktra_info_distance(city_number: int, map: dict, curr_time: int) -> list[tuple]:
    list_of_info = []
    for i in range(10):
        start_city = str(random.randint(0, city_number))
        end_city = str(random.randint(0, city_number))
        distance = calculate_dijkstra_distance(map, start_city, end_city)
        list_of_info.append((start_city, end_city, distance))
    return list_of_info


def get_dijsktra_info_time(start_city: int, end_city: int, map: dict, curr_time: str) -> str:
    return ""


def print_dijkstra_info(cities_info: list[tuple]):
    for start_city, end_city, distance in cities_info:
        print(f"Distance from {start_city} to {end_city} is {distance:.2f}")
        

