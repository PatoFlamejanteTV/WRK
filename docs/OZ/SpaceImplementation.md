# SPACE Implementation

CPUs are implemented using NT threads.  MMUs are built using NT processes.
Because NT threads are bound to processes, each SPACE CONTEXT/MODE is represented
as an NT process with an NT thread for each SPACE CPU.
SPACE.exe listens on the exception port for the NT processes, which allows it to
manipulate the state of the NT threads to chain PCBs, implement portal traversal
(including for memory faults) and other SPACE operations.

BasicOZ is loaded by SPACE.exe, and then communicates by causing traps which SPACE.exe
handles to implement the SPACE 'hardware' emulation.
