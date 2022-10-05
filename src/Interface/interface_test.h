/*
---------------------
Micro Mouse 2023 
Description
    This interface is used to call the test cases from between the algorithim
    layers to the test cases developed in the tests directory
---------------------
*/
#include "tests/maze.h"
#include "interface.h"
#include <stdio.h>
#ifndef TEST_INTERFACE_H
#define TEST_INTERFACE_H
class test_interface: public interface {
    private:
        // location coordanates
        int x;
        int y;
    public:
        /// @brief Initalizes the test case
        /// @param testcase maze object containing mouse instance
        /// @param start_x x location to start mouse
        /// @param start_y y location to start mouse
        test_interface(Maze testcase, int start_x, int start_y);
        /*
            Movement functions to be called by the algorithm, notice how the 
        left and right movements return an array of ints representing the mouse's
        new perspective. While forward/backwards return a bool representing if
        the mouse hit a wall.
        */ 
        int * left();
        int * right();
        bool backwards();
        bool forward();
};
#endif
