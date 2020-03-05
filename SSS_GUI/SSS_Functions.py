"""
The following Python implementation of Shamir's Secret Sharing is
released into the Public Domain under the terms of CC0 and OWFa:
https://creativecommons.org/publicdomain/zero/1.0/
http://www.openwebfoundation.org/legal/the-owf-1-0-agreements/owfa-1-0

Refer to https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing
"""

from __future__ import division
from __future__ import print_function

import random
import functools
import datetime
import sys
import binascii

class SSS_Functions(object):

   

    # 12th Mersenne Prime
    # (for this application we want a known prime number as close as
    # possible to our security level; e.g.  desired security level of 128
    # bits -- too large and all the ciphertext is large; too small and
    # security is compromised)
    _PRIME = 2 ** 216091 - 1
    #_PRIME = 2 ** 128 - 1
    # 13th Mersenne Prime is 2**521 - 1

    _RINT = functools.partial(random.SystemRandom().randint, 0)

    def __init__(self):
        pass

    def _eval_at(self, poly, x, prime):
        accum = 0
        for coeff in reversed(poly):
            accum *= x
            accum += coeff
            accum %= prime
        return accum

    def create_shares(self, minimum, shares, prime=_PRIME):
        if minimum > shares:
            raise ValueError("Minimum shares must be more than actual shares")
        poly = [SSS_Functions._RINT(prime - 1) for i in range(minimum)]
        #s = "The quick brown fox jumps over the lazy dog.".encode("hex")
     
        secret_string = """-----BEGIN PGP MESSAGE-----

hQIMA6Wp4Rh52viEARAAjlzVcipTz08uDZcha6iZDPCp2ePjeFxheL3hzR0WdjTD
JeWJmtD8vafyzJJwjWLiB2Df+GAHaNibc3rR0XsOpbr3oRb3v9TeVFJVqloZ03bd
vuQK2wbZ0fYOkZkFrajO3pjIlYuglnrjdjQqk7EoqbwKClJoOdbzxCLnXKFEV244
2I2eZY/AGJcoBSUxqTimvqTdWPQc9rQ5I3skVl/fcOu1Q/gT6OiaRR3qWT7clwfo
BvanB2qPt2U6SP7BbW+ZZaQj9Z7hfGWRqX313nKKS+vofj0BN7SlZ8koVREGh5Nk
ipljDOuH0gWlRmpjbPC3yVoovZnoL4sPmnuwwRDUKDLt9WYFZRijNbFcjZmlIRU8
1KYWw8mkqqvSEcrR/nyCdo0fFU7RDXh9Z+hxp8/uY/u2GC85a0Rgz8fXpETCMKam
X23C9YzA3YD0wQrisRxQPMubziQtdasgzNCp3ZLNIlegHV1K49wuJD6xu90eq+SX
i+vzvWF9vab489LqJ/kv6I9T+RsLbviIk2mLvcwzYv2vckzACQ/Pkcbk7VzIMuOd
YCYPjCKxdTRfijKbnTgzmFM/x0fl/Fa0n5Tu1vqy/uNL9ID6TeyRMZJE99SX+Rze
7+CSVrEdoT2EHPJxVNLZ9EtIoL52ruXEFMIw1fDfnYxi1yp6UWd1e+a4d5Zs0YrS
6QGlCNvYUcthk5cjmMt1w+9GpG+7juJKNcJzASV96yUKV7Sjdh53YVNEqP3hRB53
JEONj3grugxXHwkIj1ksXYQUpzLaxE5g3wRCp7aD1i7tqKTsEfAz/C+5H6ldETqb
zkIHhr8mxfiX5pCy1GygTjUPji9sPStMbHTYyaweCKXxWPfCZOmDEIcmndVkr2Pt
YwdQ72VaJWTx97Ov8FRFWXLGjENgXeUna34bOjzq5c9N0LfaZB2oTraNLIBL0Zgd
EYi3JKAMP0O2A/57o6P4WjcbMagBkQNvbYS31yJ6fnSbeUe09bo83WoBUA6VELbc
QWcoIVP59dSZ6l6voPK8Q7eCdQstlOZKyEV2y/aaVttRcyqGxPFPDqbMRB/Qk5Xc
zSV8uMjVT3fuwe8qIqyuejlRFEjS9BQt2aAx4z6fk+08aL5Et6QWQ68Ut8GENlBU
McU2buT0R/ln2f8H6g/08Tig+0sW3XU0wHSUA0HCXjpIkllG+Rht3yWjsuFy7jRa
gjGMoWQyyRPFhF9IBJaaaQjuNXImx8PxaN6JTZmKDdKncKDZQn4bSRMeBGQMTMP6
NjIrLjDYnZ/TgQvVfuclQ1Gy/nJcApB3EkZNdcdLiZIe1BougpYqF4xn72LTUpm7
aZEZG46jgWNv0AGjVGk1lgUQTMtQvcAIYNwJUT6C8bwPlxt4i3ZCdc4jDffpnPpm
vgIq2GMLMDKZMFLAgC834Pm6uZcKCAVmaQytpc4kFb9Cbh0hWDm4h2IeyRSTdjQp
zIvJ3PB8VpGwL+Q0P5nPC7D/TSktamXEErB3DlogpYGXL+5gSqtWsKgDCY/Rx4O5
XlQ5l7cOhmm3Yh6dxgrLyAXXlcpZQE6xSzH1cwUIa95S1LYZnbf2zpw=
=vqMC
-----END PGP MESSAGE-----
"""
        #secret_string = "\t"
        string = ""
   
        for c_char in secret_string:
            c_int = ord(c_char)
            c_char = str(c_int)
            if c_int < 100:
                c_char = "0" + c_char
                if c_int < 10:
                    c_char = "0" + c_char
            
            string += c_char
                
        secret_int = int(string)
        

       
        
        
        poly[0] = secret_int
        points = [(i, SSS_Functions._eval_at(self, poly, i, prime))
                for i in range(1, shares + 1)]
        return poly[0], points

    def _extended_gcd(self, a, b):
        x = 0
        last_x = 1
        y = 1
        last_y = 0
        while b != 0:
            quot = a // b
            a, b = b, a % b
            x, last_x = last_x - quot * x, x
            y, last_y = last_y - quot * y, y
        return last_x, last_y

    def _divmod(self, num, den, p):
        inv, _ = SSS_Functions._extended_gcd(self, den, p)
        return num * inv

    def _lagrange_interpolate(self, x, x_s, y_s, p):
        k = len(x_s)
        assert k == len(set(x_s)), "points must be distinct"
        def PI(vals):  # upper-case PI -- product of inputs
            accum = 1
            for v in vals:
                accum *= v
            return accum
        nums = []  # avoid inexact division
        dens = []
        for i in range(k):
            others = list(x_s)
            cur = others.pop(i)
            nums.append(PI(x - o for o in others))
            dens.append(PI(cur - o for o in others))
        den = PI(dens)
        num = sum([SSS_Functions._divmod(self, nums[i] * den * y_s[i] % p, dens[i], p)
                for i in range(k)])
        return (SSS_Functions._divmod(self, num, den, p) + p) % p

    def recover_secret(self, shares, prime=_PRIME):
        if len(shares) < 2:
            raise ValueError("Shares have to be more than 2")
        x_s, y_s = zip(*shares)
        return SSS_Functions._lagrange_interpolate(self, 0, x_s, y_s, prime)

    def main_share_creation(self):
        secret, shares = SSS_Functions.create_shares(self, minimum=3, shares=5)

        print('Secret:                                                     ',
            secret)
        print('Shares:')
        if shares:
            for share in shares:
                print('  ', share)

        print('Secret recovered from minimum subset of shares:             ',
            SSS_Functions.recover_secret(self, shares[:3]))
    

class Secondary_Functions(object):   
    path_to_log = ""
    path_separator = ""

    paramplatform= ""

    def Read_Encrypted_File(self, file):
        try:
            with open(file) as stream:
                content = stream.read()
                content = int(content)
                pass
        except Exception as exc:
                Secondary_Functions.WriteLog(self, exc)



    def WriteLog(self, exc):
            # Function to write passed in Exceptions into a log file if so chosen
            # in a try/catch block
            with open(Secondary_Functions.path_to_log + Secondary_Functions.path_separator +
                    'ssslog.txt', "a") as logfile:
                dt = datetime.datetime.now()
                dtwithoutmill = dt.replace(microsecond=0)
                logfile.write("{0}".format(dtwithoutmill))
                logfile.write(": ")
                logfile.write("{0}".format(sys.exc_info()[0]))
                logfile.write(" -----> ")
                logfile.write("{0}".format(exc))
                logfile.write("\n\r")

            print(sys.exc_info()[0])
            print(exc)