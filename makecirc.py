#!/usr/bin/python
import os,sys,math
from datetime import datetime, date, time
#import erc
#robot = erc.ERC()

circle_radius = ((23-6.5)/2)
circle_steps = 13
startAboveDistance = 50 # how far above homing point the first move should be
startAboveSpeed = 46 # 11 23 46 etc 187
descendToHomeSpeed = 46 # just moving from above to touchoff point
cutDepth = 10
cutSpeed = 11
num_pos = circle_steps + 2
Cnum = 0 # coordinate number or MOV number starts at 0

outFile = sys.stdout #open('','w')

def writeHeader(num_pos,jobName):
  global outFile
  outFile.write('/JOB\x0a\x0d//NAME '+jobName+'\x0a\x0d//POS\x0a\x0d///NPOS ')
  outFile.write(str(num_pos))
  outFile.write(',0,0,0\x0a\x0d///TOOL 0\x0a\x0d///RECTAN\x0a\x0d///RCONF 0,0,0,0,0\x0a\x0d')

def writeMain():
  global Cnum,outFile
  Cnum = 0 # reset the counter for the main part of the program
  outFile.write('//INST\x0a\x0d///DATE ')
  outFile.write(datetime.now().strftime("%Y/%m/%d %H:%M")) # 2016/08/02 21:44
  outFile.write('\x0a\x0d///ATTR 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0\x0a\x0d///FRAME BASE\x0a\x0dNOP\x0a\x0d*1\x0a\x0d')

def writeLine(text):
  global outFile
  outFile.write(text+'\x0a\x0d')

def writeCoord(x,y,z,angle):
  global Cnum,outFile
  outFile.write('C'+str(Cnum).zfill(3)+'='+'%0.3f,%0.3f,%0.3f,' % (x,y,z)+angle+'\x0a\x0d')
  Cnum += 1

def writeMOVL(velocity):
  global Cnum,outFile
  outFile.write('MOVL V='+str(velocity)+' C'+str(Cnum).zfill(3)+' CONT\x0a\x0d')
  Cnum += 1

def writeMOVC(velocity):
  global Cnum,outFile
  outFile.write('MOVC V='+str(velocity)+' C'+str(Cnum).zfill(3)+' CONT\x0a\x0d')
  Cnum += 1

def main():
  #RPOS = robot.execute_command('RPOS')
  RPOS = ['911.817', '-764.452', '258.905', '-80.46', '-81.78', '-77.02', '0', '0', '0', '0', '0', '0', '0', '0', '0']
  x = float(RPOS[0])
  y = float(RPOS[1])
  z = float(RPOS[2])
  angle = ','.join(RPOS[3:6])
  writeHeader(num_pos,'CIRC')
  writeCoord(x,y,z+startAboveDistance,angle)
  writeCoord(x,y,z,angle)
  for i in range(circle_steps):
    rads = 2 * math.pi / (circle_steps - 1) * i
    writeCoord(x+circle_radius*math.cos(rads),y+circle_radius*math.sin(rads),z-cutDepth,angle)
  writeMain()
  writeMOVL(startAboveSpeed)
  writeLine('PAUSE')
  writeMOVL(descendToHomeSpeed)
  for i in range(circle_steps):
    writeMOVC(cutSpeed)
  writeLine('JUMP *1')
  writeLine('END')

if __name__ == "__main__":
  main()
'''
C000=764.569,-155.385,-535.165,-98.01,-83.01,-59.58
C001=764.569,-155.385,-585.165,-98.01,-83.01,-59.58
C002=756.319,-155.385,-595.165,-98.01,-83.01,-59.58
C003=764.569,-147.135,-595.165,-98.01,-83.01,-59.58
C004=772.819,-155.385,-595.165,-98.01,-83.01,-59.58
C005=756.319,-155.385,-595.165,-98.01,-83.01,-59.58
//INST
///DATE 2016/08/02 21:44
///ATTR 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0
///FRAME BASE
NOP
*1
MOVL C000 V=46.0 CONT
PAUSE
MOVL C001 V=11.0 CONT
MOVC C002 V=11.0 CONT
MOVC C003 V=11.0 CONT
MOVC C004 V=11.0 CONT
MOVC C005 V=11.0 CONT
JUMP *1
END
'''
