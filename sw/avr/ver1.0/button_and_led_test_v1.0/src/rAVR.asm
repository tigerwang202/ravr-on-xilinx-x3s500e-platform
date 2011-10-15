/*
 * rAVR.asm
 *
 *  Created: 2011-10-11 22:13:59
 *   Author: Wang
 */ 

.cseg
.org 0

start:

;initial one bit in register
ldi r16,$80

rd_port:

;read port (key status) r22 wired to key button input
mov r17,r22
cpi r17,$00
;go and blink one LED if no key pressed
breq do_xor

cpi r17,$01
;go and right shift LEDs if key[EAST] pressed
breq do_rshift

cpi r17,$02
;go and left shift LEDs if key[WEST] pressed
breq do_lshift

;jump to read keys
or r16,r16
brne rd_port

do_rshift:
cpi r16,1
breq set80
lsr r16
mov r20,r16
brne pause
set80:
ldi r16,$80
mov r20,r16
or r16,r16
brne pause

do_lshift:
cpi r16,$80
breq set1
lsl r16
mov r20,r16
brne pause
set1:
ldi r16,$01
mov r20,r16
or r16,r16
brne pause

do_xor:
; blink led
eor r20,r16

; delay
pause:
ldi r17,$18
cycle3:
ldi r18,$FF
cycle2:
ldi r19,$FF
cycle1:
or r19,r19
or r19,r19
subi r19,1
brne cycle1
subi r18,1
brne cycle2
subi r17,1
brne cycle3

or r16,r16
brne rd_port
