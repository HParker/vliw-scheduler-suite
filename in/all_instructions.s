#### BEGIN BASIC BLOCK ####
## 43 3 part instructions
## Add instructions in all forms
c0    add $r0.1 = $r0.1, (-0x10)
c0    add $r0.1 = $r0.1, $r0.1
c0    addcg $r0.1, $b0.0 = $b0.1, $r0.2, $r0.3

## and instructions all forms
c0    and $r0.2 = $r0.2, (-0x20)
c0    and $r0.2 = $r0.2, $r0.2
c0    andc $r0.3 = $r0.3, (-0x30)
c0    andc $r0.3 = $r0.3, $r0.3

## Max all forms
c0    max $r0.4 = $r0.4, (-0x40)
c0    max $r0.4 = $r0.4, $r0.4
c0    maxu $r0.5 = $r0.5, (-0x40)
c0    maxu $r0.5 = $r0.5, $r0.5

## Min all forms
c0    min $r0.6 = $r0.6, (-0x40)
c0    min $r0.6 = $r0.6, $r0.6
c0    minu $r0.7 = $r0.7, (-0x40)
c0    minu $r0.7 = $r0.7, $r0.7

## Or all forms
c0    or $r0.8 = $r0.8, (-0x40)
c0    or $r0.8 = $r0.8, $r0.8
c0    orc $r0.9 = $r0.9, (-0x40)
c0    orc $r0.9 = $r0.9, $r0.9

## all shXadd forms
c0    sh1add $r0.10 = $r0.10, (-0x40)
c0    sh1add $r0.10 = $r0.10, $r0.10

c0    sh2add $r0.11 = $r0.11, (-0x40)
c0    sh2add $r0.11 = $r0.11, $r0.11

c0    sh3add $r0.12 = $r0.12, (-0x40)
c0    sh3add $r0.12 = $r0.12, $r0.12

c0    sh4add $r0.13 = $r0.13, (-0x40)
c0    sh4add $r0.13 = $r0.13, $r0.13

## all sh forms
c0    shl $r0.14 = $r0.14, (-0x40)
c0    shl $r0.14 = $r0.14, $r0.14
c0    shr $r0.15 = $r0.15, (-0x40)
c0    shr $r0.15 = $r0.15, $r0.15
c0    shru $r0.16 = $r0.16, (-0x40)
c0    shru $r0.16 = $r0.16, $r0.16

## All sub forms
c0    sub $r0.17 = $r0.17, $r0.17
c0    sub $r0.17 = (0x40), $r0.17

## all extend instruction forms
c0    sxtb $r0.1 = $r0.2
c0    sxth $r0.1 = $r0.2
c0    zxtb $r0.1 = $r0.2
c0    zxth $r0.1 = $r0.2

## All xor forms
c0    xor $r0.18 = $r0.18, (-0x40)
c0    xor $r0.18 = $r0.18, $r0.18

## All mpy forms
c0    mpyll $r0.6 = $r0.6, (-0x40)
c0    mpyll $r0.6 = $r0.6, $r0.6

c0    mpyllu $r0.6 = $r0.6, (-0x40)
c0    mpyllu $r0.6 = $r0.6, $r0.6

c0    mpylh $r0.6 = $r0.6, (-0x40)
c0    mpylh $r0.6 = $r0.6, $r0.6

c0    mpylhu $r0.6 = $r0.6, (-0x40)
c0    mpylhu $r0.6 = $r0.6, $r0.6

c0    mpyhh $r0.6 = $r0.6, (-0x40)
c0    mpyhh $r0.6 = $r0.6, $r0.6

c0    mpyhhu $r0.6 = $r0.6, (-0x40)
c0    mpyhhu $r0.6 = $r0.6, $r0.6

c0    mpyl $r0.6 = $r0.6, (-0x40)
c0    mpyl $r0.6 = $r0.6, $r0.6

c0    mpylu $r0.6 = $r0.6, (-0x40)
c0    mpylu $r0.6 = $r0.6, $r0.6

c0    mpyh $r0.6 = $r0.6, (-0x40)
c0    mpyh $r0.6 = $r0.6, $r0.6

