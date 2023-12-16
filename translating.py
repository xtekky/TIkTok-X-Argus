# translating from .c to .py

# note that *(a2+ 16)  is equal to a2[16] 
# -> *(x + y) = x[y]

# uLL = 0 so 0x18uLL = 0x180 in .py

# undefined .c functions (some not implemented yet, some unique .c)

def __readfsqword(): return
def malloc(): return
def smh_malloc(): return
def calc_checks(): return
def free(): return
def do_some_mutex4(): return

# .c types in python
# None = undefined type
_QWORD = None
__int64: int
__fastcall: None
_BYTE: bytearray = []
void: None

# .c vars in python
byte_165A0: _BYTE = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47] # weak


#----- (000000000007F846) ----------------------------------------------------
def does_something_b64(a1: _QWORD, a2: __int64) ->  _QWORD *__fastcall:
    
    # undefined yet
    v7: list = []
    
    # define vars
    v2: __int64 # r15
    v3: _BYTE   # r12
    v4: void    # rbx
    v5: __int64 # rsi
    v7[7]: __int64 # [rsp+0h] [rbp-38h] BYREF

    v7[1] = __readfsqword(0x28)
    v7[0] = 0 # 0LL = 0
    
    v7[1] = __readfsqword(0x28)
    v7[0] = 0
    base64_encode(0, 0, v7, a2[16] , a2[12] )
    v2 = v7[0]
    
    if v7[0]:
        v3 = malloc(v7[0])
        base64_encode(v3, v2, v7, a2[16] , a2[12])
        # v4 = smh_malloc(0x18uLL) uLL = 0 so 0x18uLL = 0x180 in .py
        v4 = smh_malloc(0x180)
        calc_checks(v4, v3, v7[0])
        free(v3)
        v5 = v4

    else:
        v5 = 0

    do_some_mutex4(a1, v5)
    return a1

# implementing base64_encode in .py
# ----- (00000000000736D2) ----------------------------------------------------
def base64_encode(a1: _BYTE, a2: __int64, a3: __int64, a4: __int64 , a5: __int64) ->  _QWORD *__fastcall:
    if a5:
        if (a5 / 3 - ((a5 % 3 == 0) - 1)) >> 62:
            a3 = -1
            return 4294967254
        v6 = 4 * (a5 / 3 - ((a5 % 3 == 0) - 1)) + 1
        if not a1 or v6 > a2:
            a3 = v6
            return 4294967254
        v7 = 1
        v8 = a1
        while v7 - 1 < 3 * (a5 / 3):
            v9 = a4 + v7 - 1
            v10 = a4 + v7
            v11 = a4 + v7 + 1
            v8 = byte_165A0[v9 >> 2]
            v8[1] = byte_165A0[(v10 >> 4) | (16 * v9) & 0x30]
            v8[2] = byte_165A0[4 * (v10 & 0xF) + (v11 >> 6)]
            v8[3] = byte_165A0[v11 & 0x3F]
            v8 += 4
            v7 += 3
        if v7 - 1 < a5:
            v13 = a4 + v7 - 1
            v14 = 0
            if v7 < a5:
                v14 = a4 + v7
            v8 = byte_165A0[v13 >> 2]
            v8[1] = byte_165A0[(v14 >> 4) | (16 * v13) & 0x30]
            v15 = 61
            if v7 < a5:
                v15 = byte_165A0[4 * (v14 & 0xF)]
            v8[2] = v15
            v8[3] = 61
            v8 += 4
        a3 = v8 - a1
        v8 = 0
    else:
        a3 = 0
    return 0

# .c code


# //----- (00000000000736D2) ----------------------------------------------------
# __int64 __fastcall base64_encode(_BYTE *a1, unsigned __int64 a2, unsigned __int64 *a3, __int64 a4, unsigned __int64 a5)
# {
#   unsigned __int64 v6; // rdx
#   unsigned __int64 v7; // r15
#   _BYTE *v8; // r14
#   unsigned __int8 v9; // si
#   unsigned __int64 v10; // rax
#   unsigned __int64 v11; // rdx
#   unsigned __int64 v13; // rdx
#   unsigned int v14; // er10
#   char v15; // cl

#   if ( a5 )
#   {
#     if ( (a5 / 3 - ((a5 % 3 == 0) - 1LL)) >> 62 )
#     {
#       *a3 = -1LL;
#       return 4294967254LL;
#     }
#     v6 = 4 * (a5 / 3 - ((a5 % 3 == 0) - 1LL)) + 1;
#     if ( !a1 || v6 > a2 )
#     {
#       *a3 = v6;
#       return 4294967254LL;
#     }
#     v7 = 1LL;
#     v8 = a1;
#     while ( v7 - 1 < 3 * (a5 / 3) )
#     {
#       v9 = *(a4 + v7 - 1);
#       v10 = *(a4 + v7);
#       v11 = *(a4 + v7 + 1);
#       *v8 = byte_165A0[v9 >> 2];
#       v8[1] = byte_165A0[(v10 >> 4) | (16 * v9) & 0x30];
#       v8[2] = byte_165A0[4 * (v10 & 0xF) + (v11 >> 6)];
#       v8[3] = byte_165A0[v11 & 0x3F];
#       v8 += 4;
#       v7 += 3LL;
#     }
#     if ( v7 - 1 < a5 )
#     {
#       v13 = *(a4 + v7 - 1);
#       v14 = 0;
#       if ( v7 < a5 )
#         v14 = *(a4 + v7);
#       *v8 = byte_165A0[v13 >> 2];
#       v8[1] = byte_165A0[(v14 >> 4) | (16 * v13) & 0x30];
#       v15 = 61;
#       if ( v7 < a5 )
#         v15 = byte_165A0[4 * (v14 & 0xF)];
#       v8[2] = v15;
#       v8[3] = 61;
#       v8 += 4;
#     }
#     *a3 = v8 - a1;
#     *v8 = 0;
#   }
#   else
#   {
#     *a3 = 0LL;
#   }
#   return 0LL;
# }



# _QWORD *__fastcall does_something_b64(_QWORD *a1, __int64 a2)
# {
#   unsigned __int64 v2; // r15
#   _BYTE *v3; // r12
#   void *v4; // rbx
#   __int64 v5; // rsi
#   unsigned __int64 v7[7]; // [rsp+0h] [rbp-38h] BYREF

#   v7[1] = __readfsqword(0x28u);
#   v7[0] = 0LL;
#   base64_encode(0LL, 0LL, v7, a2[16] , a2[16] );
#   v2 = v7[0];
#   if ( v7[0] )
#   {
#     v3 = malloc(v7[0]);
#     base64_encode(v3, v2, v7, a2[16] , a2[16] );
#     v4 = smh_malloc(0x18uLL);
#     calc_checks(v4, v3, v7[0]);
#     free(v3);
#     v5 = v4;
#   }
#   else
#   {
#     v5 = 0LL;
#   }
#   do_some_mutex4(a1, v5);
#   return a1;
# }
