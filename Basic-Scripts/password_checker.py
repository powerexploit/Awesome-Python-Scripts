  # Password-checker

   #This program can help us to find how many times a password has been used,either on anonymous or your own used sites.

   #It will take help of requests,hashlib and sys modules

   #You need to install pip3 into your machine to be able to use this code.

  
  
import requests
import hashlib
import sys

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f': {res.status_code}, got some eror,please check API')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should change your password right now!')
    else:
      print(f'{password} was not found,very good password.')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
