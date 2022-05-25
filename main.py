import konlpy

dict_translator_for_under_char = {

    "IC" : "아아", # 감탄사
    "EFN" : "어라",#평서형 종결어미
    "EFQ":"나이까", # 의문형 종결어미
    "EFO":"라", #명령형 종결어미
    "EFA":"자", #청유형 종결어미
    "EFI":"도다", # 감탄형 종결어미
    "EFR":"이까", # 존칭형 종결 어미
}
dict_translator_for_no_under_char = {

    "IC" : "아아", # 감탄사
    "EFN" : "어라",#평서형 종결어미
    "EFQ":"나이까", # 의문형 종결어미
    "EFO":"라", #명령형 종결어미
    "EFA":"자", #청유형 종결어미
    "EFI":"도다", # 감탄형 종결어미
    "EFR":"이까", # 존칭형 종결 어미
}
def checkUnderChar (word):    #아스키(ASCII) 코드 공식에 따라 입력된 단어의 마지막 글자 받침 유무를 판단해서 뒤에 붙는 조사를 리턴하는 함수
    last = word[-1]     #입력된 word의 마지막 글자를 선택해서
    criteria = (ord(last) - 44032) % 28     #아스키(ASCII) 코드 공식에 따라 계산 (계산법은 다음 포스팅을 참고하였습니다 : http://gpgstudy.com/forum/viewtopic.php?p=45059#p45059)
    if criteria == 0:       #나머지가 0이면 받침이 없는 것
        return 0
    else:                   #나머지가 0이 아니면 받침 있는 것
        return 1
   # 출처 : https://github.com/letsgo247/under-checker

if __name__ == '__main__':
    has_under_char = False
    inputText = input("한글 문장을 입려하여 주세요.\n")
    posTaggier = konlpy.tag.Kkma()
    posTaggedText = posTaggier.pos(inputText)

    whiteSpace=[]
    for index, char in enumerate(inputText):
        if char==' ':
            whiteSpace.append(index)

    #출력을 위한 문자열
    translated_text=""
    
    #전의 단어가 종성을 가지고 있는지 확인
    if has_under_char == True:
        dict_translator = dict_translator_for_under_char
    else:
        dict_translator = dict_translator_for_no_under_char

    dictKeys=dict_translator.keys()
    for word, pos in posTaggedText:
        if pos not in dictKeys:
            translated_text+=word
        else:
            translated_text+=dict_translator[pos]

        has_under_char=checkUnderChar(word) #다음 글자를 위해 현재 단어가 받침이 있는지 없는지 확인

    print(posTaggedText)



    print(translated_text)