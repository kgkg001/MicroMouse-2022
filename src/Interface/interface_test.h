/*
---------------------
Micro Mouse 2023 
Description
    This interface is used to call the test cases from between the algorithim
    layers to the test cases developed in the tests directory
---------------------
*/
#include <stdio.h>
class test_interface {
    private:
        // location coordanates
        int x;
        int y;
    public:
        // Inialize this class before the algorithm begins
        test_interface(maze testcase);
        // called from outside the interface to "move" the algorith along
        bool left();
        bool right();
        bool backwards();
        bool forward();
};

