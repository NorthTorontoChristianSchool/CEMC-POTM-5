import math

n = 3

while n <= 200000:
    # Calculate the two other side lengths
    a = n - 1
    c = n + 1

    # Check if triangle is right angled
    if a ** 2 + n ** 2 == c ** 2:
        print("Right angled:", n)

    # Calculate the area of the triangle using Heron's Formula
    s = (a + n + c) / 2
    area = math.sqrt((s * (s - a) * (s - n) * (s - c)))

    # Check if area is remarkable
    if area.is_integer():
        print("Remarkable:", n)

        # Find the solution for Part B
        if math.sqrt((n ** 2 - 4) / 3).is_integer() and n % 3 != 0 and n % 2 == 0:
            print("Satisties Part B:", n)

    # Increment n
    n += 1