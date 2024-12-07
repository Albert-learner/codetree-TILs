import sys
from collections import defaultdict
from heapq import heappop, heappush


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Coordinate) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Gem:
    def __init__(self, x, y, number, direction, weight):
        self.x = x
        self.y = y
        self.number = number
        self.direction = direction
        self.weight = weight


def init_mapper():
    return {'L': 0, 'D': 1, 'U': 2, 'R': 3}


def simulate(gems, time, last_crash_time, dx, dy):
    map_dict = defaultdict(list)
    
    # Move gems and group by new positions
    for gem in gems:
        gem.x += dx[gem.direction]
        gem.y += dy[gem.direction]
        coordinate = Coordinate(gem.x, gem.y)
        map_dict[coordinate].append(gem)
    
    # Process collisions
    to_remove = []
    for coordinate, gem_list in map_dict.items():
        if len(gem_list) > 1:
            last_crash_time[0] = time
            # Create a max-heap to process gems
            pq = []
            for gem in gem_list:
                heappush(pq, (-gem.weight, -gem.number, gem))
            
            heappop(pq)  # Keep the most significant gem
            while pq:
                _, _, gem_to_remove = heappop(pq)
                to_remove.append(gem_to_remove)
    
    # Remove collided gems
    gems = [gem for gem in gems if gem not in to_remove]
    return gems


def main():
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    results = []
    mapper = init_mapper()
    dx = [-0.5, 0.0, 0.0, 0.5]
    dy = [0.0, -0.5, 0.5, 0.0]

    line_index = 1
    for _ in range(T):
        N = int(data[line_index])
        line_index += 1
        gems = []
        for num in range(1, N + 1):
            x, y, w, d = data[line_index].split()
            x = float(x)
            y = float(y)
            w = int(w)
            d = mapper[d]
            gems.append(Gem(x, y, num, d, w))
            line_index += 1
        
        time = 0
        last_crash_time = [-1]  # Use list to emulate mutable integer
        while time < 4000:
            time += 1
            gems = simulate(gems, time, last_crash_time, dx, dy)
        
        results.append(last_crash_time[0])
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    main()