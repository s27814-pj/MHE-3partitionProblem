import copy


def generate_neighbours(current_list):
    result=[]
    for i in range(len(current_list)):
        # neighbour = current_list.copy()
        neighbour = copy.deepcopy(current_list)
        tmp=current_list[(i+1)%len(current_list)].get_index()
        neighbour[(i+1)%len(current_list)].set_index(current_list[i].get_index())
        neighbour[i].set_index(tmp)
        # print (i, neighbour, goal(neighbour))
        result.append(neighbour)
    return result

def generate_neighbours_indexes(current_list):
    result=[]
    for i in range(len(current_list)):
        neighbour = copy.deepcopy(current_list)