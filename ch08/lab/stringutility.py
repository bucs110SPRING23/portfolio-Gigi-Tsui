class StringUtility:
    mystring = "Hello"
    print(mystring[0])
    print(mystring[-1])

    mystring = 'Hello'
    size = len(mystring) #returns 5

    mystring = "Hello" + "Goodbye"
    print(mystring)


    def __init__ (self, stri):
        self.stri = stri

        def __str__ (self):
            return self.stri
        
    def vowels(self):
        vowels_count=sum([1 for char in self.strong.lower()if char in "aeiou" ])
        if vowels_count < 5:
            return str(vowels_count)
        else:
            return "many"

    def bothEnds(self):
        if len(self.stri) <=2:
            return ""
        else:
            return self.stri[:2]+self.stri[-2:]
        
    def fixStart(self):
        if len(self.stri) <=1:
            return self.stri
        else:
            return self.stri[0]+self.stri[1:].replace(self.stri[0], "*")
        
    def asciiSum(self):
        return sum(ord(char) for char in self.stri)
    
    def cipher(self):
        encoded = ""
        for char in self.stri:
            if not char.isalpha():
                result += char
            else:
                shift=len(self.stri)





