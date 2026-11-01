string_to_process = "   sMitH, aLeX    "
word = (string_to_process.strip().title().replace(",","").split())
a = word[0]
b = word[1]
print(b+" "+a)
# Expected output: "Alex Smith"