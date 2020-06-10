import os
os.chdir('../../../')

from otp.chat import WhiteListData

def acceptWord():
    word = raw_input('> ').rstrip().lower()

    if word == 'exit()':
        saveChanges()
        return

    if word.startswith('r '):
        word = word.replace('r ', '')
        if word not in LOCAL_LIST:
            print 'Could not remove unknown word "%s" from the whitelist.' % word
        else:
            LOCAL_LIST.remove(word)
            print 'Removed "%s" from the whitelist.' % word
    elif word.startswith('m '):
        merge = word.replace('m ', '')

        if os.path.isfile(merge):
            print 'Opening %s...' % merge

            with open(merge) as file:
                for line in file.readlines():
                    line = line.replace('\r', '').replace('\n', '').lower()
                    print 'Adding %s...' % line
                    LOCAL_LIST.append(line)
        else:
            print 'No file named %s!' % merge
    elif word in LOCAL_LIST:
        print 'The word "%s" is already whitelisted.' % word
    else:
        LOCAL_LIST.append(word)
        print 'Added the word "%s" to the whitelist.' % word

    acceptWord()

def removeDuplicates(list):
    seen = set()
    seen_add = seen.add
    return [x for x in list if not (x in seen or seen_add(x))]

def saveChanges():
    global LOCAL_LIST
    print 'Saving the whitelist...'

    with open('otp/chat/WhiteListData.py', 'w') as f:
        f.write('WHITELIST = [\n')

        LOCAL_LIST.sort()
        LOCAL_LIST = removeDuplicates(LOCAL_LIST)

        for word in LOCAL_LIST:

            if '\\' in word:
                print 'Word contains illegal characters: %s' % word
                continue
            try:
                word.decode('ascii')
            except:
                print 'Word cannot be decoded in ASCII mode: %s' % word
                continue

            if "'" in word:
                f.write('    "%s",\n' % word)
            else:
                f.write("    '%s',\n" % word)

        f.write(']')

    print 'Your changes have been saved! Make sure to push your changes!'

LOCAL_LIST = WhiteListData.WHITELIST

print 'Welcome to the Toontown Stride Whitelist Tool!'
print 'Type any word you want to add to the whitelist.'
print 'If you wish to remove a word, type "r <word>".'
print 'If you wish to merge a file, type "m <file>".'
print 'When you are done and want to save your changes, type "exit()".'


acceptWord()
