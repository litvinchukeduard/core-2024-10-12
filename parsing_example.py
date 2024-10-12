import re
'''
Написати код, яка буде діставати дату з рядків певного формату
'''

# 2024-10-12 16:25 | Привіт
# yyyy-mm-dd hh:mm | message
# \d{4}-\d{2}-\d{2}
# \d{2}:\d{2}
# [a-z]+

# 2024-10-12 16:25 | Привіт
# (?P<first>\w+)
# (?P<name>regex)

example_string = "2024-10-12 16:25 | Hello"
# pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
# pattern = r"(?P<date>\d{4}\-\d{2}\-\d{2}) (?P<time>\d{2}:\d{2}) | (?P<message>\w+)"
pattern = r"(?P<date>\d{4}\-\d{2}\-\d{2}) (?P<time>\d{2}:\d{2})"

result = re.match(pattern, example_string)
print(result.groupdict())
