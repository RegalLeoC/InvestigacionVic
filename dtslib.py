def interpolation_search(array, find):
    pos = 0
    low = 0
    high = 0
    al = 0
    ah = 0

    low = 0
    high = (len(array) - 1)

    while find != array[pos]:
        al = array[low]
        ah = array[high]

        pos = low + ((find - al) * (high - low) / (ah - al))
        pos = int(pos)
        if array[pos] == find:
            return pos

        if array[pos] < find:
            low = pos + 1
            al = array[pos]

        if array[pos] > find:
            high = pos - 1
            ah = array[pos]
