n = int(input())

guest_list = set()

for _ in range(n):
    estimated_guest = input()

    guest_list.add(estimated_guest)

while True:
    guest = input()

    if guest == 'END':
        break

    if guest in guest_list:
        guest_list.remove(guest)

result = sorted(list(guest_list))

print(len(guest_list))
for guest in guest_list:
    print(guest)
