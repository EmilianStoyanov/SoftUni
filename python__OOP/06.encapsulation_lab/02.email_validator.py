class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def __get_email_parts(self, email):
        at_index = email.index("@")
        dot_index = email.rindex(".")

        return [
            email[:at_index],
            email[at_index + 1:dot_index],
            email[dot_index + 1:],
        ]

    def validate(self, email):
        [name, mail, domain] = self.__get_email_parts(email)

        return self.__validate_name(name) and \
               self.__validate_mail(mail) and \
               self.__validate_domain(domain)
