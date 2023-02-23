import pygame
import sys
import random
import os
from collections import deque


pygame.init()  # Loads all pygame modules so we don't have to do so manually

SCREEN_LENGTH = 480
SCREEN_DIMENSIONS = (SCREEN_LENGTH + 1, SCREEN_LENGTH + 1)
window = pygame.display.set_mode(SCREEN_DIMENSIONS)
clock = pygame.time.Clock()
pygame.display.set_caption("Maze Generator")

FPS = 30
MAZE_SIZE = 16
CELL_LENGTH = SCREEN_LENGTH // MAZE_SIZE
CELL_BORDER_WIDTH = 4

WALL = "W"
CLEAR = "C"
VISITED = "V"
UNVISITED = "U"
UNEXPLORED = "N"
EXPLORED = "E"

PURPLE = pygame.Color("0x8e44ad")
BROWN = pygame.Color("0x964B00")
GREEN = pygame.Color("0x00FF00")
LIGHT_CYAN_GREY = pygame.Color("0x85929e")
DARK_GREY = pygame.Color("0x333333")
LIGHT_BROWN = pygame.Color("0x888888")


class Cell:
    """The cell class creates the objects that represent each node on the maze
    Each cell has the following: x and y positions, True/False for each wall on face,
    a status of visited/unvisited, and status of explored/unexplored, as well as a parent
    cell which is the cell that the mouse came from to reach this cell."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top_border = True
        self.bottom_border = True
        self.left_border = True
        self.right_border = True
        self.status = UNVISITED
        self.explored = UNEXPLORED
        self.parent = None
        # self.is_current = False

    def __str__(self):
        return f"|X({self.x}) and Y({self.y})|"

    def draw(self):
        x_cord = self.x * CELL_LENGTH
        y_cord = self.y * CELL_LENGTH

        if is_destination(self) and self.explored == EXPLORED:
            pygame.draw.rect(window, GREEN, (x_cord, y_cord, CELL_LENGTH, CELL_LENGTH))
        elif is_destination(self):
            pygame.draw.rect(
                window, LIGHT_BROWN, (x_cord, y_cord, CELL_LENGTH, CELL_LENGTH)
            )
        elif self.explored == EXPLORED:
            pygame.draw.rect(
                window, DARK_GREY, (x_cord, y_cord, CELL_LENGTH, CELL_LENGTH)
            )
        elif self.status == VISITED:
            # rect(the window, the color, the x-width, the y-height)
            pygame.draw.rect(
                window, LIGHT_CYAN_GREY, (x_cord, y_cord, CELL_LENGTH, CELL_LENGTH)
            )

        if self.top_border:
            # line(the window, the color, tuple of starting x and y cords, tuple of ending x and y cords, line width)
            pygame.draw.line(
                window,
                PURPLE,
                (x_cord, y_cord),
                (x_cord + CELL_LENGTH, y_cord),
                CELL_BORDER_WIDTH,
            )
        if self.bottom_border:
            pygame.draw.line(
                window,
                PURPLE,
                (x_cord, y_cord + CELL_LENGTH),
                (x_cord + CELL_LENGTH, y_cord + CELL_LENGTH),
                CELL_BORDER_WIDTH,
            )
        if self.left_border:
            pygame.draw.line(
                window,
                PURPLE,
                (x_cord, y_cord),
                (x_cord, y_cord + CELL_LENGTH),
                CELL_BORDER_WIDTH,
            )
        if self.right_border:
            pygame.draw.line(
                window,
                PURPLE,
                (x_cord + CELL_LENGTH, y_cord),
                (x_cord + CELL_LENGTH, y_cord + CELL_LENGTH),
                CELL_BORDER_WIDTH,
            )

    def set_parent(self, new_parent):
        if self.parent == None:
            self.parent = new_parent
        else:
            raise Exception("Cannot change parent once initialized.")


class Aldous:
    """Aldous is the class the creates maze objects out of cells via the Aldous-Broder algorithm.
    Creates a random maze from the set of all mazes with the dimensions given to its constructor."""

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cell_num = height * width
        self.num_visited = 0
        self.grid = self.run_algo()

    def run_algo(self):
        self.grid = generate_start_grid(self.height, self.width)

        current_cell = self.grid[random.randint(0, self.height - 1)][
            random.randint(0, self.width - 1)
        ]
        current_cell.visited = True

        while self.cell_num != self.num_visited:

            current = current_cell
            cx = current.x
            cy = current.y

            neighbors = find_any_neighbors(current, self.grid)
            neighbor = random.choice(neighbors)

            if neighbor.status == UNVISITED:

                nx = neighbor.x
                ny = neighbor.y

                if (cy == ny) and (cx > nx):
                    current.left_border = False
                    neighbor.right_border = False
                elif (cy == ny) and (cx < nx):
                    current.right_border = False
                    neighbor.left_border = False
                elif (cx == nx) and (cy > ny):
                    current.top_border = False
                    neighbor.bottom_border = False
                elif (cx == nx) and (cy < ny):
                    current.bottom_border = False
                    neighbor.top_border = False
                else:
                    raise Exception("Cells were not neighbors")

                neighbor.status = VISITED
                self.num_visited += 1

            current_cell = neighbor

        return self.grid


class Mouse:
    """Mouse is the triangular object that points in the direction of its orientation,
    The mouse has an x and y position along with its orientation of Right, Left, Bottom, or Top.
    The class contains funcitonality for changing the orientation of the mouse towards a cell and
    moving to a specified cell."""

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def draw(self):
        center_x_cord = (self.x * CELL_LENGTH) + CELL_LENGTH // 2
        center_y_cord = (self.y * CELL_LENGTH) + CELL_LENGTH // 2

        half_side_length = CELL_LENGTH // 4

        if self.orientation == "Right":
            p1 = (center_x_cord - half_side_length, center_y_cord - half_side_length)
            p2 = (center_x_cord - half_side_length, center_y_cord + half_side_length)
            p3 = (center_x_cord + half_side_length, center_y_cord)
            points = (p1, p2, p3)
            pygame.draw.polygon(window, BROWN, points)
        elif self.orientation == "Left":
            p1 = (center_x_cord + half_side_length, center_y_cord - half_side_length)
            p2 = (center_x_cord + half_side_length, center_y_cord + half_side_length)
            p3 = (center_x_cord - half_side_length, center_y_cord)
            points = (p1, p2, p3)
            pygame.draw.polygon(window, BROWN, points)
        elif self.orientation == "Bottom":
            p1 = (center_x_cord - half_side_length, center_y_cord - half_side_length)
            p2 = (center_x_cord + half_side_length, center_y_cord - half_side_length)
            p3 = (center_x_cord, center_y_cord + half_side_length)
            points = (p1, p2, p3)
            pygame.draw.polygon(window, BROWN, points)
        elif self.orientation == "Top":
            p1 = (center_x_cord - half_side_length, center_y_cord + half_side_length)
            p2 = (center_x_cord + half_side_length, center_y_cord + half_side_length)
            p3 = (center_x_cord, center_y_cord - half_side_length)
            points = (p1, p2, p3)
            pygame.draw.polygon(window, BROWN, points)

    def reorient_by_cell(self, current_cell, cell_to_face):
        if where_is_neighbor(current_cell, cell_to_face) == "Left":
            self.orientation = "Left"
        elif where_is_neighbor(current_cell, cell_to_face) == "Right":
            self.orientation = "Right"
        elif where_is_neighbor(current_cell, cell_to_face) == "Above":
            self.orientation = "Top"
        elif where_is_neighbor(current_cell, cell_to_face) == "Below":
            self.orientation = "Bottom"
        else:
            raise Exception(
                "ERROR: orient_mouse could not find appropriate orientation."
            )

    def move_by_cell(self, cell_to_move_to):
        cell_to_move_to.explored = EXPLORED
        self.x = cell_to_move_to.x
        self.y = cell_to_move_to.y


def generate_start_grid(height, width):
    retVal = []
    for h in range(height):
        sublist = []
        for w in range(width):
            sublist.append(Cell(w, h))

        retVal.append(sublist)

    return retVal


def find_any_neighbors(current, grid):
    neighbors = []

    cx = current.x
    cy = current.y

    neighbors = []

    for ybump in range(-1, 2, 1):
        for xbump in range(-1, 2, 1):
            y_index = cy + ybump
            x_index = cx + xbump
            if (
                (abs(ybump) != abs(xbump))
                and (y_index >= 0)
                and (y_index <= MAZE_SIZE - 1)
                and (x_index >= 0)
                and (x_index <= MAZE_SIZE - 1)
            ):
                new_neighbor = grid[y_index][x_index]
                neighbors.append(new_neighbor)

    return neighbors


def where_is_neighbor(current, neighbor):
    cx = current.x
    cy = current.y
    nx = neighbor.x
    ny = neighbor.y

    if (cy == ny) and (cx == nx + 1):
        return "Left"
    elif (cy == ny) and (cx + 1 == nx):
        return "Right"
    elif (cx == nx) and (cy == ny + 1):
        return "Above"
    elif (cx == nx) and (cy + 1 == ny):
        return "Below"
    else:
        raise Exception("neighbor not found")


def manhatten(location_cell):

    goal_lower = MAZE_SIZE // 2 - 1
    goal_upper = MAZE_SIZE // 2

    lc_x = location_cell.x
    lc_y = location_cell.y

    if abs(lc_x - goal_lower) < abs(lc_x - goal_upper):
        tc_x = goal_lower
    else:
        tc_x = goal_upper

    if abs(lc_y - goal_lower) < abs(lc_y - goal_upper):
        tc_y = goal_lower
    else:
        tc_y = goal_upper

    dx = abs(tc_x - lc_x)
    dy = abs(tc_y - lc_y)

    return dx + dy


def is_destination(cell):
    cx = cell.x
    cy = cell.y

    goals = (MAZE_SIZE // 2 - 1, MAZE_SIZE // 2)

    if (cx in goals) and (cy in goals):
        return True
    else:
        return False


def find_valid_neighbors(current, maze):
    reachable_neighbors = []

    all_neighbors = find_any_neighbors(current, maze.grid)

    for neighbor in all_neighbors:
        if neighbor.explored == UNEXPLORED:

            # Neighbor is ontop and passage is open
            if (
                where_is_neighbor(current, neighbor) == "Above"
                and current.top_border == False
            ):
                reachable_neighbors.append(neighbor)

            # Neighbor is right and passage is open
            if (
                where_is_neighbor(current, neighbor) == "Right"
                and current.right_border == False
            ):
                reachable_neighbors.append(neighbor)

            # Neighbor is to left and passage is open
            if (
                where_is_neighbor(current, neighbor) == "Left"
                and current.left_border == False
            ):
                reachable_neighbors.append(neighbor)

            # Neighbor is below and passage is open
            if (
                where_is_neighbor(current, neighbor) == "Below"
                and current.bottom_border == False
            ):
                reachable_neighbors.append(neighbor)

    return reachable_neighbors


def are_neighbors(current_cell, target_cell):
    cx = current_cell.x
    cy = current_cell.y
    tx = target_cell.x
    ty = target_cell.y

    if (cy == ty) and (cx == tx + 1):
        return True
    elif (cy == ty) and (cx + 1 == tx):
        return True
    elif (cx == tx) and (cy == ty + 1):
        return True
    elif (cx == tx) and (cy + 1 == ty):
        return True
    else:
        return False


def are_valid_neighbors(current_cell, target_cell):
    cx = current_cell.x
    cy = current_cell.y
    tx = target_cell.x
    ty = target_cell.y

    if (cy == ty) and (cx == tx + 1) and current_cell.left_border == False:
        return True
    elif (cy == ty) and (cx + 1 == tx) and current_cell.right_border == False:
        return True
    elif (cx == tx) and (cy + 1 == ty) and current_cell.bottom_border == False:
        return True
    elif (cx == tx) and (cy == ty + 1) and current_cell.top_border == False:
        return True
    else:
        return False


def optimize_neighbor_order(neighbors):
    # implement a selection sort to order the neighbors so that the neighbors
    # with the lowest distance to the center will be popped first

    for i in range(len(neighbors)):
        largest_val = manhatten(neighbors[i]) + 1
        largest_index = i
        for j in range(i, len(neighbors)):
            if (manhatten(neighbors[j]) + 1) > largest_val:
                largest_val = manhatten(neighbors[j]) + 1
                largest_index = j
        temp = neighbors[i]
        neighbors[i] = neighbors[largest_index]
        neighbors[largest_index] = temp

    return neighbors


def render_maze(maze, mouse):
    for row in maze.grid:
        for cell in row:
            cell.draw()

    mouse.draw()
    pygame.display.flip()
    clock.tick(FPS)


########################################################
### Simple Depth-First-Search with an Explicit Stack ###
########################################################

# Create an empty stack and push the starting node onto the stack.
# Repeat the following steps until the stack is empty:
# a. Pop a node from the stack and mark it as visited.
# b. Check to see if this cell is your destination, if so, quit.
# c. For each unvisited neighbor of the current node, push the neighbor onto the stack.
# Once the stack is empty, the algorithm has finished and all nodes have been visited


######################################
### Moving and Searching Algorithm ###
######################################

# Create the maze
# Create the mouse
# Create an empty stack that will be used to store the possible progressions in the search
# Push the first node onto the stack
# Repeat the following steps until the stack is empty (every visitable cell has been visited) or destination found
# Pop a node from the stack and mark it as visited, set it as our target_cell
# If we are currently on this cell:
# do nothing, this is our first move

# If we are not neighboring the cell on a face
# While current_cell is not neighboring target_cell:
# Orient the mouse to current_cell.parent, re-render
# Move the mouse to current_cell.parent, re-render
# current_cell = current_cell.parent
# (Else)If we are neighboring the target_cell on a face
# Orient the mouse towards the target_cell, re-render
# Move the mouse to the target_cell, re-render
# current_cell = target_cell
# If current_cell is our destination:
# QUIT
# ELSE
# For each unvisited neighbor of the current_cell, push that neighbor to the stack


def movement(current_cell, stack, maze, mouse):

    target_cell = stack.pop()

    if current_cell == target_cell:
        current_cell.explored = EXPLORED

    while (current_cell != target_cell) and (
        are_valid_neighbors(current_cell, target_cell) == False
    ):
        mouse.reorient_by_cell(current_cell, current_cell.parent)
        render_maze(maze, mouse)

        mouse.move_by_cell(current_cell.parent)
        render_maze(maze, mouse)

        current_cell = current_cell.parent

    if are_valid_neighbors(current_cell, target_cell):

        target_cell.set_parent(current_cell)

        mouse.reorient_by_cell(current_cell, target_cell)
        render_maze(maze, mouse)

        current_cell = target_cell
        # current_cell.explored = EXPLORED
        mouse.move_by_cell(current_cell)
        render_maze(maze, mouse)

    neighbors = find_valid_neighbors(current_cell, maze)
    neighbors = optimize_neighbor_order(neighbors)
    for neighbor in neighbors:
        if neighbor not in stack:
            stack.append(neighbor)

    # check_stack(stack) was used for debugging, not needed

    return current_cell


def check_stack(stack):
    # check to see if stack has duplicte values
    if len(set(stack)) != len(stack):
        raise Exception("Set contains duplicate values.")
    for cell in stack:
        if cell.explored == EXPLORED:
            raise Exception("Cell in stack reached unreachable state.")


def main():
    maze = Aldous(MAZE_SIZE, MAZE_SIZE)
    mouse = Mouse(0, MAZE_SIZE - 1, "Bottom")

    stack = []
    current_cell = maze.grid[MAZE_SIZE - 1][0]
    stack.append(current_cell)

    iterating = False
    stop = False
    render_maze(maze, mouse)
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:

                if iterating == False:
                    iterating = True
                else:
                    iterating = False

            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
                and not iterating
            ):
                if not stop:
                    current_cell = movement(current_cell, stack, maze, mouse)
                if is_destination(current_cell):
                    stop = True

        if iterating:
            if not stop:
                current_cell = movement(current_cell, stack, maze, mouse)
            if is_destination(current_cell):
                stop = True


if __name__ == "__main__":
    main()

    # the issue is that there was a cell popped from that stack that was explored which shouldn't be possible
