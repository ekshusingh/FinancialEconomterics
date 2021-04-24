import pandas as pd
import technical_indicator as ti
import sys
import talib as ta

sys.stdout = open('output.txt','w')

file_path = "AARTIIND__EQ__NSE__NSE__MINUTE.csv"
data = pd.read_csv(file_path, low_memory = False)
data = data[['open','high','low','close']]
data = data.dropna()
data = data.reset_index()
data = data.rename(columns={'open':'Open','high':'High','low':'Low','close':'Close'})

data['output'] = ''

for i in range(1,data.shape[0]-4):
    data['output'][i]=(data['Close'][i+4]-data['Close'][i-1])/data['Close'][i-1]

data["output"]=data["output"]*1000

data=ti.add(data)


data.to_csv('preprocessed_data.csv',sep=',',index=True,header=True)

print('done')