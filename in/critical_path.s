#### BEGIN BASIC BLOCK ####
c0    ldw $r0.1 = 0x0[$r0.1]
c0    ldw $r0.2 = 0x0[$r0.2]

c0    ldw $r0.3 = 0x0[$r0.3] ## should schedule second

c0    ldw $r0.4 = 0x0[$r0.4] ## should schedule first

c0    add $r0.5 = $r0.4, $r0.4
c0    add $r0.6 = $r0.5, $r0.4
c0    add $r0.7 = $r0.6, $r0.6

c0    add $r0.8 = $r0.3, $r0.3
c0    add $r0.9 = $r0.8, $r0.8
#### END BASIC BLOCK ####
