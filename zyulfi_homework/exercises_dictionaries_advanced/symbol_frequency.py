# Задача 9: Честота на символите (букви)
# Условие:
# char_frequency(text) брои честотата на всеки символ, игнорира интервали и пунктуация, използвай малки букви.

def char_frequency(curr_string):
    char_dict = {}
    for ch in curr_string.lower():
        if 97 <= ord(ch) <= 122:
            if ch not in char_dict:
                char_dict[ch] = 0
            char_dict[ch] += 1

    return char_dict

print(char_frequency("Hello, world!"))



# Очакван изход (поредността може да е различна):
# {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}

