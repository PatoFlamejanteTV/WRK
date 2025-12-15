# WRK v1.2

The Windows Research Kernel v1.2 contains the sources for the core of
the Windows (NTOS) kernel and a build environment for a kernel that will run on
    x86     (Windows Server 2003 Service Pack 1) and
    AMD64   (Windows XP x64 Professional)
A future version may also support booting WRK kernels on Windows XP x86 systems,
but the current kernels will fail to boot due to differences in some shared structures.

The NTOS kernel implements the basic OS functions
for processes, threads, virtual memory and cache managers, I/O management,
the registry, executive functions such as the kernel heap and synchronization,
the object manager, the local procedure call mechanism, the security reference
monitor, low-level CPU management (thread scheduling, Asynchronous and Deferred
Procedure calls, interrupt/trap handling, exceptions), etc.

The NT Hardware Abstraction Layer, file systems, network stacks, and device
drivers are implemented separately from NTOS and loaded into kernel mode
as dynamic libraries.  Sources for these dynamic components are not included
in the WRK, but some are available in various development kits published
by Microsoft, such as the Installable File System (IFS) Kit and the
Windows Driver Development Kit (DDK).

WRK v1.2 includes most of the NTOS kernel sources from the latest released
version of Windows, which supports the AMD64 architecture on the Desktop.
The kernel sources excluded from the kit are primarily in the areas of
plug-and-play, power management, the device verifier, kernel debugger
interface, and virtual dos machine.  The primary modifications to WRK
from the released kernel are related to cleanup and removal of server
support, such as code related to the Intel IA64.
