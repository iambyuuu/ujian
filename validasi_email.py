import re

def Ujivalidasi(email):
          return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$', email)

valid=Ujivalidasi(input('MASUKKAN NAMA EMAIL ANDA :'))
if valid:
          print('VALID')
else:
          print('INVALID')


