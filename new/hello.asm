
hello.o:     file format elf64-x86-64
hello.o
architecture: i386:x86-64, flags 0x00000011:
HAS_RELOC, HAS_SYMS
start address 0x0000000000000000

Sections:
Idx Name          Size      VMA               LMA               File off  Algn
  0 .text         0000007f  0000000000000000  0000000000000000  00000040  2**0
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000000  0000000000000000  0000000000000000  000000bf  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  2 .bss          00000001  0000000000000000  0000000000000000  000000bf  2**0
                  ALLOC
  3 .rodata       0000000e  0000000000000000  0000000000000000  000000bf  2**0
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .init_array   00000008  0000000000000000  0000000000000000  000000d0  2**3
                  CONTENTS, ALLOC, LOAD, RELOC, DATA
  5 .comment      0000002e  0000000000000000  0000000000000000  000000d8  2**0
                  CONTENTS, READONLY
  6 .note.GNU-stack 00000000  0000000000000000  0000000000000000  00000106  2**0
                  CONTENTS, READONLY
  7 .eh_frame     00000098  0000000000000000  0000000000000000  00000108  2**3
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, DATA
SYMBOL TABLE:
0000000000000000 l    df *ABS*	0000000000000000 hello.C
0000000000000000 l    d  .text	0000000000000000 .text
0000000000000000 l    d  .data	0000000000000000 .data
0000000000000000 l    d  .bss	0000000000000000 .bss
0000000000000000 l     O .bss	0000000000000001 _ZStL8__ioinit
0000000000000000 l    d  .rodata	0000000000000000 .rodata
000000000000002c l     F .text	000000000000003e _Z41__static_initialization_and_destruction_0ii
000000000000006a l     F .text	0000000000000015 _GLOBAL__sub_I_main
0000000000000000 l    d  .init_array	0000000000000000 .init_array
0000000000000000 l    d  .note.GNU-stack	0000000000000000 .note.GNU-stack
0000000000000000 l    d  .eh_frame	0000000000000000 .eh_frame
0000000000000000 l    d  .comment	0000000000000000 .comment
0000000000000000 g     F .text	000000000000001a main
0000000000000000         *UND*	0000000000000000 _ZSt4cout
0000000000000000         *UND*	0000000000000000 _ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
000000000000001a g     F .text	0000000000000012 _Z3foov
0000000000000000         *UND*	0000000000000000 _ZNSt8ios_base4InitC1Ev
0000000000000000         *UND*	0000000000000000 .hidden __dso_handle
0000000000000000         *UND*	0000000000000000 _ZNSt8ios_base4InitD1Ev
0000000000000000         *UND*	0000000000000000 __cxa_atexit



Disassembly of section .text:

0000000000000000 <main>:
   0:	55                   	push   %rbp
   1:	48 89 e5             	mov    %rsp,%rbp
   4:	be 00 00 00 00       	mov    $0x0,%esi
			5: R_X86_64_32	.rodata
   9:	bf 00 00 00 00       	mov    $0x0,%edi
			a: R_X86_64_32	_ZSt4cout
   e:	e8 00 00 00 00       	callq  13 <main+0x13>
			f: R_X86_64_PC32	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc-0x4
  13:	b8 00 00 00 00       	mov    $0x0,%eax
  18:	5d                   	pop    %rbp
  19:	c3                   	retq   

000000000000001a <_Z3foov>:
  1a:	55                   	push   %rbp
  1b:	48 89 e5             	mov    %rsp,%rbp
  1e:	81 7d fc e7 03 00 00 	cmpl   $0x3e7,-0x4(%rbp)
  25:	7f 02                	jg     29 <_Z3foov+0xf>
  27:	eb f5                	jmp    1e <_Z3foov+0x4>
  29:	90                   	nop
  2a:	5d                   	pop    %rbp
  2b:	c3                   	retq   

000000000000002c <_Z41__static_initialization_and_destruction_0ii>:
  2c:	55                   	push   %rbp
  2d:	48 89 e5             	mov    %rsp,%rbp
  30:	48 83 ec 10          	sub    $0x10,%rsp
  34:	89 7d fc             	mov    %edi,-0x4(%rbp)
  37:	89 75 f8             	mov    %esi,-0x8(%rbp)
  3a:	83 7d fc 01          	cmpl   $0x1,-0x4(%rbp)
  3e:	75 27                	jne    67 <_Z41__static_initialization_and_destruction_0ii+0x3b>
  40:	81 7d f8 ff ff 00 00 	cmpl   $0xffff,-0x8(%rbp)
  47:	75 1e                	jne    67 <_Z41__static_initialization_and_destruction_0ii+0x3b>
  49:	bf 00 00 00 00       	mov    $0x0,%edi
			4a: R_X86_64_32	.bss
  4e:	e8 00 00 00 00       	callq  53 <_Z41__static_initialization_and_destruction_0ii+0x27>
			4f: R_X86_64_PC32	_ZNSt8ios_base4InitC1Ev-0x4
  53:	ba 00 00 00 00       	mov    $0x0,%edx
			54: R_X86_64_32	__dso_handle
  58:	be 00 00 00 00       	mov    $0x0,%esi
			59: R_X86_64_32	.bss
  5d:	bf 00 00 00 00       	mov    $0x0,%edi
			5e: R_X86_64_32	_ZNSt8ios_base4InitD1Ev
  62:	e8 00 00 00 00       	callq  67 <_Z41__static_initialization_and_destruction_0ii+0x3b>
			63: R_X86_64_PC32	__cxa_atexit-0x4
  67:	90                   	nop
  68:	c9                   	leaveq 
  69:	c3                   	retq   

000000000000006a <_GLOBAL__sub_I_main>:
  6a:	55                   	push   %rbp
  6b:	48 89 e5             	mov    %rsp,%rbp
  6e:	be ff ff 00 00       	mov    $0xffff,%esi
  73:	bf 01 00 00 00       	mov    $0x1,%edi
  78:	e8 af ff ff ff       	callq  2c <_Z41__static_initialization_and_destruction_0ii>
  7d:	5d                   	pop    %rbp
  7e:	c3                   	retq   