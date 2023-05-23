from bardapi import Bard
import os
import sys

#bard.set_cookies(WQin_hbVw-fwN0Pz7pAx3_bVephaLNLX_mOPwnMtOvrQMtDnlme67RxUP2LFFa0lmUIxXw)
os.environ['_BARD_API_KEY']="WQin_hbVw-fwN0Pz7pAx3_bVephaLNLX_mOPwnMtOvrQMtDnlme67RxUP2LFFa0lmUIxXw."

try:
    word = sys.argv[1]
except:
    print("Please Specify a Word !!")
    exit(-1)
    

#input_text = "what is capital of west bengal?"

print(Bard().get_answer(word)['content'])