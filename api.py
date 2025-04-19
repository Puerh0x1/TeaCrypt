from ALGS.RSA.mathKeyGen import *
from KEYSAVE.jwk_save import *

genRes = mainGeneration(2048)
n = genRes[2]
e = genRes[4]
d = genRes[5]
rsaSave(e, n, d, "MAIN-KEY", "keys.jwk")


