from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers, RSAPrivateNumbers

def savePublicKeyPEM(e, n, output_file="public_key.pem"):
    public_numbers = RSAPublicNumbers(e=e, n=n)
    public_key = public_numbers.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(output_file, "wb") as f:
        f.write(pem)
    return pem.decode("utf-8")

def savePrivateKeyPEM(d, e, n, p, q, output_file="private_key.pem"):
    if n != p * q:
        raise ValueError("n not equal to p * q")
    dmp1 = d % (p - 1)
    dmq1 = d % (q - 1)
    iqmp = pow(q, -1, p)
    public_numbers = RSAPublicNumbers(e=e, n=n)
    private_numbers = RSAPrivateNumbers(
        p=p,
        q=q,
        d=d,
        dmp1=dmp1,
        dmq1=dmq1,
        iqmp=iqmp,
        public_numbers=public_numbers
    )
    private_key = private_numbers.private_key()
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(output_file, "wb") as f:
        f.write(pem)
    return pem.decode("utf-8")