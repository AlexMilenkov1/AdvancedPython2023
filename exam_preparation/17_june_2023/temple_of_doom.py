from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = deque(int(x) for x in input().split())

accomplished_all_challenges = True

while challenges:
    if not substances and challenges:
        accomplished_all_challenges = False
        break

    first_tool = tools.popleft()
    last_substances = substances.pop()

    multiplied_value = first_tool * last_substances

    if multiplied_value in challenges:
        challenges.remove(multiplied_value)
    else:
        first_tool += 1
        tools.append(first_tool)

        last_substances -= 1
        substances.append(last_substances)

        if substances[-1] <= 0:
            substances.pop()

if accomplished_all_challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f'Tools: {", ".join(str(x) for x in tools)}')
if substances:
    print(f'Substances: {", ".join(str(x) for x in substances)}')
if challenges:
    print(f'Challenges: {", ".join(str(x) for x in challenges)}')
