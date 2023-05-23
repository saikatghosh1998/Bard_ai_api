from bardapi import Bard
import os
import sys

os.environ['_BARD_API_KEY']=""

try:
    word = sys.argv[1]
except:
    print("Please Specify a Word !!")
    exit(-1)
    

#input_text = "what is capital of west bengal?"

print(Bard().get_answer(word)['content'])