from ALGS.RSA.keyGen import *
from KEYSAVE.jwk_save import *
from KEYSAVE.pem_save import *

RSA_keys = mainGeneration(1024)

print(RSA_keys)

savePublicKeyPEM(RSA_keys[4], RSA_keys[2])
savePrivateKeyPEM(RSA_keys[5], RSA_keys[4], RSA_keys[2], RSA_keys[0], RSA_keys[1])
print("~RSA keys saved~")