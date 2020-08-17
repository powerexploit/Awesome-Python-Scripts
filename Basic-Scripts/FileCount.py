filename=input("Enter the filename:")
with open(filename) as f1:
  text=f1.read()
  count_tab=0
  count_space=0
  count_nl=0
  for char in text:
    if char=='\t':
      count_tab += 1
    if char==' ':
      count_space += 1
    if char=='\n':
      count_nl += 1

print("TABS= ",count_tab)
print("SPACES= ",count_space)
print("NEW LINES= ",count_nl)
