string="731671765313306249192251196744265747423553491949349698352031277450632623978318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
product=0
index=0
greatest=0
print 999-12
for i in range (0,987):
    product=int(string[i])*int(string[i+1])*int(string[i+2])*int(string[i+3])*int(string[i+4])*int(string[i+5])*int(string[i+6])*int(string[i+7])*int(string[i+8])*int(string[i+9])*int(string[i+10])*int(string[i+11])*int(string[i+12])
    if product>greatest:
        greatest=product
        index=i+1
print greatest, index
