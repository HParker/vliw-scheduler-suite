#### BEGIN BASIC BLOCK ####
c0 cmpeq $b0.1 = $r0.10, (-0x40)
c0 cmpeq $b0.2 = $r0.14, (-0x40)
c0 addcg $r0.16, $b0.3 = $b0.4, $r0.17, $r0.18
;;
c0 addcg $r0.11, $b0.0 = $b0.1, $r0.12, $r0.13
c0 cmpeq $b0.2 = $r0.15, (-0x40)
c0 cmpeq $b0.4 = $r0.19, (-0x40)
;;
#### END BASIC BLOCK ####
