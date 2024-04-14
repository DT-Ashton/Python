my_list = list(map(int,input("Nhập list: ").split()))
max_value = my_list[0]
i = 1
while i < len(my_list):
  if my_list[i] > max_value:
    max_value = my_list[i]
  i = i + 1
print("Max của list là:", max_value)
