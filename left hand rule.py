"""
	This is a simple wall follower algorithm based on
        a left hand rule.
    https://en.wikipedia.org/wiki/Maze_solving_algorithm#Wall_follower
    
"""

def solve_maze():
    """
    	N
    W		E
    	S
    
    UP 	 	(N)	- maze.get_neighbours()[0][1]
    RIGHT 	(E)	- maze.get_neighbours()[1][2]
    DOWN 	(S) - maze.get_neighbours()[2][1]
    LEFT 	(W) - maze.get_neighbours()[1][0]
    
    """
    
    facing = "S"
    
    while maze.is_maze_solved() == False:
        
        left_wall = get_left_wall(facing)
        front_wall = get_front_wall(facing)
        
        if left_wall != 1:
            #facing = rotate_cw(facing)
            facing = rotate_facing(facing, "CCW")
            step_where_facing(facing)
            continue
        elif front_wall != 1:
            step_where_facing(facing)
            continue
        else:
            #facing = rotate_ccw(facing)
            facing = rotate_facing(facing, "CW")
            continue
    else:
        print "GOTCHA!!!!!"

		
def get_left_wall(facing):
    if facing == "N":
        return maze.get_neighbours()[1][0]
    elif facing == "E":
        return maze.get_neighbours()[0][1]
    elif facing == "S":
        return maze.get_neighbours()[1][2]
    elif facing == "W":
        return maze.get_neighbours()[2][1]
    
def get_front_wall(facing):
    if facing == "N":
        return maze.get_neighbours()[0][1]
    elif facing == "E":
        return maze.get_neighbours()[1][2]
    elif facing == "S":
        return maze.get_neighbours()[2][1]
    elif facing == "W":
        return maze.get_neighbours()[1][0]
    
def step_where_facing(facing):
    if facing == "N":
        maze.up()
    elif facing == "E":
        maze.right()
    elif facing == "S":
        maze.down()
    elif facing == "W":
        maze.left()
    
def rotate_facing(facing, rotation):

    directions = ["N", "E", "S", "W"]
    facindex = directions.index(facing)
    
    if rotation == "CW":
        if facindex == len(directions) - 1:
            return directions[0]
        else:
            return directions[facindex + 1]
        
    elif rotation == "CCW":
        if facindex == 0:
            return directions[-1]
        else:
            return directions[facindex - 1]

solve_maze()