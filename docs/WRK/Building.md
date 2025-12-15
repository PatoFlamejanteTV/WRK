# Building/deploying a WRK kernel for x86 [or amd64]

    0. Copy the WRK into a directory, say %wrk%.
    1. set arch=x86 [or amd64]
    2. path %wrk%\tools\%arch%;%path%
    3. cd %wrk%\base\ntos
    4. nmake -nologo %arch%=
        will produce kernel files in BUILD\EXE\%arch%
        [wrkx86.* or wrkx64.*]
    5. copy the kernel to %SystemRoot%\system32\
    6. if x86, find the Multi-processor version of hal.dll [see below]
    7. add a line to C:\boot.ini of the target system
        to boot this kernel and the MP hal [see below]
    8. reboot and select the boot option for the new kernel
    9. you will boot up on a kernel you built/linked yourself!
        [always keep the original boot.ini line and kernel/hal available so you
         can still boot your system if something fails with your WRK kernel modifications]
    10. set up a debugger [see below]

### Multi-processor hal (x86 only, amd64 hals are all MP)
    All hals are renamed hal.dll, so you have to use the link command to
    see what type of hal hal.dll really is:
        link -dump -all hal.dll | findstr pdb
    The MP hals have an 'm' in the native name of the hal, e.g. halmacpi.dll
    You may already have an MP hal installed on UP systems, due to hyperthreading.
    If the hal isn't MP, you need to find the MP hal that corresponds to the current hal
    the target system does have, i.e.
        halacpi.dll  -> halacpim.dll    ; ACPI PIC-based PC  [used by VirtualPC]
        halaacpi.dll -> halmacpi.dll    ; ACPI APIC-based PC
        halapic.dll  -> halmps.dll      ; MPS
    Look in the WRK WS03SP1HALS\x86 directory for the MP hal you need.

### Boot.ini
    Edit boot.ini (you may have to use attrib -h -s -r first)
    Copy the line for the first operating system listed to the end of the file and edit it.
        [boot loader]
        timeout=30
        default=multi(0)disk(0)rdisk(0)partition(2)\WINDOWS
        [operating systems]
        multi(0)disk(0)rdisk(0)partition(2)\WINDOWS="Windows Server 2003, Standard"
        multi(0)disk(0)rdisk(0)partition(2)\WINDOWS="test" /kernel=wrkx86.exe /hal=halmacpi.dll
    Note that the filenames must be short (8.3) names.
    You can add additional options for debugging (as specified in the WinDbg/KD help).

### Debugging WRK
    The WinDBG/KD debuggers will work with the WRK.  The documentation is pretty thorough, and
    includes information about how to debug across a serial port, locally (examining kernel
    data from user-mode), and debugging kernels running on VirtualPC.

    Version 6.6.3.5 of the WinDBG/KD debuggers is available with the Curriculum Resource Kit
    Tools ("CurriculumResourceKit-CRK\CRKTools\Debugging Tools" directory on the CD).
    The latest version of the Windows Debugging Tools can be downloaded from
    http://www.microsoft.com/whdc/devtools/debugging.
