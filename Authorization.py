import uuid


class RegistrationErrors(Exception):
    pass


class ShortPassError(RegistrationErrors):
    pass


class WrongSymbPassError(RegistrationErrors):
    pass


class ShortEmailError(RegistrationErrors):
    pass


class WrongSymbEmailError(RegistrationErrors):
    pass


class IncorrectEmailError(RegistrationErrors):
    pass


class AlreadyRegistered(RegistrationErrors):
    pass


class AuthorizationErrors(Exception):
    pass


class WrongEmailError(AuthorizationErrors):
    pass


class WrongPassError(AuthorizationErrors):
    pass


class UserToken:
    def __init__(self):
        self.__id = uuid.uuid4()

    def __str__(self):
        return self.__id


class DB:
    users = {'truemail@gmail.com': 'qwerty1234567890'}
    users_token = {'truemail@gmail.com': UserToken()}

    wrong_symb = ' /\\\\#$%^&*,{}[]<>'

    wrong_symb_email = ' /?\\\\!|#$%^&*()-=+{}[],<>'

    def reg(self, email: str, password: str):
        if len(email) <= 11:
            raise ShortEmailError
        elif email.find('.') != len(email) - 3 and email.find('.') != (len(email) - 4) or email.find('@') <= 6:
            raise IncorrectEmailError
        elif len(set(email).intersection(self.wrong_symb_email)) > 0:
            raise WrongSymbEmailError
        elif len(password) <= 13:
            raise ShortPassError
        elif len(set(password).intersection(self.wrong_symb)) > 0:
            raise WrongSymbPassError
        elif email in self.users.keys():
            raise AlreadyRegistered
        else:
            self.users[email] = password
            self.users_token[email] = UserToken()
            return "200"

    def auth(self, email: str, password: str):
        if email in self.users.keys():
            if password != self.users[email]:
                raise WrongPassError
            else:
                return self.users_token[email]
        else:
            raise WrongEmailError