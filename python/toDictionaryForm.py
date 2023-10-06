from konlpy.tag import Okt,Kkma
from konlpy.utils import pprint
from string import punctuation

def tokenize(text):
    kkma = Kkma()
    okt = Okt()

    data = []

    #Make translator, wtf is translator?
    translator = str.maketrans("", "", punctuation)
    #create new string with no punctuation
    clear = text.translate(translator)
    
    #To get original word from input user (Stem = False)
    textInput = okt.pos(clear, norm=True)
    #To get dict form of the word (stem = True)
    dictForm = okt.pos(clear, norm=True, stem=True)

    # Iterate over dictForm
    for i in range(len(dictForm)):
        # print(f"{textInput[i][0]} -> {dictForm[i][0]}")
        wordType = dictForm[i][1] # get the 'type' of the word (noun,verb or etc)
        if ( wordType == 'Verb' or wordType == 'Noun' or wordType == 'Adjective'):
            # Insert into data
            data.append({
                'text': textInput[i][0],
                'dictionary-form': dictForm[i][0],
                'translation': ""
            })
    
    return data
        

    


# tokenize('네, 안녕하세요. 반갑습니다.')
print(tokenize("샘플 코드에서 YOUR_CLIENT_ID또는 YOUR-CLIENT-ID에는 애플리케이션을 등록하고 발급받은 클라이언트 아이디 값을 입력합니다"))




# {
#     'text': 받은,
#     'dictionary-form': 받다,
#     'translation': "Tungir Maybe"
# }





