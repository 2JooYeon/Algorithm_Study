def solution(phone_book):
    phone_book.sort()

    for i in range(0, len(phone_book) - 1):
        if phone_book[i + 1].find(phone_book[i]) in range(1, ):
            return False

    return True