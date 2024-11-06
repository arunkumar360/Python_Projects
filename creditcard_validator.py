odd_sum = 0
even_sum = 0
total = 0


card_no = input('Enter your Card Number: ')
card_no = card_no.replace(' ','')
card_no = card_no.replace('-','')

card_no = card_no[::-1]


for n in card_no[::2]:
    odd_sum += int(n)

for x in card_no[1::2]:
    x = int(x) * 2
    if x >= 10:
        even_sum += 1 + (x % 10)
    else:
        even_sum += x

total = odd_sum + even_sum


if (total % 10 == 0):
    print('VALID')

else:
    print('INVALID')