def like_a_Moth_to_a_Flame(words_split):
    
    for i in words_split:
        print(i,sep=' ')

    print(len(words_split))
words = "Today we're learning how to study for exams with scientifically-proven techniques. We start by talking about why rereading, highlighting and summarising are pretty inefficient, and then talk about the evidence behind Active Recall as the most efficient revision technique. We end with a few suggestions as to how to incorporate Active Recall into your study routine. Enjoy xx"

words_split=words.split()

like_a_Moth_to_a_Flame(words_split)
