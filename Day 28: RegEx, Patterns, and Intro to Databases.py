#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    check = "@gmail.com"
    emailList = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if emailID[-10:] in check:
            emailList.append(firstName)

    print("\n".join(x for x in sorted(emailList)))

        
        
