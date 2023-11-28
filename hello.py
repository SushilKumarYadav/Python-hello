print("Hello")


def list_length(list1):
    count = 0
    for item in list1:
        count += 1
    return count


def sorting(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def linear_search(data, key):
    for idx, item in enumerate(data):
        if item == key:
            return idx
    return -1