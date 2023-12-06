def emoji_convertor(message):
    words = message.split(' ')
    emojis = {':)': '😀', ':D': '😁', ':(': '☹️'}

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '

    return output

print(emoji_convertor(input("> ")))