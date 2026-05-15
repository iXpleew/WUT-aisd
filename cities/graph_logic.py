import heapq
import random
from destination import Destination


def create_destination(path: dict, source: str, dest: str, distance: float, morning: int, noon: int, evening: int):
    new_destination = Destination(dest, distance, morning, noon, evening)
    if source in path:
        path[source].append(new_destination)
    else:
        path[source] = [new_destination]


def define_dijkstra_type(current_minute_of_day: float, city: Destination) -> float:
    if current_minute_of_day < 0:
        return city.length
    elif 420 <= current_minute_of_day < 600:
        return city.morning_time
    elif 600 <= current_minute_of_day < 960:
        return city.noon_time
    elif 960 <= current_minute_of_day < 1200:
        return city.evening_time
    else:
        return city.night_time()


def return_minutes_from_midnight(time_str: str) -> int:
    hour = int(time_str[:2])
    minutes = int(time_str[3:])
    return (hour * 60) + minutes


def format_minutes_to_time(total_minutes: float) -> str:
    hour = (int(total_minutes) // 60) % 24
    minutes = int(total_minutes) % 60
    return f"{hour:02d}:{minutes:02d}"


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
            distance = current_distance + neighbour.length
            if distance < distances_from_start[neighbour.destination]:
                distances_from_start[neighbour.destination] = distance
                heapq.heappush(queue, (distance, neighbour.destination))
    
    return distances_from_start[final_location]


def calculate_dijkstra_time(map: dict, start: str, final: str, current_time: str):
    start_time_minutes = return_minutes_from_midnight(current_time)
    
    time_from_start = {}
    for key in map:
        if key == start:
            time_from_start[key] = 0.0
        else:
            time_from_start[key] = float('inf')
    
    queue = [(0.0, start)]
    
    while queue:
        elapsed_time, current_node = heapq.heappop(queue)
        
        if elapsed_time > time_from_start[current_node]:
            continue
        
        for neighbour in map[current_node]:
            current_time_of_day = (start_time_minutes + elapsed_time) % 1440
            travel_time = define_dijkstra_type(current_time_of_day, neighbour)
            new_elapsed_time = elapsed_time + travel_time
            
            if new_elapsed_time < time_from_start[neighbour.destination]:
                time_from_start[neighbour.destination] = new_elapsed_time
                heapq.heappush(queue, (new_elapsed_time, neighbour.destination))
    
    final_elapsed = time_from_start[final]
    if final_elapsed == float('inf'):
        return "inf"
        
    final_time_of_day = (start_time_minutes + final_elapsed) % 1440
    return format_minutes_to_time(final_time_of_day)


def get_dijkstra_info_distance(city_number: int, map: dict) -> list[tuple]:
    list_of_info = []
    for _ in range(10):
        start_city = str(random.randint(0, city_number))
        end_city = str(random.randint(0, city_number))
        distance = calculate_dijkstra_distance(map, start_city, end_city)
        list_of_info.append((start_city, end_city, distance))
    return list_of_info


def get_dijkstra_info_time(city_number: int, map: dict, curr_time: str) -> list[tuple]:
    list_of_info = []
    for _ in range(10):
        start_city = str(random.randint(0, city_number))
        end_city = str(random.randint(0, city_number))
        final_time = calculate_dijkstra_time(map, start_city, end_city, curr_time)
        list_of_info.append((start_city, end_city, final_time))
    return list_of_info


def print_dijkstra_info(cities_info: list[tuple]):
    for start_city, end_city, result in cities_info:
        if isinstance(result, float):
            print(f"Distance from {start_city} to {end_city} is {result:.2f}")
        else:
            print(f"Arrival time from {start_city} to {end_city} is {result}")