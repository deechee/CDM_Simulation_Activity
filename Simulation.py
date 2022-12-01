#####
# Import packages
from faker import Faker
import random
import numpy as np
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
age = np.random.choice(70,500)

age = pd.DataFrame(age, columns=["age"])

# gender
gender = np.random.randint(2, size=500)
gender = np.where(gender == 1, "Male", "Female")

gender = pd.DataFrame(gender, columns=["gender"])


# bmi

# height

# country

# city

# education level (primary, high school, bachelor, master, phD)

# 10 gene_expression values ranging from

# 5 SNP values (0,1,2)

# case_control status defined as a function of some of your other variables


#all_data = [age], [sample_id]
#all_data_df = pd.DataFrame(all_data, columns=['name', 'sample_id'])
