class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp1: str
        temp2: str
        length = len(s)

        # 데이터 길이를 반으로 나눈 값만큼 반복문을 돌리도록 계산
        repeat = length // 2

        for i in range(repeat):
            # 리스트의 데이터 수가 홀수개인 경우.
            # 정가운데를 제외하고 맨 앞과 맨 뒤를 차례로 바꿔 준다.
            if length % 2 == 1:
                temp1 = s[i]
                end_no:int = length-1-i
                temp2 = s[end_no]
                s[end_no] = temp1
                s[i] = temp2

            # 리스트의 데이터 수가 짝수개인 경우.
            else:
                temp1 = s[i]
                end_no:int = length-1-i
                temp2 = s[end_no]
                s[end_no] = temp1
                s[i] = temp2