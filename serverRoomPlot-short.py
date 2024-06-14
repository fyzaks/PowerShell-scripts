from pathlib import Path
import pandas as pd
import plotly
import plotly.express as px
from os import path

dir="c:/temp/"

#dirG="c:/temp/"
dirG="H:/INTRANET/common/"

dataIn=path.join(dir,"roomAlert-log.csv")
pngOut=path.join(dir,"roomAlert-log-short.png")
htmlOut=path.join(dir,"ServerRoomTemps-short.html")
htmlOutG=path.join(dirG,"ServerRoomTemps-short.html")
shortFile=path.join(dir,"sort-log.csv")

out = open(shortFile, "w")


txt = Path(dataIn).read_text()

# Read in the first line. It has the headers.
top = '\n'.join(txt.splitlines()[:1]) + "\n"
# Read in the latest log enteries.
short = '\n'.join(txt.splitlines()[-150:]) + "\n"

# Merge the two
out.write(top)
out.write(short)

out.close()

# Start Making the html graph
#out = open(shortFile, "r")
df = pd.read_csv(shortFile)

df.columns = ['Timestamp','Back-F','Front-F','Internal-F','Internal-%RH','Internal-Power']

df = (df.sort_values(by="Timestamp"))

figurl = px.line(df, x="Timestamp", y = ["Back-F", "Front-F", "Internal-F", "Internal-%RH"], title='Server Room Temperature & %RH - Last ~7 Days')

plotly.offline.plot(figurl, filename=htmlOut)

#out.close()
print("That's all folks")