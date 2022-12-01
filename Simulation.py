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

df=pd.DataFrame()

# country & city
country_city = pd.read_csv('worldcities.csv', usecols=['city', 'country']).sample(500)

df["city"] = country_city["city"]
df["country"] = country_city["country"]

# gender
gender = np.random.randint(2, size=500)
gender = np.where(gender == 1, "Male", "Female")

df["gender"] = gender

# name (First and Last)
def gen_name(x):
    if x == "Female":
        return fake.name_female()
    else: 
        return fake.name_male()

name = df["gender"].apply(gen_name)
df["name"] = name

# sample_id (any reference of your choice) if in 8-digit barcode
sample_ID = np.random.randint(500, size=500)

df["sample_ID"] = sample_ID

# age
age = np.random.choice(range(18,80),500)

df["age"] = age

#bmi
def gen_bmi(x):
    if x == "Female":
        return normal(loc=22.5, scale=5, size=1)[0]
    else: 
        return normal(loc=26.5, scale=6, size=1)[0]

df["bmi"] = df["gender"].apply(gen_bmi)


# height
def gen_height(x):
    if x == "Female":
        return normal(loc=164.4, scale=5.59, size=1)[0]
    else: 
        return normal(loc=178.2, scale=6.35, size=1)[0]

df["height"] = df["gender"].apply(gen_height)

# education level (primary, high school, bachelor, master, phD)
elements=["primary", "high school", "bachelor", "master", "phD"]

education_level=[]

for i in range(500):
    sample_education=random.sample(elements, k=1)
    education_level.append(sample_education[0])
 
df["education_level"] = education_level

# 10 gene_expression values ranging from

######## 5 SNP values (0,1,2) ##########
# rs2231142: MAF=0.10
# rs16890979: MAF=0.30
# rs2910164: MAF=0.31
# rs6922269: MAF=0.27
# rs17228212: MAF=0.26
def calc_hwe(maf):
    p_0 = round((1-maf)*(1-maf), 2)
    p_1 = round(maf*(1-maf), 2)
    p_2 = round(maf*maf, 2)
    p = [p_0, p_1, p_2]
    return p

def gen_SNP(x):
    return random.choices([0,1,2], calc_hwe(x), k=500)

MAFs = pd.DataFrame([0.1, 0.3, 0.31, 0.27, 0.26], columns = ["MAF"])
test = MAFs["MAF"].apply(gen_SNP)

df_t = pd.DataFrame(list(test)).T
df_t.columns = ["SNP1", "SNP2", "SNP3", "SNP4", "SNP5"]

df_t.head()

# case_control status defined as a function of some of your other variables
# logit_p = b0 + b1*var1
# p = 1/(1+exp(-(logit_p)))
# y ~ binomial(1, p)

#all_data = [sample_ID], [name], [gender]
#all_data_df = pd.DataFrame(all_data, columns=['sample_id', 'name', 'gender'])
