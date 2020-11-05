from Crypto.Util.number import inverse, long_to_bytes

c = 97938185189891786003246616098659465874822119719049
e = 65537
n = 196284284267878746604991616360941270430332504451383

# from factordb
p = 10252256693298561414756287
q = 19145471103565027335990409
phi = (p-1) * (q-1)
d = inverse(e, phi)                                                                                                                                                                              

m = pow(c, d, n)
print(long_to_bytes(m))