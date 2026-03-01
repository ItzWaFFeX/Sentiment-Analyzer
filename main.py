from colorama import Fore, Style, init
from textblob import TextBlob

init()

print(f"{Fore.RED} SENTIMENT SPY {Style.RESET_ALL} ")
while True:
    text = input(f"{Fore.LIGHTMAGENTA_EX}Enter here : ")
    if text.lower() == "exit":
        print(f"{Fore.CYAN} Goodbye! {Style.RESET_ALL}")
        break
    if not text:
        continue
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        print(f"{Fore.LIGHTGREEN_EX} Positive input detected - {score} {Style.RESET_ALL}")
    elif score < 0:
         print(f"{Fore.RED} Negative input detected - {score} {Style.RESET_ALL}")
    else:
         print(f"{Fore.YELLOW} Neutral input detected - {score} {Style.RESET_ALL}")
