import random

import konlpy

dict_translator_for_under_char = {

    "IC" : "아아", # 감탄사
    "EFN" : "어라",#평서형 종결어미
    "EFQ":"이란 말인가", # 의문형 종결어미
    "EFO":"라", #명령형 종결어미
    "EFA":"자", #청유형 종결어미
    "EFI":"도다", # 감탄형 종결어미
    "EFR":"이까", # 존칭형 종결 어미
}
dict_translator_for_no_under_char = {

    "IC" : "아아", # 감탄사
    "EFN" : "어라",#평서형 종결어미
    "EFQ":"란 말인가", # 의문형 종결어미
    "EFO":"라", #명령형 종결어미
    "EFA":"자", #청유형 종결어미
    "EFI":"도다", # 감탄형 종결어미
    "EFR":"이까", # 존칭형 종결 어미
}

bible_name=["마가복음", "누가복음", "요한복음", "마태복음", "사도행전"]


header = ["예수께서 자리에서 일어나 가라사대, ", "예수께서 무리를 보시고 산에 올라가 앉으시니 제자들이 나아온지라. 입을 열어 가르쳐 가라사대 ", "예수께서 무리를 흩어 보내시고 배에 오르사 이르되, ",
         "예수께서 한 어린 아이를 불러 저희 가운데 세우시고 가라사대 ",
         "이에 예수께서 무리와 제자들에게 말씀하여 가라사대"]
tail=[" 이에 제자들이 나아와 가로되 참으로 큰 가르침을 받았나이다.", " 이 말을 들은 청중 중 한 장정이 가로되 이 몸을 주의 나라에서 주의 우편에 앉게 하소서.", " 이후 말씀을 마치신 예수께서 머물러 서 계시었다.",
 " 이 말을 듣은 좌중은 아무 말도 하지 못 하였다."]



def checkUnderChar (word):    #아스키(ASCII) 코드 공식에 따라 입력된 단어의 마지막 글자 받침 유무를 판단해서 뒤에 붙는 조사를 리턴하는 함수
    last = word[-1]     #입력된 word의 마지막 글자를 선택해서
    criteria = (ord(last) - 44032) % 28     #아스키(ASCII) 코드 공식에 따라 계산 (계산법은 다음 포스팅을 참고하였습니다 : http://gpgstudy.com/forum/viewtopic.php?p=45059#p45059)
    if criteria == 0:       #나머지가 0이면 받침이 없는 것
        return 0
    else:                   #나머지가 0이 아니면 받침 있는 것
        return 1
   # 출처 : https://github.com/letsgo247/under-checker

if __name__ == '__main__':
    has_under_char = 0
    inputText = input("한글 문장을 입력하여 주세요.\n")
    posTaggier = konlpy.tag.Kkma()
    posTaggedText = posTaggier.pos(inputText)

    print(posTaggedText)

    #원래 문장에서 공백 위치 기억
    whitespaceNum=0
    whiteSpace=[]
    for index, char in enumerate(inputText):
        if char==' ':
            whiteSpace.append(index)

    #출력을 위한 문자열
    translated_text=""

    #hearder 붙임
    translated_text+=header[random.randint(0,4)]



    temp_text=""
    for word, pos in posTaggedText:
        # 전의 단어가 종성을 가지고 있는지 확인
        if has_under_char == 1:
            dict_translator = dict_translator_for_under_char
        else:
            dict_translator = dict_translator_for_no_under_char

        dictKeys = dict_translator.keys()
        if pos not in dictKeys:
            temp_text+=word
        else:
            temp_text+=dict_translator[pos]

        has_under_char=checkUnderChar(word) #다음 글자를 위해 현재 단어가 받침이 있는지 없는지 확인

    # 단어 사이 띄어쓰기 추가
    for i, char in enumerate(temp_text):
        if (len(whiteSpace)>0 and i + whitespaceNum == whiteSpace[0]):
            translated_text += " "
            whitespaceNum += 1
            whiteSpace.pop(0)
        translated_text += char

    #tail 붙임
    translated_text += tail[random.randint(0, 2)]


    print(translated_text)
    print(bible_name[random.randint(0,4)] +" "+ str(random.randint(1,50))+ ":"+str(random.randint(1,72)))