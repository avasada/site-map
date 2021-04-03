import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd


with open("hello_world_urls.txt") as F:
    urls = eval(F.read())

nodes = []
for key in urls:
    nodes.append(key)

edges = []
for key in nodes:
    edge = urls[key]
    edges.append(edge)

def create_df():
    return pd.DataFrame(
        
        {'node_name': nodes,
         
         'edges': edges},
        
         )
    
df = create_df()

df["count"] = df["edges"].transform(lambda x: len(x))

plt.figure(figsize = (10, 6))

plt.scatter(df.index, df["count"])
plt.xticks(df.index, df["node_name"], rotation = 90)
plt.ylabel("number of hyperlinks")
plt.xlabel("helloworld urls")
plt.title("helloworld sitemap", size = 20)
plt.savefig("helloworld_sitemap.png")