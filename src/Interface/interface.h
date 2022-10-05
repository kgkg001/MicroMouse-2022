//------------------------------------
// UB IEEE 2022-2023
//  Base class for interfaces 
// An abstraction that allows us to connect each individual algrorith
// to a desired interface. That way we can swap them if were interacting with
// physical or virtual testing. Or depending on the degree of data manipulation 
// desired by the algorithm
//------------------------------------
#ifndef INTERFACE_H
#define INTERFACE_H
/// @brief Still have some work todo to determine the depth of things
/// we want to inherit. Probably best to provide algorithms with a way to access
///     - Instance data (sensor array readouts)
///     - Instance functionality (motor movements)
/// while still absracting the way those are implemented in the instances
class interface {
    public:
        int * left();
        int * right();
        bool forward();
        bool backwards();
        void * grab_buffer();
    private:
        void * communication_buffer;
};
#endif