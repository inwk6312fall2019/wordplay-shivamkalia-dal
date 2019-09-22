def has_no_e():
    fin = open("words.txt","r")
    toal_no_of_words = 0
    count = 0
    for line in fin:
        toal_no_of_words = toal_no_of_words + 1
        words = line.strip()
        if words.find("e") == -1:
            print(words)
            count = count + 1
    percent_of_no_e = (count/total_no_of_words) * 100
    print("Percent:", percent_of_no_e)

