# how do I tell if two line segments intersect?
#
# a line is defined by x1,y1 -> x2,y2
# ex: (0,0) -> (0,10)
# or: (0,10) -> (0,0) these two pairs of coordinates represent the same line segment
#
# case 1: perpendicular lines
#   two lines are perpendicular if one is horizontal and the other is vertical
#   a horizontal line H is one where y1 == y2
#   a vertical line V is one where x1 == x2
#   perpendicular lines intersect if:
#       V.x >= H.x1 and V.x <= H.x2 and V.y1 == H.y or V.y2 == H.y
#   perpendicular lines intersect at most once
#   if they intersect, the point of intersection is: (H.x, V.y)
#
# case 2: parallel lines
#   two lines are parallel if they are both horizontal or both vertical
#   parallel lines intersect if:
#       case 1: horizontal
#           H1.y == H2.y and H1.x