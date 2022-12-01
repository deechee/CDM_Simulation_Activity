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

# country & city

country_city_raw = pd.read_csv('worldcities.csv')
country_city = country_city_raw[['city_ascii', 'country']]

countries = ['Japan', 'France']


def sample_country_city(country_city, countries, n=500):
    cc_list=[]
    for i in range(n):
        x = 0
        while x == 0:
            data = pd.DataFrame.sample(country_city).values[0]
            country = data[1]

            if country in countries:
                cc_list.append(data)
                x=1
    return cc_list
country_city_list = sample_country_city(country_city, countries) 


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

name = gender["gender"].apply(gen_name)

gender["name"] = name

# sample_id (any reference of your choice) if in 8-digit barcode
sample_ID = np.random.randint(500, size=500)
sample_ID = pd.DataFrame(sample_ID, columns=["sample_ID"])

gender["sample_ID"] = sample_ID

# age
age = np.random.choice(range(18,80),500)

gender["age"] = age

#bmi
def gen_bmi(x):
    if x == "Female":
        return normal(loc=22.5, scale=5, size=1)
    else: 
        return normal(loc=26.5, scale=6, size=1)

bmi = gender["gender"].apply(gen_bmi)
gender["bmi"] = bmi


# height
def gen_height(x):
    if x == "Female":
        return normal(loc=164.4, scale=5.59, size=1)
    else: 
        return normal(loc=178.2, scale=6.35, size=1)

height = gender["gender"].apply(gen_height)

gender["height"] = height

# education level (primary, high school, bachelor, master, phD)
elements=["primary", "high school", "bachelor", "master", "phD"]

education_level=[]

for i in range(500):
    sample_education=random.sample(elements, k=1)
    education_level.append(sample_education[0])

education_level = pd.DataFrame(education_level, columns=["education_level"])
gender["education_level"] = education_level

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

MAFs = [0.1, 0.3, 0.31, 0.27, 0.26]
MAFs.apply(gen_SNP)

SNP_1 = random.choices([0,1,2], calc_hwe(0.1), k=500)


SNP = np.random.randint(3, size=500)

SNP = pd.DataFrame(SNP, columns=["SNP"])
print(SNP)

# case_control status defined as a function of some of your other variables
# logit_p = b0 + b1*var1
# p = 1/(1+exp(-(logit_p)))
# y ~ binomial(1, p)

#all_data = [sample_ID], [name], [gender]
#all_data_df = pd.DataFrame(all_data, columns=['sample_id', 'name', 'gender'])
