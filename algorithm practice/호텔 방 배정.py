def solution(k, room_number):
    answer = []
    
    while(room_number):
        request = room_number.pop(0)
        room = 0
        while(room==0):
            if request in answer:
                request +=1
            else:
                room=request
        answer.append(room)
    return answer

