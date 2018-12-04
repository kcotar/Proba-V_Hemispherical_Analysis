def lai_regression_tree(red, nir, swr):
    def lm1():
        return -81.6881 * red + 15.0418 * nir - 0.4057 * swr + 1.4031

    def lm2():
        return -24.0033 * red + 9.173 * nir - 5.8086 * swr + 1.6433

    def lm3():
        return -65.1493 * red + 15.0276 * nir - 9.0058 * swr + 2.2076

    def lm4():
        return -41.5203 * red + 22.3618 * nir - 12.723 * swr + 1.1193

    def lm5():
        return -52.9773 * red + 24.8897 * nir - 21.8901 * swr + 1.4483

    def lm6():
        return -15.1563 * red + 9.3988 * nir - 7.6653 * swr + 1.6635

    def lm7():
        return -16.9035 * red + 21.3388 * nir - 15.4071 * swr + 0.3428

    def lm8():
        return -0.9145 * red + 11.9112 * nir - 11.5279 * swr + 1.2964

    def lm9():
        return -0.8543 * red + 3.2059 * nir - 7.2433 * swr + 2.2925

    def lm10():
        return -0.8543 * red + 0.8521 * nir - 0.7583 * swr + 1.9067

    def lm11():
        return 17.4634 * red + 1.3887 * nir - 1.2138 * swr + 4.4155

    def lm12():
        return 25.5392 * red + 35.2374 * nir - 1.2138 * swr - 5.379

    def lm13():
        return 25.5392 * red + 24.6614 * nir - 1.2138 * swr - 2.1892

    def lm14():
        return 4.5677 * red + 5.354 * nir - 1.2138 * swr + 3.4534

    def lm15():
        return -13.306 * red + 3.8747 * nir - 1.2138 * swr + 3.7635

    def lm16():
        return -53.2391 * red + 33.662 * nir - 65.5203 * swr + 5.248

    def lm17():
        return -20.2034 * red + 8.8669 * nir - 7.5193 * swr + 3.8496

    def lm18():
        return -3.2782 * red + 10.8108 * nir - 1.0848 * swr + 2.015

    def lm19():
        return -6.0899 * red + 35.6658 * nir - 1.0848 * swr - 5.6287

    def lm20():
        return -18.2842 * red + 18.8421 * nir - 27.658 * swr + 3.1622

    def lm21():
        return -19.4996 * red + 11.8758 * nir - 20.0604 * swr + 4.6908

    def lm22():
        return -0.5909 * red + 0.4096 * nir + 20.9992 * swr + 2.6588

    def lm23():
        return 69.2544 * red + 16.4314 * nir - 34.0781 * swr + 4.2931

    def lm24():
        return 1.1306 * red + 0.8428 * nir - 1.533 * swr + 5.6459

    def lm25():
        return -0.7386 * red + 12.06 * nir - 13.1953 * swr + 3.4138

    def lm26():
        return -31.5893 * red - 9.3832 * nir + 37.7237 * swr + 4.2786

    def lm27():
        return -38.7619 * red + 15.7977 * nir - 37.7504 * swr + 6.1439

    def lm28():
        return -1.2909 * red + 0.2565 * nir - 13.8849 * swr + 7.3529

    def lm29():
        return -32.7635 * red - 4.6061 * nir - 0.5582 * swr + 7.9611

    def lm30():
        return -30.7094 * red + 15.892 * nir - 20.1586 * swr + 3.2738

    def lm31():
        return -26.1889 * red + 4.0189 * nir - 23.0857 * swr + 7.983

    def lm32():
        return -0.8184 * red + 5.8318 * nir - 0.3528 * swr + 2.8148

    def lm33():
        return -3.1853 * red + 16.5606 * nir - 21.7941 * swr + 2.4798

    def lm34():
        return -5.0312 * red + 0.4015 * nir - 32.3442 * swr + 10.2371

    def lm35():
        return -159.1147 * red + 0.468 * nir - 12.4162 * swr + 10.0088

    def lm36():
        return -90.8246 * red + 0.3968 * nir - 0.5802 * swr + 6.6977

    def lm37():
        return -37.3347 * red + 20.0834 * nir - 29.8225 * swr + 3.4682

    def lm38():
        return -25.814 * red + 16.5308 * nir - 15.2689 * swr + 1.6289

    def lm39():
        return -1.5868 * red + 23.924 * nir - 2.6819 * swr - 2.5872

    def lm40():
        return -1.5868 * red + 1.315 * nir - 2.6744 * swr + 4.0671

    def lm41():
        return -66.9723 * red + 0.2135 * nir - 1.0893 * swr + 6.9541

    def lm42():
        return -1.9123 * red + 0.2135 * nir - 0.9534 * swr + 4.8092

    def lm43():
        return -26.0211 * red + 0.2375 * nir - 34.2189 * swr + 10.248

    def lm44():
        return -1.9362 * red - 2.5694 * nir - 12.4305 * swr + 7.4051

    def lm45():
        return -25.2304 * red + 11.6064 * nir - 17.3696 * swr + 3.5214

    def lm46():
        return -35.3402 * red + 2.883 * nir - 11.0477 * swr + 6.1106

    def lm47():
        return -5.3662 * red + 10.362 * nir - 10.3735 * swr + 1.3253

    def lm48():
        return -9.5461 * red + 10.2931 * nir - 4.9649 * swr + 0.7688

    def lm49():
        return -12.7943 * red + 26.5544 * nir - 7.8023 * swr - 1.798

    def lm50():
        return -5.5197 * red + 15.8046 * nir - 14.4097 * swr + 0.7791

    def lm51():
        return -6.3964 * red + 9.4974 * nir - 7.3578 * swr + 1.1528

    def lm52():
        return -7.7941 * red + 8.8883 * nir - 4.286 * swr + 0.7315

    def lm53():
        return -5.4335 * red + 26.2113 * nir - 25.1102 * swr - 0.3145

    def lm54():
        return -1.6026 * red + 12.2658 * nir - 15.2125 * swr + 1.6957

    def lm55():
        return 0.1936 * red - 11.4502 * nir + 13.5873 * swr + 6.9087

    def lm56():
        return 0.1936 * red + 25.7867 * nir - 3.3987 * swr - 4.375

    def lm57():
        return 0.0637 * red + 0.6376 * nir - 0.8791 * swr + 4.7288

    def lm58():
        return -13.0128 * red + 0.7997 * nir - 0.8791 * swr + 6.0141

    def lm59():
        return -0.4022 * red - 0.2833 * nir - 0.8791 * swr + 4.3126

    def lm60():
        return -0.131 * red + 0.0128 * nir - 0.9583 * swr + 4.1371

    def lm61():
        return -0.0252 * red + 7.7669 * nir - 26.2739 * swr + 5.5015

    def lm62():
        return -2.4719 * red + 11.6316 * nir - 10.8583 * swr + 1.0332

    def lm63():
        return -6.1198 * red + 7.4522 * nir - 3.5415 * swr + 0.7961

    def lm64():
        return -2.8265 * red + 8.7698 * nir - 5.7795 * swr + 0.6763

    def lm65():
        return -1.0665 * red + 8.0532 * nir - 12.8816 * swr + 2.6686

    def lm66():
        return 1.8848 * red + 5.2528 * nir - 15.5814 * swr + 4.3267

    def lm67():
        return -8.1453 * red + 6.2698 * nir - 0.0627 * swr + 0.1287

    def lm68():
        return -8.3801 * red + 6.4386 * nir - 1.1229 * swr + 0.3947

    def lm69():
        return -0.5294 * red + 7.5858 * nir - 4.2725 * swr + 0.1327

    def lm70():
        return -21.6441 * red + 5.2704 * nir - 3.6257 * swr + 3.345

    def lm71():
        return -63.8554 * red + 5.0485 * nir - 1.3364 * swr + 8.5205

    def lm72():
        return -323.2656 * red + 5.0485 * nir - 8.6817 * swr + 46.4681

    def lm73():
        return -129.1425 * red + 5.0485 * nir - 5.8252 * swr + 18.92

    def lm74():
        return -8.6992 * red + 4.6764 * nir - 2.0389 * swr + 1.2188

    def lm75():
        return -4.5767 * red + 7.5198 * nir - 5.6171 * swr + 1.1562

    def lm76():
        return -5.4879 * red + 4.7736 * nir - 1.4735 * swr + 0.462

    def lm77():
        return -7.2841 * red + 7.4664 * nir - 3.809 * swr + 0.8708

    def lm78():
        return -4.4317 * red + 3.183 * nir - 0.9099 * swr + 0.4857

    def lm79():
        return -7.5069 * red + 8.6116 * nir - 5.4034 * swr + 1.2064

    def lm80():
        return -5.8722 * red + 5.3633 * nir - 1.714 * swr + 0.4597

    def lm81():
        return -4.5503 * red + 10.986 * nir - 5.587 * swr - 0.0181

    def lm82():
        return -0.161 * red + 7.7357 * nir - 10.2435 * swr + 1.9184

    def lm83():
        return -3.33 * red + 4.4655 * nir - 3.9432 * swr + 1.6008

    def lm84():
        return -5.8486 * red + 7.8497 * nir - 5.4229 * swr + 1.1878

    def lm85():
        return -5.5425 * red + 0.6367 * nir - 0.5439 * swr + 1.2828

    def lm86():
        return -1.3726 * red + 0.6367 * nir - 0.537 * swr + 0.4777

    def lm87():
        return -6.1443 * red + 7.1365 * nir - 4.1034 * swr + 0.9345

    def lm88():
        return -1.4208 * red + 2.9605 * nir - 0.1697 * swr - 0.2641

    def lm89():
        return -1.4208 * red - 1.2441 * nir - 0.1697 * swr + 1.0974

    def lm90():
        return -1.4208 * red - 12.2131 * nir - 0.1697 * swr + 4.5431

    def lm91():
        return -3.8882 * red + 2.8494 * nir - 1.1868 * swr + 0.5939

    def lm92():
        return -1.1277 * red + 1.1456 * nir - 2.6483 * swr + 1.3183

    def lm93():
        return -1.9273 * red - 36.5379 * nir - 3.8322 * swr + 15.3573

    def lm94():
        return 0.6021 * red - 10.5854 * nir - 4.4423 * swr + 5.9403

    def lm95():
        return -2.7188 * red + 2.4911 * nir - 1.0963 * swr + 0.436

    def lm96():
        return -3.9518 * red + 5.7953 * nir - 4.8106 * swr + 1.2348

    def lm97():
        return -0.0363 * red + 0.048 * nir - 0.0239 * swr + 0.0972

    if red <= 0.047:
        if nir <= 0.256:
            if red <= 0.03:
                if nir <= 0.191:
                    if nir <= 0.154:
                        if red <= 0.012:
                            return lm1()
                        if red > 0.012:
                            return lm2()
                    if nir > 0.154:
                        return lm3()
                if nir > 0.191:
                    if swr <= 0.132:
                        return lm4()
                    if swr > 0.132:
                        return lm5()
            if red > 0.03:
                if nir <= 0.2:
                    return lm6()
                if nir > 0.2:
                    if swr <= 0.152:
                        return lm7()
                    if swr > 0.152:
                        if red <= 0.039:
                            return lm8()
                        if red > 0.039:
                            if nir <= 0.243:
                                return lm9()
                            if nir > 0.243:
                                return lm10()
        if nir > 0.256:
            if red <= 0.025:
                if nir <= 0.305:
                    if swr <= 0.143:
                        if nir <= 0.275:
                            if swr <= 0.134:
                                if red <= 0.018:
                                    return lm11()
                                if red > 0.018:
                                    if red <= 0.021:
                                        if red <= 0.019:
                                            if nir <= 0.262:
                                                return lm12()
                                            if nir > 0.262:
                                                return lm13()
                                        if red > 0.019:
                                            return lm14()
                                    if red > 0.021:
                                        return lm15()
                            if swr > 0.134:
                                return lm16()
                        if nir > 0.275:
                            if swr <= 0.136:
                                return lm17()
                            if swr > 0.136:
                                if red <= 0.02:
                                    return lm18()
                                if red > 0.02:
                                    return lm19()
                    if swr > 0.143:
                        return lm20()
                if nir > 0.305:
                    if swr <= 0.156:
                        if red <= 0.012:
                            if swr <= 0.143:
                                if nir <= 0.333:
                                    return lm21()
                                if nir > 0.333:
                                    return lm22()
                            if swr > 0.143:
                                if nir <= 0.345:
                                    return lm23()
                                if nir > 0.345:
                                    return lm24()
                        if red > 0.012:
                            if swr <= 0.142:
                                if nir <= 0.336:
                                    return lm25()
                                if nir > 0.336:
                                    return lm26()
                            if swr > 0.142:
                                if nir <= 0.33:
                                    return lm27()
                                if nir > 0.33:
                                    if nir <= 0.35:
                                        return lm28()
                                    if nir > 0.35:
                                        return lm29()
                    if swr > 0.156:
                        if red <= 0.02:
                            if nir <= 0.354:
                                return lm30()
                            if nir > 0.354:
                                if swr <= 0.17:
                                    return lm31()
                                if swr > 0.17:
                                    return lm32()
                        if red > 0.02:
                            if nir <= 0.347:
                                return lm33()
                            if nir > 0.347:
                                if swr <= 0.174:
                                    return lm34()
                                if swr > 0.174:
                                    if nir <= 0.382:
                                        return lm35()
                                    if nir > 0.382:
                                        return lm36()
            if red > 0.025:
                if nir <= 0.31:
                    if swr <= 0.163:
                        return lm37()
                    if swr > 0.163:
                        return lm38()
                if nir > 0.31:
                    if swr <= 0.167:
                        if red <= 0.033:
                            if nir <= 0.333:
                                if swr <= 0.153:
                                    return lm39()
                                if swr > 0.153:
                                    return lm40()
                            if nir > 0.333:
                                if swr <= 0.154:
                                    return lm41()
                                if swr > 0.154:
                                    return lm42()
                        if red > 0.033:
                            if nir <= 0.352:
                                return lm43()
                            if nir > 0.352:
                                return lm44()
                    if swr > 0.167:
                        if nir <= 0.359:
                            return lm45()
                        if nir > 0.359:
                            return lm46()
    if red > 0.047:
        if swr <= 0.286:
            if nir <= 0.279:
                if swr <= 0.205:
                    if nir <= 0.202:
                        if swr <= 0.156:
                            return lm47()
                        if swr > 0.156:
                            return lm48()
                    if nir > 0.202:
                        if swr <= 0.167:
                            if swr <= 0.149:
                                return lm49()
                            if swr > 0.149:
                                return lm50()
                        if swr > 0.167:
                            return lm51()
                if swr > 0.205:
                    return lm52()
            if nir > 0.279:
                if swr <= 0.208:
                    if nir <= 0.34:
                        if swr <= 0.179:
                            return lm53()
                        if swr > 0.179:
                            return lm54()
                    if nir > 0.34:
                        if swr <= 0.179:
                            if swr <= 0.169:
                                if nir <= 0.386:
                                    if red <= 0.117:
                                        if red <= 0.063:
                                            if swr <= 0.157:
                                                return lm55()
                                            if swr > 0.157:
                                                return lm56()
                                        if red > 0.063:
                                            return lm57()
                                    if red > 0.117:
                                        return lm58()
                                if nir > 0.386:
                                    return lm59()
                            if swr > 0.169:
                                return lm60()
                        if swr > 0.179:
                            return lm61()
                if swr > 0.208:
                    if nir <= 0.348:
                        if swr <= 0.245:
                            return lm62()
                        if swr > 0.245:
                            if nir <= 0.308:
                                return lm63()
                            if nir > 0.308:
                                return lm64()
                    if nir > 0.348:
                        if nir <= 0.394:
                            return lm65()
                        if nir > 0.394:
                            return lm66()
        if swr > 0.286:
            if swr <= 0.418:
                if nir <= 0.328:
                    if red <= 0.152:
                        if nir <= 0.267:
                            if red <= 0.121:
                                return lm67()
                            if red > 0.121:
                                if nir <= 0.24:
                                    return lm68()
                                if nir > 0.24:
                                    if red <= 0.137:
                                        if red <= 0.134:
                                            return lm69()
                                        if red > 0.134:
                                            if nir <= 0.255:
                                                return lm70()
                                            if nir > 0.255:
                                                if swr <= 0.326:
                                                    return lm71()
                                                if swr > 0.326:
                                                    if swr <= 0.33:
                                                        return lm72()
                                                    if swr > 0.33:
                                                        return lm73()
                                                if red > 0.137:
                                                    return lm74()
                        if nir > 0.267:
                            return lm75()
                    if red > 0.152:
                        if nir <= 0.292:
                            if swr <= 0.372:
                                if nir <= 0.272:
                                    return lm76()
                                if nir > 0.272:
                                    return lm77()
                            if swr > 0.372:
                                return lm78()
                        if nir > 0.292:
                            if swr <= 0.378:
                                return lm79()
                            if swr > 0.378:
                                return lm80()
                if nir > 0.328:
                    if swr <= 0.361:
                        if nir <= 0.353:
                            return lm81()
                        if nir > 0.353:
                            if swr <= 0.313:
                                return lm82()
                            if swr > 0.313:
                                return lm83()
                    if swr > 0.361:
                        return lm84()
            if swr > 0.418:
                if swr <= 0.475:
                    if nir <= 0.356:
                        if red <= 0.202:
                            if nir <= 0.323:
                                if red <= 0.186:
                                    if nir <= 0.304:
                                        if swr <= 0.428:
                                            return lm85()
                                        if swr > 0.428:
                                            return lm86()
                                    if nir > 0.304:
                                        if swr <= 0.436:
                                            return lm87()
                                        if swr > 0.436:
                                            if swr <= 0.46:
                                                if nir <= 0.313:
                                                    return lm88()
                                                if nir > 0.313:
                                                    return lm89()
                                                if swr > 0.46:
                                                    return lm90()
                                if red > 0.186:
                                    return lm91()
                            if nir > 0.323:
                                if nir <= 0.342:
                                    return lm92()
                                if nir > 0.342:
                                    if swr <= 0.435:
                                        return lm93()
                                    if swr > 0.435:
                                        return lm94()
                        if red > 0.202:
                            return lm95()
                    if nir > 0.356:
                        return lm96()
                if swr > 0.475:
                    return lm97()

    return float('NaN')