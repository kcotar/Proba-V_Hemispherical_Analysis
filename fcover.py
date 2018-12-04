def fcover_regression_tree(red, nir, swr):
    def lm1():
        return -11.1873 * red + 1.5544 * nir + 1.5089 * swr + 0.3383

    def lm2():
        return -3.4221 * red + 1.3576 * nir - 0.2228 * swr + 0.3626

    def lm3():
        return -11.4519 * red + 2.9736 * nir + 0.4769 * swr + 0.2387

    def lm4():
        return -4.0937 * red + 2.2689 * nir - 0.2354 * swr + 0.2573

    def lm5():
        return -3.0595 * red + 1.8312 * nir - 0.6835 * swr + 0.5037

    def lm6():
        return -13.0264 * red + 1.646 * nir - 0.1174 * swr + 0.5894

    def lm7():
        return -0.195 * red + 2.0258 * nir + 0.8388 * swr + 0.2217

    def lm8():
        return -6.2407 * red + 2.5135 * nir - 0.1189 * swr + 0.263

    def lm9():
        return -0.0914 * red + 3.2612 * nir - 2.5093 * swr + 0.2827

    def lm10():
        return -3.5936 * red + 3.0121 * nir - 1.3453 * swr + 0.243

    def lm11():
        return -3.3277 * red + 2.272 * nir - 1.2261 * swr + 0.355

    def lm12():
        return -3.73 * red + 2.8726 * nir - 0.6097 * swr + 0.1899

    def lm13():
        return -3.2351 * red + 2.4099 * nir - 0.5469 * swr + 0.2445

    def lm14():
        return -0.2076 * red + 2.8251 * nir - 2.0663 * swr + 0.164

    def lm15():
        return -3.8238 * red + 2.8013 * nir - 0.3736 * swr + 0.1544

    def lm16():
        return -2.6628 * red + 2.6984 * nir - 1.0549 * swr + 0.235

    def lm17():
        return -2.0522 * red + 2.3863 * nir - 1.5494 * swr + 0.3285

    def lm18():
        return -2.4207 * red + 3.1013 * nir - 1.2468 * swr + 0.1678

    def lm19():
        return -1.8105 * red + 1.6421 * nir - 1.3138 * swr + 0.6259

    def lm20():
        return -0.6749 * red - 3.6578 * nir - 19.5773 * swr + 4.7115

    def lm21():
        return -0.6749 * red + 12.0891 * nir - 9.3541 * swr - 1.2989

    def lm22():
        return 6.2796 * red + 7.6278 * nir - 9.3541 * swr - 0.1327

    def lm23():
        return -0.3364 * red + 0.1923 * nir - 2.98 * swr + 1.2379

    def lm24():
        return -1.7843 * red + 2.059 * nir - 1.482 * swr + 0.5176

    def lm25():
        return -0.0394 * red + 1.3591 * nir - 1.2482 * swr + 0.689

    def lm26():
        return -0.1141 * red + 1.2768 * nir - 0.0659 * swr + 0.5365

    def lm27():
        return -0.0931 * red + 2.5174 * nir - 1.2056 * swr + 0.2912

    def lm28():
        return -3.0549 * red + 2.4022 * nir - 1.6418 * swr + 0.4472

    def lm29():
        return 0.0248 * red + 0.2305 * nir - 0.0356 * swr + 0.9025

    def lm30():
        return 8.4438 * red + 0.1123 * nir - 10.8156 * swr + 2.66

    def lm31():
        return 6.4498 * red + 0.1123 * nir - 4.0391 * swr + 1.5602

    def lm32():
        return 1.1083 * red + 0.2128 * nir - 0.3717 * swr + 0.9434

    def lm33():
        return -0.0323 * red + 0.3274 * nir - 0.6229 * swr + 0.9474

    def lm34():
        return -2.2275 * red + 0.2921 * nir - 0.3033 * swr + 0.9527

    def lm35():
        return 1.0377 * red + 0.0074 * nir + 6.8333 * swr - 0.1421

    def lm36():
        return 1.0377 * red + 0.0074 * nir + 1.1922 * swr + 0.749

    def lm37():
        return 0.2961 * red + 0.0074 * nir - 0.3046 * swr + 1.0211

    def lm38():
        return -0.0379 * red + 0.0459 * nir - 0.0952 * swr + 0.9717

    def lm39():
        return -0.0379 * red - 2.6247 * nir + 3.3825 * swr + 1.3533

    def lm40():
        return -0.0379 * red + 0.0692 * nir + 1.3659 * swr + 0.7477

    def lm41():
        return -0.0379 * red + 0.4619 * nir - 1.3673 * swr + 1.0135

    def lm42():
        return -0.0379 * red + 0.0797 * nir - 0.0501 * swr + 0.907

    def lm43():
        return -0.0379 * red + 0.2794 * nir - 0.0501 * swr + 0.8626

    def lm44():
        return -0.0379 * red + 0.0489 * nir + 41.6118 * swr - 6.5351

    def lm45():
        return 33.1218 * red - 0.2834 * nir + 133.3182 * swr - 23.5683

    def lm46():
        return 34.7008 * red + 0.0489 * nir + 94.8346 * swr - 16.8027

    def lm47():
        return -0.0379 * red + 0.0489 * nir - 0.0501 * swr + 0.9508

    def lm48():
        return -0.0269 * red + 0.4133 * nir - 1.0316 * swr + 1.0099

    def lm49():
        return -0.0269 * red + 0.0047 * nir - 0.0016 * swr + 0.9809

    def lm50():
        return 2.8848 * red + 0.0047 * nir - 3.6703 * swr + 1.6203

    def lm51():
        return 3.5781 * red + 7.1076 * nir - 4.5437 * swr - 1.2744

    def lm52():
        return 3.5781 * red + 5.2686 * nir - 4.5437 * swr - 0.4844

    def lm53():
        return 3.5781 * red + 5.2686 * nir - 4.5437 * swr - 0.4847

    def lm54():
        return -2.3149 * red + 0.0047 * nir + 0.7073 * swr + 0.8725

    def lm55():
        return -0.0269 * red + 0.0047 * nir + 0.4035 * swr + 0.9057

    def lm56():
        return -0.0269 * red + 0.0047 * nir - 0.0016 * swr + 0.9824

    def lm57():
        return -0.0269 * red - 0.2037 * nir + 0.117 * swr + 1.0364

    def lm58():
        return -0.0269 * red - 0.3127 * nir + 0.117 * swr + 1.0641

    def lm59():
        return -1.8237 * red - 0.0444 * nir - 0.6459 * swr + 1.1666

    def lm60():
        return -3.9434 * red + 1.1766 * nir - 1.1615 * swr + 0.8098

    def lm61():
        return -2.9785 * red + 0.1251 * nir - 0.2215 * swr + 1.0189

    def lm62():
        return -1.037 * red + 3.093 * nir - 1.7221 * swr + 0.1728

    def lm63():
        return -1.6556 * red + 2.8893 * nir - 1.8309 * swr + 0.3043

    def lm64():
        return -0.6404 * red + 1.7465 * nir - 1.5344 * swr + 0.5568

    def lm65():
        return -0.0175 * red + 0.0119 * nir - 0.0172 * swr + 0.9121

    def lm66():
        return -1.4041 * red + 0.2945 * nir - 0.0151 * swr + 0.8445

    def lm67():
        return -0.0489 * red - 0.1646 * nir - 1.1411 * swr + 1.1806

    def lm68():
        return -0.4313 * red + 0.9526 * nir - 0.1146 * swr + 0.5971

    def lm69():
        return -4.5275 * red + 2.2675 * nir - 0.1146 * swr + 0.7986

    def lm70():
        return -0.5148 * red + 1.4164 * nir - 0.0508 * swr + 0.3486

    def lm71():
        return -0.031 * red + 0.0479 * nir - 1.3301 * swr + 1.1445

    def lm72():
        return -0.9645 * red + 2.5116 * nir - 2.1418 * swr + 0.4519

    def lm73():
        return -1.6843 * red + 0.5487 * nir - 1.1828 * swr + 1.022

    def lm74():
        return -0.016 * red + 1.4031 * nir - 1.6513 * swr + 0.6456

    def lm75():
        return -3.7877 * red + 2.7929 * nir - 0.253 * swr + 0.1193

    def lm76():
        return -2.2717 * red + 2.3372 * nir - 1.2551 * swr + 0.3769

    def lm77():
        return -4.0204 * red + 3.0626 * nir - 0.7264 * swr + 0.239

    def lm78():
        return -1.7443 * red + 1.611 * nir - 0.5137 * swr + 0.1485

    def lm79():
        return -3.1988 * red + 3.4787 * nir - 1.4011 * swr + 0.2265

    def lm80():
        return -1.7331 * red + 2.3423 * nir - 2.3031 * swr + 0.6291

    def lm81():
        return -0.8204 * red + 1.551 * nir - 2.3947 * swr + 0.851

    def lm82():
        return -2.2057 * red + 2.8434 * nir - 1.7193 * swr + 0.3681

    def lm83():
        return -1.3716 * red + 1.678 * nir - 1.5129 * swr + 0.5948

    def lm84():
        return -3.1817 * red + 2.479 * nir - 0.6304 * swr + 0.2304

    def lm85():
        return -2.3333 * red + 1.5005 * nir - 0.0296 * swr + 0.1058

    def lm86():
        return -1.4045 * red + 2.6229 * nir - 0.7704 * swr - 0.1275

    def lm87():
        return -1.3583 * red + 1.187 * nir - 0.3166 * swr + 0.1208

    def lm88():
        return -2.0511 * red + 2.2578 * nir - 1.6352 * swr + 0.5178

    def lm89():
        return -1.3226 * red + 0.9229 * nir - 0.3089 * swr + 0.2031

    def lm90():
        return -1.8454 * red + 1.3305 * nir - 0.5247 * swr + 0.2996

    def lm91():
        return -0.7488 * red + 0.8476 * nir - 0.2633 * swr + 0.0547

    if swr <= 0.273:
        if nir <= 0.278:
            if red <= 0.048:
                if nir <= 0.217:
                    if nir <= 0.163:
                        if red <= 0.014:
                            return lm1()
                        if red > 0.014:
                            return lm2()
                    if nir > 0.163:
                        if red <= 0.021:
                            return lm3()
                        if red > 0.021:
                            return lm4()
                if nir > 0.217:
                    if red <= 0.027:
                        if red <= 0.02:
                            if nir <= 0.262:
                                if swr <= 0.139:
                                    return lm5()
                                if swr > 0.139:
                                    return lm6()
                            if nir > 0.262:
                                if swr <= 0.139:
                                    return lm7()
                                if swr > 0.139:
                                    return lm8()
                        if red > 0.02:
                            return lm9()
                    if red > 0.027:
                        return lm10()
            if red > 0.048:
                if nir <= 0.224:
                    if red <= 0.083:
                        if nir <= 0.182:
                            if nir <= 0.151:
                                return lm11()
                            if nir > 0.151:
                                return lm12()
                        if nir > 0.182:
                            return lm13()
                    if red > 0.083:
                        if red <= 0.108:
                            if nir <= 0.194:
                                if swr <= 0.193:
                                    return lm14()
                                if swr > 0.193:
                                    return lm15()
                            if nir > 0.194:
                                return lm16()
                        if red > 0.108:
                            return lm17()
                if nir > 0.224:
                    return lm18()
        if nir > 0.278:
            if red <= 0.036:
                if nir <= 0.33:
                    if red <= 0.024:
                        if nir <= 0.305:
                            if swr <= 0.142:
                                return lm19()
                            if swr > 0.142:
                                if nir <= 0.289:
                                    if swr <= 0.146:
                                        if red <= 0.02:
                                            return lm20()
                                        if red > 0.02:
                                            if nir <= 0.281:
                                                return lm21()
                                            if nir > 0.281:
                                                return lm22()
                                    if swr > 0.146:
                                        return lm23()
                                if nir > 0.289:
                                    return lm24()
                        if nir > 0.305:
                            if swr <= 0.142:
                                return lm25()
                            if swr > 0.142:
                                if red <= 0.017:
                                    return lm26()
                                if red > 0.017:
                                    return lm27()
                    if red > 0.024:
                        return lm28()
                if nir > 0.33:
                    if red <= 0.021:
                        if swr <= 0.183:
                            if red <= 0.018:
                                if red <= 0.011:
                                    if swr <= 0.16:
                                        return lm29()
                                    if swr > 0.16:
                                        if red <= 0.009:
                                            if red <= 0.006:
                                                return lm30()
                                            if red > 0.006:
                                                return lm31()
                                        if red > 0.009:
                                            return lm32()
                                if red > 0.011:
                                    if nir <= 0.36:
                                        return lm33()
                                    if nir > 0.36:
                                        if nir <= 0.396:
                                            return lm34()
                                        if nir > 0.396:
                                            if red <= 0.013:
                                                if swr <= 0.161:
                                                    return lm35()
                                                if swr > 0.161:
                                                    return lm36()
                                            if red > 0.013:
                                                return lm37()
                            if red > 0.018:
                                if swr <= 0.167:
                                    if swr <= 0.143:
                                        return lm38()
                                    if swr > 0.143:
                                        if swr <= 0.149:
                                            if swr <= 0.145:
                                                return lm39()
                                            if swr > 0.145:
                                                return lm40()
                                        if swr > 0.149:
                                            return lm41()
                                if swr > 0.167:
                                    if nir <= 0.351:
                                        return lm42()
                                    if nir > 0.351:
                                        if swr <= 0.179:
                                            return lm43()
                                        if swr > 0.179:
                                            if swr <= 0.18:
                                                if red <= 0.019:
                                                    return lm44()
                                                if red > 0.019:
                                                    if red <= 0.02:
                                                        return lm45()
                                                    if red > 0.02:
                                                        return lm46()
                                            if swr > 0.18:
                                                return lm47()
                        if swr > 0.183:
                            if nir <= 0.381:
                                return lm48()
                            if nir > 0.381:
                                if nir <= 0.449:
                                    if swr <= 0.197:
                                        if nir <= 0.425:
                                            return lm49()
                                        if nir > 0.425:
                                            if nir <= 0.429:
                                                if swr <= 0.193:
                                                    return lm50()
                                                if swr > 0.193:
                                                    if nir <= 0.426:
                                                        return lm51()
                                                    if nir > 0.426:
                                                        if nir <= 0.428:
                                                            return lm52()
                                                        if nir > 0.428:
                                                            return lm53()
                                            if nir > 0.429:
                                                if swr <= 0.188:
                                                    return lm54()
                                                if swr > 0.188:
                                                    return lm55()
                                    if swr > 0.197:
                                        return lm56()
                                if nir > 0.449:
                                    if swr <= 0.202:
                                        if nir <= 0.477:
                                            return lm57()
                                        if nir > 0.477:
                                            return lm58()
                                    if swr > 0.202:
                                        return lm59()
                    if red > 0.021:
                        if nir <= 0.363:
                            return lm60()
                        if nir > 0.363:
                            return lm61()
            if red > 0.036:
                if nir <= 0.333:
                    if swr <= 0.216:
                        return lm62()
                    if swr > 0.216:
                        return lm63()
                if nir > 0.333:
                    if swr <= 0.227:
                        if nir <= 0.367:
                            return lm64()
                        if nir > 0.367:
                            if red <= 0.066:
                                if swr <= 0.19:
                                    return lm65()
                                if swr > 0.19:
                                    return lm66()
                            if red > 0.066:
                                if swr <= 0.195:
                                    if red <= 0.135:
                                        return lm67()
                                    if red > 0.135:
                                        if red <= 0.186:
                                            return lm68()
                                        if red > 0.186:
                                            return lm69()
                                if swr > 0.195:
                                    if nir <= 0.401:
                                        return lm70()
                                    if nir > 0.401:
                                        return lm71()
                    if swr > 0.227:
                        if nir <= 0.374:
                            return lm72()
                        if nir > 0.374:
                            if red <= 0.073:
                                return lm73()
                            if red > 0.073:
                                return lm74()
    if swr > 0.273:
        if swr <= 0.389:
            if nir <= 0.308:
                if red <= 0.144:
                    if nir <= 0.257:
                        return lm75()
                    if nir > 0.257:
                        return lm76()
                if red > 0.144:
                    if nir <= 0.27:
                        if red <= 0.165:
                            return lm77()
                        if red > 0.165:
                            return lm78()
                    if nir > 0.27:
                        return lm79()
            if nir > 0.308:
                if swr <= 0.323:
                    if nir <= 0.345:
                        return lm80()
                    if nir > 0.345:
                        return lm81()
                if swr > 0.323:
                    if nir <= 0.354:
                        return lm82()
                    if nir > 0.354:
                        return lm83()
        if swr > 0.389:
            if swr <= 0.475:
                if nir <= 0.348:
                    if red <= 0.201:
                        return lm84()
                    if red > 0.201:
                        if red <= 0.218:
                            if nir <= 0.319:
                                return lm85()
                            if nir > 0.319:
                                return lm86()
                        if red > 0.218:
                            return lm87()
                if nir > 0.348:
                    return lm88()
            if swr > 0.475:
                if red <= 0.266:
                    if nir <= 0.377:
                        return lm89()
                    if nir > 0.377:
                        return lm90()
                if red > 0.266:
                    return lm91()

    return float('NaN')
