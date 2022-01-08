class Patient:
      def __init__(self, name, age, sex, bmi, num_of_children, smoker):
            self.name = name
            self.age = age
            self.sex = sex                     #  0 for male and 1 for female
            self.bmi = bmi
            self.num_of_children = num_of_children
            self.smoker = smoker          #  0 for non-smoker and 1 for smoker

      def estimated_insurance_cost(self):
            estimated_insurance_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
            print(f'{self.name}\'s estimated insurance costs is {estimated_insurance_cost} dollars.')

      def update_name(self, new_name):
            if not type(new_name) is str:
                  raise TypeError('Please enter the new patient name as string.')
            else:
                  self.name = new_name
                  print(f'The patirnt name has been updated to {self.name}.')
                  self.estimated_insurance_cost()

      def update_age(self, new_age):
            self.age = new_age
            print(f'{self.name} is now {self.age} years old.')
            self.estimated_insurance_cost()

      def update_sum_children(self, new_sum_children):
            self.num_of_children = new_sum_children
            if self.num_of_children <= 1:
                  print(f'{self.name} has {self.num_of_children} child.')
            else:
                  print(f'{self.name} has {self.num_of_children} children.')
            self.estimated_insurance_cost()

      def patient_profile(self):
            patient_information = {}
            patient_information['Name'] = self.name
            patient_information['Age'] = self.age
            patient_information['Sex'] = self.sex
            patient_information['BMI'] = self.bmi
            patient_information['Number of Children'] = self.num_of_children
            patient_information['Snoker'] = self.smoker
            return patient_information

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
# print(patient1.name)
# print(patient1.age)
# print(patient1.sex)
# print(patient1.bmi)
# print(patient1.num_of_children)
# print(patient1.smoker)
# patient1.estimated_insurance_cost()
# patient1.update_age(26)
# patient1.update_sum_children(1)
# print(patient1.patient_profile())
patient1.update_name(1)
patient1.update_name('Tom Smith')