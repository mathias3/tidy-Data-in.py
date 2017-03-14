# Import pandas as pd
import pandas as pd

# Melt df2 into new dataframe: df2_melted
df2_melted = pd.melt(df2, id_vars = "Country")

# print df2_melted
print(df2_melted)

----
# Rename the columns of df2_melted: df2_tidy
df2_tidy = df2_melted.rename(columns = {'variable':'Year','value':'Income'}, inplace = False)

# Print out df2_tidy
print(df2_tidy)
---

# Melt the Black, Blue, and Brown columns of eyes: eyes_melted
eyes_melted =  pd.melt(eyes, id_vars = ["Name", "Wear_Glasses"])

# Rename the variable column and save to eyes_renamed
eyes_renamed = eyes_melted.rename(columns = {'variable':"Eye_Color"}, inplace = False)

# print out eyes_renamed
print(eyes_renamed)
----
# Filter eyes_ranamed and save to eyes_filtered 
eyes_filtered =  eyes_renamed[eyes_renamed.value == 1]

# Delete the `value` column and save to eyes_tidy
eyes_tidy = eyes_filtered.drop(['value'], axis = 1)

# print eyes_tidy
print(eyes_tidy)
