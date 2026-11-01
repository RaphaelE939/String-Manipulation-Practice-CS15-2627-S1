player_response = input(""
                        "\nHow would you like to process your string?"
                          "\n1.Form a list?"
                          "\n2.Reverse 2 names?"
                          "\n3.Create a title(with 5 words seperated by commas)?"
                          "\n4.Find the total and average of 4 numbers?")
if player_response == "1":
    while True:
        string_to_process = input("Input your string:")
        if "," not in string_to_process:
            print("Please separate your words using commas")
        else:
            u_string = string_to_process.upper()
            print(u_string.replace(",", " | "))
            break
elif player_response == "2":
    while True:
        string_to_process = input("Input your string:")
        word = (string_to_process.strip().title().replace(",", "").split())
        if len(word) != 2:
            print("Please input only 2 names")
        else:
            a = word[0]
            b = word[1]
            print(b + " " + a)
            break
elif player_response == "3":
    while True:
        string_to_process = input("Input your string:")
        words = string_to_process.replace(",", "::").split("::")
        if len(words) != 5:
            print("Please input only 5 words seperated by commas")
        else:
            a = words[0].replace(" ", "").title()
            b = (words[1].replace(" ", "").title())
            c = (words[2].replace(" ", "").title())
            d = (words[3].replace(" ", "").title())
            e = (words[4].replace(" ", "").title())
            print(a + " " + b + " " + c + " " + d + " " + e)
            break
elif player_response == "4":
    while True:
        string_to_process = input("Input your string:")
        try:
            numbas = string_to_process.strip().split(",")
            a = int(numbas[0])
            b = int(numbas[1])
            c = int(numbas[2])
            d = int(numbas[3])
            tot = (a + b + c + d)
            avg = tot / 4
            print(f"Total: {tot}")
            print(f"Average: {avg}")
            break
        except:
            print("Please input 4 valid numbers only")
else:
    print("Please try again! Input the valid numbers or characters needed for your desired process!")