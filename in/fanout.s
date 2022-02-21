#### BEGIN BASIC BLOCK ####
c0    ldw $r0.1 = 0x0[$r0.1] ## Fans out 2
c0    ldw $r0.2 = 0x0[$r0.2] ## Fans out 3 (scheduld first)

## fan out to 2 from $r0.1
c0    add $r0.3 = $r0.1, (0x01)
c0    add $r0.4 = $r0.1, (0x01)

## fan out to 3 from $r0.2
c0    add $r0.5 = $r0.2, (0x01)
c0    add $r0.6 = $r0.2, (0x01)
c0    add $r0.7 = $r0.2, (0x01)
#### END BASIC BLOCK ####
