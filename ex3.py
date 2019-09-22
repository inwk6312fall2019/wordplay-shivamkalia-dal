def avoid_word(words,str):
        for i in str:
                if i in words:
                        return 0
        return 1


str= input('enter string')
fin=open('words.txt')
for j in fin:
        words=j.strip()
        k=avoid_word(words,str)
        if k==1:
                print(word)
