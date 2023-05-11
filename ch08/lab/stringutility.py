
class StringUtility:
    mystring = "Hello"
    print(mystring[0]) #prints H
    print(mystring[-1]) #prints o

    mystring = 'Hello'
    size = len(mystring) #returns 5

    mystring = "Hello" + "Goodbye"
    print(mystring)

    def __init__(self, string):
        self.string= string
    
    def __str__(self):
        return self.string
    
    def vowels(self):
        vowels_count = sum([1 for char in self.string.lower()if char in "aeiou"])
        if vowels_count < 5:
            return str(vowels_count)
        else: 
            return "many"
    
    def bothEnds(self):
        if len(self.string) <= 2:
            return ""
        else:
            return self.string[:2] + self.string[-2:]
        
    def fixStart(self):
        if len(self.string) <=1:
            return self.string
        else:
            return self.string[0]+self.string[1:].replace(self.string[0], "*")
        
    def asciiSum(self):
        return sum(ord(char) for char in self.string)
    
    def cipher(self):
        new_string = ""
        shift_amount = len(self.string)
        char_values = [ord(char) for char in self.string]

        for i in range(shift_amount):
            if (65 <= char_values[i] <= 90) or (97 <= char_values[i] <= 122):
                if (char_values[i] > 96) and (char_values[i] + shift_amount > 122):
                    char_values[i] = char_values[i] - 26
                elif (char_values[i] < 91) and (char_values[i] + shift_amount > 90):
                    char_values[i] = char_values[i] - 26
                if shift_amount > 26 and i > 0:
                    char_values[i] = char_values[i] - 26
                char_values[i] = char_values[i] + shift_amount

        for i in range(len(char_values)):
            new_string = new_string + chr(char_values[i])
        
        return new_string

        # uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]

