import colorama
from colorama import Fore, Style
from cesar import implement_caesar_cipher

colorama.init(autoreset=True)


def main():
    print(f"{Fore.CYAN}Caesar Cipher Tool")

    msg = input("Enter your message: ")
    shift = int(input("Enter shift key (number): "))
    mode = input("Encrypt or Decrypt? (e/d): ").lower()

    is_decrypt = True if mode == 'd' else False

    output = implement_caesar_cipher(msg, shift, decrypt=is_decrypt)

    label = "Decrypted" if is_decrypt else "Encrypted"
    print(f"\n{Fore.GREEN}{label} message: {Fore.YELLOW}{output}")


if __name__ == "__main__":
    main()