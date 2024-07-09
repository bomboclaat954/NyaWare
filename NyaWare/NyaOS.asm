org 0x07c00

start:
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov bx, 0x8000
    mov si, msg
    call print


print:
    push si
    push ax
    .loop:
        lodsb
        or al, al
        jz .done
        mov ah, 0x0E
        int 0x10
        jmp .loop
    .done:
        pop ax
        pop si
        ret

msg db "Your computer was succesfully repaired (Windows has been deleted)", 13, 0

times (510-($-$$)) db 0x00
dw 0xAA55
