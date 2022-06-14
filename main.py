import random
from colorama import colorama_text
import colorama
from pygame import Color

num = random.randint(0, 100000)

print(colorama.Fore.YELLOW + "Generated number = %s" %(num))
