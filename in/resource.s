#### BEGIN BASIC BLOCK ####
c0    add $r0.1 = $r0.1, $r0.1 ## 5/4 = 1.25 resource score
c0    add $r0.2 = $r0.2, $r0.2
c0    add $r0.3 = $r0.3, $r0.3
c0    add $r0.4 = $r0.4, $r0.4
c0    add $r0.5 = $r0.5, $r0.5

c0    mpyhs $r0.6 = $r0.6, $r0.6 ## 3/2 = 1.5 (should schedule first)
c0    mpylu $r0.7 = $r0.7, $r0.7
c0    mpylu $r0.8 = $r0.8, $r0.8
#### END BASIC BLOCK ####
