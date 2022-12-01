#####
# Import packages
from faker import Faker

# create object for making fake data
fake = Faker()

# name (First and Last)
name = []
for i in range(500):
  name.append(fake.name())
print(name)

# sample_id (any reference of your choice)
# age
# gender
# bmi
# height
# country
# city
# education level (primary, high school, bachelor, master, phD)
# 10 gene_expression values ranging from
# 5 SNP values (0,1,2)
# case_control status defined as a function of some of your other variables
