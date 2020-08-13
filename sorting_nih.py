import pandas as pd

data_link = ['/home/lohdjinavieroastery/Documents/test_env/db_raw/bt0.csv', 
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt1.csv', 
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt2.csv', 
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt3.csv', 
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt4.csv',
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt5.csv',
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt6.csv',
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt7.csv',
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt8.csv',
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt9.csv',
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt10.csv',
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/reportheader.csv']

def open_file_raw(file_link, sortir):
    open_file = pd.read_csv(file_link, index_col=False, header=0)
    file_sort = open_file.sort_values(by=[sortir],)
    file_sort.to_csv(file_link)
    
def execute_sorting():   
	m0 = open_file_raw(data_link[0],'roastcode')
	m1 = open_file_raw(data_link[1],'roastcode')
	m2 = open_file_raw(data_link[2],'roastcode')
	m3 = open_file_raw(data_link[3],'roastcode')
	m4 = open_file_raw(data_link[4],'roastcode')
	m5 = open_file_raw(data_link[5],'roastcode')
	m6 = open_file_raw(data_link[6],'roastcode')
	m7 = open_file_raw(data_link[7],'roastcode')
	m8 = open_file_raw(data_link[8],'roastcode')
	m9 = open_file_raw(data_link[9],'roastcode')
	m10 = open_file_raw(data_link[10],'roastcode')
	rhead = open_file_raw(data_link[11],'roastbatch')

