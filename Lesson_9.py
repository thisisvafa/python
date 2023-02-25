print("how many kms do you want to convert?")

# kms = input()
# kms = float(input()) 
# kms / 1.60934 # For example, if you select number 50 in terminal => 50 / 1.60934

# OR

kms = input()

miles = float(kms) / 1.60934
# miles = int(kms) / 1.60934
miles =  round(miles,3)

# print("ok you said " + kms)
# print(f"ok you said {kms} KMs")
print(f"ok converted data is: {miles}")
# print(f"ok converted data is: { round(miles,2) }")