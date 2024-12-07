def solution(genres, plays):
    answer = []
    num = len(genres)

    music = dict()

    if num==1:
        return [0]
    
    for i in range(num):
        genre = genres[i]
        if genre in music.keys():
            music[genre].append([i,plays[i]])
        else:
            music[genre]=[[i,plays[i]]]

    music = list(map(lambda x:music[x], music))

    music = sorted(music, key = lambda genre: -sum(song[1] for song in genre))
    
    music = [sorted(genre, key=lambda song:(-song[1], song[0])) for genre in music]

    for genre in music:
        answer.append(genre[0][0])
        if len(genre)>1:
            answer.append(genre[1][0])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

'''
# 유형
<< 가능한 조합의 경우 >>

# 문제요구사항
- 베스트 앨범에 들어갈 노래의 '고유 번호 순서' => 고유번호(즉, 인덱스)를 기억해야 함

# 접근
- 필요한 정보
    - 장르
    - 고유번호
    - 횟수
- 모든 정보가 다 필요하므로 장르별로 [고유번호, 재생횟수]를 요소로 갖는 딕셔너리 생성

- 총 누적 재생횟수가 높은 장르부터 => 각 장르별 누적 재생횟수를 알아야 하므로 장르별로 정렬 -> 합계를 기준으로 장르 내림차순 정렬
- 각 장르에서는 재생횟수가 높은 고유번호부터 => 각 장르에서 재생횟수를 기준으로 장르 내에서 고유번호 내림차순 정렬, 같은 횟수는 고유번호 오름차순 정렬

# 문제풀이
- 각 장르별 누적 재생횟수를 알아야 하므로 장르별로 정렬
  => music = [genre:[[id,play],[id,play],...],genre:[[id,play],[id,play],...]] 으로 해시 생성
- 합계를 기준으로 장르 내림차순 정렬
  => sorted(music, key = lambda genre: -sum(song[1] for song in genre))
- 장르 내에서 고유번호 내림차순 정렬, 같은 횟수는 고유번호 오름차순 정렬
  => [sorted(genre, key = lambda song: (-song[1],song[0])) for genre in music]
- 차례대로 최대 2개씩 고유번호만 answer=[]에 담기

************************** 핵심 **************************
- 장르별로 노래를 그룹화
- 각 장르별 재생 횟수 합 계산
- 장르 내에서 노래 정렬
**********************************************************

!!!!!!!!!!!!!!!!!!!!!!!!!! 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!
'''