from file_search_engine import SearchEngine
import sys
import os

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

if sys.argv[1] == "-d":
    if not os.path.isfile(sys.argv[1]):
        print("when you put -d option, your query has to be a document path. If your query is an string, remove -d option.")
        sys.exit()


directory = sys.argv[len(sys.argv) - 2]
mode = int(sys.argv[len(sys.argv) - 1])
query = sys.argv[1]
fse = SearchEngine(directory, query, mode)
fse.main()


