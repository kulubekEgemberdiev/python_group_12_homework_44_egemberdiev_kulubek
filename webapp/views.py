from django.shortcuts import render
from urllib.parse import parse_qs


# Create your views here.
def get_numbers(request):
    numbers_int = ''
    if request.method == 'POST':
        numbers = request.POST.get('numbers')
        numbers_int = [int(i) for i in numbers]

    return numbers_int


def index_view(request):
    secret_numbers = [7, 5, 8, 6]
    number = get_numbers(request)
    guess = Checker.guess_numbers(secret_numbers, number)
    return render(request, "index.html", guess)


class Checker:
    @staticmethod
    def check_numbers(numbers):
        for i in numbers:
            if i < 1 or i > 9 or i != int:
                return False
        return True

    @staticmethod
    def check_length(numbers):
        if len(numbers) != 4:
            return False
        return True

    @staticmethod
    def check_unique(numbers):
        if len(set(numbers)) != len(numbers):
            return False
        return True

    @staticmethod
    def guess_numbers(secret, numbers):
        bulls = 0
        cows = 0
        message = ''

        if Checker.check_numbers(numbers) and Checker.check_length(numbers) and Checker.check_unique(numbers):
            for i in range(len(numbers)):
                if numbers[i] == secret[i]:
                    bulls += 1
                elif numbers[i] in secret:
                    cows += 1

            if bulls == 4:
                message = 'You got it right!'
            else:
                message = f"You got {bulls} bulls and {cows} cows."
        else:
            message = "Error! You entered an invalid number! You must enter 4 numbers separated by a space from 1 to 9!"
        return message
