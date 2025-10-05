# Iris - Mini Project for Data Science 1

Date: 05/10/2025

----------------------------
## Overview:
This mini project uses the Iris dataset to calculate the mean length and width of the sepal and petal of each iris species and plots them in a table. The main purpose of this project is to practice using Git and GitHub.<br>
The Python code in this project is located in the code folder, the Iris dataset is located in the data folder, and the output file and chart are located in the output folder above. Running the code will also automatically save the output to the output folder.
The code will automatically generate two output files in the output folder. <br>


----------------

## Data:
The dataset used in this project is Iris.csv, located in the data folder above.<br>
I used the iris dataset in this project because it is a simple, clear, and classic dataset, making it ideal for a simple data analysis and programming exercise.<br>
The Iris dataset contains **50 samples of each of the three iris species**, and records the **length** and **width** of the **sepal** and **petal** of each flower: 
- **Setosa**
- **Versicolor** 
- **Virginica**.

In this project, I used Python to categorize data by species. For each species, I calculated the **mean length and width of the sepal and petal**. Then, I created a table and plotted a bar chart to compare the size differences of the sepal and petal between the three iris species.<br>
The data source is https://www.kaggle.com/datasets/saurabh00007/iriscsv/code.

----------------

## Folder Structure:
```
Jiaqi_Data-Science-1/  
├── code/                 
│   └── Iris_codes.py          
├── data/               
│   └── Iris.csv         
├── output/             
│   ├── iris_output.csv   
│   └── iris_plot.png 
├── requirements.txt     
├── environment.yml      
└── README.md            
```
---------

## Environmental Requirements:
This project uses Python and utilizes:
- **pandas** *(for data processing)*
- **matplotlib** *(for plotting)*
- **os** *(for correctly specifying the dump file path)*

os is a built-in Python library and does not require installation.<br>
To configure your environment, first please ensure that Python 3.8+ is already installed. Next, Open Git Bash and use one of the following methods:<br>
*Option 1 (conda)*
```
conda env create -f environment.yml
conda activate iris-env
```
*Option 2 (pip)*
```
pip install -r requirements.txt
```
----------

## Steps to Reproduce

- Choose a folder in which you want to clone this project, open Git Bash, and type:
```
cd your_folder_path 
# For example: cd C:\Users\your_name\Desktop
git clone https://github.com/guiqvlaixi2164-max/Jiaqi_Data-Science-1.git
cd Jiaqi_Data-Science-1
```
- Configure the required environment. The steps for this are described in the Environmental Requirements section above.
- Run the codes. Type in Git Bash:
```
cd code
python Iris_codes.py
```
If nothing goes wrong, the code will automatically save the output to the output folder.
##### ***Note! !*** Do not run the code when you have opened the iris_output.csv file or iris_plot.png file in the output folder!  Close them first and then run the code.

- Check if the output is the same as what is shown below.

Hopefully these steps won't be very complicated!

-------------

## Output Description:

One is a CSV file that records the sample mean of the length and width of the sepal and petal of each iris specie; <br>

| Species |	mean_sepal_length |	mean_sepal_width |	mean_petal_length |	mean_petal_width
|--------|----------|----------|-----------|------|
Iris-setosa	| 5.006 |	3.418 |	1.464 |	0.244
Iris-versicolor |	5.936 |	2.77 |	4.26 |	1.326
Iris-virginica |	6.588 |	2.974 |	5.552 |	2.026

<br>
the other is an image that compares the length and width of the sepal and petal of each iris specie in a bar chart.<br>

![iris_plot](https://raw.githubusercontent.com/guiqvlaixi2164-max/Jiaqi_Data-Science-1/main/output/iris_plot.png)



































