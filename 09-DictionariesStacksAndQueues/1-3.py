###
# Describes a mobile phone with a dictionary
#

# A dictionary stores data as key: value pairs
mobile = {
    "OS": "Android",
    "Brand": "Samsung",
    "Model": "Galaxy S24",
    "RAM_GB": 8,
    "Storage_GB": 256,
    "Color": "Black"
}

# items() returns (key, value) pairs, unpacked into two variables
for key, value in mobile.items():
    print(f"{key} : {value}")