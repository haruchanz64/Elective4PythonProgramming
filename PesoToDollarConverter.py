def convert_php_to_usd(amount_php):
    exchange_rate = 0.01743022  # Current exchange rate, definitely did research for this :) (https://www.xe.com/currencyconverter/convert/?Amount=1&From=PHP&To=USD)
    amount_usd = amount_php * exchange_rate
    return amount_usd


def main():
    amount_php = float(input("Please enter the amount in Philippine Peso (PHP) to be converted to USD: "))
    converted_amount = convert_php_to_usd(amount_php)
    print(f"PHP {amount_php} is approximately {converted_amount:.2f} USD.")


main()
