/*
---------------------
Micro Mouse 2023 
Description
    class used to handle test case construction through the use of maze 
objects which hold one of the possible maze constructions
---------------------
*/
#include "src/Interface/interface_test.h"
#include <stdio.h>

#ifndef MAZE_H
#define MAZE_H
/// @brief abstraction of the maze into a 2D array for the use of testing
class maze {
    private:
    // array representing the 2d maze object can be of various sizes
    int grid[16][16];
    mouse jerry;
    public:
    // constructor of the maze object
    maze(mouse jerry, int *array);
    // checking directional calls 
    bool left();
    bool right();
    bool backwards();
    bool forward();
};
/// @brief place holder for the location of the mouse in the maze, used in debugging
class mouse {
    private:
    int x_location;
    int y_location;

    public:
    /// @brief describes the starting location of te mouse
    /// @param x starting x location
    /// @param y starting y location
    mouse(int x, int y);
    void change_location(int x, int y);
};
#endif