# NT Facilities used to implement SPACE

Objects
    Threads 	    - NT unit of CPU scheduling
    Processes 	    - NT virtual address space container
    Sections 	    - NT sharable memory objects
    Exception port  - NT mechanism for subsystem fault handling

Functions
    MapView	        - Map process addresses to section offsets
    Wait/Reply port - Receive/Send message to port
