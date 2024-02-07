class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict은 존재하지 않는 키에 접근 했을때, 기본값이 할당되어 있기 때문에 에러가(keyerror) 나지 않음
        # 딕셔너리는 K, V를 함께 할당해야하는데 defaultdict은 key 만 할당될 시에 value를 default로 0을 할당하여 에러가 나지 않는다.
        # 괄호 안의 list는 해당 딕셔너리의 value가 list임을 표현
        anagrams = collections.defaultdict(list)
        
        # join을 활용하여 애너그램을 알파벳순 정렬하여 키로 활용한다.
        # 그리고 리스트에 해당 단어를 더한다.
        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return list(anagrams.values())
    