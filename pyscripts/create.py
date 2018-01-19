# Create main folder
import os
import sys
f_path = r'C:\users\SaberH\home\/' + sys.argv[1] 
if not os.path.exists(f_path):
	os.makedirs(f_path, mode=0o777, exist_ok=False)
# create html file
# f= open("dace/file.txt", "w+")
# for i in range(10):
#     f.write("this is line %d\r\n" % (i+1))
# f.close()
