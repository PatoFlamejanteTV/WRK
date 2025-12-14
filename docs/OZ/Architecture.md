# Architecture

The SPACE abstractions are implemented in a user-mode program (SPACE.exe)
which runs as a native subsystem process under Windows.  Students run BasicOZ
on top of SPACE, using SPACE to provide the basic hardware abstractions.
By modifying BasicOZ students implement various projects which improve
the rather simple capabilities of BasicOZ.

Multiple instances of SPACE.exe can run on a single machine, effectively
implementing a multicomputer upon which students can experiment
with distributed algorithms.

SPACE.exe supports an extensible set of emulated devices.  Each device
is presented to BasicOZ as a set of registers.  The device emulations can
cause interrupts and perform DMA operations to memory
