## TikTok X-Argus
## Reversing the Argus Algorithm

X-Argus Api (also includes Mssdk)
- https://rapidapi.com/tiktok-api-development-tiktok-api-development-default/api/tiktok-services1

```js

X-Argus 
R0fy5TvUEH0E6kFiGAQFnDJhAZRtBWVjFXygipEnVBxrRsmOfPV+BxlZqR8/QvHfQ34cw8zKhLtUf+zJo/Sc3/CEICpL3DRdtx2+au1li5h9Rhs6jPopy2zq1d1qVxE6W1QhzL1YdKiPX9IumXadNtxo7XXLL+/cIYQqFTNfobF2DFzWT2I1MuMNwXoB+nPYdnf852vOkKYpXwm4SzwOMN4Q 47 47 f2 e5 3b d4 10 7 d 04 ea 41 62 18 04 05 9 c 32 61 01 94 6 d 05 65 63 15 7 c a0 8 a 91 27 54 1 c 6b 46 c9

8 e 7 c f5 
7 e 07  19  59 
a9 1f  3f  42 
f1 df 43  7 e 
1 c c3 cc ca 
84 bb 54  7f 
ec c9 a3 f4 
9 c df f0 84  
20  2 a 4b dc 
34  5 d b7 1 d 
be 6 a ed 65  
8b  98  7 d 46  
1b  3 a 8 c fa 
29 cb 6c ea 
d5 dd 6 a 57  
11  3 a 5b  54  
21 cc bd 58  
74 a8 8f  5f 
d2 2 e 99  76  
9 d 36 dc 68 
ed 75 cb 2f 
ef dc 21  84  
2 a 15  33  5f 
a1 b1 76  0 c 
5 c d6 4f  62  
35  32 e3 0 d 
c1 7 a01 fa 
73 d8 76  77 
fc e7 6b ce 
90 a6 29  5f  
09 b8 4b  3 c 
0 e 30 de 10
  
```

aes encryption point  
final result place;   
search: `0xc253c` eor `w9`,` w11`,` w9` ;   

```js
0x70ef40853c 	0xc253c eor 		w9, w11, w9 ; x9= 0x564fafa4 -> 0xfce76bce , x11= 0xaaa8c46a -> 0xaaa8c46a                                          ；xa-debug 0xfce76bce 
0x70ef408540 	0xc2540 eor 		w11, w12, w0 ; x0= 0xedef6a38 -> 0xedef6a38 , x11= 0xaaa8c46a -> 0x90a6295f , x12= 0x7d494367 -> 0x7d494367      ; xa-debug 0x90a6295f 
0x70ef408544 	0xc2544 		eor w12, w13, w1 ; x1= 0x24ee9fad -> 0x24ee9fad , x12= 0x7d494367-> 0x9b84b3c , x13= 0x2d56d491 -> 0x2d56d491          ；xa-debug 0x09b84b3c 
0x70ef408548 	0xc2548 		eor w8, w10, w8 ; x8= 0x8ac41b06 -> 0xe30de10 , x10= 0x84f4c516 -> 0x84f4c516                                          ；xa-debug 0x0e30de10
```

eor w9, w11, w9 ;  
0x564fafa4 ^ 0xa4aa9470 = 0xf2e53bd4 Trace  
down: 0x564fafa4 has always existed 0xa4aa9470 This value is changed.  
Analyze 0x564fafa4  
```js
0x70ef407eac 	0xc1eac eor 		w9, w9, w1 ; x1= 0x6200 -> 0x6200 , x9= 0x604fcd40 -> 0x604faf40 
0x70ef407eb0 	0xc1eb0 eor 		w9, w9, w3 ; x3= 0xe4 -> 0xe4 , x9= 0x604faf40 -> 0x604fafa4 
0x70ef407eb4 	0xc1eb4 eor 		w9, w9 , w18 ; x9= 0x604fafa4 -> 0x564fafa4 , x18= 0x36000000 -> 0x36000000
```
0x36000000 This value is familiar, like aes' RCON.  
static const uint8_t Rcon[11] = {0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36 };  

Go back up to see if aes is used, findcrypt in ida can recognize it.  
In fact, the positioning is very simple, the offset here is 0xc1eb4. Take it to ida for static analysis.  
```js
.text: 00000000000 C1EA8 LDR W3, [X15,W3,UXTW# 2 ] 
.text: 00000000000 C1EAC EOR W9, W9, W1 
.text: 00000000000 C1EB0 EOR W9, W9, W3 
.text: 00000000000 C1EB4 EOR W9, W9 
.text: 00000000000 C1EB8 EOR W18, W4, W9 
.text: 00000000000 C1EBC STP W9, W18, [X11]
```
Exactly, this function is the aes algorithm.

```js
__int64 __fastcall sub_C1DE8 (__int64 a1, unsigned  int *a2, unsigned  int a3)
 .text: 00000000000 C1DE8 ; __unwind { 
.text: 00000000000 C1DE8 LSR W8, W2, # 2
 .text: 00000000000
 C1DEC AND W8, W8, W8, # 0 : 00000000000 C1DF0 ADD W8, W8, # 6
 .text: 00000000000 C1DF4 STR X8, [X0,# 0x1E0 ] 
.text: 00000000000C1DF8 LDR W9, [X1] 
.text: 00000000000 C1DFC CMP W2, # 0x20
 .text: 00000000000 C1E00 REV W9, W9 
.text: 00000000000 C1E04 STR W9, [X0] 
.text: 00000000000 C1E08 LDR W10 ] 
.text: 00000000000 C1E0C REV W10, W10 
.text: 00000000000 C1E10 STR W10, [X0,# 4 ] 
.text: 00000000000 C1E14 LDR W10, [X1,#8 ] 
.text: 00000000000 C1E18 REV W10, W10 
.text: 00000000000 C1E1C STR W10, [X0,# 8 ] 
.text: 00000000000 C1E20 REV W10 , [X1,# 0xC ] 
.text: 00000000000
 .text : 00000000000 C1E28 STR W10, [X0,# 0xC ]
```
This function has 3 parameters, what is it to chase in 010. For 64-bit instructions, the first three functions are generally x0, x1, and x2; 

