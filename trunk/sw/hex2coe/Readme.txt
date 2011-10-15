Note:
(1) hex2coe is a small tool which converts avr-gcc generated hex file 
    to Xilinx specified block ram initialized eco file.
    Usage: open command window, type following command.
    hex2coe.exe [infile.hex] [outfile.coe]
    infile.hex  : AVRStudio generate programing file after build.
    outfile.coe : COE file used to initialize the Block ram in Core generated.
(2) Our project use 16 bit length word block ram to store program, 
    hex2coe can only convert gcc generated hex in Intel style to 16 bit length word.
    I use AVRStudio 5.0 to generate the hex file from assemble language.
    Any other application(like CVAVR, ICCAVR, IAR EMAVR) is not tested unless mentioned.
(3) The program was written by standard C, so you can use any C compiler to build executable file
    We use Visual C++ 2010 Express, which can download from MS web site for free.
    You can use GCC. It's no problem. The pre-complied EXE file was running in 32-bit Windows XP system.
(4) Finally, we got the original source for 8-bit block ram initialized file from http://moxi.jp/wiki, then modified for 16 bit ram.
    Thanks for their great idea.
(5) You can get further information about Intel style hex information from en.wikipedia.org/wiki/Hexadecimal.

Enjoy! :)
 tigerwang202#gmail.com
2011-10-16