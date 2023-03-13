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
#  N: Janitor exit
#  M: Banker exit
#  W: Water tile
#  Z: Elevator, specify distance it travels (in tiles) and its speed
#
# Rules for parameters
#
#  - put parameters in order of which the entity appears in the map (left to right, top to bottom)
#  - level_param is a 2d array, each subarray contains the parameters for one entity
# -----------------------------------------------------------------------------------------------

level_map = [
'                            ',
'                            ',
' F     C N                  ',
' XX    XXX            XX    ',
' XXBX          M            ',
' XXXX         XX         XX ',
' XXXX  GE     XX            ',
' XX    XXXXXXXX   XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']
level_param = [[225, 2]]


level_map_0 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X     C                    X',
'X     X       C   N  M     X',
'X C    XXXWWWWXXXXXXXXXXXXXX',
'XXXXX                      X',
'XXXXXXXXXXXXXXXXXXXXXXX    X',
'X                        XXX',
'X  XXXXXXXXXXXXX  C        X',
'X              XXXXXXXXXXXXX',
'X                          X',
'XZ     G                   X',
'XXXXXXXXXXXXXX             X',
'X  B         XXXXXXXXXX    X',
'XXXXXXXXXXX     C   C    XXX',
'X  J      F                X',
'XXXXXXXXXXXWWXXXWWWWXXXXXXXX']
level0_param = [[3, 2], [350, 2]]

level_map_1 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                         BX',
'X                         XX',
'X  X  X   X   X   X   X  XXX',
'X WWWWWWWWWWWWWWWWWWWWWWWWWX',
'X                          X',
'X     B    J       N   M    X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                          X',
'X                          X',
'X          X     X    X    X',
'XX  X E    X     X    X    X',
'XXXXXXXXXXXXXXXXXXXXXXXXXX X',
'X                          X',
'X                        XXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']
level1_param=[[101,1],[100,2],[80,2]]



level_map_2 = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XX          NM    XXXXXXXXXX',
'XXX         XXX    XXXXXXXXX',
'XXXX          X     XXXXXXXX',
'XXXX B        X      XXXXXXX',
'XXXXXX       XXX      XXXXXX',
'XXXXXXX X              XXXXX',
'XXXXXXX X                XXXX',
'XXXXXXXXX                XXX',
'XXXXXXXXXX                XX',
'XXXXXXXXXXX                X',
'XXXXXXXXXXXX   E           X',
'XXXXXXXXXXXXX              X',
'XXXXXXXXXXXXXX             X',
'XXXXXXXXXXXXXXX            X',
'XXXXXXXXXXXXXXXX           X']
level2_param = [[335, 2]]

#11 rows
# tile_size = 64
# screen_width = 1280
# screen_height = len(level_map) * tile_size
