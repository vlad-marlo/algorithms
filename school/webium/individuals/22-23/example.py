s = open('24_7_D5.txt').readline()
s = s.replace('XYZY', 'XYZ YZY').replace('XY', '*').replace('ZY', '*').replace('X', ' ').replace('Y', ' ').replace('Z',
                                                                                                                   ' ')
print(len(max(s.split(), key=len)))