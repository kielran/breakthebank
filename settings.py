#-------------------------------------------------------------------------------------------------
# Rules for creating level maps
#
#  X: tile
#  B: Banker player
#  J: Janitor player
#  E: enemy, specify the distance it travels and its speed
#  F: Janitor item
#  G: Banker item
#  L: Lever, specify id     **not implmented yet**
#  O: Obstacle, specify id  **id not implemented yet**
#  C: Point obstacle
#
#
# Rules for parameters
#
#  - put parameters in order of which the entity appears in the map (left to right, top to bottom)
#  - level_param is a 2d array, each subarray contains the parameters for one entity
# -----------------------------------------------------------------------------------------------

level_map = [
'                            ',
'                            ',
' F      C                   ',
' XX    XXX            XX    ',
' XX J          O            ',
' XXXX         XX         XX ',
' XXXX  GE     XX            ',
' XX    XXXXXXXX   XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',]

level_param = [[335, 2]]

# level_map = [
# '                            ',
# '                            ',
# '                            ',
# ' XX    XXX            XX    ',
# ' XX P                       ',
# ' XXXX         XX         XX ',
# ' XXXX       XX              ',
# ' XX    X  XXXX    XX  XX    ',
# '       X  XXXX    XX  XXX   ',
# '    XXXX  XXXXXX  XX  XXXX  ',
# 'XXXXXXXX  XXXXXX  XX  XXXX  ']

# level_map = [
# '                            ',
# '                            ',
# '                            ',
# '                            ',
# '                            ',
# '                            ',
# '                            ',
# '                            ',
# '         XE  B              ',
# '  P J  XXXXXXXXXXXXX        ',
# 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']

#11 rows
# tile_size = 64
# screen_width = 1280
# screen_height = len(level_map) * tile_size
