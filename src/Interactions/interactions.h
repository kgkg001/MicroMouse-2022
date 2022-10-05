/*
---------------------
Micro Mouse 2023 
Description
    abstract class used to call individual interaction or abstract conglomerates
    interacts with individual interface obects through the use of interface abstraction
---------------------
*/
#ifndef INTERACTIONS_H
#define INTERACTIONS_H
/// @brief TODO implement some sort of information buffer for the interface to use
/// additionally find a way to hold multiple interaction child object under one
/// declaration for use in the sensor array, or movement interactions
class interaction {
    private:
    public:
};
#endif
/* 
    IMPORTANT!
----------------
        We must be critical of the way we copy in the Arduino.ino files to the
    interactions context, more research must be done to insure proper compilation
    of these files. A good place to start, would be looking through arduino
    specific makefiles to understand how to include the correct file types and 
    preserve our libraries intended interactions
*/
