import matsuo_bot as x
import sfc_matsuo_bot as y

phase = 0
limit = 3
first_word = 'SFC'

def dialogue(w):
    global phase, limit
    try:
        phase += 1
        print('phase' + str(phase))
        word1 = x.load_w2v(w)
        sentence1 = x.make_sentence(word1)
        print('matsuo:' + sentence1)
        word2 = y.tokenize(sentence1)
        sentence2 = y.make_sentence(word2)
        print('student:' + sentence2)
        next_word_base = y.tokenize(sentence2)
        if not phase >= limit:
            dialogue(next_word_base)
        else:
            return
    except Exception as e:
        print('occur an error.' + e)
        exit(0)
def main():
    dialogue(first_word)


if __name__ == '__main__':
    main()