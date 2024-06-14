import pandas as pd
import plotly
import plotly.express as px
from os import path

dir="c:/temp/"
dataIn=path.join(dir,"roomAlert-log.csv")
pngOut=path.join(dir,"roomAlert-log.png")
htmlOut=path.join(dir,"ServerRoomTemps.html")
sortfile=path.join(dir,"sort-log.csv")

raURL="https://raapi-production.roomalert.com/api/v1/device-data/public/samples/csv?publicHash=2634e4e3-af92-4e01-85c2-00b460826768&startTime=1716467471&endTime=1716489071&temperatureScale=F&timeZone=America/Chicago&reportName=Data%20Group%201_2024-05-23_01-31-11.csv"

df = pd.read_csv(dataIn)
#df = pd.read_csv(raURL)


print(df)

#drop 1st row
#df = df.iloc[1:]
#print(df)

#add new headders
#df.loc[1:] = ['Timestamp','Back-F','Front-F','Internal-F','Internal-%RH','Internal-Power']
#df.columns = ['Timestamp','Back-F','Front-F','Internal-F','Internal-%RH','Internal-Power']
print(df)

df = (df.sort_values(by="Timestamp"))
#print(df.sort_values(1,ascending=True,inplace=True))
#print("\n",df)

#fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')

fig = px.line(df, x="Timestamp", y = ["Back-F", "Front-F", "Internal-F", "Internal-%RH"], title='Server Room Temperature & %RH')

#fig.show()
plotly.offline.plot(fig, filename=htmlOut)
fig.write_image(pngOut)

print(df)
df.to_csv(sortfile, mode='a', index=False)
