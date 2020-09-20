class SearchEngine:
    def __init__(self, directory_name, query, mode):
        import pandas
        from helper import Helper
        self.helper = Helper
        self.pandas = pandas
        self.directory_name = Helper.clean_path(directory_name)
        self.file_names = Helper.get_files_name(directory_name)
        self.query = query
        self.mode = mode

    def count_query(self):
        result = self.pandas.DataFrame(columns=['file', 'term_frequency'])
        for name in self.file_names:
            path = self.directory_name + name
            content = self.helper.get_file_content(path, True, self.query)
            rec = {}
            rec['file'] = name
            rec['term_frequency'] = len(content) - 1
            result = result.append(rec, ignore_index=True)
        return self.helper.sort_result(result, 'term_frequency')

    def cosine_similarity(self):
        from sklearn.metrics.pairwise import linear_kernel
        result = self.pandas.DataFrame(columns=['file', 'cosine_similarity'])
        for name in self.file_names:
            tfidf = self.helper.vectorize(self.query, self.directory_name + name)
            cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
            rec = {}
            rec['file'] = name
            rec['cosine_similarity'] = cosine_similarities[1]
            result = result.append(rec, ignore_index=True)
        return self.helper.sort_result(result, 'cosine_similarity')

    def euclidean_similarity(self):
        from sklearn.metrics.pairwise import euclidean_distances
        result = self.pandas.DataFrame(columns=['file', 'euclidean_similarity'])
        for name in self.file_names:
            tfidf = self.helper.vectorize(self.query, self.directory_name + name)
            eu_similarities = euclidean_distances(tfidf)
            rec = {}
            rec['file'] = name
            rec['euclidean_similarity'] = eu_similarities[1, 0]
            result = result.append(rec, ignore_index=True)
        return self.helper.sort_result(result, 'euclidean_similarity', False)

    def manhattan_similarity(self):
        import scipy
        result = self.pandas.DataFrame(columns=['file', 'manhattan_similarity'])
        for name in self.file_names:
            vectors_dict = {}
            tfidf = self.helper.vectorize(self.query, self.directory_name + name)
            matrix = scipy.sparse.coo_matrix(tfidf)
            for docId, wordId, vectorVal in zip(matrix.row, matrix.col, matrix.data):
                if wordId not in vectors_dict.keys():
                    vectors_dict[wordId] = [vectorVal, 0]
                else:
                    vectors_dict[wordId][1] = vectorVal
            rec = {}
            rec['file'] = name
            manhattan_dist = 0
            for word in vectors_dict.keys():
                manhattan_dist += abs(vectors_dict[word][0] - vectors_dict[word][1])
            rec['manhattan_similarity'] = manhattan_dist
            result = result.append(rec, ignore_index=True)
        return self.helper.sort_result(result, 'manhattan_similarity', False)

    def jaccard_similarity(self):
        result = self.pandas.DataFrame(columns=['file', 'jaccard_similarity'])
        for name in self.file_names:
            query_tokens = self.helper.get_unique_tokens(self.query)
            file_tokens = self.helper.get_unique_tokens(self.directory_name + name, True)
            rec = {}
            rec['file'] = name
            rec['jaccard_similarity'] = len(query_tokens & file_tokens) / len(file_tokens.union(query_tokens))
            result = result.append(rec, ignore_index=True)
        return self.helper.sort_result(result, 'jaccard_similarity')

    def topic_similarity(self):
        from gensim import corpora, models
        docs = []
        df = self.helper.get_df(self.file_names, self.directory_name)
        for name in self.file_names:
            Text = self.helper.get_file_content(self.directory_name + name, True, ' ')
            words = self.helper.cleaner(Text, df, len(self.file_names))
            docs.append(words)

        dictionary_LDA = corpora.Dictionary(docs)
        dictionary_LDA.filter_extremes(no_below=1)
        corpus = [dictionary_LDA.doc2bow(list_of_tokens) for list_of_tokens in docs]
        num_topics = 4
        lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary_LDA, passes=3, alpha=[0.01] * num_topics, eta=[0.01] * len(dictionary_LDA.keys()))
        for score, topic in lda_model.show_topics(formatted=True, num_topics=num_topics, num_words=10):
            print("Topic" + str(score) + ":")
            print(topic)
            print()

    def main(self):
        from tabulate import tabulate
        if self.mode == 0:  # term frequency
            print(tabulate(self.count_query(), headers='keys', tablefmt='psql', showindex="never"))

        elif self.mode == 1: # cosine similarity
            print(tabulate(self.cosine_similarity(), headers='keys', tablefmt='psql', showindex="never"))

        elif self.mode == 2: # Euclidean similarity
            print(tabulate(self.euclidean_similarity(), headers='keys', tablefmt='psql', showindex="never"))

        elif self.mode == 3: # manhattan similarity
            print(tabulate(self.manhattan_similarity(), headers='keys', tablefmt='psql', showindex="never"))

        elif self.mode == 4: # jaccard similarity
            print(tabulate(self.jaccard_similarity(), headers='keys', tablefmt='psql', showindex="never"))

        elif self.mode == 5:  # topic extraction
            print(tabulate(self.topic_similarity(), headers='keys', tablefmt='psql', showindex="never"))
