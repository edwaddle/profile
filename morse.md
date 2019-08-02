#Morse Code tutorial

In this tutorial I will show you hot to build a morse code encryption program using python

## Prerequisites

for this code, you will need to install these:
- pycharm
- python 3

## Let's write some code..

first you need to make a dictionary:
```
MORSE_CODE_DICT = {'A':'*---', 'B':'---***','C':'---*---*','D':'---**',
'E':' *','F':'**---*', 'G':'------*', 'H':'****', 'I':'**', 'J':'*---------', 'K':'---*---', 'L':'*---**','M':'------', 'N':'---*', 'O':'---------','P':'*------*','Q':'------*---','R':'*---*','S':'***','T':'---','U':'**---','V':'***---','W':'*------','X':'---**---','Y':'---*------','Z':'------**','1':'*------------','2':'**---------','3':'***------','4':'****---','5':'*****','6':'---****','7':'------***','8':'---------**','9':'------------*','0':'---------------' }
```

The letters are the keys and the Morse code are the values. Next we have to define what encrypt means when we encrypt the message.
First you start the define encrypt function like this:
```
def encrypt(message):
```
then you set cipher to nothing because you have't receive the message yet:
```
cipher = ' '
```
Then you make a for loop which repeats a loop a certain time in which we are using to loop letter for each word:
```
for letter in message:
```
Next check if there is a letter by make a if else statement. If the message letter in not equal to space, then do this action:
`if letter != ' ':`
If the letter isin't a space, then go to the dictionary, find the letter,  add it to cipher, and add a space behind it:
cipher += MORSE_CODE_DICT[letter] + ' '
If the next letter is a space, then do this:
`else:`
then,write the statement cipher in progress and add the cipher, this command makes it so you print out the word every time you translate a word.
`print("cipher in progress:  ", cipher)`
Then do the loop again and set cipher to zero:
`return cipher`
That is the end of the if loop

Next you need to be able to receive the message the user wants to encrypt, you use input which takes the user's message and sets it to clear text message, the words in the parentheses just writes a question:
`cleartextmessage = input("Please enter the text you want to encrypt: ")`

Then you turn the message into all uppercase and encrypt it using the encrypt function. Set that as secret message and print it:
`secretmessage = encrypt(cleartextmessage.upper())
print(secretmessage)`
Now you print out the encrypted message.

this is a [hyperlink](https://google.com)
