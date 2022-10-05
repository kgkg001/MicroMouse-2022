//------------------------------------
// UB IEEE 2022-2023
//  Base class for algorithms 
//  All algorithm implementations must inherit from this,
//  allows for communication between algorithms and interfaces
//------------------------------------
#include <iostream>
#include "../Interface/interface.h"
#ifndef ALGO_H
#define ALGO_H
/// @brief Abstraction, this class allows your algorithm to interact 
/// with your choosen interface object. Giving it access to the interface 
/// functions and data. Along with adding additional modularity with testing
class algorithm {
    public:
        void gather_interface(interface inter){
            //TODO implement how we gather the algo from the constructor
        }
    private:
        interface inter;
};
#endif