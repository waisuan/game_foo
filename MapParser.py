def init_file():
    fo = open("map/whirland.txt", "r")
    fo.readline().rstrip()  # metadata
    return fo


file_object = init_file()
content = file_object.readlines()
stats = content[0].rstrip().split(';')
map_size = stats[0]
start_point = stats[1].split(',')
building_list = stats[2].split(',')
drop_list = stats[3].split(',')
portal_list = stats[4].split(',')
print map_size
map_size = map_size.split(',')
row = int(map_size[0])
col = int(map_size[1])
map_board = [[0 for x in range(row)] for x in range(row)]
for line in range(1, row + 1):
    for char_index in range(len(content[line]) - 1):
        map_board[line - 1][char_index] = content[line][char_index]
row = int(start_point[0])
col = int(start_point[1])
print map_board[row][col]
building_dict = {}
for building in building_list:
    building_dict[building] = ""
for building in range(len(map_board) + 1, len(building_list) + len(map_board) + 1):
    tokens = content[building].split(';')
    building_dict[tokens[0]] = tokens[1]
portal_dict = {}
for portal in portal_list:
    portal_dict[portal] = ""
tokens = content[len(building_list) + len(map_board) + 1].split(';')
portal_dict[tokens[0]] = tokens[1]
file_object.close()
