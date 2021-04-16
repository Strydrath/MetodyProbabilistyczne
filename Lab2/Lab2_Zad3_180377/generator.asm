.686
.XMM
.model flat
public _generator
.data
p db 7
q db 3
m db 31
.code
_generator PROC
push ebp
mov ebp, esp
mov eax, [ebp+8]
ror eax,9
;and eax, 01111111000000000000000000000000b
shl eax,1
shr eax,1
mov ebx, 8
mov ecx,23
mov edx,eax
mov edi,eax
ptl:
rol edx,4
xor edx,edi
add ecx,7
bt edx, ecx
ja zero
sub ecx,7
bts eax,ecx
jmp dalej
zero:
sub ecx,7
btr eax,ecx
dalej:
mov edx,eax
mov edi,eax
loop ptl
pop ebp
ret
_generator ENDP
END