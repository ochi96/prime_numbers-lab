

def prime_number(guess):
    if guess==0 or guess==1 or abs(guess)!=guess:
        return False
    elif guess>=2:
        for number in range(2,guess):
            if (guess%number)==0:
                return False
        else:
            return True
    else:
        return True

def primeNumbers(maximum):
    prime_numbers=[]
    for number in range(maximum+1):
        if prime_number(number):
            prime_numbers.append(number)
            continue
    return prime_numbers
