def single_root_words(root_word, *other_world):
    same_words = []
    for word in other_world:
        if root_word.lower().count(word.lower()) or word.lower().count(root_word.lower()):
            same_words.append(word)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))