#----------------------------------------------------------------------------------------
# Rules for creating level maps
# 
#  X: tile
#  B: Banker player
#  J: Janitor player
#  E{distance to travel}: enemy, specify the distance it travels right after (ex: E350)
#  F: Janitor item
#  G: Banker item
#  L{leverId}: lever, specify id that corresponds with what obstacle it removes (ex: L1)  **not implmented yet**
#  O{obstacleId}: obstacle, specify id (ex: O1)  **id not implemented yet**
#  C: point obstacle
#
# ---------------------------------------------------------------------------------------

level_map = [
'                            ',
'                            ',
' F      C                   ',
' XX    XXX            XX    ',
' XX J          O            ',
' XXXX         XX         XX ',
' XXXX  GE350   XX              ',
' XX    XXXXXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

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
