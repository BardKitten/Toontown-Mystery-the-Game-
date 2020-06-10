import string
import types

try:
    language = settings['language']
except:
    language = 'English'

def getLanguage():
    return language

print 'TTLocalizer: Running in language: %s' % language
from toontown.toonbase.TTLocalizerEnglish import *

if language != 'English':
    l = {}
    g = {}
    module = 'toontown.toonbase.TTLocalizer' + language
    englishModule = __import__('toontown.toonbase.TTLocalizerEnglish', g, l)
    foreignModule = __import__(module, g, l)
    for key, val in englishModule.__dict__.items():
        if key not in foreignModule.__dict__:
            print 'WARNING: Foreign module: %s missing key: %s' % (module, key)
            locals()[key] = val
        elif isinstance(val, types.DictType):
            fval = foreignModule.__dict__.get(key)
            for dkey, dval in val.items():
                if dkey not in fval:
                    print 'WARNING: Foreign module: %s missing key: %s.%s' % (module, key, dkey)
                    fval[dkey] = dval

            for dkey in fval.keys():
                if dkey not in val:
                    print 'WARNING: Foreign module: %s extra key: %s.%s' % (module, key, dkey)

    for key in foreignModule.__dict__.keys():
        if key not in englishModule.__dict__:
            print 'WARNING: Foreign module: %s extra key: %s' % (module, key)
