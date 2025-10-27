# Задача 3: Честота на думи
# Напиши програма, която брои срещанията на всяка дума в даден текст (string). Изисквания:
#
# Игнорирай големината на буквите.
# Игнорирай пунктуацията.
# Изведи 3-те най-често срещани думи.

class Words:
    def __init__(self, curr_string):
        self.curr_string = curr_string

    def prepare_of_string(self):
        text = ""
        for ch in self.curr_string.lower():
            if 97 <= ord(ch) <= 122 or ch == " ":
                text += ch
        return text

    def word_frequency(self):
        curr_dict = {}
        word_list = self.prepare_of_string().split(" ")
        print(word_list)
        for curr_word in word_list:
            if curr_word not in curr_dict:
                curr_dict[curr_word] = 0
            curr_dict[curr_word] += 1

        return [word for word in dict(sorted(curr_dict.items(), key=lambda item: (-item[1], item[0]))).keys()][0:3]


w = Words("ASCII stands for American Standard Code for Information Interchange.")

print(w.prepare_of_string())
print(w.word_frequency())
