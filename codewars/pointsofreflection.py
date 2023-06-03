def symmetric_point(p, q):
    diff_x = q[0]-p[0]
    x = q[0] +  diff_x

    diff_y = q[1]-p[1]
    y = q[1] +  diff_y

    return [x,y]
