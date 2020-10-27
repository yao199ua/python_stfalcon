pasta = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque oirri quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quareat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

number_of_sentences = sent_tokenize(pasta)
print(len(number_of_sentences)) # 4 sentences

print(pasta.count('quis')) # 2 times
print(pasta.count(' ')) # 112 times
characters = len(pasta) - pasta.count(' ')
print(characters) # 650 chacarters excluding spaces
short_pasta = pasta[:100] + '...' 
# HOW TO GET RID OF 'to' IN THE END???
print(short_pasta)

import textwrap
textwrap.shorten(pasta, width=100, placeholder="...")
print(pasta)

def truncate(pasta, max_size):
    if len(pasta <= max_size):
        return text
    return textwrap.wrap(text, max_size-100)[0] + "..."
