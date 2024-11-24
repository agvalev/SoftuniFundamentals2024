def check_employess_hapiness():
    happiness_list = list(map(int, input().split()))
    happiness_factor = int(input())

    improved_hapiness = [h * happiness_factor for h in happiness_list]

    average_happiness = sum(improved_hapiness) / len(improved_hapiness)

    happy_count = sum(h >= average_happiness for h in improved_hapiness)

    total_count = len(improved_hapiness)

    message = 'happy' if happy_count >= total_count / 2 else 'not happy'

    result = f'"Score: {happy_count}/{total_count}. Employees are {message}!"'

    return (result)


result = (check_employess_hapiness())
print(result)
