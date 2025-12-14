# SPACE Primitives

SPACE is based on the idea that threads, virtual memory, and IPC are a bad
semantic match as the low-level abstractions in a system.  What actually exists
in the hardware is the CPU, MMU, and trap/interrupt mechanism.  Threads, virtual
memory, etc, should be higher-level abstractions built on top of fundamental
abstractions representing the hardware:

    CPU  - sequences through instructions while referencing memory.
    MMU  - maps CPU virtual addresses into physical addresses, for valid mappings
    TRAP - an interruption in the normal sequencing of a CPU due to an invalid
           memory mapping, a trap, exception, or an external interrupt.

    CONTEXT - a set of MMU mappings is represented by a CONTEXT value (e.g. a
          hardware contextid, or the root of the page table (CR3 on x86).  The
          permissible operations for each mapping are determined by the CPU MODE.
    MODE - the current CPU MODE selects how permission bits are applied from each
          mapping in the current CONTEXT (analogous to Ring0..Ring3 on x86 hardware).
    PORTAL - for each CONTEXT maps hardware TRAPs to a handler, including
          specification of a new CONTEXT and MODE as well as the handler itself
    PCB  - when a CPU traverses a PORTAL, the previous execution environment (CONTEXT,
          MODE, Program Counter, and CPU registers) are recorded in a PCB (Processor
          Control Block).  PCBs are normally chained each time a new TRAP occurs.
