import re

class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


emails = []

while True:
    email = input()

    if email == 'End':
        break

    emails.append(email)

regex = r'(([a-z]{4,})(@[a-z]+)(\.com|\.bg|\.org|.net))'

for current_email in emails:
    match = re.match(regex, current_email)

    if match:
        print(match.group(2))