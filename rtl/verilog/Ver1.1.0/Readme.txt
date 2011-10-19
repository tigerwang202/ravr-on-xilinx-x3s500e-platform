Note:
2011-10-16
Initial version was released, and it's a synthesize one. 
(1) The core is running under Xilinx Spartan-3E demo board,
but it's easy to transport to other boards.
(2) The core acts the same way compared to Russian's original rAVR design on
Opencores (http://opencores.org/project,avr8).
(3) It used block ram to store program. You can use hex2coe tools in sw folder to
convert your own complied hex file to initialized file for Core generate.
(4) The avr's function is very limited. It seems work properly, but further more
test is needed.

2011-10-16
Version 1.0.1
Combine two fetch stage to one . That's the same as ATMEL's core.

2011-10-18
Version 1.1.0
One stage pipeline support added.