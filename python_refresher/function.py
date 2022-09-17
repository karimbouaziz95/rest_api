
def user_age_in_seconds():
    age = int(input("Enter your age: "))
    age_in_secs = age * 365 * 24 * 3600
    print(f"Age in seconds is: {age_in_secs}")
    
sequence = [1,2,3,4]
doubled = list(map(lambda x:x*2, sequence))
print(doubled)