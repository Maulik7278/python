print("hello maulik")


def check_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return f"{x} is Not Prime"
            break
    else:
        return f"{x} is Prime"