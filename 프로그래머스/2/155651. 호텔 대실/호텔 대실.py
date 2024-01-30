def transform(time):
    if int(time[3:]) + 10 >= 60:
        return str(int(time[:2]) + 1).zfill(2) + str(int(time[3:]) + 10 - 60).zfill(2)
    return time[:2] + str(int(time[3:]) + 10).zfill(2)


def solution(book_time):
    answer = 0
    book_time.sort(key = lambda x: x[0])
    rooms = [] #마지막 시간을 저장할 리스트
    for idx in range(len(book_time)):
        start_time = book_time[idx][0][:2] + book_time[idx][0][3:] # 새 예약의 대실 시작 타임       
        if idx == 0:
            rooms.append(transform(book_time[0][1]))
            answer += 1
            print(rooms)
        else:
            for i in range(len(rooms)):
                if rooms[i] > start_time: # 새 방이 필요한 경우
                    answer += 1
                    rooms.append(transform(book_time[idx][1]))
                    rooms.sort()
                    break
                else: #방 청소 후 대실 가능
                    rooms[i] = transform(book_time[idx][1])
                    rooms.sort()
                    break
    # print(rooms)
    return answer