"""
caesar Cipher decrypter/encrypter
khaled

"""
import optparse
import sys
import os
class caesar_cipher(object):
    def __init__(self,message='',key=0,_file=''):
        self.message = message
        self.key     = key
        self.chars   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._file    = _file
    def encode(self):
        plaintext = ""
        for letter in self.message:
            if letter.islower():
                self.chars = self.chars.lower()
            else:
                self.chars = self.chars.upper()
            if letter in self.chars:
                if (self.key + self.chars.find(letter)) >= self.chars.__len__():
                    plaintext += self.chars[self.key + self.chars.find(letter) - self.chars.__len__()]
                else:
                    plaintext += self.chars[self.key + self.chars.find(letter)]
            else:
                plaintext += letter.lstrip()
        return plaintext

    def decode(self):
        cipher = ""
        for letter in self.message:
            if letter.islower():
                self.chars = self.chars.lower()
            else:
                self.chars = self.chars.upper()
            if letter in self.chars:
                if self.chars.find(letter) - self.key < 0 :
                    cipher += self.chars[self.chars.find(letter) - self.key + self.chars.__len__()]
                else:
                    cipher += self.chars[ self.chars.find(letter) - self.key]
            else:
                cipher += letter.lstrip()
        return cipher

    def bruteforce(self):
        for index in range(self.chars.__len__()):
            self.key = index
            print "using key %s : %s " % ( index , self.decode())

    def bruteforce_file(self):
        try:
            with open(self._file,"r") as f:
                lines =  [line for line in f.readlines()]
        except IOError:
            print "cannot access file ( permission denied / file not found)"
            exit(0)
        all_lines = ''.join(lines)
        self.message = all_lines
        self.bruteforce()


    def encode_file(self):
        try:
            with open(self._file,"r") as f:
                lines  = [ line for line in f.readlines()]
                for line in lines:
                    self.message = line
                    print self.encode()
        except IOError as e:
            print "cannot access file ( permission denied / file not found)"
            exit(0)

    def decode_file(self):
        try:
            with open(self._file,"r") as f:
                lines = [line for line in f.readlines()]
                for line in lines:
                    self.message = line
                    print self.decode()
        except IOError as e:
            print "cannot access file ( permission denied / file not found)"
            exit(0)
def main():
    parser = optparse.OptionParser('Usage : python %s -t/f <text/file> -k <key> -o operation . \n \
    available operations : \n\t d : decode \n\t e : encode \n\t b : bruteforce \n \
    examples : \n\tpython %s -t KhAlEd -k 6 -o e\n\tpython %s -t QnGrKj -k 6 -o d\n \
    \tpython %s -t QnGrKj -o b\n\tpython %s -f /etc/passwd -k 5 -o e' % (sys.argv[0],sys.argv[0],sys.argv[0],sys.argv[0],sys.argv[0]))
    parser.add_option('-t',dest='inputt',type='string',help="missing text input")
    parser.add_option('-f',dest='inputf',type='string',help="missing input file")
    parser.add_option('-k',dest='inputk',type='int',help="missing cipher key")
    parser.add_option('-o',dest='inputo',type='string',help="missing operation")
    (options , args) = parser.parse_args()
    if (options.inputt == None and options.inputf == None ) or options.inputo == None or (options.inputt != None and options.inputf != None):
        print parser.usage
        exit(0)
    else:
        handle = caesar_cipher(options.inputt , options.inputk , options.inputf)
        if options.inputo == "e":
            if options.inputf == None:
                print handle.encode()
            else:
                handle.encode_file()
        elif options.inputo == "d":
            if options.inputf == None:
                print handle.decode()
            else:
                handle.decode_file()
        elif options.inputo == "b":
            if options.inputf == None:
                handle.bruteforce()
            else:
                handle.bruteforce_file()
        else:
            print "not a valid operation"


if __name__ == '__main__':
    main()
