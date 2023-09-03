#import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load the dataset
df=pd.read_csv(r"D:/data_frames/nasa_data_planetary_sys/NASA_Exoplanet_Planetary.csv", low_memory=False)

#print info from the dataset
df.head()
df.info()

#show correlation between planet and star mass and radius
print("Correlation between planet radius and star radius:", df['pl_radj'].corr(df['st_rad']))
print("Correlation between planet mass and star mass:", df['pl_bmassj'].corr(df['st_mass']))

#using matplotlib show a graph containing two axes (xy) containing planet radius on X and star radius on Y.
plt.figure(figsize=(10, 5))
plt.scatter(df['pl_radj'], df['st_rad'])
plt.xlabel('planet radius (in Jupiter radius)')
plt.ylabel('Star Radius (in Solar radius)')
clb = plt.colorbar()
plt.tight_layout()
plt.xlabel('planet radius (in Jupiter radius)')
plt.ylabel('Star Radius (in Solar radius)')
plt.title('Planet Radius vs Star Radius')
plt.legend()
plt.show()