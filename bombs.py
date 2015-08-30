import itertools


def distance_squared(p1, p2):
    deltas = (c1 - c2 for (c1, c2) in zip(p1, p2))
    return sum(delta * delta for delta in deltas)

def nearest_bomb(location, bombs):
    return min(distance_squared(location, bomb) for bomb in bombs)

def bomb_search(locations, bombs):
    return max((nearest_bomb(loc, bombs), loc) for loc in locations)

if __name__ == '__main__':
    bombs = [(23, 43, 12), (100, 90, 95)]
    locations = itertools.product(range(101), repeat=3)
    print(bomb_search(locations, bombs))
    sams_location = (62, 67, 54)
    print(nearest_bomb(sams_location, bombs))