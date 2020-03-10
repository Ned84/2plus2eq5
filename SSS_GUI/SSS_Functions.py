# -*- coding: utf-8 -*-
"""
*** S-S-S Shamir's Secret Sharing ***
"Easily share secrets in parts and reconstruct them again from
an minimum amount of parts.
Easily switch the Tor-Exit-Node Destination Country in
your Tor-Browser.
GUI Copyright (C) 2020  Ned84 ned84@protonmail.com
For further information visit:
https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# from __future__ import division
# from __future__ import print_function

import random
import functools
import datetime
import sys
import shutil
import os


class SSS_Functions(object):

    total_shares = 2
    min_shares = 2
    secret_out = ""
    prime = 0
    security_lvl = 0

    prime_array = [127,
                   521,
                   607,
                   1279,
                   2203,
                   2281,
                   3217,
                   4253,
                   4423,
                   9689,
                   9941,
                   11213,
                   19937,
                   21701,
                   23209,
                   44497,
                   86243,
                   110503,
                   132049,
                   216091,
                   756839,
                   859433,
                   1257787,
                   1398269,
                   2976221,
                   3021377,
                   6972593,
                   13466917,
                   20996011,
                   24036583,
                   25964951,
                   30402457,
                   32582657,
                   37156667,
                   42643801,
                   43112609,
                   57885161,
                   74207281,
                   77232917,
                   82589933]

    _RINT = functools.partial(random.SystemRandom().randint, 0)

    def __init__(self):
        pass

    def _eval_at(self, polynomial, x, prime):
        accum = 0
        for coeff in reversed(polynomial):
            accum *= x
            accum += coeff
            accum %= prime
        return accum

    def create_shares(self, minimum, shares, secret, prime):
        if minimum > shares:
            raise ValueError("Minimum shares must be more than actual shares")
        elif minimum == 0 or shares == 0:
            raise ValueError(
                "Minimum and total shares must be more than zero.")
        polynomial = [SSS_Functions._RINT(prime - 1) for i in range(minimum)]

        polynomial[0] = secret
        points = [(i, SSS_Functions._eval_at(self, polynomial, i, prime))
                  for i in range(1, shares + 1)]

        c = 1
        for i in range(1, shares + 1):
            c += 1

        return polynomial[0], points

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

        def PI(vals):
            accum = 1
            for v in vals:
                accum *= v
            return accum
        nums = []
        dens = []
        for i in range(k):
            others = list(x_s)
            cur = others.pop(i)
            nums.append(PI(x - o for o in others))
            dens.append(PI(cur - o for o in others))
        den = PI(dens)
        num = sum([SSS_Functions._divmod(
            self, nums[i] * den * y_s[i] % p, dens[i], p)
                for i in range(k)])
        return (SSS_Functions._divmod(self, num, den, p) + p) % p

    def recover_secret(self, shares, prime):
        if len(shares) < 2:
            raise ValueError("Shares have to be more than 2")
        x_s, y_s = zip(*shares)
        return SSS_Functions._lagrange_interpolate(self, 0, x_s, y_s, prime)

    def Share_Creation(self, file, chosen_sec_lvl):
        secret_string = "|"
        secret_string += file

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

        for number in SSS_Functions.prime_array:
            if secret_int.bit_length() < number:
                if number < 127:
                    SSS_Functions.security_lvl = 127
                    SSS_Functions.prime = 2 ** SSS_Functions.security_lvl - 1
                    break
                else:
                    SSS_Functions.security_lvl = number
                    SSS_Functions.prime = 2 ** SSS_Functions.security_lvl - 1
                    break

        if chosen_sec_lvl != "Default":
            if int(chosen_sec_lvl) > SSS_Functions.security_lvl:
                SSS_Functions.security_lvl = int(chosen_sec_lvl)
                SSS_Functions.prime = 2 ** SSS_Functions.security_lvl - 1

        secret, shares = SSS_Functions.create_shares(
            self, minimum=SSS_Functions.min_shares,
            shares=SSS_Functions.total_shares,
            secret=secret_int,
            prime=SSS_Functions.prime)

        return shares

    def Share_Combining(self, sec_lvl, minimum, shares, folder):
        try:
            succeeded = False
            prep_list = [(int(shares[i][:3]), int(shares[i][3:]))
                         for i in range(0, len(shares))]

            # new_shares = []
            # for share in shares:
            #     new_shares[i][0] = i
            #     new_shares[i][1] = shares[i]
            #     i += 1

            prime = 2 ** int(sec_lvl) - 1
            secret = SSS_Functions.recover_secret(
                self, prep_list[:int(minimum)], prime=prime)

            i = 1
            secret_string = ""
            secret_ascii = ""
            for char in str(secret):
                secret_ascii += char

                if i >= 3:
                    secret_string += chr(int(secret_ascii))
                    secret_ascii = ""
                    i = 0
                i += 1

            if "BEGIN PGP MESSAGE" in secret_string[:25]:
                file = folder + "/Combined_Shares.txt.asc"
            else:
                file = folder + "/Combined_Shares.txt"

            with open(file, "w") as stream:
                stream.write(secret_string[1:])

            succeeded = True
            return succeeded

        except Exception as exc:
            Secondary_Functions.WriteLog(self, exc)
            return succeeded


class Secondary_Functions(object):
    path_to_log = ""
    path_separator = ""

    platform = ""
    share_fileNames = []

    def Read_Encrypted_File(self, file):
        try:
            with open(file) as stream:
                content = stream.read()
            return content
        except Exception as exc:
            Secondary_Functions.WriteLog(self, exc)

    def Save_Shares(self, folder, shares, sec_lvl, minimum, total):
        try:
            succeeded = False
            path = folder + "/Shares"
            overview_text = "Security Level:\t" + str(sec_lvl) + "\n" +\
                            "Minimum Shares:\t" + str(minimum) + "\n" +\
                            "Total Shares:\t" + str(total)
            if not os.path.exists(path):
                os.makedirs(path)
            else:
                shutil.rmtree(path)
                os.makedirs(path)
            i = 1

            for share in shares:
                file = path + "/Share_" + str(i) + ".share"
                with open(file, "w") as stream:
                    if i <= 9:
                        stream.write("00" + str(i) + (hex(share[1])[2:]))
                    elif i <= 99:
                        stream.write("0" + str(i) + (hex(share[1])[2:]))
                    else:
                        stream.write(str(i) + (hex(share[1])[2:]))
                i += 1

            file = path + "/Overview" + ".txt"
            with open(file, "w") as stream:
                stream.write(overview_text)

            succeeded = True
            return succeeded
        except Exception as exc:
            Secondary_Functions.WriteLog(self, exc)
            return succeeded

    def Load_Shares(self, files):
        shares_list = []

        stream_line = ""
        stream_int = ""

        for file in files[0]:
            with open(file, "r") as stream:
                stream_line = stream.read()
                stream_int = int(stream_line[3:], 16)
                stream_line = stream_line[:3] + str(stream_int)
                shares_list.append(stream_line)
        return shares_list

    def WriteLog(self, exc):
        # Function to write passed in Exceptions
        # into a log file if so chosen
        # in a try/catch block
        with open(Secondary_Functions.path_to_log +
                  Secondary_Functions.path_separator +
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
