def sunsetViews(buildings, direction):
    sunset_view_index = []
    n = len(buildings)

    if n == 0:
        return sunset_view_index

    start, step, end = (0, 1, n) if direction == 'WEST' else (n - 1, -1, -1)

    largest_height = 0

    for i in range(start, end, step):
        if buildings[i] > largest_height:
            sunset_view_index.append(i)
            largest_height = buildings[i]

    sunset_view_index.sort()
    return sunset_view_index
