/*
---------------------
Micro Mouse 2023 
Description
    class used to handle test case construction through the use of maze 
objects which hold one of the possible maze constructions
---------------------
*/
#include <stdio.h>

#ifndef MAZE_H
#define MAZE_H
/// @brief abstraction of the maze into a 2D array for the use of testing
class Maze {
    private:
        // array representing the 2d maze object can be of various sizes
        int * grid;
        Mouse jerry;
    public:
        // constructor of the maze object
        Maze(Mouse jerry, int *array);
        // checking directional calls 
        int * left();
        int * right();
        bool backwards();
        bool forward();
};
/// @brief place holder for the location of the mouse in the maze, used in debugging
class Mouse {
    private:
        /// @brief describes in 1/  the view of the mouse in the maze
        int * orientation_array;
        /// @brief describes via "North","South","East","West" mouse facing direction
        char *orientation_direction;
        location current_location;
    public:
        /// @brief describes the starting location of te mouse
        /// @param x starting x location
        /// @param y starting y location
        Mouse(location start_location);
        /// @brief changes the direction the mouse is facing
        /// @param clockwise true->rotate clockwise, false->rotate counterclockwise
        /// @return updates & returns the orientation array, and updates orientation_direction 
        int * change_orientation(bool clockwise);
        /// @brief moves the mouse object to (x,y) in the maze
        /// @param x corresponds to x axis
        /// @param y corresponds to y axis
        void change_location(int x, int y);

};

class location{
    private:
        int x_location;
        int y_location;
    public:
        int x();
        int y();
};

/* 
    This section includes an example maze to be used in testing. Remember that
    the maze class technically has no limits in size, but try to make the mazes
    transversable such that debuging is easier

    //----------EXAMPLE MAZE 1---------//
    1111111111111111       /\    
    1000001000001101      North
    1101010011100101  <West * East>
    1001010010101101      South
    1010000100000001       \/
    1111111111111111

    Above is an example 4 x 14 maze that has a path from either side, the mouse
    could be inserted at locations (1,1),(4,1),(14,1),(14,4). When using maze Arrays
    the 1 integer will represent a wall and the 0 will represent an open path
    the combination of (2x2) zeros in the middle of the maze represent the endpoint

*/

int bensArray[16][6] = {
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,
    1,1,0,1,0,1,0,0,1,1,1,0,0,1,0,1,
    1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,
    1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
};
#endif