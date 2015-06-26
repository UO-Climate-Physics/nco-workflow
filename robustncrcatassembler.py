import os
from math import fmod

dirlist = os.listdir('/Users/BisharaKorkor/research/netcdfscripts')

ncfiles = []

for file in dirlist:
    if file.endswith('.nc'):
        ncfiles.append(file)

tmin = int(ncfiles[0].split('.')[1])
ncrcom = 'ncrcat '
inc = 2 # timestep increment i.e. 3 if you want to hourly resolution for times steps of 20 min.

for file in ncfiles:
    print file
    if fmod(int(file.split('.')[1]) - tmin, inc) == 0:
        ncrcom += file + ' '

ncrcom += 'incof' + str(inc) + '.nc'

os.system(ncrcom)
