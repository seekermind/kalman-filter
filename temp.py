est = [68.0]
msr = [75, 71, 70, 74]
E_est = [2.0]
E_msr = 4

for i in range(len(msr)+1):
    KG = E_est[i] / (E_est[i] + E_msr)
    est += [est[i] + (KG*(msr[i]-est[i]))]
    E_est += [(1-KG)*E_est[i]]
    print(est[i], KG, E_est[i])
