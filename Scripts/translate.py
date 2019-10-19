from googletrans import Translator 

def Translate(text,language_text,language_to):
    translator = Translator()
    try:
        return translator.translate(text=text,dest=language_to,src=language_text)
    except:
        return("can't do translate please check your connection internet or  language input invalid ")

def Select_Language(text):
    print('''Selcet a Language :
                    Example :
                        fa : persian
                        en : english
                        ja : japanese
2 : See all language and select\n` ''')
    option = input('Select  option 2 or Enter a Language : ')
    
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
        'fil': 'Filipino',
        'he': 'Hebrew'
    } 

    if option == '2':
        count = 1
        for i,L in LANGUAGES.items():
            print('{} : {} : {}'.format(count,i,L))
            count+=1
        try:
            language = input('Select a language :')
            return LANGUAGES.get(language)
        except:
            return "can't find the language"
    elif option == '':
        try:
            tran = Translator()
            return tran.detect(text).lang
        except:
            print("can't do translate please check your connection internet or  language input invalid ")

    else:
        try:
            return LANGUAGES.get(option)
        except:
            return "can't find the language"

def main():
    help = ''' 
Welcome to this script 
    this script can translate any language to any language
    support of 106 language 
    for translate a text you shold selsect option 2 and select language text and select the language you want to translate
    but if you don't choose the language of the text, it will automatically\n
      '''
    print('1: Help \n2: Translate ')
    option =int( input('Select an option : '))
    if option == 1:
        print(help)
        main()
    if option == 2:
        text = input('Enter your Text : ')
        print("\nchoose language text \n if you don't choose do it will automatically")
        src =  Select_Language(text)
        print('\nSelect the language you want to translate :')
        dest = Select_Language(text)
        try:
            print(str(Translate(text,src,dest).text))
        except:
            print("can't do translate please check your connection internet or  language input invalid ")

main()
