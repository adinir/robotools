#!/usr/bin/python
import os,sys
#import erc
#robot = erc.ERC()

num_circle_steps = 10
num_pos = num_circle_steps + 2

def main():
  #RPOS = robot.execute_command('RPOS')
  RPOS = ['911.817', '-764.452', '258.905', '-80.46', '-81.78', '-77.02', '0', '0', '0', '0', '0', '0', '0', '0', '0']
  x = float(RPOS[0])
  y = float(RPOS[1])
  z = float(RPOS[2])
  angle = ','.join(RPOS[3:6])
  print(angle)
  print(x)
  print(y)
  print(z)
  outFile = sys.stdout #open('','w')
  outFile.write('/JOB\x0a\x0d//NAME CIRC\x0a\x0d//POS\x0a\x0d///NPOS ')
  outFile.write(str(num_pos))
  outFile.write(',0,0,0\x0a\x0d///TOOL 0\x0a\x0d///RECTAN\x0a\x0d///RCONF 0,0,0,0,0\x0a\x0d')
  #for C in range(num_pos):

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
