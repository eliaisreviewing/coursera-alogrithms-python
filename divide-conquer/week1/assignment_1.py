
import time
# E.g. m='32', n='24'
def high_school_mult(x, y):
    result = {}
    for j in xrange(len(y)-1, -1, -1):
        for i in xrange(len(x)-1, -1, -1):
            if i+j not in result:
                result[i+j] = 0
            result[i+j] += int(y[j]) * int(x[i])

    result_to_str = ''
    for k in xrange(len(result)-1,0,-1):
        result[k - 1] += (result[k] - (result[k] % 10)) / 10
        result[k] = result[k] % 10

    for val in result.values():
        result_to_str+=str(val)

    return result_to_str


def karatsuba_mult(x,y):

    n_x = len(x)
    n_y = len(y)

    # get the longest number
    n = max(n_x, n_y)

    # base case
    if n == 1:
        return str(int(x) * int(y))

    # ensure even number of digits
    if n > 1 and n % 2 != 0:
        n+=1

    # prepend zeros if necessary
    for i in xrange(n - n_x):
        x = '0' + x

    for i in xrange(n - n_y):
        y = '0' + y

    # get the four elements for karatsuba
    a = x[:n/2]
    b = x[n/2:]
    c = y[:n/2]
    d = y[n/2:]

    ac = karatsuba_mult(a,c)
    bd = karatsuba_mult(b,d)
    ad_plus_bc = int(karatsuba_mult(str(int(a)+int(b)),str(int(c)+int(d)))) - int(ac) - int(bd)

    return str(int(ac + '0' * n) + int(str(ad_plus_bc) + '0' * (n/2)) + int(bd))



if __name__ == '__main__':

    tic = time.clock()
    result = high_school_mult('49343232348237423234723423423847324823766666693842394832749238742937842394872398472394873294872349832749823749283743298742983338888820982762772727272727272', '49343232348237423234723423423847324823766666693842394832749238742937842394872398472394873294872349832749823749283743298742983338888820982762772727272727272')
    toc = time.clock()
    print(result)
    print('mill: ' + str(toc-tic))

    tic = time.clock()
    result = karatsuba_mult('49343232348237423234723423423847324823766666693842394832749238742937842394872398472394873294872349832749823749283743298742983338888820982762772727272727272', '49343232348237423234723423423847324823766666693842394832749238742937842394872398472394873294872349832749823749283743298742983338888820982762772727272727272')
    toc = time.clock()
    print(result)
    print('mill: ' + str(toc - tic))