```js
0x70ef407df4 	0xc1df4 		str x8, [x0, # 0x1e0 ] ; x0= 0x714f36da30 -> 0x714f36da30 , x8= 0xa -> 0xa 
0x70ef407df8 	0xc1df8 		ldr w9, [x1] ; x1= 0x70e8016c40 -> 0x70e8016c40 , x9= 0x714f36e5e8 -> 0x763359f1 
0x70ef407dfc 	0xc1dfc 		cmp w2, # 0x20 	; x2= 0x10 -> 0x10
```
The read length is only 0x10, which is like the length of the key, x2 16 bits, and the assumption is that it is set as the key.  
x0: 0x714f36da30  
x1: 0x70e8016c40  
x2: 0x10 

```js
0x70ef407e00 	0xc1e00 		rev w9, w9 ; x9= 0x763359f1 -> 0xf1593376 
0x70ef407e04 	0xc1e04 		str w9, [x0] ; x0= 0x714f36da30 -> 0x714f36da30 , x9= 0xf1593376 -> 0xf1593376 
0x70ef407e08 	0xc1e08 		ldr w10, [x1, # 4 ] ; x1= 0x70e8016c40 -> 0x70e8016c40 , x10= 0x714f36e5c0 -> 0x8da96e76 
0x70ef407e0c 	0xc1e0c 		rev w10, w10 ; x10= 0x8da96e76 -> 0x766ea98d 
0x70ef407e10 	0x 		,4 # str w10, [x, 4 # str w10] ; x0= 0x714f36da30 -> 0x714f36da30 , x10= 0x766ea98d -> 0x766ea98d 
0x70ef407e14 	0xc1e14 		ldr w10, [x1, # 8 ] ; x1= 0x70e8016c40 -> 0x70e8016c40 , x10= 0x766ea98d -> 0x51bf334 
0x70ef407e18 	0xc1e18 		rev w10, w10 ; x10= 0x51bf334 -> 0x34f31b05 
0x70ef407e1c 	0xc1e1c 		str w10, [x0, # 8 ] ; x0= 0x714f36da30 -> 0x714f36da30 , x10= 0x34f31b05 -> 0x34f31b05 
0x70ef407e20	0xc1e20 		ldr w10, [x1, # 0xc ] ; x1= 0x70e8016c40 -> 0x70e8016c40 , x10= 0x34f31b05 - > 0xe45b9d7a 
0x70ef407e24 	0xc1e24 		rev w10, w10 ;
```

key: f1 59 33 76 76 6e a9 8d 34 f3 1b 05 7a 9d 5b e4

As mentioned in the previous article on general algorithm, the key length of aes is related to the number of rounds. Pseudocode here can also be determined.

```js
switch ( a3 )
{
    case 0x20u:
    case 0x18u:
    case 0x10u:
    a3=x2=16. Basically determine the key16 bit, and 128 mode.

    v9 = *(_DWORD *)((char *)&unk_1094F8 + v5);
    v4 ^= dword_1084F8[(v8 >> 16) & 0xFF] ^ dword_1088F8[(unsigned __int16)v8 >> 8] ^ dword_108CF8[(unsigned __int8) v8] ^ dword_1090F8[v8 >> 24] ^ v9;
}
```

Looking at the source code of aes, rcon will be used when the key is expanded.  
http://git.bwing.com.cn/zhanghua/freeswitch/blob/728d960017c510c8108ce6c62cfbdd691a0c8831/libs/srtp/crypto/cipher/aes.c  

```js
expanded_key->round[i].v8[ 0 ] = aes_sbox[expanded_key->round[i ​​-1 ].v8[ 13 ]] ^ rc; 
 .rodata: 00000000001094F 8 unk_1094F8 DCB     0                 ; DATA XREF: sub_C1DE8+ 68 ↑o 
 . rodata: 00000000001094F 8 ; sub_C1DE8+ 84 ↑o ... 
 .rodata: 00000000001094F 9 DCB     0
 .rodata: 00000000001094F A DCB     0
 .rodata: 00000000001094F B DCB     1
 .rodata0: 000199C DCB     0
 .rodata: 00000000001094F D DCB     0
 .rodata: 00000000001094F E DCB     0
 .rodata: 00000000001094F F DCB     2
 .rodata: 0000000000109500                  DCB     0
 .rodata: 0000000000109501                  DCB     0
 .rodata: 0000000000109502                  DCB     0
 .rodata: 0000000000109503                  DCB     4
 .rodata : 0000000000109504                  DCB     0
 .rodata: 0000000000109505                  DCB     0
 .rodata: 0000000000109506                  DCB     0
 .rodata: 0000000000109507                  DCB     8
 .rodata: 0000000000109508                  DCB     0
 .rodata: 0000000000109509                  DCB     0
 .rodata: 000000000010950 A DCB     0
 .rodata: 000000000010950B                  DCB 0x10
 .rodata: 000000000010950 C DCB     0
 .rodata: 000000000010950D DCB     0
 .rodata: 000000000010950 E DCB     0
 .rodata: 000000000010950F                  DCB 0x20
 .rodata: 0000000000109510                  DCB     0
 .rodata: 0000000000109511                  DCB     0
 .rodata: 0000000000109512                  DCB     0
 .rodata: 0000000000109513                  DCB 0x40 ; @ 
 .rodata: 0000000000109514                  DCB     0
 .rodata : 0000000000109515                 DCB     0
 .rodata: 0000000000109516                  DCB     0
 .rodata: 0000000000109517                  DCB 0x80
 .rodata: 0000000000109518                  DCB     0
 .rodata: 0000000000109519                  DCB     0
 .rodata: 000000000010951 A DCB     0
 .rodata: 000000000010951B                  DCB 0x1B
 .rodata: 000000000010951 C DCB     0
 .rodata: 000000000010951 D DCB     0
 .rodata: 000000000010951 E DCB     0
 .rodata: 000000000010951F                  DCB 0x36 ; 6
```
The case1 branch is also taken here.

