import konlpy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputText = input("한글 문장을 입려하여 주세요.\n")
    posTaggier = konlpy.tag.Kkma()
    posTaggedText = posTaggier.pos(inputText)

    print(posTaggedText)