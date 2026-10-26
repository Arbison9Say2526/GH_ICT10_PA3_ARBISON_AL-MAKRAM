#PA3
from pyscript import display, document


def countries_capital(e):
    document.getElementById('output').innerHTML = ''
    user_input = document.getElementById('input1').value.capitalize().strip()

    countries = {
    'Madagascar': 'Antananarivo',
    'Mongolia': 'Ulaanbaatar',
    'Egypt': 'Cairo',
    'The Philippines': 'Metro Manila',
    'USA': 'Washington, D.C',
    'Denmark': 'Copenhagen',
    'Chile': 'Santiago'
    }

    countries_checker = user_input in countries

    display_message = (f'Ay G theres no {user_input} in this list. Better luck next time', f'{user_input} is in the list. The capital of the abovementioned is {countries.get(user_input)}')

    display(display_message[countries_checker], target='output')