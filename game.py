import random
from colorama import colorama_text
import colorama

num = random.randint(0, 100000)

print(colorama.Fore.GREEN + "Generated number = %s" %(num))
