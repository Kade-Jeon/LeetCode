class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #식별자 별로 구분하기 위해 각각 리스트를 생성
        letters: List[str] = []
        digits: List[str] = []
        
        # input log데이터에서 식별자 다음이 숫자인지, 문자인지 구분하여 각각 리스트에 담는다.
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        #숫자로그는 입력 순서대로이기 때문에 그냥 담아 반환하면 되므로 별도 정렬이 필요 없다.

        #문자로그는 식별자 뒤 문자 순서대로 정렬 후
        #식별자 순으로 정렬 (문자 로그가 같은 경우를 위해서)
        letters.sort(key=lambda x:( x.split()[1:], x.split()[0]))
    #    print(letters+digits)
        return letters+digits