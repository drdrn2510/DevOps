items = []
my_dict = {}
while (inputdata := input("Enter a string (leave empty to stop): ")):
    items.append(inputdata)

print(f"Your list: {items}")


for item in items:
    print(f"enter {item} IP address")
    my_dict[item] = input("IP address: ")


print(f"Your dictionary: {my_dict}")

servername=input("Enter server name: ")

if servername in my_dict:
    print(f"{servername} has IP address {my_dict[servername]}")
