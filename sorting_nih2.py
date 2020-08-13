import pandas as pd

data_link1 = [
		'/home/lohdjinavieroastery/Documents/test_env/db_raw/bt0.csv', 
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
		]
data_link2 = ['/home/lohdjinavieroastery/Documents/test_env/db_raw/reportheader.csv']
def open_file_raw(file_link, sortir):
    open_file = pd.read_csv(file_link, index_col=False, header=0)
    file_sort = open_file.sort_values(by=[sortir],)
    file_sort.to_csv(file_link)

def execute_sorting():
	for file in range(len(data_link1)):
		open_file_raw(data_link1[file], 'roastcode')
	for file in range(len(data_link2)):
		open_file_raw(data_link2[file], 'roastbatch')

