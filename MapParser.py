file_object = open("map/whirland.txt", "r")
file_object.readline().rstrip()  # metadata
content = file_object.readlines()

stats = content[0].rstrip().split(';')
map_size = stats[0].split(',')
start_point = stats[1].split(',')
building_list = stats[2].split(',')
drop_list = stats[3].split(',')
portal_list = stats[4].split(',')

# Map board.
row = int(map_size[0])
col = int(map_size[1])
map_board = [[0 for x in range(row)] for x in range(row)]
for line in range(1, row + 1):
    for char_index in range(len(content[line]) - 1):
        map_board[line - 1][char_index] = content[line][char_index]
row = int(start_point[0])
col = int(start_point[1])

# Buildings.
building_dict = {}
for building in building_list:
    building_dict[building] = ""
# From END of board to (NUM OF BUILDINGS + END of board)
for building in range(len(map_board) + 1, len(building_list) + len(map_board) + 1):
    tokens = content[building].split(';')
    building_dict[tokens[0]] = tokens[1]

# Portals.
portal_dict = {}
for portal in portal_list:
    portal_dict[portal] = ""
tokens = content[len(building_list) + len(map_board) + 1].split(';')
portal_dict[tokens[0]] = tokens[1]

file_object.close()
