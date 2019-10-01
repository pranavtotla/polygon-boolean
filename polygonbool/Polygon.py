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