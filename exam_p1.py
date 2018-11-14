
def get_value(name):
    # return the value of given name
    letter_dict = {'a': 1, 'b':2, 'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
    }
    value = sum(letter_dict[l] for l in name)
    return value


def  get_name_list(file_name):
    '''
    return list of names from selected file input

    list includes only first names in lower case
    '''
    full_name_list = open(file_name).read().splitlines()
    first_name_list = [full_name.split(' ')[0] for full_name in full_name_list]
    name_list = [name.lower() for name in first_name_list]
    return name_list


def who_has_highest_value(name_list):
    '''
    return the name with highest value among the given name_list
    '''
    i = 0
    highest_name = name_list[0]
    highest_name_value = get_value(name_list[0])
    name = name_list[i]
    for name in name_list:
        name_value = get_value(name)
        if name_value > highest_name_value:
            highest_name_value = name_value
            highest_name = name
        i += 1
    print(highest_name, highest_name_value)


def roster_name_values(name_list):
    i = 0
    roster_dict = {}
    name = name_list[i]
    for name in name_list:
        roster_dict[name] = get_value(name)
    i += 1
    return roster_dict


def get_words(file_name):
    '''
    return a list of words from selected file input
    '''
    full_word_list = open(file_name).read().splitlines()
    word_list = [word.lower() for word in full_word_list]
    return word_list


def word_values(word_list):
    i = 0
    word_dict = {}
    name = word_list[i]
    for word in word_list:
        word_dict[word] = get_value(name)
    i += 1
    return word_dict


def get_words_with_same_value(word_dict, my_name_value):
    '''
    return a list of matched words 
    '''
    matches = []
    word_item = word_dict.items()
    for word in word_item:
        if word[1] == my_name_value:
            matches.append(word[0])
    return matches



def main():
    name_list = get_name_list('Exam2018/exam2018/roster.txt')
    # print(get_name_list('Exam2018/exam2018/roster.txt'))

    print(get_value('sarah'))
    # print(get_value(get_name_list('Exam2018/exam2018/roster.txt')[-6]))

    # print(who_has_highest_value(name_list))

    roster_dict = roster_name_values(name_list)
    #print(roster_name_values(name_list))

    word_list = get_words('Exam2018/exam2018/positive-words.txt')
    # print(get_words('Exam2018/exam2018/positive-words.txt'))

    word_dict = word_values(word_list)
    # print(word_values(word_list))

    print(get_words_with_same_value(word_dict, get_value('sarah')))


if __name__ == '__main__':
    main()




