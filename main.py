import pandas as pd

pd_df = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {value["letter"]:value["code"] for key,value in pd_df.iterrows()}

user_name = input("Please enter your name:")
nato_result = [data_dict[x.upper()] for x in user_name if x.upper() in data_dict]

print(nato_result)
