def get_email_count():
    return int(input("How many emails (internetX@gmail.net do you need to create? (X = number of emails): "))


def generate_emails(count):
    return [f"internet{i + 1}@gmail.net" for i in range(count)]


def update_emails(emails):
    return [email.replace(".net", ".com") for email in emails]


def display_emails(title, emails):
    print(f"\n{title}:")
    for email in emails:
        print(email)


def main():
    email_count = get_email_count()
    emails = generate_emails(email_count)

    # Display original generated email before conversion
    display_emails("Original Emails", emails)

    # Convert emails
    updated_emails = update_emails(emails)

    # Display updated emails
    display_emails("Update Emails", updated_emails)


main()
