import zipfile , sys , optparse

def crackzip(fname , words):
    with open(words,"r") as f:
        psds = [line for line in f.readlines()]
        for ps in psds:
            ps = ps.strip("\n")
            zz = zipfile.ZipFile(fname)
            try:
                zz.extractall(pwd=ps)
                print "[+] cracked : password = "+ps
                return
            except Exception as e:
                pass

def main():
    parser = optparse.OptionParser("Usage : python %s -z file.zip -p wordlist" % sys.argv[0])
    parser.add_option("-z" , dest = 'zipname' ,type = "string" , help = "zip archive to crack" )
    parser.add_option("-p" , dest = 'wordlist' , type="string" , help = "passwords list" )
    (options , args) = parser.parse_args()
    zipname  = options.zipname
    wordlist = options.wordlist
    if ( zipname == None or wordlist == None):
        print parser.usage
    else:
        crackzip(zipname , wordlist)

if __name__ == '__main__':
    main()
