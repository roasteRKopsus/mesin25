import pandas as pd

def capture_csv_suhu(file_link,args):
    open_file = pd.read_csv(file_link, index_col=False, header=0)
    captured_item = open_file.iloc[:,[args]]
    return captured_item

def execute_cleanser():
	df0 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt0.csv', 1).rename(columns={'1': '0'})
	df1 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt0.csv', 59).rename(columns={'59': '1'})
	df2 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt2.csv', 1).rename(columns={'1': '2'})
	df3 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt2.csv', 59).rename(columns={'59': '3'})
	df4 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt4.csv', 1).rename(columns={'1': '4'})
	df5 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt4.csv', 59).rename(columns={'59': '5'})
	df6 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt6.csv', 1).rename(columns={'1': '6'})
	df7 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt6.csv', 59).rename(columns={'59': '7'})
	df8 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt8.csv', 1).rename(columns={'1': '8'})
	df9 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt8.csv', 59).rename(columns={'59': '9'})
	df10 = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt10.csv', 1).rename(columns={'1': '10'})
	dfec = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/reportheader.csv',24).rename(columns={'end_roast_bt': 'end_celcius'})
	dfet = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/reportheader.csv',25).rename(columns={'end_roast': 'end_time'})
	dfrc = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/bt10.csv', 60)
	dfrh = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/reportheader.csv',1)
	dfdr = capture_csv_suhu('/home/lohdjinavieroastery/Documents/test_env/db_raw/reportheader.csv',9)
	roastlog_df = pd.concat([dfrh, dfrc, dfdr, df0, df1,df2, df3,df4, df5,df6, df7,df8, df9,df10, dfec, dfet], axis=1, join='inner')
	roastlog_df.to_csv('/home/lohdjinavieroastery/Documents/test_env/data_result/roastlog_raw.csv')
	

