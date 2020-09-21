from file_search_engine import SearchEngine
import sys
import os

directory = ""
mode = -1
query = ""

if sys.argv[len(sys.argv) - 1] not in ['0', '1', '2', '3', '4', '5']:
    print("Please specify the running mode. Running modes are:")
    print("0:  term frequency")
    print("1:  cosine similarity")
    print("2:  Euclidean similarity")
    print("3:  manhattan similarity")
    print("4:  jaccard similarity")
    print("5:  topic extraction")
    print()
    sys.exit()

if not os.path.isdir(sys.argv[len(sys.argv) - 2]):
    print("Please specify the target directory which contains the target documents.")
    sys.exit()

mode = int(sys.argv[len(sys.argv) - 1])
if mode == 5: # topic extraction does not need input query
    directory = sys.argv[len(sys.argv) - 2]
    file_searcher = SearchEngine(directory, "", mode)
    file_searcher.main()
    sys.exit()

if sys.argv[1] == "-d":
    if not os.path.isfile(sys.argv[2]) or len(sys.argv) != 5 :
        print("when you put -d option, your query has to be a document path. If your query is a string, remove -d option.")
        sys.exit()
    query = open(sys.argv[2], 'r').read()

if sys.argv[1] != "-d":
    if os.path.isfile(sys.argv[1]):
        print("Your query is a file path instead of a string. Please use -d option for file path.")
        sys.exit()
    query = sys.argv[1]

directory = sys.argv[len(sys.argv) - 2]
file_searcher = SearchEngine(directory, query, mode)
file_searcher.main()
sys.exit()

