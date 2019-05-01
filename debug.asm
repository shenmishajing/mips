break
syscall
eret
mfco $t0, $t1, 1
mtco $t0, $t1, 1
mfhi $t0
mflo $t0
mthi $t0
mtlo $t0
jalr $t0, $t1
blez $zero, L2
bgtz $zero, L2
bltz $zero, L2
bgez $zero, L2
lw $t0, 10($t1)
lb $t0, 10($t1)
lh $t0, 10($t1)
lbu $t0, 10($t1)
lhu $t0, 10($t1)
sw $t0, 10($t1)
sb $t0, 10($t1)
sh $t0, 10($t1)
j L2
add $zero, $zero, $zero
add $zero, $zero, $zero
add $zero, $zero, $zero
add $zero, $zero, $zero
add $zero, $zero, $zero
add $zero, $zero, $zero
add $zero, $zero, $zero
L2:nor $at, $zero, $zero
add $v1, $at, $at
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
nor $s4, $v1, $zero
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $v1, $v1, $v1
add $a2, $v1, $v1
add $v1, $a2, $a2
add $a0, $v1, $v1
add $t5, $a0, $a0
add $t0, $t5, $t5
slt $v0, $zero, $at
add $t6, $v0, $v0
add $t6, $t6, $t6
nor $t2, $zero, $zero
add $t2, $t2, $t2
sw $a2, 4($v1)
lw $a1, 0($v1)
add $a1, $a1, $a1
add $a1, $a1, $a1
sw $a1, 0($v1)
add $t1, $t1, $v0
sw $t1, 0($a0)
lw $t5, 20($zero)
L0:lw $a1, 0($v1)
add $a1, $a1, $a1
add $a1, $a1, $a1
sw $a1, 0($v1)
lw $a1, 0($v1)
and $t3, $a1, $t0
add $t5, $t5, $v0
beq $t5, $zero, L3
L1:lw $a1, 0($v1)
add $s2, $t6, $t6
add $s6, $s2, $s2
add $s2, $s2, $s6
and $t3, $a1, $s2
beq $t3, $zero, L4
beq $t3, $s2, L5
add $s2, $t6, $t6
beq $t3, $s2, L6
sw $t1, 0($a0)
L4:j L0
beq $t2, $at, L7
L7:j L8
nor $t2, $zero, $zero
add $t2, $t2, $t2
L8:sw $t2, 0($a0)
L5:j L0
lw $t1, 96($s1)
sw $t1, 0($a0)
L6:j L0
lw $t1, 32($s1)
sw $t1, 0($a0)
L3:j L0
lw $t5, 20($zero)
add $t2, $t2, $t2
or $t2, $t2, $v0
add $s1, $s1, $t6
and $s1, $s1, $s4
add $t1, $t1, $v0
beq $t1, $at, L9
L9:j L10
add $t1, $zero, $t6
add $t1, $t1, $v0
L10:lw $a1, 0($v1)
add $t3, $a1, $a1
add $t3, $t3, $t3
sw $t3, 0($v1)
sw $a2, 4($v1)
lw $a1, 0($v1)
and $t3, $a1, $t0
j L1