```c
void  AES_init_ctx_iv ( struct AES_ctx* ctx, const  uint8_t * key, const  uint8_t * iv)
{ KeyExpansion (ctx->RoundKey, key); memcpy (ctx->Iv, iv, AES_BLOCKLEN); }
```

The key is found, then find the offset iv (determine whether it is cbc or ecb mode.)  
It can be known that it is called by sub_C2978. Continue this line of thinking to push upwards.  

```c
.text:00000000000C6B14 ; DATA XREF: .rodata:000000000010C97C↓o 
.text:00000000000C6B14 LDP X9, X10, [X0,#8] ; jumptable 00000000000C6AF8 case 1 
.text:00000000000C6B18 MOV X0, X8 
.text:00000000000C6B1C LDR X1, [ X9,#0x10] 
.text:00000000000C6B20 LDR W2, [X9,#0xC] 
.text:00000000000C6B24 LDR X3, [X10,#0x10] 
.text:00000000000C6B28 B sub_C2978
```
 
Been chasing here: kind of like a complete aes.  
a1 = 1  

```c
signed __int64 __fastcall sub_C6B5C(int ** a1, __int64 a2, char * a3, _BYTE * a4, unsigned int a5) {
        _BYTE * v5; // x19 char *v6; // x20   __int64 v7; // x21   __int64 v8; // x23 int v9; // w24 unsigned int v10; // w25   _OWORD *v11; // x22   __int64 i; // x8   _BYTE *v13; // x19 char *v14; // x20   __int64 v15; // x21 int v16; // w8 unsigned __int64 v17; // x22 unsigned __int64 v18; // x23 signed __int64 result; // x0

        v13 = a4;
        v14 = a3;
        v15 = a2;
        v16 = ** a1;
        if (v16 == 1) // go here   {     v5 = a4;     v6 = a3;     v7 = a2; if ( a5 & 0xF )     {       result = 0xFFFFFFFF LL;     } else     {       v8 = 0LL ;       v9 = 0 ;       v10 = a5 >> 4 ;       v11 = (_OWORD *)(a2 + 488 ); while ( v9 != v10 )       { for ( i = 0LL ; i ! =

            16;
        ++i) *
    ((_BYTE * ) v11 + i) ^= v6[i];
sub_C2970(v7, (unsigned int * )(v7 + 488));
++v9;
v6 += 16;*(_OWORD * ) & v5[v8] = * v11;
v8 += 16 LL;
}
result = 0 LL;
}
}
else {
    if (v16 == 2) {
        sub_C2CA0(a2, a3, a4, a5);
    } else if (v16 = = 3) {
        sub_C2F24(a2, a3, a4, a5);

    } else {
        v17 = 0 LL;
        v18 = a5;
        while (v17 < v18) {
            sub_C224C(v15, (unsigned int * ) & v14[v17], & v13[v17]);
            v17 += 16 LL;
        }
    }
    result = 0 LL;
}
return result;
}
```
```c
static void XorWithIv(uint8_t * buf,
        const uint8_t * Iv) {
        uint8_t i;
        for (i = 0; i < AES_BLOCKLEN; ++i) // The block in AES is always 128bit no matter the key size   {     buf[i] ^= Iv[i];   } }
```
aes - cbc has the processing of plaintext buf and iv XOR, which is very suspicious here, look at the data for:

```c
(i = 0 LL; i != 16; ++i) * ((_BYTE * ) v11 + i) ^= v6[i];
```

