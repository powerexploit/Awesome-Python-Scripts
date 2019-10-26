#! python27
import sys , os , zipfile
# Command line argument
# First type Program name then Zip folder path and then type ZIP File name
sys.argv
# it take second argument of CMD i.e Folder path
os.chdir(sys.argv[1])
# it takes third argument of cmd Zip File Name with extention ( .zip)
yourZip=zipfile.ZipFile(sys.argv[2])
# It extract Zip File
yourZip.extractall()
yourZip.close()
