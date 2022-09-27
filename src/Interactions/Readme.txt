Interaction files deal with collecting data from sensors & giving commands
Often times these will call other libraries, still have to decide how to best 
inline our library submodules.
All interactions are commanded from the interface objects, allowing different
algorithms to call the interaction type (i.e MotionLeft) independently of the 
way it is executed. that way if we switch motors its not a big deal for the algorithm