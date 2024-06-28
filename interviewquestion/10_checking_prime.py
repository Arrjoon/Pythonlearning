def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2,n//2):
        if n%i == 0:
            return False
    
    return True


print(is_prime(2))
print(is_prime(1))
print(is_prime(4))
print(is_prime(5))
print(is_prime(7))
print(is_prime(6))
