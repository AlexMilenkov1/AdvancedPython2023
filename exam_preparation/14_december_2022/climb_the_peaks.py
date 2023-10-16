from collections import deque

food_portions = deque(int(x) for x in input().split(', '))
stamina = deque(int(x) for x in input().split(', '))

conquered_peaks = []
peaks_difficulty = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}

all_conquered = False

while food_portions and stamina:

    last_daily_food_portion = food_portions.pop()
    first_daily_stamina = stamina.popleft()

    summed_values = last_daily_food_portion + first_daily_stamina

    for peak, difficulty_level in peaks_difficulty.items():
        if summed_values >= difficulty_level:
            conquered_peaks.append(peak)
            del peaks_difficulty[peak]
            break
        else:
            break

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print('Conquered peaks:')
    print(f"\n".join(conquered_peaks))
