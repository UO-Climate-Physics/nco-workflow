import os

ncrcom = 'ncrcat '

tmin = 2400
tmax = 2409
inc = 2

for i in range(tmin, tmax+1, inc):
    ncrcom += 'a023.' + str(i) + '.nc '

ncrcom += 'incof' + str(inc) + '.nc'

os.system(ncrcom)