```c
.text: 00000000000 C2A4C loc_C2A4C ; CODE XREF: sub_C6B5C -40F 8↓j 
.text: 00000000000 C2A4C LDRB W9, [X20,X8] 
.text: 
000000000000 C2A50 LDRB W10, [X22, X80 ] 002000 W10, W9 ; eor iv 
.text: 00000000000 C2A58 STRB W9, [X22,X8] 
.text: 00000000000 C2A5C ADD X8, X8, # 1

0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9= 0x35 -> 0x2a , x10= 0x1f -> 0x1f                                                          ; xa-debug aes_iv 
0x70ef408a58 	0xc2a58 strb w9 		, [x22, x8] ; x8= 0x0 - > 0x0 , x9 0x2a , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0x0 -> 0x1 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0x1-> 0x1 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x1 -> 0x1 , x9= 0x2a -> 0x47 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x1 -> 0x1 , x10= 0x1f -> 0xe1 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor w9, w10, w9 		; x9= 0x47 -> 0xa6 , x10= 0xe1 -> 0xe1 
0c2584			strb w9, [x22, x8] ; x8= 0x1 -> 0x1 , x9= 0xa6 -> 0xa6 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c add x8, x8 		, 		# 1 	; x8= 0x1 -> cmp 0x408 
0xc2	 # 0x10 	; x8= 0x2 -> 0x2 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x2 -> 0x2 , x9= 0xa6 -> 0x47 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef4	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x2 -> 0x2 , x10= 0xe1 - > 0x9 , x22= 0x714f36de90 - > 0x714f36de90 
0x70ef408a54 	0xc2a54 eor w9, w10, w9 x0 - > 0x9 		= 0x47 > 0x9 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0x2 -> 0x2 , x9= 0x4e -> 0x4e , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 0xc2 	a5c 		add x8, x8, # 1 	;0x2 -> 0x3 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0x3 -> 0x3 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x3 -> 0x3 , x9= 0x4e -> 0x47 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x3 -> 0x3 , x10= 0x9 -> 0xa4 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9=0x47 -> 0xe3 , x10= 0xa4 -> 0xa4 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0x3 -> 0x3 , x9= 0xe3 -> 0xe3 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0x3 -> 0x4 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0x4 -> 0x4 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x4 -> 0x4, x9= 0xe3 -> 0x47 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x4 -> 0x4 , x10= 0xa4 -> 0x12 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9= 0x47 -> 0x55 , x10= 0x12 -> 0x12 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0x4 -> 0x4 , x9= 0x55 -> 0x55 , x22=0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0x4 -> 0x5 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0x5 -> 0x5 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x5 -> 0x5 , x9= 0x55 -> 0x1 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x5 -> 0x5 , x10= 0x12 -> 0x52, x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9= 0x1 -> 0x53 , x10= 0x52 -> 0x52 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0x5 -> 0x5 , x9= 0x53 -> 0x53 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0x5 -> 0x6 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0x6 ->0x6 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x6 -> 0x6 , x9= 0x53 -> 0x90 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x6 -> 0x6 , x10= 0x52 -> 0x83 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor w9, w10, w9 		; x9= 0x90 -> 0x13 , x10= 0x83 -> 0x83 
0x70ef408a58			strb w9, [x22, x8] ; x8= 0x6 - > 0x6 , x9 = 0x13 -> 0x13 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c add 
x8	 		, x8 		, # 1 	; # 0x10 	; x8= 0x7 -> 0x7 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x7 -> 0x7 , x9= 0x13 -> 0xe , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef40	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x7 -> 0x7 , x10= 0x83 -> 0xf4 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, wxfxe - > 0x9 = 0 > 0xf4 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0x7 -> 0x7 , x9= 0xfa -> 0xfa , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c	 0xc2 	; x8, # 1a5c 		add x8, x0x7 -> 0x8 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0x8 -> 0x8 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x8 -> 0x8 , x9= 0xfa -> 0x18 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x8 -> 0x8 , x10= 0xf4 -> 0x18 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9=0x18 -> 0x0 , x10= 0x18 -> 0x18 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0x8 -> 0x8 , x9= 0x0 -> 0x0 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0x8 -> 0x9 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0x9 -> 0x9 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0x9 -> 0x9 , x9=0x0 -> 0xf6 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0x9 - > 0x9 , x10= 0x18 -> 0xde , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9= 0xf6 -> 0x28 , x10= 0xde -> 0xde 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0x9 - > 0x9 , x9= 0x28 -> 0x28 , x22=0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0x9 -> 0xa 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0xa -> 0xa 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0xa -> 0xa , x9= 0x28 -> 0x3d , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0xa -> 0xa , x10= 0xde -> 0x9e, x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9= 0x3d -> 0xa3 , x10= 0x9e -> 0x9e 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0xa -> 0xa , x9= 0xa3 -> 0xa3 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0xa -> 0xb 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0xb-> 0xb 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0xb - > 0xb , x9= 0xa3 -> 0x44 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0xb -> 0xb , x10= 0x9e -> 0x5 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor w9, w10, w9 		; x9= 0x44 -> 0x41 , x10= 0x5 -> 0x5 
0x2a588008			strb w9, [x22, x8] ; x8= 0xb - > 0xb , x9 = 0x41 -> 0x41 , x22= 0x714f36de90 - > 0x714f36de90 
0x70ef408a5c 	0xc2a5c add x8 		, 		x8, # 1 	; # 0x10 	; x8= 0xc -> 0xc 0x70ef408a4c 0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0xc -> 0xc , x9= 0x41 -> 0x9 , x20= 0x70e803bb20 -> 0x70e803bb20 0x70ef40
	
	
	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0xc - > 0xc , x10= 0x5 -> 0x1a , x22= 0x714f36de90 - > 0x714f36de90 
0x70ef408a54 	0xc2a54 eor w9 		, w10, w9 x1 , x9= 0x = 9 > 0x1a 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0xc -> 0xc , x9= 0x13 -> 0x13 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	;0xc -> 0xd 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0xd -> 0xd 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0xd -> 0xd , x9= 0x13 -> 0x47 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0xd -> 0xd , x10= 0x1a -> 0x96 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9=0x47 -> 0xd1 , x10= 0x96 -> 0x96 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0xd -> 0xd , x9= 0xd1 -> 0xd1 , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0xd -> 0xe 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0xe -> 0xe 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0xe -> 0xe, x9= 0xd1 -> 0xb8 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0xe -> 0xe , x10= 0x96 -> 0x9e , x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9= 0xb8 -> 0x26 , x10= 0x9e -> 0x9e 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0xe -> 0xe , x9= 0x26 -> 0x26 , x22=0x714f36de90 -> 0x714f36de90 
0x70ef408a5c 	0xc2a5c 		add x8, x8, # 1 	; x8= 0xe -> 0xf 
0x70ef408a60 	0xc2a60 		cmp x8, # 0x10 	; x8= 0xf -> 0xf 
0x70ef408a4c 	0xc2a4c ldrb 		w9, [x20, x8] ; x8= 0xf -> 0xf , x9= 0x26 -> 0x44 , x20= 0x70e803bb20 -> 0x70e803bb20 
0x70ef408a50 	0xc2a50 		ldrb w10, [x22, x8] ; x8= 0xf -> 0xf , x10= 0x9e -> 0x12, x22= 0x714f36de90 -> 0x714f36de90 
0x70ef408a54 	0xc2a54 eor 		w9, w10, w9 ; x9= 0x44 -> 0x56 , x10= 0x12 -> 0x12 
0x70ef408a58 	0xc2a58 strb 		w9, [x22, x8] ; x8= 0xf -> 0xf , x9= 0x56 -> 0x56 , x22= 0x714f36de90 -> 0x714f36de90
```
Just get `iv = 1FE109A4125283F418DE9E051A969E12`

