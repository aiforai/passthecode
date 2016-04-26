#!/usr/bin/python
# -*- coding: utf-8 -*-
import crypt


def testpass(cryptPass):
    salt = cryptpass[0:2]
    dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptword = crypt.crypt(word, salt)
        if cryptword == cryptpass:
            print '[+] Found Password: ' + word + '\n'
            return
    print '[-] Password Not Found.\n'
    return


def main():
    passfile = open('passwords.txt')
    for line in passfile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptpass = line.split(':')[1].strip(' ')
            print '[*] Cracking Password For: ' + user
            testPass(cryptpass)


if __name__ == '__main__':
    main()
