import sys
from collections import defaultdict


class Gem:
    def __init__(self, x, y, number, direction, weight):
        self.x = x
        self.y = y
        self.number = number
        self.direction = direction
        self.weight = weight


def init_mapper():
    return {'L': 0, 'D': 1, 'U': 2, 'R': 3}


def simulate(gems, dx, dy):
    position_map = defaultdict(list)
    to_remove = set()

    # Move gems and group by positions
    for gem in gems:
        gem.x += dx[gem.direction]
        gem.y += dy[gem.direction]
        coordinate = (gem.x, gem.y)
        position_map[coordinate].append(gem)

    # Process collisions
    for coordinate, gem_list in position_map.items():
        if len(gem_list) > 1:
            # Mark all except the heaviest gem for removal
            gem_list.sort(key=lambda g: (-g.weight, -g.number))
            to_remove.update(gem_list[1:])

    # Remove collided gems
    gems = [gem for gem in gems if gem not in to_remove]
    return gems, bool(to_remove)  # Return whether any collision occurred


def main():
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    results = []
    mapper = init_mapper()
    dx = [-1, 0, 0, 1]  # Adjusted to integer-based movement
    dy = [0, -1, 1, 0]

    line_index = 1
    for _ in range(T):
        N = int(data[line_index])
        line_index += 1
        gems = []
        for num in range(1, N + 1):
            x, y, w, d = data[line_index].split()
            x = int(float(x) * 2)  # Convert to integer by doubling
            y = int(float(y) * 2)  # Convert to integer by doubling
            w = int(w)
            d = mapper[d]
            gems.append(Gem(x, y, num, d, w))
            line_index += 1
        
        time = 0
        last_crash_time = -1
        while time < 4000 and gems:
            time += 1
            gems, collision_occurred = simulate(gems, dx, dy)
            if collision_occurred:
                last_crash_time = time
        
        results.append(last_crash_time)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    main()