Here is exactly 16 times, and in aes;
```c
static void XorWithIv(uint8_t * buf,
    const uint8_t * Iv) {
    uint8_t i;
    for (i = 0; i < AES_BLOCKLEN; ++i) // The block in AES is always 128bit no matter the key size
    {
        buf[i] ^= Iv[i];
    }
}
```
```c
void AES_CBC_encrypt_buffer(struct AES_ctx * ctx, uint8_t * buf, size_t length) {
    size_t i;
    uint8_t * Iv = ctx -> Iv;
    for (i = 0; i < length; i += AES_BLOCKLEN) {
        XorWithIv(buf, Iv);
        Cipher((state_t * ) buf, ctx -> RoundKey);
        Iv = buf;
        buf += AES_BLOCKLEN;
    } /* store Iv in ctx for next call */
    memcpy(ctx -> Iv, Iv, AES_BLOCKLEN);
}

// See how many groups there are here;
```

search: 0xc2a54. A total of 160 groups of 160/16=10. Exactly 10 rounds.   
See if aes can decrypt   
and solve it.  


```txt
35 47 47 47 47 01 90 0e 18 f6 3d 44 09 47 b8 44 48 f3 cb 74 b0 84 a6 5a eb eb 76 62 3c ca 64 31 ab 50 4a 9e d0 e1 ee 87 5a 27 66 6 ab 6a e0 c4 e1 f5 3d 30 7c 49 c5 c3 6c 9a 15 f0 d3 05 50 82 3d 22 ac ef 49 d1 9e f0 87 8f 62 13 54 3e 1d 11 c7 0e 5a 8b a6 25 e8 6d 2f 4c b5 b7 72 9 04 69 8b 80 81 82 e7 71 54 0a bd fb dd 09 a2 0c c6 a0 aa 5f 82 46 70 1c 4d 18 c6 f3 60 a8 dc a8 b3 6c bb 37 33 ff fd c7 fd ff fd 47 fd 47 47
```

It just matches the previous buf plaintext.  
3547474747 35 is a fixed value, and 47474747 is the random value of the previous frida script hook.  

Continue to push back up to see how these data are generated, look for in the trace file

#### aes operation before encryption
```
0x70ef3baf44 0x74f44 orr x8, x8, x9 ; x8=0x100000000->0x180e900100000000, x9=0x180e900000000000->0x180e900000000000
```
01 90 0e 18 happens to be little endian. 0x180e900100000000.

```
0x70ef3baf3c 	0x74f3c 		ldr x9, [x11, w9, uxtw # 3 ] ; x9= 0x2 -> 0xe800000000000 , x11= 0x714f36f580 -> 0x714f36f580 
0x70ef3baf40 	0x74f40 		ldr x8, [x11, w8, uxtw # 3 ] ; x8= 0x1 -> 0x1800000000000000 , x11= 0x714f36f580 -> 0x714f36f580 
0x70ef3baf44 	0x74f44 		orr x8, x8, x9 ; x8= 0x1800000000000000 -> 0x180e800000000000 , x9= 0xe800000000000 -> 0xe800000000000  0x70ef3bb6bc 0x756bc lsl 		x8, x8, x11 ; x8=
  
0x3 -> 0x1800000000000000 , x11= 0x3b -> 0x3b

```
There is an lsl command here. translate to python

```py
def  lsl ( data, lsr_offset ): 
    result = (data >> ( 64 - lsr_offset)) | (data << lsr_offset) return result & 0xffffffffffffffff res = lsl( 0x3 , 0x3b ) print ( hex (res)) # 0x180000000000000 lsl x8 , x8, x11 ; x8= 0x3a -> 0xe800000000000 , x11= 0x2e -> 0x2e The summary is: ((lsl( 0x3 , 0x3b ) ^ lsl ( 0x3a , 0x2e )) ^ 0x100000000000 ) ^ 0x100000
```

It seems that there are several constants, and we will see different results in the trace.  
Move on to the next result. f6 3d 44 09  

Looking alone can find some strings.  

