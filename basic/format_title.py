string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"
words = string_to_process.replace(",","::").split("::")
a = words[0].replace(" ", "").title()
b = (words[1].replace(" ", "").title())
c = (words[2].replace(" ", "").title())
d = (words[3].replace(" ", "").title())
e = (words[4].replace(" ", "").title())
print(a+" "+b+" "+c+" "+d+" "+e)
# Expected output: "The Tale Of Two Cities"