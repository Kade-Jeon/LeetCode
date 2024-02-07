class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #결과 담을 리스트
        result = []

        #특수문자 제거 후, 공백으로 잘라서 리스트로 만듦
        removed = re.sub(r"[^A-Za-z]", r" ", paragraph).lower()
        splited = removed.split()

        #리스트를 돌면서 각 단어가 금지된 것과 일치하면 패스, 일치하지 않으면 결과에 담음
        for word in splited:
            if word in banned:
                continue
            result.append(word)

        # 결과에서 가장 많은 값이 나온건 0번째 인덱스임, most는 Tuple로 반환됨.
        most = collections.Counter(result).most_common().pop(0)
        # 튜플 ex.('ball', 2) 이므로 0번째 요소가 단어임
        return most[0]