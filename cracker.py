#!/usr/bin/python
import crypt , os , sys
# linux crypt password cracker
def crack(p , s , d):
    with open(d,"r") as f:
        pwds = [ line for line in f.readlines()]
        for ps in pwds:
            ps = ps.strip("\n")
            if crypt.crypt(ps,s) == p:
                print "[+] cracked %s = %s"  % ( ps , p)
                return
def main():
    if len(sys.argv) == 3:
        password = sys.argv[1]
        wordlist = sys.argv[2]
        salt     = password[:2]
        crack(password,salt,wordlist)
    else:
        print "Usage : python %s <password> <wordlist>" % sys.argv[0]

if __name__ == '__main__':
    main()
