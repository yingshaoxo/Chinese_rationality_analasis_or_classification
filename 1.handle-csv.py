import pandas as pd

df = pd.read_csv('all_me.csv')
df = df['Message']

all_text = []
for msg in df:
    msg = str(msg)
    if (('"channel_id":' not in msg) and '"user_id":' not in msg) and ('"users":' not in msg) and ('"chat_id":' not in msg) and ('"photo":' not in msg) and ('nan' != msg):
        print(msg)
        all_text.append(msg)

with open('msgs.txt', 'w') as f:
    f.write("""

——————————————

""".join(all_text))
