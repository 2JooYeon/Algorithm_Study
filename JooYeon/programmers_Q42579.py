def solution(genres, plays):
    answer = []
    # {총 재생 횟수 : 장르}
    plays_genre = {}
    # 많이 재생된 순서로 노래의 고유번호를 담는 리스트
    sorted_index = []
    # {장르 : [재생 많은 순서의 고유번호]}
    genre_index_list = {}

    # {총 재생 횟수 : 장르} 만들기
    unique_genre = set(genres)
    unique_genre = list(unique_genre)
    for genre in unique_genre:
        # 특정 장르의 노래 고유번호 리스트 뽑기
        index_temp = list(filter(lambda x: genres[x] == genre, range(0, len(genres))))
        # 특정 장르의 노래들의 재생횟수 리스트 뽑기
        play_temp = list(map(lambda x: plays[x], index_temp))
        # 특정 장르의 노래들 재생횟수 총 합산
        plays_sum = sum(play_temp)
        # {총 재생 횟수 : 장르} 만들기
        plays_genre[plays_sum] = genre

        # {고유 번호 : 재생횟수} 만들기
        index_plays = dict(zip(index_temp, play_temp))
        # 특정 장르의 노래들 재생횟수 높은 순서대로 재생횟수 정렬
        play_temp.sort(reverse=True)
        # 장르 내에서 많이 재생된 노래 순서로 고유번호 정렬
        sorted_index.clear()
        for count in play_temp:
            sorted_index.append(list(filter(lambda x: index_plays[x] == count, index_temp)))

        # 리스트 풀어주기
        sorted_index_temp = sum(sorted_index, [])
        # {장르 : [재생 많은 순서의 고유번호]} 만들기
        genre_index_list[genre] = sorted_index_temp

    copy_plays_genre = sorted(plays_genre.items(), reverse=True)
    copy_plays_genre = dict(copy_plays_genre)
    # 재생 많이 된 순서로 장르표시
    hot_genres = copy_plays_genre.values()
    for genre in hot_genres:
        # 장르에 속한 곡이 두 곡 이상일 때
        if (len(genre_index_list[genre]) > 1):
            for index in genre_index_list[genre][0:2]:
                answer.append(index)
        else:
            answer.append(genre_index_list[genre][0])

    return answer