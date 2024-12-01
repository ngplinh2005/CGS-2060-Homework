# CGS 2060 – Fall Semester 2024
# CGS 2060 Homework #4 – Fundraising!
# Linh Nguyen

import pandas as pd
import matplotlib.pyplot as plt

# 1. Horizontal Bar Graph - Number of Dogs Saved
bar_data = pd.read_csv("HW #4 - bar.csv")
print(bar_data.head())  

plt.barh(bar_data["Year"], bar_data["Dogs Saved"], color="skyblue")
plt.title("Number Of Dogs Saved")
plt.xlabel("Dogs Saved")
plt.ylabel("Year")
plt.show()
plt.clf()

# 2. Line Graph - Individual Dog Costs
line_data = pd.read_csv("HW #4 - line.csv", index_col="Year")
print(line_data.head())  

plt.plot(line_data.index, line_data["Chipped"], label="Chipped", marker="o")
plt.plot(line_data.index, line_data["Shots"], label="Shots", marker="s")
plt.title("Individual Dog Costs")
plt.xlabel("Year")
plt.ylabel("Cost Per Dog")
plt.legend()
plt.xticks(line_data.index)  # Ensure x-axis uses integers
plt.show()
plt.clf()

# 3. Scatter Plot - Age vs. Weight
scatter_data = pd.read_csv("HW #4 - scatter.csv")
print(scatter_data.head())  

plt.scatter(scatter_data["Age"], scatter_data["Weight"], color="green", alpha=0.6)
plt.title("Age vs. Weight")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()
plt.clf()

# 4. Pie Chart - Dog Genders
pie_data = pd.read_csv("HW #4 - pie.csv")
print(pie_data.head()) 

labels = pie_data["Gender"]
sizes = pie_data["Percent"]
explode = [0.2 if label == "Neutered Male" else 0 for label in labels]

plt.pie(sizes, labels=labels, explode=explode, autopct="%1.1f%%", startangle=90)
plt.title("Dog Genders")
plt.show()
plt.clf()

print("Done!")