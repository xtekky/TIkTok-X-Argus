# Argus main function

class Argus:
    def __init__(self) -> None:
        return

    double = None
    __int64 = int
    __m128 = int

    def generate_xargus(
        self,
        a1: __int64,
        a2: __m128,
        a3: __m128,
        a4: __m128,
        a5: __m128,
        a6: double,
        a7: double,
        a8: __m128,
        a9: __m128,
    ) -> int:

        dest: int
        off_A3F30: int
        v18: int
        v19: int
        v20: int
        v21: int

        v45: int
        v47: int
        v48: int
        v49: int
        v50: int
        v51: int
        v52: int
        v53: int
        v54: int
        v55: int
        v57: int
        v58: int
        v59: int
        v60: int
        v61: int
        v62: int
        v63: int
        v64: int
        v65: int
        v66: int
        v68: int
        v69: int
        v70: int
        v71: int
        v72: int
        v73: int
        v74: int
        v75: int
        v78: int
        v79: int
        v80: int
        v81: int
        v82: int
        v83: int
        v84: int
        v85: int
        v86: int
        v87: int
        v88: int
        v89: int
        v91: int
        v92: int
        v93: int
        v94: int
        v95: int
        v96: int
        v97: int
        v98: int
        v99: int
        v100: int
        v103: int
        v104: int
        v105: int
        v106: int
        v107: int
        v108: int
        v109: int
        v110: int
        v111: int

        v139: int
        v140: int
        v141: int
        v142: int
        v143: int
        v144: int
        v144: int
        v145: int
        v146: int
        v147: int
        v148: int
        v149: int
        v150: int
        v151: int

        v104: int
        dword_0: int
        xmmword_A4020: int
        off_A4010: int

        v152 = _readfsqword(0x28)
        v9 = a1
        v10 = a1 + 8
        v70 = a1 + 16
        v68 = a1 + 24
        v73 = a1 + 32
        v74 = a1 + 40
        v75 = a1 + 48
        v72 = a1 + 56
        ptr = a1 + 72
        v77 = a1 + 80

        memcpy(dest, off_A3F30, 0xE0)
        v113 = 538970409
        self.more_mutex2(v100, v10)
        v116 = self.do_some_mutex3(v100.m128i_i64) + 16
        self.do_some_mutex(v100)
        v114 = 1
        v115 = rand_from_time()
        self.mutex_rwlock(v111, v10)

        if self.mutex_and_calc4(v111.m128i_i64):

            v11 = v109
            self.mutex_rwlock2(v109, v10)
            v12 = 1
            v13 = 0
        else:
            v11 = v110
            self.mutex_rwlock(v110, v10)
            v13 = 1
            v12 = 0
        v117 = self.do_some_mutex(v11.m128i_i64) + 16

        if v12:
            self.do_some_mutex(v109)
        if v13:
            self.do_some_mutex(v110)

        v14 = self.sub_43094(v10)
        v15 = 0

        if not v14:
            v15 = v9

        v132 = v15
        v16 = v10 + 10
        self.mutex_unlock_lock(v100, v16)
        v17 = self.mutex_unlock_lock2(v100.m128i_i64)
        self.mult1(v108, v17)
        self.mult2(v100)

        v118 = self.do_some_mutex3(v108) + 16
        self.mult3(v107, a2.m128_u64, a3, a4, a5, v18, v19, a8, a9)
        v119 = self.do_some_mutex3(v107.m128i_i64) + 16
        version_string = self.get_version_string()
        v120 = self.str_sig(a2, a3, a4, a5, v20, v21, a8, a9, v107, v17)
        v22 = v73 + 16
        v122 = v73 + 12
        v123 = v22
        v124 = 0
        v125 = v9
        self.sm3_hash(v105, v70)

        v126 = 6
        v127 = v106
        self.sm3_hash(v103, v68)
        v128 = 6
        v129 = v104
        v102 = dword_0
        v101 = xmmword_A4020
        v100 = off_A4010
        v23 = self.UND_pthread2(v103, v68)
        v24 = self.sub_45AF4(v23)

        self.malloc_shit(v150, "sign")
        # DWORD2(v101) = UND_pthread3(v24, v150)
        self.calc_smh3(v150)
        v25 = self.UND_pthread2(v150, v150)
        v26 = self.sub_45AF4(v25)
        self.malloc_shit(v150, "setting")
        # LODWORD(v102) = UND_pthread3(v26, v150)
        self.calc_smh3(v150)
        v27 = self.UND_pthread2(v150, v150)
        v28 = self.sub_45AF4(v27)
        self.malloc_shit(v150, "report")
        # HIDWORD(v101) = UND_pthread3(v28, v150)
        self.calc_smh3(v150)
        v130 = v100
        v131 = v74 + 16
        v138 = a1 + 64
        self.maybe_malloc_check(v97)
        self.maybe_malloc_check(v94)
        if self.calc7(v75) or self.calc7(v72):

            v137 = "none"

        else:

            v137 = v72 + 16
            self.calc_and_mutex(v150, v75, 0)
            v29 = self.do_some_mutex2(v150)
            self.calc_cool3_0(v97, v29)
            self.do_some_mutex(v150)
            v133 = v98
            v134 = v99
            self.call_more_calc1(v147, v68, v70)
            self.call_more_calc1(v150, v147, v72)
            self.calc_smh3(v147)
            self.sm3_hash(v147, v150)
            self.calc_cool3_0(v94, v147)
            self.calc_smh3(v147)
            v135 = v95
            v136 = v96
            self.calc_smh3(v150)

        v30 = self.j_UND_calc_smh6(dest)
        self.calc_checks2(v91, 0, v30)
        self.j_UND_calc_smh7(dest, v93)
        v31 = rand_from_time()
        v71 = HIWORD(v31)
        v90 = HIWORD(v31)
        self.mutex_unlock_lock(v144, v16)
        v32 = self.mutex_unlock_lock2(v144.m128i_i64)
        self.malloc_shit(v150, "sign_key")
        self.sub_8334E(v146, v32, v150)
        v33 = self.do_some_mutex2(v146)
        self.sub_7F908(v147, v33)
        v34 = self.do_some_mutex2(v147)
        self.calc_smh1(v87, v34)
        self.do_some_mutex(v147)
        self.do_some_mutex(v146)
        self.calc_smh3(v150)
        self.mult2(v144)
        self.calc_checks(v150, v89, 16)
        self.calc_and_mutex(v147, v150, 0)
        v35 = self.do_some_mutex2(v147)
        self.calc_smh1(v86, v35)
        self.do_some_mutex(v147)
        self.calc_smh3(v150)
        self.calc_checks(v150, v89 + 16, 16)
        self.calc_and_mutex(v147, v150, 0)
        v36 = self.do_some_mutex2(v147)
        self.calc_smh1(v85, v36)
        self.do_some_mutex(v147)
        self.calc_smh3(v150)
        v69 = v31
        # LODWORD(v150) = v31
        self.calc_checks(v146, v150, 4)
        self.call_more_calc1(v147, v87, v146)
        self.call_more_calc1(v150, v147, v87)
        self.sm3_hash(v83, v150)
        self.calc_smh3(v150)
        self.calc_smh3(v147)
        self.calc_smh3(v146)
        v82 = self.calc_tyhon(v89, v88)
        self.maybe_malloc_check(v81)
        self.calc_smh1(v139, v83)
        if v84 <= 31:
            self.calc_checks2(v150, 0, 32 - v84)
            self.calc_1_caller(v139, v150)
            self.calc_smh3(v150)

        v37 = v93
        v38 = v92
        v39 = v140
        v40 = 0
        self.calc_checks2(v147, 0, 576)
        self.calc_checks(v146, v39, 32)
        self.calc_checks(v144, v37, v38)
        v41 = v146[2]
        v42 = v148
        v151 = 0
        v150 = 0

        while v40 != 4:
            v150[v40] = v41[8 * v40]
            v40 += 1

        v42 = v150  # list()??
        v150 = 0
        v151 = 0
        for i in range(0, 71):
            v44 = v151[1]
            v45 = v150
            for j in range(1, 4):
                v149[j] = v150[j]
            v47 = v45[1] ^ v44 << 61
            # v151 = v47 ^ ((0x3DC94C3A046D678B >> (i % 0x3E)) & 1 | 0xFFFFFFFFFFFFFFFC) ^ v45 ^ v47 >> 1
            # .c -> *(&v151 + 1) = v47 ^ ((0x3DC94C3A046D678BuLL >> (i % 0x3Eu)) & 1 | 0xFFFFFFFFFFFFFFFCLL) ^ v45 ^ __ROR8__(v47, 1)
            # v151[1] = v47 ^ ((0x3DC94C3A046D678BuLL >> (i % 0x3Eu)) & 1 | 0xFFFFFFFFFFFFFFFCLL) ^ v45 ^ __ROR8__(v47, 1)

            v151[1] = (
                v47
                ^ ((0x3DC94C3A046D678B >> (i % 0x3E)) & 1 | 0xFFFFFFFFFFFFFFFC)
                ^ v45
                ^ __ROR8__(v47, 1)
            )
            v42[i + 1] = v150

        v48 = 16 * ((v144.m128i_i32[3] + 16) / 16)
        v49 = v48 - v144.m128i_i8[12]

        self.maybe_malloc_check(v150)
        self.calc_smh2(v150, v49, v49)
        self.calc_1_caller(v144, v150)
        v50 = 0
        self.calc_checks2(v141, 0, v48)
        v51 = v148
        v52 = v145
        v53 = v143

        while v50 < v48:
            v54 = v52[v50]
            v55 = v52[v50 + 8]
            for k in range(0, 72):
                v57 = v55
                v55 = (
                    v51[8 * k]
                    ^ ((v55 << 1) | (v55 >> 7)) & ((v55 << 8) | (v55 >> 8))
                    ^ v54
                    ^ ((v55 << 2) | (v55 >> 6))
                )
                v54 = v57
            v53[v50] = v54
            v53[v50 + 8] = v55
            v50 += 16

        v58 = malloc(v48)
        v59 = v142
        v60 = v142
        memcpy(v58, v53, v142)
        self.calc_smh3(v141)
        self.calc_smh3(v150)
        self.calc_smh3(v144)
        self.calc_smh3(v146)
        self.calc_smh3(v147)

        if v58 and v59 > 0:
            self.calc_smh2(v81, v59, 0x20)
            memcpy(v81[2], v58, v60)
        # elif not v58:
        #     goto LABEL_36
        # free(v58)
        # LABEL_36:

        if v58:
            free(v58)

        self.calc_smh3(v139)
        self.call_more_calc1(v150, v73, v81)
        # HIDWORD(v149) = _byteswap_ulong(calc_tyhon(v90, 2))

        v61 = 0
        self.calc_checks2(v147, 0, v150 >> 32)
        v62 = v150 >> 32
        v63 = 0

        if v150 >= 0:
            v63 = v150 >> 32
        while True:
            v62 -= 1
            if v63 == v61:
                break
            v148[v61] = v151[v62] ^ v149[v61 & 3 + 4]
            v61 += 1

        v80 = 0x1800000000000000
        v64 = (((v104 & 0x3F) | 0x6000) << 46) | ((v106 & 0x3F) << 40)
        v80 = v64 | rand_from_time()

        self.calc_checks(v139, v82, 1)
        self.calc_checks(v79, v80, 8)
        self.call_more_calc1(v141, v139, v79)
        self.call_more_calc1(v144, v141, v147)
        self.sub_53A5C(v78, v71)
        self.call_more_calc1(v146, v144, v78)
        self.calc_smh3(v78)
        self.calc_smh3(v144)
        self.calc_smh3(v141)
        self.calc_smh3(v79)
        self.calc_smh3(v139)

        v139 = [1]
        self.sub_7FA8C(v141, v146, v86, v85, v139)
        v65 = self.do_some_mutex2(v141)
        self.calc_smh1(v144, v65)
        self.do_some_mutex(v141)
        self.sub_53A5C(v79, v69)
        self.call_more_calc1(v139, v79, v144)
        self.does_something_b64(v78, v139)
        v66 = self.do_some_mutex2(v78)
        self.calc_smh1(v141, v66)
        self.do_some_mutex(v78)
        self.calc_smh3(v139)
        self.calc_smh3(v79)

        # import ctypes

        # libc = ctypes.CDLL('libc.so.6')

        # buffer = ctypes.c_char_p()
        # r = libc.asprintf(ctypes.byref(buffer), b"The total is %d\n", 5+8)

        # libc.puts(buffer)
        # libc.printf(b"%d characters generated\n", r)

        ptr = "%s" % "X-Argus"
        v77 = "%s" % v143

        self.calc_smh3(v141)
        self.calc_smh3(v144)
        self.calc_smh3(v146)
        self.calc_smh3(v147)
        self.calc_smh3(v150)
        self.calc_smh3(v81)
        self.calc_smh3(v83)
        self.calc_smh3(v85)
        self.calc_smh3(v86)
        self.calc_smh3(v87)
        self.calc_smh3(v91)
        self.calc_smh3(v94)
        self.calc_smh3(v97)
        self.calc_smh3(v103)
        self.calc_smh3(v105)
        self.do_some_mutex(v107)
        self.do_some_mutex(v108)

        return _readfsqword(0x28)
