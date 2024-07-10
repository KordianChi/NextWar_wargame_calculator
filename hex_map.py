import heapq
from collections import defaultdict

class HexMap:
    def __init__(self):
        self.hex_costs = {}
        self.river_costs = defaultdict(lambda: float('inf'))
        self.road_costs = defaultdict(lambda: float('inf'))

    def add_hex(self, q, r, cost):
        self.hex_costs[(q, r)] = cost

    def add_river(self, q1, r1, q2, r2, cost):
        self.river_costs[frozenset({(q1, r1), (q2, r2)})] = cost

    def add_road(self, q1, r1, q2, r2, cost):
        self.road_costs[frozenset({(q1, r1), (q2, r2)})] = cost

    def get_movement_cost(self, q1, r1, q2, r2):
        road_cost = self.road_costs[frozenset({(q1, r1), (q2, r2)})]
        if road_cost != float('inf'):
            return road_cost

        cost = self.hex_costs.get((q1, r1), float('inf')) + self.hex_costs.get((q2, r2), float('inf'))
        
        river_cost = self.river_costs[frozenset({(q1, r1), (q2, r2)})]
        if river_cost != float('inf'):
            cost += river_cost

        return cost

    def get_neighbors(self, q, r):
        if r % 2 != 0:
            directions = [(0, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        else:
            directions = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 0), (-1, -1)]
        return [(q + dq, r + dr) for dq, dr in directions]

    def heuristic(self, q1, r1, q2, r2):
        # Heurystyka dla siatki heksagonalnej
        return max(abs(q1 - q2), abs(r1 - r2), abs((q1 - r1) - (q2 - r2)))

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = defaultdict(lambda: float('inf'))
        g_score[start] = 0
        f_score = defaultdict(lambda: float('inf'))
        f_score[start] = self.heuristic(*start, *goal)

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                total_cost = g_score[current]
                return total_cost

            for neighbor in self.get_neighbors(*current):
                tentative_g_score = g_score[current] + self.get_movement_cost(*current, *neighbor)
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(*neighbor, *goal)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return float('inf')

    def is_path_cost_exceeded(self, start, goal, value):
        total_cost = self.a_star(start, goal)
        return (total_cost > value, total_cost)

