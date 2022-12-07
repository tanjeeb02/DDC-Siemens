import BAC0
import time
import pandas as pd
import os
import re

bacnet = BAC0.connect(ip='192.168.1.49/24')
interval = 5

# Declaration of global variables #
keys, results, dev_address, dev_name, obj_name, obj_values = ([] for i in range(6))
data = {}

# File for raw data #
base_raw = os.path.dirname(os.path.abspath(__file__))    
file_raw = open(os.path.join(base_raw, 'source\\raw.csv'))
raw_data = pd.read_csv(file_raw)


 Exporting data to .csv file #
 def export():
     keys = ['Object Name', 'Value']  
     for i,j in zip(keys,results):
         data[i] = j
    
     df = pd.DataFrame(data, columns = keys)
     base_data = os.path.dirname(os.path.abspath(__file__))    
     file_data = os.path.join(base_data, 'source\\data.csv')
     df.to_csv(file_data, index=False)
     print(df, "\n")

# Main Function #
def main():
    bacnet.whois()
    for i in range(len(bacnet.devices)):
        dev_address.append(str(bacnet.devices[i][2])) 
        dev_name.append(bacnet.devices[i][0])
    
    while True:    
        # Reading properties from device #
        for i in range(raw_data.shape[0]):
            for j in range(len(dev_name)):
                if raw_data['Device Name'][i] == dev_name[j]:
                    obj_name.append(raw_data['BACnet Object Name'][i])
                    value = (bacnet.read(str(dev_address[j]) + ' ' + raw_data['BACnet Object type'][i] + ' ' + str(int(raw_data['BACnet Object Instance'][i])) + ' presentValue'))
                    obj_values.append("{:.1f}".format(value))
                else:
                    continue
                
        results.extend((obj_name, obj_values))
        export()
        time.sleep(interval)
        obj_name.clear(); obj_values.clear(); results.clear()
        
        
if __name__ == '__main__':
    main()
