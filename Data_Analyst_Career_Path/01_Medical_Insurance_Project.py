'''
Suppose you are a medical professional curious about how certain factors contribute to medical insurance costs. Using a formula that estimates a person’s yearly insurance costs, you will investigate how different factors such as age, sex, BMI, etc. affect the prediction.
'''

# create the initial variables below
'''
These are the variables we will need to create:
age: age of the individual in years
sex: 0 for female, 1 for male*
bmi: individual’s body mass index
num_of_children: number of children the individual has
smoker: 0 for a non-smoker, 1 for a smoker

Create the following variables for a 28-year-old, nonsmoking woman who has three children and a BMI of 26.2.
'''

age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

'''
insurance_cost = 250 ∗ age − 128 ∗ sex
+ 370 ∗ bmi + 425 ∗ num_of_children
+ 24000 ∗ smoker − 12500
'''
# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
# add 4 years to our age variable
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")

age -= 4   # reset age

# BMI Factor
# Where bmi was increased by 3.1
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")

bmi -= 3.1 # reset bmi

# Male vs. Female Factor
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars")

sex = 0 # reset sex