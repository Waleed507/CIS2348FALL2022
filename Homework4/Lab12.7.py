# Waleed Yusuf
# 2104654

def get_age():
    input_age = int(input())
    if input_age < 18 or input_age > 75:
        raise ValueError('Invalid age.')
    return input_age


def fat_burning_heart_rate(input_age):
    input_heart_rate = (220 - input_age) * 0.7
    return input_heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {heart_rate} bpm')

    except ValueError as error:
        print(error)
        print(f'Could not calculate heart rate info.\n')
