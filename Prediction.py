import pandas as pd
def check_for_disease():
    pd.read_csv("/static/Dataset/Dataset.csv")
    print(pd.head())
print('ok')    
check_for_disease()