#### BEGIN BASIC BLOCK ####
  c0    add $r0.1 = $r0.1, (0x01) ## Second
  c0    add $r0.2 = $r0.2, (0x01) ## First

  ## $r0.1 children
  c0    add $r0.3 = $r0.1, (0x01)
  c0    add $r0.4 = $r0.3, (0x01)

  ## $r0.2 children
  c0    add $r0.5 = $r0.2, (0x01)
  c0    add $r0.6 = $r0.5, (0x01)
  ## $r0.2's other child (fanning out)
  c0    add $r0.7 = $r0.2, (0x01)
#### END BASIC BLOCK ####
