#####
# Import packages
from faker import Faker
import random
import numpy as np
from numpy.random import normal
import pandas as pd

# create object for making fake data
fake = Faker()

# set seed
random.seed(0) # not sure if this is how to do it

# name (First and Last)
name = []
for i in range(500):
  name.append(fake.name())
print(name)

# sample_id (any reference of your choice) if in 8-digit barcode

sample_ID = fake.ean(length=8)

# age
age1 = np.random.choice(70,250)
age2 = np.random.choice(70,250)

age1 = pd.DataFrame(age1, columns=["age"])
age2 = pd.DataFrame(age2, columns=["age"])

#gender
gender1 = ["Male"]*250
gender2 = ["Female"]*250

#bmi
bmi1 = normal(loc=26.5, scale=6, size=250)
bmi2 = normal(loc=26.5, scale=6, size=250)


# height
height1 = normal(loc=178.2, scale=6.35, size=250)
height2 = normal(loc=164.4, scale=5.59, size=250)


df_male = pd.DataFrame({'gender': gender1, 'age': age1, 'bmi': bmi1, 'height': height1})
df_female = pd.DataFrame({'gender': gender2, 'age': age2, 'bmi': bmi2, 'height': height2})

# country

# city

# education level (primary, high school, bachelor, master, phD)

# 10 gene_expression values ranging from

# 5 SNP values (0,1,2)

# case_control status defined as a function of some of your other variables
