# -*- coding: utf-8 -*-
# 在当前文件夹中建立Verilog工程目录，使用Opencores.org SVN上文件树结构
# wangmengyin 2011-09-26
import os
from time import gmtime, strftime
print "Create Verilog project in cuerrent directory using Opencore SVN style."
print "tigerwang202@gmail.com 2011-09-26."

## {{{ http://code.activestate.com/recipes/82465/ (r4)
def _mkdir(newdir):
    """works the way a good mkdir should :)
        - already exists, silently complete
        - regular file in the way, raise an exception
        - parent directory(ies) does not exist, make them as well
    """
    if os.path.isdir(newdir):
        pass
    elif os.path.isfile(newdir):
        raise OSError("a file with the same name as the desired " \
                      "dir, '%s', already exists." % newdir)
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            _mkdir(head)
        print "_mkdir %s" % repr(newdir)
        if tail:
            os.mkdir(newdir)
## end of http://code.activestate.com/recipes/82465/ }}}

def _mkfile(newfile):
    if os.path.isfile(newfile) == False:
        file(newfile,'w')
        print "_mkfile %s" % repr(newfile)

subDirName = ['backend'\
             ,'bench','bench/verilog','bench/VHDL'\
             ,'rtl','rtl/verilog','rtl/VHDL'\
             ,'sim','sim/rtl_sim','sim/gate_sim'\
             ,'lint'\
             ,'fv'\
             ,'lib'\
             ,'syn', 'syn/synplicity'\
             ,'doc','doc/src'\
             ,'sw']
fileName = ['doc\\Readme.txt', 'doc\\CHANGES.txt', 'Directory structure.txt']

noteContents = """
block_name/  Top level directory of a core 
    backend/  Top level backend directory 
        <vendor>/  Vendor specific floorplan, place and route directory structure 
    sim/  Top level simulations directory 
        rtl_sim/  RTL simulations 
            bin/  RTL simulation scripts 
            run/  For running RTL simulations 
            src/  Special sources for RTL simulations 
            out/  Dump and other useful output from RTL simulation 
            log/  Log files 
        gate_sim/  Gate-level simulations 
            bin/  Gate-level simulation scripts 
            run/  For running gate-level simulations 
            src/  Special sources for gate-level simulations 
            out/  Dump and other useful output from gate-level simulation 
            log/  Log files 
   syn/  Synthesis 
       <vendor>/  Each synthesis tool has separate directory 
           bin/  For synthesis scripts 
           run/  For running synthesis scripts 
           src/  Special sources for synthesis 
           out/  For generated netlists (Synopsys db, verilog) 
           log/  Log files (including reports) 
   lint/  Lint 
           bin/  Lint scripts 
           run/  For running linter 
           out/  Lint report 
           log/  Log files 
   fv/  Formal verification 
   lib/  Vendor target libraries 
   rtl/  RTL sources 
           verilog/  For verilog sources 
           vhdl/  For VHDL sources 
   bench/  Bench sources 
       verilog/  For verilog sources 
       vhdl/  For VHDL sources 
   doc/  Put specification, design and other PDF documents here 
       src/  Source version of all documents (Word, StarOffice, Frame Maker) 
   sw/  Put sources for utilities or software test cases here
"""

for name in subDirName:
    _mkdir(name)
for name in fileName:
    _mkfile(name)

try:
    fb = open(fileName[2], 'w')
    fb.write(noteContents)
finally:
    fb.close()
    
changelogNote = 'Note: This Changes file is being maintained since ' + \
    strftime("%a, %d %b %Y", gmtime()) + '\n'
    
try:
    fb = open(fileName[1], 'w')
    fb.write(changelogNote)
finally:
    fb.close()
print "Done!"

    
