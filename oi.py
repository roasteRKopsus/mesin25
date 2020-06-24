import sys, subprocess 
import os.path


def execute_converter():
	DATABASE = 'froco.mdb'
	save_path = '/home/lohdjinavieroastery/Documents/test_env/db_raw'

	table_names = 'bt0', 'bt2', 'bt4', 'bt6', 'bt8', 'bt10', 'reportheader', 

	for table in table_names:
		if table != '': 
			filename = table.replace(" ","_")+'.csv'
			file_dir = os.path.join(save_path, filename) 
			file = open(file_dir, 'wb')
			contents = subprocess.Popen(["mdb-export", DATABASE, table],stdout=subprocess.PIPE).communicate()[0]
			file.write(contents)
			file.close()
        
        
       
