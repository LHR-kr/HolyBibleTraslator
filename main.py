import konlpy

dict_translator = {
    "VCP" : "이니라", # 긍정 지정사
    "VCN" : "아니하다", # 부정 지정사
    "IC" : "아아", # 감탄사
    "EFN" : "",#평서형 종결어미
    "EFQ":"", # 의문형 종결어미
    "EFO":"", #명령형 종결어미
    "EFA":"", #청유형 종결어미
    "EFI":"", # 감탄형 종결어미
    "EFR":"", # 존칭형 종결 어미

}


if __name__ == '__main__':
    inputText = input("한글 문장을 입려하여 주세요.\n")
    posTaggier = konlpy.tag.Kkma()
    posTaggedText = posTaggier.pos(inputText)

    print(posTaggedText)