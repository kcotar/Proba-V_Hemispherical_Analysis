def fapar_regression_tree(red, nir, swr):
    def lm1():
        return -6.0128 * red + 1.8125 * nir - 1.0507 * swr + 0.6654

    def lm2():
        return -3.0557 * red + 1.1624 * nir - 1.1979 * swr + 0.7658

    def lm3():
        return -0.1008 * red + 1.7536 * nir - 1.407 * swr + 0.5746

    def lm4():
        return -0.1008 * red - 0.1488 * nir - 0.3494 * swr + 0.7894

    def lm5():
        return -0.1008 * red - 0.302 * nir - 0.3494 * swr + 0.7677

    def lm6():
        return -0.1008 * red + 1.1547 * nir - 1.9413 * swr + 0.7711

    def lm7():
        return -4.3919 * red + 1.3503 * nir - 1.361 * swr + 0.7537

    def lm8():
        return -6.2214 * red + 2.4376 * nir - 1.4163 * swr + 0.6339

    def lm9():
        return -5.6258 * red + 2.0759 * nir - 0.5864 * swr + 0.5445

    def lm10():
        return -3.5698 * red + 1.189 * nir - 1.2471 * swr + 0.7418

    def lm11():
        return -0.9265 * red + 0.8671 * nir - 0.0469 * swr + 0.6787

    def lm12():
        return -0.0579 * red + 0.9057 * nir - 2.4404 * swr + 0.9705

    def lm13():
        return -1.3831 * red + 0.2706 * nir - 0.3582 * swr + 0.9017

    def lm14():
        return 0.0308 * red - 0.6634 * nir + 0.8421 * swr + 1.0351

    def lm15():
        return 5.2484 * red - 0.0063 * nir - 1.9672 * swr + 1.1559

    def lm16():
        return -0.052 * red + 0.4787 * nir - 0.7392 * swr + 0.866

    def lm17():
        return -0.052 * red - 0.8535 * nir + 1.7688 * swr + 0.9669

    def lm18():
        return -4.1799 * red + 1.219 * nir - 0.0273 * swr + 0.5783

    def lm19():
        return -13.1783 * red + 0.8397 * nir - 0.0273 * swr + 0.7828

    def lm20():
        return -0.7739 * red - 1.999 * nir - 0.0273 * swr + 1.5637

    def lm21():
        return -0.4073 * red + 0.0656 * nir - 0.0273 * swr + 0.8936

    def lm22():
        return -0.2319 * red - 0.3504 * nir - 0.0273 * swr + 1.0511

    def lm23():
        return 2.2127 * red + 1.1012 * nir - 2.0036 * swr + 0.8237

    def lm24():
        return 1.3611 * red - 0.1006 * nir - 0.5484 * swr + 0.9968

    def lm25():
        return 0.0464 * red - 0.2621 * nir + 0.4272 * swr + 0.8992

    def lm26():
        return -2.6154 * red + 0.0191 * nir - 0.1778 * swr + 0.954

    def lm27():
        return -0.2049 * red + 0.0191 * nir - 4.2506 * swr + 1.4204

    def lm28():
        return -0.0853 * red + 0.0187 * nir - 0.0125 * swr + 0.8959

    def lm29():
        return -0.0853 * red - 0.2744 * nir + 0.7658 * swr + 0.9002

    def lm30():
        return -0.0722 * red + 0.0102 * nir - 0.0834 * swr + 0.9066

    def lm31():
        return -0.0722 * red + 1.7069 * nir - 0.1639 * swr + 0.3972

    def lm32():
        return -0.0722 * red - 0.0185 * nir + 0.0495 * swr + 0.9135

    def lm33():
        return -1.0978 * red - 0.1855 * nir + 2.752 * swr + 0.6153

    def lm34():
        return -2.933 * red - 0.3737 * nir + 4.5901 * swr + 0.4267

    def lm35():
        return -3.6206 * red + 1.007 * nir - 1.3157 * swr + 0.8214

    def lm36():
        return -0.0962 * red + 0.5077 * nir - 1.5021 * swr + 0.9525

    def lm37():
        return -4.1369 * red - 0.7268 * nir + 1.3947 * swr + 1.0373

    def lm38():
        return -3.9841 * red - 0.0358 * nir - 0.0167 * swr + 0.961

    def lm39():
        return -2.9896 * red + 1.201 * nir - 1.6879 * swr + 0.8001

    def lm40():
        return -3.9752 * red - 0.2386 * nir - 0.4461 * swr + 1.1291

    def lm41():
        return -4.0119 * red + 0.8065 * nir - 0.6637 * swr + 0.7735

    def lm42():
        return -3.1056 * red - 0.1011 * nir - 0.3332 * swr + 1.0295

    def lm43():
        return -1.3176 * red + 1.2998 * nir - 1.7022 * swr + 0.7047

    def lm44():
        return 1.1818 * red + 0.513 * nir - 0.031 * swr + 0.6059

    def lm45():
        return 0.0544 * red - 0.0295 * nir - 0.031 * swr + 0.7911

    def lm46():
        return -0.0812 * red + 0.0265 * nir - 0.0555 * swr + 0.7897

    def lm47():
        return -0.1067 * red + 1.0604 * nir - 2.2319 * swr + 0.8049

    def lm48():
        return -0.9723 * red - 0.4809 * nir - 0.0327 * swr + 1.0489

    def lm49():
        return -1.8109 * red + 1.0433 * nir - 1.3554 * swr + 0.7447

    def lm50():
        return -2.1913 * red + 0.1179 * nir - 0.4584 * swr + 0.936

    def lm51():
        return -3.3856 * red + 3.3572 * nir - 1.9452 * swr + 0.4221

    def lm52():
        return -4.7386 * red + 2.7 * nir - 0.0474 * swr + 0.2611

    def lm53():
        return -0.457 * red + 3.5854 * nir - 2.2956 * swr + 0.2139

    def lm54():
        return -4.3521 * red + 3.3629 * nir - 0.4307 * swr + 0.1917

    def lm55():
        return -3.4604 * red + 2.6021 * nir - 1.0172 * swr + 0.4151

    def lm56():
        return -2.5253 * red + 2.5467 * nir - 2.4462 * swr + 0.604

    def lm57():
        return -4.9402 * red + 3.0895 * nir - 0.0475 * swr + 0.2003

    def lm58():
        return -1.3128 * red + 1.9877 * nir - 2.0303 * swr + 0.567

    def lm59():
        return -3.1781 * red + 1.634 * nir - 0.5412 * swr + 0.4734

    def lm60():
        return -0.2409 * red + 3.0608 * nir - 2.5933 * swr + 0.2758

    def lm61():
        return -4.1017 * red + 4.0697 * nir - 1.0289 * swr + 0.1693

    def lm62():
        return -2.8038 * red + 2.7732 * nir - 1.3879 * swr + 0.3881

    def lm63():
        return -1.9086 * red + 2.5118 * nir - 1.9376 * swr + 0.4333

    def lm64():
        return -4.2083 * red + 4.096 * nir - 1.1589 * swr + 0.1855

    def lm65():
        return -1.1514 * red + 2.8564 * nir - 1.8557 * swr + 0.2782

    def lm66():
        return -2.0119 * red + 2.4333 * nir - 0.7707 * swr + 0.2132

    def lm67():
        return -4.2732 * red + 4.0651 * nir - 2.1603 * swr + 0.4929

    def lm68():
        return -0.6986 * red + 2.0754 * nir - 1.5928 * swr + 0.436

    def lm69():
        return -0.6488 * red + 1.4602 * nir - 0.0846 * swr + 0.2909

    def lm70():
        return -0.3304 * red - 0.6134 * nir - 0.0672 * swr + 1.0996

    def lm71():
        return -0.0208 * red + 0.0163 * nir - 0.1833 * swr + 0.7892

    def lm72():
        return -0.0208 * red - 0.2341 * nir - 2.0098 * swr + 1.2597

    def lm73():
        return 0.8456 * red + 0.0857 * nir - 0.3688 * swr + 0.735

    def lm74():
        return -0.0566 * red + 0.9117 * nir - 0.2842 * swr + 0.4807

    def lm75():
        return -2.527 * red + 1.9771 * nir - 3.1293 * swr + 1.0174

    def lm76():
        return -0.6734 * red + 1.7867 * nir - 1.8834 * swr + 0.538

    def lm77():
        return -0.5329 * red + 1.0826 * nir - 1.3773 * swr + 0.6525

    def lm78():
        return -0.0098 * red + 0.5722 * nir - 1.2545 * swr + 0.7838

    def lm79():
        return -2.0797 * red + 1.0568 * nir - 1.045 * swr + 0.6699

    def lm80():
        return -0.0202 * red + 1.4165 * nir - 1.6138 * swr + 0.4957

    def lm81():
        return -0.1234 * red + 1.9691 * nir - 2.1302 * swr + 0.4615

    def lm82():
        return -4.2795 * red + 5.2579 * nir - 0.2601 * swr - 0.361

    def lm83():
        return -0.2258 * red + 1.2152 * nir - 2.3191 * swr + 0.7993

    def lm84():
        return -4.4169 * red + 2.0649 * nir + 0.46 * swr + 0.1878

    def lm85():
        return -5.0593 * red + 3.4492 * nir - 0.331 * swr + 0.2043

    def lm86():
        return -1.2744 * red + 1.0928 * nir - 0.851 * swr + 0.5165

    def lm87():
        return -2.8812 * red + 2.2959 * nir - 0.8044 * swr + 0.3735

    def lm88():
        return -4.1935 * red + 3.3526 * nir - 0.5321 * swr + 0.1571

    def lm89():
        return -2.0655 * red + 1.7933 * nir - 0.3225 * swr + 0.112

    def lm90():
        return -0.3445 * red + 0.5094 * nir - 0.2386 * swr + 0.353

    def lm91():
        return -2.1092 * red + 3.5957 * nir - 0.8852 * swr - 0.113

    def lm92():
        return -3.973 * red + 3.7871 * nir - 0.078 * swr - 0.1846

    def lm93():
        return -3.0767 * red + 3.6253 * nir - 1.0766 * swr + 0.0709

    def lm94():
        return -0.8515 * red + 0.8762 * nir - 0.9327 * swr + 0.5653

    def lm95():
        return -3.2282 * red + 3.342 * nir - 1.5559 * swr + 0.4004

    def lm96():
        return -1.5533 * red + 0.8635 * nir - 1.5465 * swr + 0.9656

    def lm97():
        return -4.0027 * red + 2.8495 * nir - 0.0199 * swr + 0.0589

    def lm98():
        return -2.5597 * red + 1.6898 * nir - 1.0352 * swr + 0.6249

    def lm99():
        return -3.5183 * red + 2.0561 * nir - 0.1795 * swr + 0.2833

    def lm100():
        return -3.4056 * red + 3.4099 * nir - 0.9416 * swr + 0.1656

    def lm101():
        return -2.2443 * red + 1.9667 * nir - 0.3838 * swr + 0.1316

    def lm102():
        return -2.4213 * red + 2.2576 * nir - 0.8938 * swr + 0.3285

    def lm103():
        return -2.0772 * red + 2.1624 * nir - 0.988 * swr + 0.3106

    def lm104():
        return -1.5287 * red + 1.5285 * nir - 0.3804 * swr + 0.0982

    if red <= 0.059:
        if nir <= 0.254:
            if red <= 0.037:
                if nir <= 0.17:
                    return lm1()
                if nir > 0.17:
                    if red <= 0.02:
                        return lm2()
                    if red > 0.02:
                        if red <= 0.027:
                            if swr <= 0.145:
                                return lm3()
                            if swr > 0.145:
                                if nir <= 0.223:
                                    if nir <= 0.215:
                                        return lm4()
                                    if nir > 0.215:
                                        return lm5()
                                if nir > 0.223:
                                    return lm6()
                        if red > 0.027:
                            return lm7()
            if red > 0.037:
                if nir <= 0.179:
                    if nir <= 0.146:
                        return lm8()
                    if nir > 0.146:
                        return lm9()
                if nir > 0.179:
                    return lm10()
        if nir > 0.254:
            if red <= 0.025:
                if red <= 0.017:
                    if swr <= 0.155:
                        if nir <= 0.295:
                            if swr <= 0.135:
                                return lm11()
                            if swr > 0.135:
                                return lm12()
                        if nir > 0.295:
                            if red <= 0.011:
                                if swr <= 0.142:
                                    if nir <= 0.331:
                                        return lm13()
                                    if nir > 0.331:
                                        return lm14()
                                if swr > 0.142:
                                    return lm15()
                            if red > 0.011:
                                if swr <= 0.146:
                                    if nir <= 0.336:
                                        return lm16()
                                    if nir > 0.336:
                                        return lm17()
                                if swr > 0.146:
                                    if nir <= 0.35:
                                        if nir <= 0.333:
                                            if nir <= 0.319:
                                                return lm18()
                                            if nir > 0.319:
                                                if nir <= 0.322:
                                                    return lm19()
                                                if nir > 0.322:
                                                    return lm20()
                                        if nir > 0.333:
                                            return lm21()
                                    if nir > 0.35:
                                        return lm22()
                    if swr > 0.155:
                        if nir <= 0.414:
                            if nir <= 0.331:
                                return lm23()
                            if nir > 0.331:
                                return lm24()
                        if nir > 0.414:
                            return lm25()
                if red > 0.017:
                    if swr <= 0.142:
                        if nir <= 0.275:
                            if swr <= 0.13:
                                return lm26()
                            if swr > 0.13:
                                return lm27()
                        if nir > 0.275:
                            if red <= 0.02:
                                if nir <= 0.302:
                                    return lm28()
                                if nir > 0.302:
                                    return lm29()
                            if red > 0.02:
                                if nir <= 0.305:
                                    if swr <= 0.136:
                                        return lm30()
                                    if swr > 0.136:
                                        return lm31()
                                if nir > 0.305:
                                    if nir <= 0.337:
                                        return lm32()
                                    if nir > 0.337:
                                        if nir <= 0.369:
                                            return lm33()
                                        if nir > 0.369:
                                            return lm34()
                    if swr > 0.142:
                        if nir <= 0.327:
                            return lm35()
                        if nir > 0.327:
                            if swr <= 0.165:
                                if nir <= 0.374:
                                    return lm36()
                                if nir > 0.374:
                                    return lm37()
                            if swr > 0.165:
                                return lm38()
            if red > 0.025:
                if red <= 0.036:
                    if nir <= 0.33:
                        return lm39()
                    if nir > 0.33:
                        if swr <= 0.167:
                            return lm40()
                        if swr > 0.167:
                            if nir <= 0.359:
                                return lm41()
                            if nir > 0.359:
                                return lm42()
                if red > 0.036:
                    if nir <= 0.317:
                        return lm43()
                    if nir > 0.317:
                        if swr <= 0.186:
                            if swr <= 0.164:
                                if nir <= 0.386:
                                    return lm44()
                                if nir > 0.386:
                                    return lm45()
                            if swr > 0.164:
                                if nir <= 0.363:
                                    if red <= 0.048:
                                        return lm46()
                                    if red > 0.048:
                                        return lm47()
                                if nir > 0.363:
                                    return lm48()
                        if swr > 0.186:
                            if nir <= 0.367:
                                return lm49()
                            if nir > 0.367:
                                return lm50()
    if red > 0.059:
        if swr <= 0.308:
            if nir <= 0.287:
                if red <= 0.101:
                    if nir <= 0.202:
                        if nir <= 0.172:
                            if red <= 0.08:
                                if swr <= 0.166:
                                    return lm51()
                                if swr > 0.166:
                                    return lm52()
                            if red > 0.08:
                                if swr <= 0.186:
                                    return lm53()
                                if swr > 0.186:
                                    return lm54()
                        if nir > 0.172:
                            if red <= 0.078:
                                return lm55()
                            if red > 0.078:
                                if swr <= 0.204:
                                    return lm56()
                                if swr > 0.204:
                                    return lm57()
                    if nir > 0.202:
                        if swr <= 0.202:
                            return lm58()
                        if swr > 0.202:
                            return lm59()
                if red > 0.101:
                    if nir <= 0.24:
                        if red <= 0.124:
                            if nir <= 0.205:
                                if swr <= 0.216:
                                    return lm60()
                                if swr > 0.216:
                                    return lm61()
                            if nir > 0.205:
                                return lm62()
                        if red > 0.124:
                            if swr <= 0.263:
                                return lm63()
                            if swr > 0.263:
                                return lm64()
                    if nir > 0.24:
                        if red <= 0.149:
                            if swr <= 0.243:
                                return lm65()
                            if swr > 0.243:
                                return lm66()
                        if red > 0.149:
                            return lm67()
            if nir > 0.287:
                if swr <= 0.236:
                    if swr <= 0.2:
                        if nir <= 0.339:
                            if swr <= 0.183:
                                return lm68()
                            if swr > 0.183:
                                return lm69()
                        if nir > 0.339:
                            if swr <= 0.175:
                                return lm70()
                            if swr > 0.175:
                                if red <= 0.091:
                                    if nir <= 0.356:
                                        return lm71()
                                    if nir > 0.356:
                                        return lm72()
                                if red > 0.091:
                                    if red <= 0.157:
                                        if swr <= 0.187:
                                            return lm73()
                                        if swr > 0.187:
                                            return lm74()
                                    if red > 0.157:
                                        return lm75()
                    if swr > 0.2:
                        if nir <= 0.335:
                            return lm76()
                        if nir > 0.335:
                            if nir <= 0.372:
                                return lm77()
                            if nir > 0.372:
                                return lm78()
                if swr > 0.236:
                    if nir <= 0.344:
                        if red <= 0.094:
                            return lm79()
                        if red > 0.094:
                            if red <= 0.14:
                                return lm80()
                            if red > 0.14:
                                if red <= 0.19:
                                    return lm81()
                                if red > 0.19:
                                    return lm82()
                    if nir > 0.344:
                        return lm83()
        if swr > 0.308:
            if swr <= 0.418:
                if nir <= 0.322:
                    if red <= 0.157:
                        if nir <= 0.267:
                            if red <= 0.128:
                                return lm84()
                            if red > 0.128:
                                return lm85()
                        if nir > 0.267:
                            if red <= 0.141:
                                return lm86()
                            if red > 0.141:
                                return lm87()
                    if red > 0.157:
                        if nir <= 0.292:
                            if red <= 0.183:
                                return lm88()
                            if red > 0.183:
                                return lm89()
                        if nir > 0.292:
                            if red <= 0.192:
                                if swr <= 0.376:
                                    if swr <= 0.339:
                                        return lm90()
                                    if swr > 0.339:
                                        return lm91()
                                if swr > 0.376:
                                    return lm92()
                            if red > 0.192:
                                return lm93()
                if nir > 0.322:
                    if red <= 0.18:
                        return lm94()
                    if red > 0.18:
                        if nir <= 0.357:
                            return lm95()
                        if nir > 0.357:
                            return lm96()
            if swr > 0.418:
                if red <= 0.257:
                    if red <= 0.205:
                        if nir <= 0.325:
                            return lm97()
                        if nir > 0.325:
                            return lm98()
                    if red > 0.205:
                        if nir <= 0.364:
                            if red <= 0.224:
                                if nir <= 0.336:
                                    return lm99()
                                if nir > 0.336:
                                    return lm100()
                            if red > 0.224:
                                return lm101()
                        if nir > 0.364:
                            return lm102()
                if red > 0.257:
                    if swr <= 0.501:
                        return lm103()
                    if swr > 0.501:
                        return lm104()

    return float('Nan')
