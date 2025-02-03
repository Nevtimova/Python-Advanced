numbers_dictionary = {}

while True:
    line = input()
    if line == "Search":
        break
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

while True:
    line = input()
    if line == "Remove":
        break
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

while True:
    line = input()
    if line == "End":
        break
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)


# Email Validator
class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = {".com", ".bg", ".org", ".net"}

while True:
    email = input()
    if email == "End":
        break

    try:
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        name, domain = email.split("@")
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if not any(domain.endswith(ext) for ext in valid_domains):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        print("Email is valid")
    except Exception as e:
        print(e)


# Password Validator
class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


special_chars = {"@", "*", "&", "%"}

while True:
    password = input()
    if password == "Done":
        break

    try:
        if len(password) < 8:
            raise PasswordTooShortError("Password must contain at least 8 characters")
        if password.isdigit() or password.isalpha() or password.isalnum():
            raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
        if not any(char in special_chars for char in password):
            raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
        if " " in password:
            raise PasswordContainsSpacesError("Password must not contain empty spaces")
        print("Password is valid")
    except Exception as e:
        print(e)


# Rotate Matrix
class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    if not all(len(row) == matrix_length for row in matrix):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

    for row in matrix:
        if not all(cell.isdigit() for cell in row):
            raise MatrixContentError("The matrix must consist of only integers")

    matrix = [[int(cell) for cell in row] for row in matrix]
    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


mtrx = []
while True:
    line = input().split()
    if not line:
        break
    mtrx.append(line)

try:
    rotated_matrix = rotate_matrix(mtrx)
    for row in rotated_matrix:
        print(" ".join(map(str, row)))
except Exception as e:
    print(e)


# Online Banking
class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin, balance, age = map(int, input().split(", "))

while True:
    command = input()
    if command == "End":
        break

    try:
        action, *details = command.split("#")
        if action == "Send Money":
            amount, entered_pin = map(int, details)
            if entered_pin != pin:
                raise PINCodeError("Invalid PIN code")
            if age < 18:
                raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
            if amount > balance:
                raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
            balance -= amount
            print(f"Successfully sent {amount:.2f} money to a friend")
            print(f"There is {balance:.2f} money left in the bank account")
        elif action == "Receive Money":
            amount = int(details[0])
            if amount < 0:
                raise MoneyIsNegativeError("The amount of money cannot be a negative number")
            balance += amount // 2
            print(f"{amount / 2:.2f} money went straight into the bank account")
    except Exception as e:
        print(e)
