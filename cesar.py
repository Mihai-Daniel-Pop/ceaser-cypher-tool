def implement_caesar_cipher(message, key, decrypt=False):
   result = ""
   for character in message:
       if character.isalpha():
           shift = key if not decrypt else -key
           if character.islower():
               result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
           else:
               result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
       else:
           result += character
   return result
