/*
---------------------
Micro Mouse 2023 
Description
    This interface is used to call the test cases from between the algorithim
    layers to the test cases developed in the tests directory
---------------------
*/
#include "tests/maze.h"
#include "interface_test.h"
/// @brief Constructor takes in a Maze insance
/// @param testcase maze instance you woukd like to test your algorithm against
//test_interface::test_interface(Maze testcase){

//}
/// @brief Analogus to the physical mouse turning left
/// @return orientation array examining the mouse's new perspective
int * test_interface::left(){

}
/// @brief Analogus to the physical mouse turning right
/// @return orientation array examining the mouse's new perspective
int * test_interface::right(){

}

/// @brief Analogus to the physical mouse moving backward
/// @return bool representing whether the mouse has hit a wall or not
bool test_interface::backwards(){

}
/// @brief Analogus to the physical mouse moving forward
/// @return bool representing whether the mouse has hit a wall or not
bool test_interface::forward(){

}