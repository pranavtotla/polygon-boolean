def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0  # Collinear
    if val > 0: return 1  # Clockwise
    return 2  # Anti clockwise

# Checks if q lies on the segment pr
def on_segment(p, q, r):
    if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
        return True 
    return False

def do_intersect(edge1, edge2): 
    o1 = orientation(edge1[0], edge1[1], edge2[0])
    o2 = orientation(edge1[0], edge1[1], edge2[1])
    o3 = orientation(edge2[0], edge2[1], edge1[0])
    o4 = orientation(edge2[0], edge2[1], edge1[1])
  
    if o1 != o2 and o3 != o4: 
        return True
  
    if o1 == 0 and on_segment(edge1[0], edge2[0], edge1[1]):
        return True 
  
    if o2 == 0 and on_segment(edge1[0], edge2[1], edge1[1]):
        return True
  
    if o3 == 0 and on_segment(edge2[0], edge1[0], edge2[1]):
        return True
  
    if o4 == 0 and on_segment(edge2[0], edge1[1], edge2[1]):
        return True

    return False
