secretPassword = "ietuet"

words = "abcdefghijklmnopqrstuvwxyz"

password = ""

for i in range(len(secretPassword)):
    char = secretPassword[i]
    
    for j in range(len(words)):
        if char == words[j]:
            print(f"Found {char} at index {j}")
            
            password = password + char
            break
        
print(password)

for char in secretPassword:
    for word in words:
        if char == word:
            password = password + char
            
print(password)