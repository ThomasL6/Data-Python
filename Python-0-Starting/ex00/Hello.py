ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modif liste
ft_list[1] = "World"

# Modif tuple
y = list(ft_tuple)
y[1] = "France"
ft_tuple = tuple(y)

# Modif set
ft_set.remove("tutu!")
ft_set.add("Le Havre")
ft_set_sorted = sorted(ft_set)
# Modif dictionnary
ft_dict["Hello"] = "42Le Havre"


print(ft_list)
print(ft_tuple)
# print(ft_set)
print(f"{{{' , '.join(ft_set_sorted)}}}")
print(ft_dict)