c0    mpyhu $r0.6 = $r0.6, (-0x40)
c0    mpyhu $r0.6 = $r0.6, $r0.6

c0    mpyhs $r0.6 = $r0.6, (-0x40)
c0    mpyhs $r0.6 = $r0.6, $r0.6

## All compare forms
c0    cmpeq $r0.6 = $r0.6, (-0x40)
c0    cmpeq $r0.6 = $r0.6, $r0.6
c0    cmpeq $b0.6 = $r0.6, (-0x40)
c0    cmpeq $b0.6 = $r0.6, $r0.6

c0    cmpge $r0.6 = $r0.6, (-0x40)
c0    cmpge $r0.6 = $r0.6, $r0.6
c0    cmpge $b0.6 = $r0.6, (-0x40)
c0    cmpge $b0.6 = $r0.6, $r0.6

c0    cmpgeu $r0.6 = $r0.6, (-0x40)
c0    cmpgt $r0.6 = $r0.6, (-0x40)
c0    cmpgtu $r0.6 = $r0.6, (-0x40)
c0    cmplt $r0.6 = $r0.6, (-0x40)
c0    cmpltu $r0.6 = $r0.6, (-0x40)
c0    cmpne $r0.6 = $r0.6, (-0x40)
c0    nandl $r0.6 = $r0.6, (-0x40)
c0    norl $r0.6 = $r0.6, (-0x40)
c0    orl $r0.6 = $r0.6, (-0x40)
c0    slct $r0.6 = $r0.6, (-0x40)
c0    slctf $r0.6 = $r0.6, (-0x40)

## 35 2 part instuctions
c0    ldw $r0.1 = 0x0[$r0.2]
c0    ldw.d $r0.1 = 0x0[$r0.2]
c0    ldw.s $r0.1 = 0x0[$r0.2]
c0    ldw.l $r0.1 = 0x0[$r0.2]
c0    ldh $r0.1 = 0x0[$r0.2]
c0    ldh.d $r0.1 = 0x0[$r0.2]
c0    ldh.s $r0.1 = 0x0[$r0.2]
c0    ldh.l $r0.1 = 0x0[$r0.2]
c0    ldhu $r0.1 = 0x0[$r0.2]
c0    ldhu.d $r0.1 = 0x0[$r0.2]
c0    ldhu.s $r0.1 = 0x0[$r0.2]
c0    ldhu.l $r0.1 = 0x0[$r0.2]
c0    ldb $r0.1 = 0x0[$r0.2]
c0    ldb.d $r0.1 = 0x0[$r0.2]
c0    ldb.s $r0.1 = 0x0[$r0.2]
c0    ldb.l $r0.1 = 0x0[$r0.2]
c0    ldbu $r0.1 = 0x0[$r0.2]
c0    ldbu.d $r0.1 = 0x0[$r0.2]
c0    ldbu.s $r0.1 = 0x0[$r0.2]
c0    ldbu.l $r0.1 = 0x0[$r0.2]
c0    stw 0x0[$r0.1] = $r0.2
c0    stw.s 0x0[$r0.1] = $r0.2
c0    stw.l 0x0[$r0.1] = $r0.2
c0    sth 0x0[$r0.1] = $r0.2
c0    sth.s 0x0[$r0.1] = $r0.2
c0    sth.l 0x0[$r0.1] = $r0.2
c0    stb 0x0[$r0.1] = $r0.2
c0    stb.s 0x0[$r0.1] = $r0.2
c0    stb.l 0x0[$r0.1] = $r0.2
c0    call 0x0[$r0.1] = $r0.2
c0    mov $r0.1 = 0x0[$r0.2]

## Load with labels
c0    add $r0.1 = $r0.1, (MY_LABEL + 0)
c0    stw 0x0[$r0.1] = OTHER_LABEL
c0    mov $r0.1 = (LABEL + 24)


## Two operations with carry

c0    divs $r0.1, $b0.0 = $b0.1, $r0.2, $r0.3
#### END BASIC BLOCK ####
