from .Services import do_intersect, orientation, on_segment

class Polygon:
    points = None
    
    def __init__(self, point_array):
        self.points = point_array

    def simplify(self):
        """
        Removes all the collinear and duplicate points from the polygon.
        :return: Polygon
        """
        def are_collinear(x, y, z):
            if (x[0] * (y[1] - z[1]) + y[0] * (z[1] - x[1]) + z[0] * (x[1] - y[1])) == 0:
                return True
            return False

        new_points = self.points[:]
        for i in range(len(self.points)):
            if are_collinear(new_points[(i - 1) % len(new_points)], new_points[i % len(new_points)], new_points[(i + 1) % len(new_points)]):
                del new_points[i]
        return self.__class__(new_points)

    def max_x(self):
        """
        Returns the maximum x coordinate of the polygon.
        :return: float
        """
        return max(point[0] for point in self.points)

    def contains(self, point):
        """
        Checks if the point lies inside the polygon.
        :param point: Point
        :return: bool
        """
        infinity = [self.max_x() + 1, point[1]]
        count = 0

        for i in range(len(self.points)):
            edge = [self.points[i], self.points[(i + 1) % len(self.points)]]
            ray = [point, infinity]

            if do_intersect(edge, ray):
                if orientation(edge[0], point, edge[1]) == 0:  # Points are collinear
                    return on_segment(edge[0], point, edge[1])
                count += 1

        return count % 2 == 1
    