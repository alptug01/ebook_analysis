import requests
from bs4 import BeautifulSoup

#web-scrapping operations as a function
def web_scrapping(name):
    link = requests.get(f"https://en.wikibooks.org/wiki/{name}/Print_version")
    soup = BeautifulSoup(link.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]
    p = list(body.children)[4]
    a = p.get_text()
    return a


def main():
    try:
        option = int(input("How many books will you enter(1 or 2): "))
        if (option == 1):

            name = input("Please enter the book name: ")
            #printing web-scraped book to txt
            file = open(f"{name}.txt", "w", encoding="utf-8")
            file.write(web_scrapping(name))
            file.close()
            #reading the txt
            file1 = open(f"{name}.txt", "r",encoding="utf-8")
            text = file1.read()
            file1.close()
            #removing unwanted word, numbers and punctuation marks
            stopword_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've","you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his','himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they','them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',"that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being','have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and','but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with','about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above','below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again','further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any','both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only','own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',"don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',"aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't",'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',"mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't",'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z','0','1','2','3','4','5','6','7','8','9',"0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz"]
            text1 = text.replace("\n", " ").replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":", " ").replace(";", " ").replace("'", " ").replace("/", " ").replace("-", " ").replace('"'," ").replace("(", " ").replace(")", " ").replace("\t", " ").replace("_", " ").replace("-", " ").replace("*", " ").replace("[", " ").replace("]", " ").replace("{", " ").replace("}", " ").replace("-", " ").replace("/", " ").replace("$", " ").replace("%", " ").replace("=", " ").replace("#", " ").replace("<", " ").replace(">", " ").replace("<=", " ").replace("==", " ").replace("<=", " ").replace(">=", " ").replace("←", " ").replace("\\", " ")
            text1 = text1.lower()
            let = text1.split()
            #to get words that are not stopword
            last_list = [x for x in let if x not in stopword_list]
            #converting list to set to remove repetitive words
            set_words = set(last_list)

            frequency = []
            set_words = list(set(set_words))
            #to find the number of repetitions of words
            for i in set_words:
                frequency.append(last_list.count(i))
            #to relate words with the number of repetitions and sort them by the number of repetitions
            frequency, set_words = zip(*sorted(zip(frequency, set_words)))
            words1 = set_words[::-1]
            frequency1 = frequency[::-1]

            #getting the number of words the user wants to see, if the user has entered more than the numbers in the txt, all will be shown
            #if the user don't enter a number, the first 20 words will be shown
            try:

                number = int(input("How many word do you want to see?(If you do not enter a number, the first 20 words will be shown): "))
                if (number > len(words1)):
                    number=len(words1)
                    print("The max value is ",number)


            except ValueError:
                number = 20
            #displaying output in an aligned format
            print(f"BOOK 1:{name}")
            str_no = "NO"
            str_word = "WORD"
            str_freq1 = "FREQ_1"
            print('%-20s %-20s %15s' % (str_no, str_word, str_freq1))

            for x_x in range(number):
                print('%-20s %-20s %15s' % (x_x + 1, words1[x_x], frequency1[x_x]))
        elif (option == 2):
            name1 = input("Please enter the first book's name: ")
            name2 = input("Please enter the second book's name: ")
            #web-scrapping operations, writing and reading txt
            file1 = open(f"{name1}.txt", "w", encoding="utf-8")
            a_1 = web_scrapping(name1)
            file1.write(a_1)
            file1.close()
            #creating different txt for second book
            file2 = open(f"{name2}.txt", "w", encoding="utf-8")
            a_2 = web_scrapping(name2)
            file2.write(a_2)
            file2.close()
            file1_1 = open(f"{name1}.txt", "r",encoding="utf-8")
            text1_1 = file1_1.read()
            file1_1.close()
            #removing unwanted word, numbers and punctuation marks
            stopword_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've","you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his','himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they','them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',"that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being','have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and','but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with','about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above','below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again','further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any','both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only','own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',"don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',"aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't",'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',"mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't",'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z','0','1','2','3','4','5','6','7','8','9',"0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz"]
            text1_1 = text1_1.replace("\n", " ").replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":", " ").replace(";", " ").replace("'", " ").replace("/", " ").replace("-", " ").replace('"', " ").replace("(", " ").replace(")", " ").replace("\t", " ").replace("_", " ").replace("-", " ").replace("*", " ").replace("[", " ").replace("]", " ").replace("{", " ").replace("}", " ").replace("-", " ").replace("/", " ").replace("$", " ").replace("%", " ").replace("=", " ").replace("#", " ").replace("<", " ").replace(">", " ").replace("<=", " ").replace("==", " ").replace("<=", " ").replace(">=", " ").replace("←", " ").replace("\\", " ")
            text1_1 = text1_1.lower()
            let_1 = text1_1.split()
            #to get words that are not stopword and converting to set
            last_list_1 = [x for x in let_1 if x not in stopword_list]
            set_words_1 = set(last_list_1)

            #reading second txt
            file2_1 = open(f"{name2}.txt", "r",encoding="utf-8")
            text2_1 = file2_1.read()
            file2_1.close()
            text2_1 = text2_1.replace("\n", " ").replace("!", " ").replace("?", " ").replace(".", " ").replace(","," ").replace(":", " ").replace(";", " ").replace("'", " ").replace("/", " ").replace("-", " ").replace('"', " ").replace("(", " ").replace(")", " ").replace("\t", " ").replace("_", " ").replace("-", " ").replace("*", " ").replace("[", " ").replace("]", " ").replace("{", " ").replace("}", " ").replace("-", " ").replace("/", " ").replace("$", " ").replace("%", " ").replace("=", " ").replace("#", " ").replace("<", " ").replace(">", " ").replace("<=", " ").replace("==", " ").replace("<=", " ").replace(">=", " ").replace("←", " ").replace("\\", " ")
            text2_1 = text2_1.lower()
            let_2 = text2_1.split()
            #same operations to find FREQ_2 and words2 like FREQ_1 and words1
            #some functions were removed due to code was so slowing when using function
            last_list_2 = [x for x in let_2 if x not in stopword_list]
            set_words_2 = set(last_list_2)

            #converting to sets to find common words
            #using the intersection function to find common words after they converted to sets
            set1 = set(set_words_1)
            set2 = set(set_words_2)
            intersets = set1.intersection(set2)
            #to find frequency_sum and intersection of words
            frequency_sum = []
            intersets = list(set(intersets))
            #to find freq_1
            freq1_1_1=[]

            for i in intersets:
                freq1_1_1.append(last_list_1.count(i))

            #to find freq_2
            freq2_2_2=[]
            for i in intersets:
                freq2_2_2.append(last_list_2.count(i))

            for i in intersets:
                frequency_sum.append(last_list_1.count(i) + last_list_2.count(i))

            frequency_sum, intersets,freq1_1_1,freq2_2_2 = zip(*sorted(zip(frequency_sum, intersets,freq1_1_1,freq2_2_2)))
            intersets = intersets[::-1]
            frequency_sum = frequency_sum[::-1]
            freq1_1_1 = freq1_1_1[::-1]
            freq2_2_2 = freq2_2_2[::-1]

            #getting word's number that will shown from user
            try:

                number = int(input("How many word do you want to see?(If you do not enter a number, the first 20 words will be shown): "))
                if (number > len(frequency_sum)):
                    number=len(frequency_sum)
                    print("The max value is ",number)
            except ValueError:
                number = 20

            #displaying common words in an aligned format
            print(" ")
            print("COMMON WORDS")
            print(f"BOOK 1:{name1}")
            print(f"BOOK 2:{name2}")
            str_no_1 = "NO"
            str_word_1 = "WORD"
            str_freq1_1 = "FREQ_1"
            str_freq1_2="FREQ_2"
            str_freq_sum="FREQ_SUM"

            print('%-20s %-20s %-20s %-20s %-20s' % (str_no_1, str_word_1, str_freq1_1,str_freq1_2,str_freq_sum))

            for x_x in range(number):
                print('%-20s %-20s %-20s %-20s %-20s' % (x_x + 1, intersets[x_x],freq1_1_1[x_x] ,freq2_2_2[x_x],frequency_sum[x_x]))

            #using the difference function of sets to find different words between two books
            words1_1=set(set_words_1)
            words1_2=set(set_words_2)
            difference_1= words1_1.difference(words1_2)
            difference_2=words1_2.difference(words1_1)
            dif_freq1=[]
            dif_freq2=[]
            difference_1=list(set(difference_1))
            difference_2=list(set(difference_2))

            #to find the number of words in the first book that differ from the second book and sorting
            for i in difference_1:
                dif_freq1.append(last_list_1.count(i) + last_list_2.count(i))

            dif_freq1, difference_1 = zip(*sorted(zip(dif_freq1, difference_1)))
            difference_1 = difference_1[::-1]
            dif_freq1 = dif_freq1[::-1]

            #to find the number of words in the second book that differ from the first book and sorting
            for i in difference_2:
                dif_freq2.append(last_list_1.count(i) + last_list_2.count(i))

            dif_freq2, difference_2 = zip(*sorted(zip(dif_freq2, difference_2)))
            difference_2 = difference_2[::-1]
            dif_freq2 = dif_freq2[::-1]
            if(number>len(difference_1)):
                number=len(difference_1)

            #displaying distinct words of the first book
            print(" ")
            print(f"BOOK 1:{name1}")
            print("DISTINCT WORDS")
            print('%-20s %-20s %-20s ' % (str_no_1, str_word_1, str_freq1_1))
            for x_x in range(number):
                print('%-20s %-20s %-20s' % (x_x + 1,difference_1[x_x],dif_freq1[x_x]))
            if(number>len(difference_2)):
                number=len(difference_2)
            print(" ")

            #displaying distinct words of the second book
            print(f"BOOK 2:{name2}")
            print("DISTINCT WORDS")
            print('%-20s %-20s %-20s ' % (str_no_1, str_word_1, str_freq1_2))
            for x_x in range(number):
                print('%-20s %-20s %-20s' % (x_x + 1,difference_2[x_x],dif_freq2[x_x]))
        else:
            print("Invalid value")
    except ValueError:
        print("Invalid value")


main()




