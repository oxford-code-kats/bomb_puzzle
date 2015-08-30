import unittest

from bombs import bomb_search, distance_squared, nearest_bomb

class BombTest(unittest.TestCase):

    def test_distance_squared(self):
        points = [
            ((0,0,0), (0,0,1), 1),
            ((0,0,0), (3,7,1), 59),
            ((2,2,2), (1,1,1), 3),
        ]

        for p1, p2, expected in points:
            with self.subTest(p1=p1, p2=p2):
                distance = distance_squared(p1, p2)
                self.assertEqual(expected, distance)

    def test_distance_squared_to_nearest_bomb(self):
        bombs = [(0,0,0), (1,1,1), (1,2,3)]
        location = (2,2,2)
        expected = 2
        self.assertEqual(expected, nearest_bomb(location, bombs))

    def test_bomb_search(self):
        bombs = [
            (0,0,0), 
            (1000, 0, 0), 
            (0, 1000, 0), 
            (0, 0, 1000),
            (1000, 1000, 0),
            (1000, 0, 1000),
            (0, 1000, 1000),
        ]

        locations = [
            (0,0,0), 
            (1000, 0, 0), 
            (0, 1000, 0), 
            (0, 0, 1000),
            (1000, 1000, 0),
            (1000, 0, 1000),
            (0, 1000, 1000),
            (1000, 1000, 1000),
            (500, 500, 500),
        ]
        expected = (1000000, (1000, 1000, 1000))

        self.assertEqual(bomb_search(locations, bombs), expected)