import os
os.chdir("E:\\pythonpro")
filehandle = open("testtext2.txt",'r')
read_strs = filehandle.readlines()
out_str = ""
line_lens = len(read_strs)
def testbig(cc):
	if(cc>='a' and cc<='z'):
		return 0
	elif (cc>='A' and cc<='Z'):
		return 1
	else:
		return 2

for i in range(0,line_lens-1):
	str_len = len(read_strs[i])
	for j in range(3,str_len-4):
		if(testbig(read_strs[i][j])==0):
			test_flg = 1
			for k in range(1,4):
				if(testbig(read_strs[i][j-k])!=1 or testbig(read_strs[i][j+k])!=1):
					test_flg = 0
			if(test_flg==1):
				if(testbig(read_strs[i][j-4])==0 and testbig(read_strs[i][j+4])==0):
                                    out_str += read_strs[i][j]



        

