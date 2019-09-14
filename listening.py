import os
import glob

import data

def main():
	tmp=os.popen('ps -A | grep ffmpeg')
	if(len(tmp.read())!=0):
		#print('processing,exit')
		return

	start_list=glob.glob('*.start')	

	process_file=open('%sprocess.txt' % data.root_dir,"r",encoding='utf-8')
	while True:
		pro_temp=process_file.readline()
		if not pro_temp:
			break
		for index in range(len(start_list)):
			start_temp=start_list[index]
			start_temp=start_temp[0:start_temp.index('.')]
			if(pro_temp[:-1]==start_temp):
				os.remove('%s%s.start' % (data.root_dir,start_temp))
				break
	process_file.close()
	
	start_list=glob.glob('*.start')
	if not (start_list):
		#print('no')
		return

	name=start_list[0]
	name=name[0:name.index('.')]
	
	name_list=glob.glob('%s.*' % name)
	name_index=0
	for index in range(len(name_list)):
		if(name_list[index]!='%s.start' % name):
			name_index=index
			break
	file_name=name_list[name_index]
	process_file=open('%sprocess.txt' % data.root_dir,"a+",encoding='utf-8')
	process_file.write('%s\n' % name)
	process_file.close()
	
	os.system('nohup ffmpeg -loglevel warning -i "%s%s" -acodec copy -vcodec libx264 -preset veryslow -crf 22 "%s%s" >%slog.txt 2>&1 &' % (data.root_dir,file_name,data.output_dir,file_name,data.root_dir))

if __name__=="__main__":
	main()
