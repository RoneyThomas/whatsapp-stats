from chat import Chat
import pandas as pd

test = Chat("./WhatsApp Chat with Camp Kappa-1.txt")
msg_df, ws_df = test.df()
print(msg_df.head())
print(ws_df.head())
