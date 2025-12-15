# SPACE Operations

The basic operations implemented by SPACE.exe manipulate the SPACE primitives.
    MapMemory(ctx, virtual, phys, modeaccess)

    MapPortal(ctx, trap, pctx, pmode, ppc, modeaccess)

    Resume()
    token = Suspend()
    Unsuspend(token)

MapMemory() and MapPortal() set CONTEXT and PORTAL mappings for a specific CONTEXT.

Portal traversal is implicit in response to a TRAP (including deliberately executing
an instruction that causes a TRAP).  The interrupt execution environment is recorded
in a PCB and subsequent portal traversals chain PCBs as a stack.

Resume() restores the most recent PCB (analogous to a return-from-interrupt instruction).
Suspend() breaks the current chain by assigning a token to it and creating a new chain.
Unsuspend() restores a previous chain.