![pasted-19](https://user-images.githubusercontent.com/113767969/190852198-5e643f1d-03d8-489a-88ce-6172e0ece5a5.png)

These results are all XORed with a key. This key: 0xfffdc7fd  

<img width="1104" alt="pasted-20" src="https://user-images.githubusercontent.com/113767969/190852214-603104b9-6a89-4f0e-a9ef-b5b995b29a28.png">

0xfffdc7fd: The generation rules are not detailed here.   
After a little bit, you can find them in the trace file.  

In fact, there is a set of algorithms.  

```js
0x70ef3bb6a4 	0x756a4 lsl 		w8, w8, w11 ; x8= 0x47 -> 0x23800 , x11= 0xb - > 0xb                                                 ；xa-xorkey   
0x70ef3bb714 	0x75714 		sxtw x8, w8 ; x8= 0x23800 -> 0x23800 0x70ef3baf3c 0x74f3c 		ldr x9, [x11, w9, uxtw # 3 ] ; x9= 0x7 -> 0x23800 , x11= 0x714f36ddc0 -> 0x714f36ddc0 0x70ef3baf40 0x74f40 		ldr x8, [x11, w8, uxtw # 3 ] ; x8= 0x1 -> 0x47 , x11=
  	
  
	0x714f36ddc0 -> 0x714f36ddc0 
0x70ef3baf44 	0x74f44 		orr x8, x8, x9 ; x8= 0x47 -> 0x23847 , x9= 0x23800 -> 0x23800 0x70ef3bb640 0x75640 		ldr x9, [x11, w9, uxtw # 3 ] ; x9= 0x1 -> 0x23847 , x11= 0x714f36ddc0 -> 0x714f36ddc0 0x70ef3bb644 0x75644 		ldr x8, [x11, w8, uxtw # 3 ] ; x8= 0x7 -> 0x2 , x11= 0x714f36ddc0 -> 0x714f36ddc0 0x70ef36ddc0 0x70 		;
  
  	
	
	0x2 -> 0x23845 , x9= 0x23847 -> 0x23847 0x70ef3bb648 0x75648 		eor x8, x8, x9 ; x8= 0x23845 -> 0x23802 , x9= 0x47 -> 0x47 0x70ef3bb658 0x75658 		ldr x9, [x11, w9, uxtw # 3 ] ; x9= 0x1 -> 0x23802 , x11= 0x714f36ddc0 -> 0x714f36ddc0 0x70ef3bb65c 0x7565c 		ldr x8, [x11, w8, uxtw # 3 ] ; x8= 0x0 - > 0x0 , x11 = 0x714f36dddc0460x70701
  
  	
    
    	
	
	0x75660 		orr x8, x8, x9 ; x8= 0x0 -> 0x23802 , x9= 0x23802 -> 0x23802 
0x70ef3bb664 	0x75664 		mvn x8, x8 ; x8= 0x23802 -> 0xffffffffffffdc7fd
   and perform the sum of the first random number byte in ramdom, lsl operation orr operation. The final mvn operation.
```

code above.  

```py
def  get_aes_xor_key ( random_hex ): 
    split_key = int (random_hex[: 2 ], 16 ) 
    random_key = lsl(split_key, 0xb ) random_key 
    = split_key | random_key 
    num_key = lsr(split_key, 0x5 ) 
    random_key = random_key ^ num_key 
    random_key = random_key ^ split_key 
    random_key = 0x0 | random_key 
    xor_key = int ( hex ((~random_key) & 0xffffffffffffffff )[- 8 :], 16 ) return xor_key
```
Data after decryption:  

**09 c0 83 f4 b8 45 83 b5 0c 36 b3 4d 7b 5b 9d 16 14 8b a5 c1 35 99 f6 56 af b7 59 2d 1e 13 40 a7 d8 9b ac 97 1f c7 58 55 5d 39 26 3e c2 a cd bb4 ab 67 ea 0d 14 f8 af 7f fa df 53 12 8e 2c 61 0d 40 72 9d ee 93 c3 e2 ec 00 f3 a5 76 61 d8 17 90 e8 b1 4a 4a b5 67 16 f3 90 f9 96 76 47 a9 7c 7d f5 40 3c 20 f6 5f cb 3b 5f 57 98 7f b9 8d db b0 e7 3b 34 9d 57 21 6f 4e 93 46 f0 ce 00 00 00 00 00 00 80 00 b8 ba**

```àsm
0x70ef3bb648 	0x75648 		eor x8, x8, x9 ; x8= 0x73b562f3d0204222 -> 0x9c083f4b84583b5 , x9= 0x7a75e1076865c197 -> 0x7a75e1076865c197 
0x70ef3bb64c 	0x7564c 		str x8, [x11, w10, uxtw # 3 ] ; x8= 0x9c083f4b84583b5 -> 0x9c083f4b84583b5 , x10= 0x7 -> 0x7 , x11= 0x714f36dbb0 -> 0x714f36dbb0 
0x70ef3bb06c 	0x7506c 		ldr x9, [x19] ; x9= 0x7a75e1076865c197 -> 0x70ef4486b8 , x19= 0x714f36dba8 -> 0x7814
0x70ef3bb070 	0x75070 ldur 		x8, [x22, # -0x20 ] ; x8= 0x9c083f4b84583b5 -> 0x0 , x22= 0x714f36dce0 - > 0x714f36dce0 Since the length is 16 bits, divide it by 8 bytes 09 c0 83 f4 b8 45 36 b3 4 d 7b 5b 9 d 16 14 8b a5 c1 35 99 f6 56 af b7 59 2 d 1 e 13 40
  

 
   
   
  a7 
d8 9b ac 97  1f c7 58  55  
5 d 39  26  08 c2 cd bb b4 
3 a 3 e ab 67 ea 0 d 14 f8 
af 7f fa df 53  12  8 e 2 c 
61  0 d 40  72  9 d ee 93 c3 
e2 ec 00 f3 a5 76  61 d8 
17  90 e8 b1 4 a4 a b5 67  
16 f3 90 f9 96  76  47  7 c 
7 d 1 a b6 a9 f5 40  3 c 20 
 f6 5f cb 3b  5f  57  98  7f 
 b9 8 d db b0 e7 3b  34  9 d 
57  21  6f  4 e 93  46 f0 ce 
00  00  00  00  00  00  80  00
   Excluding the last group of complements, there are exactly 16 groups.16 * 8 = 128 lengths. 
  It's a bit like a symmetric algorithm, but it's actually symmetric, otherwise how to decrypt it. It may be tt's own self-defined symmetric algorithm.
```
```asm
0x70ef3bb648 	0x75648 		eor x8, x8, x9 ; x8= 0x28b2874f9c4f259a -> 0x57216f4e9346f0ce , x9= 0x7f93e8010f09d554 -> 0x7f93e8010f09d554   ;xa-eor-res 0x57216f4e9346f0ce 
0x70ef3bb64c 	0x7564c 		str x8, [x11, w10, uxtw # 3 ] ; x8= 0x57216f4e9346f0ce -> 0x57216f4e9346f0ce , x10= 0x7 -> 0x7 , x11= 0x714f36dbb0 -> 0x714f36dbb0 
0x70ef3bb06c 	0x7506c 		ldr x9, [x19] ; x9= 0x7f93e8010f09d554 -> 0x70ef4486b8 , x19= 0x7-> 0x714f36dba8 
0x70ef3bb070 	0x75070 		ldur x8, [x22, # -0x20 ] ; x8= 0x57216f4e9346f0ce -> 0x0 , x22= 0x714f36dce0 -> 0x714f36dce0
```
Here is the reverse order:  

```js
0x70ef42abb4 	0xe4bb4 ldrb 		w9, [x21, x8] ; x8= 0x0 -> 0x0 , x9= 0xda778b58e2a2834b -> 0xce , x21= 0x7146b9c7e0 -> 0x7146b9c7e0 
0x70ef42abb8 	0xe4bb8 strb 		w9, [x20, x8] ; x8= 0x0 -> 0x0 , x9 = 0xce -> 0xce , x20= 0x70e80ce900 -> 0x70e80ce900 
0x70ef42abbc 	0xe4bbc 		add x8, x8, # 1 	; x8= 0x0 -> 0x1 
0x70ef42abc0 	0xe4bc0 		cmp x19, x8 ; x8= 0x1 ->0x1 , x19= 0x80 -> 0x80 
0x70ef42abb4 	0xe4bb4 ldrb 		w9, [x21, x8] ; x8= 0x1 -> 0x1 , x9= 0xce -> 0xf0 , x21= 0x7146b9c7e0 -> 0x7146b9c7e0 
0x70ef42abb8 	0xe4bb8 strb 		w9, [x20, x8] ; x8= 0x1 -> 0x1 , x9= 0xf0 -> 0xf0 , x20= 0x70e80ce900 -> 0x70e80ce900 
0x70ef42abc 	0xe4bbc 		add x8, x8, # 1 	; x8= 0x1 -> 0x2 
0x70ef42abc0 	0xe4bc0		cmp x19, x8 ; x8= 0x2 -> 0x2 , x19= 0x80 -> 0x80 
0x70ef42abb4 	0xe4bb4 ldrb 		w9, [x21, x8] ; x8= 0x2 -> 0x2 , x9= 0xf0 -> 0x46 , x21= 0x7146b9c7e0 -> 0x7146b9c7e0 
0x70ef42abb8 	0xe4bb8 strb 		w9, [x20, x8] ; x8= 0x2 -> 0x2 , x9= 0x46 -> 0x46 , x20= 0x70e80ce900 -> 0x70e80ce900 
0x70ef42abbc 	0xe4bbc 		add x8, x8, # 1 	; x8= 0x2 ->0x3 
0x70ef42abc0 	0xe4bc0 cmp x19 		, x8 ; x8= 0x3 - > 0x3 , x19= 0x80 - > 0x80 0x70ef42abb4 
0xe4bb4 	ldrb w9 , 		[x21, x8 ] ; > 0x7146b9c7e0 
0x70ef42abb8 	0xe4bb8 strb 		w9, [x20, x8] ; x8= 0x3 -> 0x3 , x9= 0x93 -> 0x93 , x20= 0x70e80ce900 -> 0x70e80ce900 
0x70ef8 , 	xe4bbc 		# add x x 0x3 -> 0xe4bbc1 	; x8= 0x3 -> 0x4 
0x70ef42abc0 	0xe4bc0 		cmp x19, x8 ; x8= 0x4 -> 0x4 , x19= 0x80 -> 0x80 
0x70ef42abb4 	0xe4bb4 ldrb w9 		, [x21, x8] ; x8= 0x4 - > 0x4 , x9 > 0x4e , x21= 0x7146b9c7e0 -> 0x7146b9c7e0 
0x70ef42abb8 	0xe4bb8 strb 		w9, [x20, x8] ; x8= 0x4 -> 0x4 , x9= 0x4e -> 0x4e , x20= 0x70e80ce900 -> 0x70e80ce909
[ 	_ 		_ _ 	_ _ _ _ 
_ 	_ 		_ _ _ _ _ _ _ _ 
_ 	_ 		_ _ -> 0x5 , x9= 0x4e -> 0x6f , x21= 0x7146b9c7e0 -> 0x7146b9c7e0 
0x70ef42abb8 	0xe4bb8 strb 		w9, [x20, x8] ; x8= 0x5 -> 0x5 , x9= 0x6f -> 0x6f , x20=0x70e80ce900 -> 0x70e80ce900
```

So reverse the result:

```js
57  21  6f  4 e 93  46 f0 ce 
b9 8 d db b0 e7 3b  34  9 d 
f6 5f cb 3b  5f  57  98  7f  
7 d 1 a b6 a9 f5 40  3 c 20 
16 f3 90 f9 96  76  47  7 c 
17  90 e8 b1 4 a 4 a b5 67 
 e2 ec 00 f3 a5 76  61 d8
61  0 d 40  72  9 d ee 93 c3 
af 7f fa df 53  12  8 e 2 c 
3 a 3 e ab 67 ea 0 d 14 f8 
5 d 39  26  08 c2 cd bb b4 
d8 9b ac 97  1f c7 58  55 
 af b7 59  2 d 1 e 13  40 a7 
14  8b a5 c1 35 99 f6 56  
0 c 36 b3 4 d 7b  5b  9 d 16  
09 c0 83 f4 b8 45  83 b5
```
These results are obtained through many rounds of XOR, and it is too troublesome to write them all down, so just follow them yourself.

There are 8 big rounds in total, and there are 72 small rounds in the big round. 
Really cruel.  
 
 After decryption is such a byte
 ```py
 b'\x08\xd2\xa4\x80\x82\x04\x10\x02\x18\x8e\x9d\xba\xf4\x08"\x0411282\n1588093228B\x14v04.03.04-ml-androidH\x80\x90\x98@ R\x08\x00\x80\x00\x00\x00\x00\x00\x00`\xee\xdb\xc6\xae\x0cj\x06\x10n4\xa2\xb8\xc7r\x06z+ \xda6tz\n\x08\x06 \x10\xbe\xe1T\x18\xbe\xe1T\x88\x01\xee\xdb\xc6\xae\x0c\xa2\x01\x04none\xa8\x01\xe2\x05'

08d2a48082041002188e9dbaf408220431313238320a3135383830393332323842147630342e30332e30342d6d6c2d616e64726f696448809098405208008000000000000060eedbc6ae0c6a06106e34a2b8c772067a2b20da36747a0a080610bee15418bee1548801eedbc6ae0ca201046e6f6e65a801e205
 ```
 This looks like a protobuf.
 
 https://protobuf-decoder.netlify.app/ lets use this site to solve the protobuf str  
 <img width="965" alt="pasted-22" src="https://user-images.githubusercontent.com/113767969/190852324-772b9a9d-e02e-4f28-b46c-a4dfe6e4552e.png">
 
For the specific functions of these fields, you can find them on Baidu or trace them.   
There is a process of sm3 calculation in it.  

Anyway, it can be reversed in the end. 
 
```c
syntax = "proto3";

message Argus {
   uint32 magic = 1; // 0x20200929 << 1
   uint32 version = 2; // 2
   uint64 rand = 3; // rand() << 1
   string msAppID = 4; // "1233"
   optional string deviceID = 5; // "7196299929824265734" comes from the registered device function
   string licenseID = 6; // "2142840551"
   optional string appVersion = 7;
   string sdkVersionStr = 8; // "v04.04.05-ov-android"
   uint32 sdkVersion = 9; // 0x4040520 << 1
   bytes envCode = 10; // 8 zeros are enough
   uint32 platform = 11;
   uint64 createTime = 12; // x_khronos << 1
   optional bytes bodyHash = 13; // sm3(x-ss-stub)[:6]
   optional bytes queryHash = 14; // sm3(query_string)[:6]
   optional ActionRecord actionRecord = 15;
   optional string secDeviceToken = 16;// From /sdi/get_token request
   optional uint64 isAppLicense = 17; // equal to createTime
   optional bytes pskHash = 18; // hash
   optional bytes pskCalHash = 19; // hash
   string pskVersion = 20; // Before logging in, it is "none", and after logging in, it is x-bd-kmsv
   uint32 callType = 21; // 738
   optional ChannelInfo channelInfo = 23;
   optional string seed = 24; // from /ms/get_seed
   optional uint32 extType = 25; // 2, 6, 8, 10 are all possible
   optional ExtraInfo extraInfo = 26;
}

message ExtraInfo {
   uint32 algorithm = 1; // 2, 4, 6, 8, 10, 12, 14, 16 correspond to different algorithms, this number comes from /ms/get_seed
   bytes algorithmData = 2; // Use query, ss-stub, 00000001 for calculation
}

message ChannelInfo {
   string phoneInfo = 1; // Mi 10 Pro
   uint32 metasecConstant = 2; // Fixed value 16, get 8 from the address in so, and become 0x10 after shifting and XOR
   string channel = 3; // googleplay
   uint32 appVersionConstant = 4; // 0x14607000 << 1, each version is different, the same version is the same.
}

message ActionRecord {
   optional uint32 signCount = 1; // Number of times the algorithm is called, count << 1
   optional uint32 reportCount = 2; // /ri/report number of reports << 1, risk control: There is verification here. The default value of 1388734 is not acceptable when searching for products. Sometimes it is. If you use the default value, a block verification will pop up.
   optional uint32 settingCount = 3; // /mscc/common_setting reporting times << 1, default value 1388734
   optional uint32 reportFailCount = 4;
   optional uint32 reportSuccessCount = 5;
   optional uint32 actionIncremental = 6; // always remains 1 << 1
   optional uint32 appLaunchTime = 7; // app launch time << 1
}
```
