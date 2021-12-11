class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDigits = len(digits)
        if numDigits == 0:
            return []
        lettersLists = self.turnNumToLettersList(digits)
        if len(lettersLists) == 1:
            return lettersLists[0]
        def combos(l):
            listLength = len(l)
            if listLength == 1:
                return l[0]
            s = []
            for i in range(listLength): 
                letterCombos = combos(l[i+1:]) 
                for letterCombo in letterCombos:
                    for letter in l[i]:
                        combo = letter + letterCombo
                        s.append(combo)
                        if len(combo) == numDigits:
                            output.append(combo)
            return s
        output = []
        combos(lettersLists)
        return output
        
    def turnNumToLettersList(self, digits: str) -> List[int]:
        output = []
        for i in range(len(digits)):
            digit = digits[i]
            if digit == '2':
                output += [['a', 'b', 'c']]
            elif digit == '3':
                output += [['d', 'e', 'f']]
            elif digit == '4':
                output += [['g', 'h', 'i']]
            elif digit == '5':
                output += [['j', 'k', 'l']]
            elif digit == '6':
                output += [['m', 'n', 'o']]
            elif digit == '7':
                output += [['p', 'q', 'r', 's']]
            elif digit == '8':
                output += [['t', 'u', 'v']]
            elif digit == '9':
                output += [['w', 'x', 'y', 'z']]
        return output
