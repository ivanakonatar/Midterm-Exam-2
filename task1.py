"""
===================   TASK 1   ====================
* Name: Caesar Cipher
*
* Caesar Cipher is encryption technique in which
* each letter in the plaintext is replaced by a
* letter some fixed number of positions down the
* alphabet. The method is named after Julius Caesar,
* who used it in his private correspondence.
*
* Write a script that will accept number of positions
* that should be shifted down the Unicode code points
* of character. White spaces and punctuation marks
* should be ignored during encryption process.
*
* Hint: `ord()` returns integer representing Unicode
* code point for single character.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def Caesar_Cipher_encryption(recenica,broj):



    nova_recenica = ''
    lista =['!',' ',',','.',':',';', '/']


    for karakter in recenica:

        if karakter not in lista:
            broj_chr = ord(karakter)

            broj_kriptovanog_slova = broj_chr + broj
            karakter = chr(broj_kriptovanog_slova)

            nova_recenica += karakter

        else:
            nova_recenica += karakter


    return nova_recenica


def decrypt(nova_recenica,broj):

    word = ''
    lista = ['!', ' ', ',', '.', ':', ';','/']

    for karakt in nova_recenica:

        if karakt not in lista:

            novo_slovo = chr(ord(karakt) - broj)
            word += novo_slovo

        else:
            word += karakt

    return word


def main():
    broj_pomjeranja = int(input("Za koliko mjesta pomjerate svaki karakter? "))

    enkriptovana_recenica = Caesar_Cipher_encryption("Ivana Konatar 11/115.", broj_pomjeranja)
    print(enkriptovana_recenica)
    dekriptovana_recenica = decrypt(enkriptovana_recenica,broj_pomjeranja)
    print(dekriptovana_recenica)

    pass

if __name__ == "__main__":
    main()