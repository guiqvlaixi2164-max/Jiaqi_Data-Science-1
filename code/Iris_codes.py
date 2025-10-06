# Preparations
import os  
import pandas as pd     # for data processing
import matplotlib.pyplot as plt     # for plotting

# These lines are for reading the csv file path correctly
script_dir=os.path.dirname(os.path.abspath(__file__))  
data_path=os.path.join(script_dir, "..", "data", "Iris.csv")  
df= pd.read_csv(data_path)

# Using pandas.groupby() to classify data by species, and to calculate the means
df_group=df.groupby(["Species"]).agg(
    mean_sepal_length=("SepalLengthCm","mean"),
    mean_sepal_width=("SepalWidthCm","mean"),
    mean_petal_length=("PetalLengthCm","mean"),
    mean_petal_width=("PetalWidthCm","mean")
).sort_values(by="mean_sepal_length")
print (df_group)

# Using matplotlib to plot a barchart
df_group.plot(kind='barh', figsize=(12,7))
plt.title("Average Sepal & Petal Length & Width by Iris Species")
plt.xlabel("Unit:cm")

# saving the df_group output and the barchart to the 'output' dir correctly
output_dir = os.path.join(script_dir, "..", "output")
df_output_path = os.path.join(output_dir, "iris_output.csv")
df_group.to_csv(df_output_path, index=True, encoding="utf-8")

plot_output_path = os.path.join(output_dir, "iris_plot.png")
plt.savefig(plot_output_path, dpi=300, bbox_inches="tight")
plt.show()
