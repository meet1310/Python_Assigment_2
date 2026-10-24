import re

text = input("Enter text: ")

emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|edu)', text)

all_emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com|edu)',
    text
)

unique_emails = set(all_emails)

print("\nValid Emails:")
for email in sorted(unique_emails):
    print(email)

print("\nTotal Valid Emails:", len(unique_emails))