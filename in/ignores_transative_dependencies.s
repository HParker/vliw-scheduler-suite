#### BEGIN BASIC BLOCK ####
c0    ldw $r0.1 = 0x0[$r0.1] ## Fans out 4, but 3 of them are transative
c0    ldw $r0.2 = 0x0[$r0.2] ## Fans out 2 (schedules first)

## fan out to 4, but 3 of them are transative
c0    add $r0.3 = $r0.1, (0x01)
c0    add $r0.4 = $r0.1, $r0.3
c0    add $r0.7 = $r0.1, $r0.3
c0    add $r0.8 = $r0.1, $r0.3

## fan out to 2 on $r0.2 which is more than the one non trasative dep above
c0    add $r0.5 = $r0.2, (0x01)
c0    add $r0.6 = $r0.2, (0x01)
#### END BASIC BLOCK ####
