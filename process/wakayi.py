from janome.tokenizer import Tokenizer
import os

text_file = '02_watanabe.txt'


def tokenize(text):
    t = Tokenizer()
    result = []
    
    lines = text.split('\n')
    
    del lines[-1]
    for line in lines:
        print('解析行:',line)
        tokens = t.tokenize(line)
        for token in tokens:
            base_form = token.base_form
            
            if not base_form in ['「', '」']:
                pos = token.part_of_speech
                pos = pos.split(',')[0]
                if pos in ['名詞','動詞','形容詞','記号']:
                    result.append(base_form)
    return result

def main():
    file_dir = os.path.abspath('src/' + text_file)
    try:
        bindata = open(file_dir, 'rb').read()
        text = bindata.decode('utf-8')
        words = tokenize(text)
    except Exception as e:
        print('error!',e)
        exit(0)

    wakati_file = 'src/02_watanabe_wakati.txt'
    with open(wakati_file, 'w', encoding='utf-8') as f:
        f.write(' '.join(words))

if __name__ == '__main__':
    main()
