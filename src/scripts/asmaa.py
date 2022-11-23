#    $Author: belal (risha) $
#    $Revision: 1.5 $

from KALIMAT_Corpus.nouns import nouns, nounsOLD

def asmaa():
    
    noun_prefix = ('|ب|ك|ل|ف|أ|م|لل')
    
    noun_suffix = ('|ا|ك|ه|ي|ل|ى|ها|تها|هم|تهم|هما|تهما|هن|تهن|ما|كما|كن|كم|نا|ان|ون|ين|وت|يه|تا|ات')
    
    # فعيل فعال فعول افعال مفعول مفعال مفعيل فعليل فعلاء فعلان فعلى فيعل مفعل فاعول استفعال تفعيل مفتعل
    noun_conjugations = '..ي.|..ا.|..و.|ا..ا.|م..و.|م..ا.|م..ي.|...ي.|...اء|...ان|...ى|.ي..|م...|.ا.و.|است..ا.|ت..ي.|م.ت..'
                        
    asmaa = u'^({0})({1})({2})$'.format(noun_prefix, noun_conjugations, noun_suffix)
    asmaa2 = u'^({0})({1})({2})$'.format(noun_prefix, nouns, noun_suffix)
    asmaa3 = u'^({0})({1})({2})$'.format(noun_prefix, nounsOLD, noun_suffix)
    return asmaa, asmaa2, asmaa3