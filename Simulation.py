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

#country

# gender
gender = np.random.randint(2, size=500)
gender = np.where(gender == 1, "Male", "Female")

gender = pd.DataFrame(gender, columns=["gender"])

# name (First and Last)
def gen_name(x):
    if x == "Female":
        return fake.name_female()
    else: 
        return fake.name_male()

name = gender.apply(lambda x: gen_name(gender[x]))

gender["name"] = name

# sample_id (any reference of your choice) if in 8-digit barcode
sample_ID = []
for i in range(500):
    sample_ID.append('000' + fake.ean(length=8))

gender["sid"] = sample_ID

# age
age = np.random.choice(70,500)

age = pd.DataFrame(age, columns=["age"])

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
