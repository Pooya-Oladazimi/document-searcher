class Helper:
    def __init__(self):
       pass

    @staticmethod
    def get_file_content(path, doesSplit, splitter):
        content = ""
        if len(path.split('.pdf')) == 1:
            file = open(path, "r")
            if doesSplit:
                content = file.read().lower().split(splitter)
            else:
                content = file.read().lower()
            file.close()
            return content
        if doesSplit:
            content = Helper.convert_pdf_to_text(path).lower().split(splitter)
        else:
            content = Helper.convert_pdf_to_text(path).lower()
        return content

    @staticmethod
    def get_filter_words():
        words = Helper.get_file_content('filters',True, '\n')
        return words

    @staticmethod
    def clean_path(path):
        if path[len(path) - 1] != '/':
            return path + '/'
        return path

    @staticmethod
    def convert_pdf_to_text(fileName):
        from tika import parser
        text = parser.from_file(fileName)
        return text['content']

    @staticmethod
    def get_files_name(path):
        from os import listdir
        names = []
        for name in listdir(path):
            if ".txt"in name or ".pdf" in name or "." not in name:
                names.append(name)
        return names

    @staticmethod
    def sort_result(datafram, key, reverse=True):
        result = datafram.sort_values(key)
        if reverse:
            result = result.iloc[::-1]
        result.reset_index(drop=True, inplace=True)
        result.index += 1
        return result

    @staticmethod
    def vectorize(query, path):
        from sklearn.feature_extraction.text import TfidfVectorizer
        content = Helper.get_file_content(path, False, '')
        corpus = []
        corpus.append(query)
        corpus.append(content)
        tfidf = TfidfVectorizer(min_df=1, stop_words="english").fit_transform(corpus)
        return tfidf

    @staticmethod
    def get_unique_tokens(Input, isPath=False):
        if isPath: # it is a file path
            temp = Helper.get_file_content(Input, True, " ")
            temp = set(temp)
            return temp
        temp = set(Input.lower().split(" "))
        return temp

    @staticmethod
    def cleaner(tokens, df, docs_count):
        import string
        import re
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer
        import nltk.stem as stemmer
        result = []
        forbiddens = Helper.get_filter_words()
        doc_tf = Helper.get_term_frequency(tokens)
        df_max = round(docs_count / 2)
        for token in tokens:
            if len(token) > 3 and re.match(r'[^\W\d]*$', token) and token not in string.punctuation and token not in stopwords.words('english')  and doc_tf[token] > 4 and df[token] > df_max:
                stemToken = stemmer.PorterStemmer().stem(token)
                final = WordNetLemmatizer().lemmatize(stemToken, pos='v')
                if final not in forbiddens:
                    result.append(final)
        return result

    @staticmethod
    def get_term_frequency(document):
        result = {}
        for word in set(document):
            result[word] = document.count(word)

        return result

    @staticmethod
    def get_df(files_name, prefix):
        result = {}
        for name in files_name:
            words = Helper.get_file_content(prefix + name, True, ' ')
            for w in set(words):
                if w in result.keys():
                    result[w] += 1
                else:
                    result[w] = 1
        return result

    @staticmethod
    def bagOfWords(tokenList):
        result_dict = {}
        for token in tokenList:
            if token in result_dict.keys():
                result_dict[token] += 1
            else:
                result_dict[token] = 1
        return result_dict

    @staticmethod
    def filter_bow(bow):
        result_dict = []
        for token in bow.keys():
            if bow[token] > 15:
                result_dict.append(token)
        return result_dict
