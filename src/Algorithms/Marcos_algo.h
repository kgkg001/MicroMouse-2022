//------------------------------------
// UB IEEE 2022-2023
// Marcos's simple algorithm example,
//  doesn't solve shit...
//  Just for referance and formatting
//------------------------------------
#include "algorithm.h"
#ifndef MARCOS_ALGO_H
#define MARCOS_ALGO_H
class marcos_algo : public algorithm {
     private:
        interface choosen_interface;
        /// @brief used to store the current location that we are in the maze
        //Mouse current_mouse;
     public:
        marcos_algo(interface choosen_interface);
        void gather_location();
        void make_decision();
        void execute_decision();
};
#endif
