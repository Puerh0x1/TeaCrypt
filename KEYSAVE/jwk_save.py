import base64
import json

def toBase64url(number):
    num_bytes = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')
    return base64.urlsafe_b64encode(num_bytes).rstrip(b'=').decode('utf-8')


def rsaSave(e, n, d, kid, keysFilename, alg='RS256'):
    # File: .jwk
    jwk_json = {
        'kty': 'RSA',
        'e': toBase64url(e),
        'n': toBase64url(n), 
        'd': toBase64url(d),
        'alg': alg,
        'kid': kid # Идентификатор ключа
    }
    with open(keysFilename, 'w') as f:
        f.write(str(jwk_json))
        print("~KEYS SAVED~")