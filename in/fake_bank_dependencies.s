#### BEGIN BASIC BLOCK ####
c0    cmpeq $r0.5 = $r0.6, (-0x40)
c0    cmpeq $b0.6 = $r0.7, $r0.7 ## This looks like a WAW, but isn't because it writes to the branch bank instead.
#### END BASIC BLOCK ####
