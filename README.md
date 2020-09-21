This python application can be used to extract topic(s) from a corpus of documents. Also, it finds the most similar documents to your desire query.
The input query can be a string or another document. 

### Compatibility 
Python 3.6

### install packages
`pip install requirements.txt `  or  `python -m pip install requirements.txt`

### Usage 
**Note**: The sample documents are examples. you can replace them with your desire documents. 

`python run.py [-d] InputString[InputFilePath] targetDirectoryPath Mode`

- **targetDirectoryPath**: the target document corpus that you want to search/process (sampleData is the example directory)

- **InputString**: The input String query for document similarity.
  - Option [-d]: if your input is a file, use -d option. InputFilePath is the path to your input document.(sampleInput directory contains an example file) 
  
  Example:
  
  `python run.py "world war" sampleData/ 3`
  
  `python run.py -d sampleInput/input  sampleData/ 4`
  
- **Mode**: The running mode for document similarity or topic extraction.
    - 0: Term Frequency. Ex: `python run.py "world war" sampleData/ 0`
    
    - 1: Cosine Similarity. Ex: `python run.py "world war" sampleData/ 1`
    
    - 2: Euclidean Similarity. Ex: `python run.py "world war" sampleData/ 2`
    
    - 3: Manhattan Similarity. Ex: `python run.py "world war" sampleData/ 3`
    
    - 4: Jaccard Similarity. Ex: `python run.py "world war" sampleData/ 4`
    
    - 5: Topic Extraction. Ex: `python run.py sampleData/ 5`
    
### Features Explanation
The sampleData contains five documents as targets. The sampleInput contains an input directory as the search query. The input can also be a string. 


#### Term Frequency 
Count the input query occurrence in the target documents. 

Example command:
    
`python run.py "world war" sampleData/ 0`
    
Output:
        
![0](https://user-images.githubusercontent.com/16546640/93804182-3a0c0d00-fc46-11ea-8a7f-838686a9bd3e.png)


#### Cosine Similarity
Ranks documents based on cosine similarity to the input query. 

Example command:

`python run.py "world war" sampleData/ 1`

Output:


![1](https://user-images.githubusercontent.com/16546640/93812493-fddea980-fc51-11ea-91f3-75a66307ce67.png)


#### Euclidean Similarity
Ranks documents based on Euclidean similarity to the input query. 

Example command:

`python run.py "world war" sampleData/ 2`

Output:

![2](https://user-images.githubusercontent.com/16546640/93812722-4e560700-fc52-11ea-8e9d-9da974aa0bad.png)


#### Manhattan Similarity
Ranks documents based on Manhattan similarity to the input query. 

Example command:

`python run.py "world war" sampleData/ 3`

Output:

![3](https://user-images.githubusercontent.com/16546640/93812913-937a3900-fc52-11ea-883f-8f9d583052f8.png)


#### Jaccard Similarity
Ranks documents based on Jaccard similarity to the input query. 

Example command:

`python run.py "world war" sampleData/ 4`

Output:

![4](https://user-images.githubusercontent.com/16546640/93813023-c290aa80-fc52-11ea-87f6-cf78770f70e5.png)


#### Topic Extraction
Extract the main topics of the documents in the corpus. It uses the LDA (Latent Dirichlet allocation) topic modeling. You may need to change the input parameter to get the accurate result for your custom corpus. You can look at the `def topic_similarity(self):` in the *file_search_engine.py*. Besides, if you do not like some of the topic words, you can put them in the **filter** file (each line one word, look at the example content in the filter file), and rerun it. It excludes them in the next run(s). 

Example command:

`python run.py sampleData/ 5`

Output:

![5](https://user-images.githubusercontent.com/16546640/93814279-9bd37380-fc54-11ea-95ed-b23c3aa3411d.png)



### Sample Documents

- Sample1: War Wikipedia article (https://en.wikipedia.org/wiki/War) 

- Sample2.txt: World War II Wikipedia article (https://en.wikipedia.org/wiki/World_War_II)

- Sample3: Europe Wikipedia article(https://en.wikipedia.org/wiki/Europe)

- Sample4: Atomic bombings of Hiroshima and Nagasaki Wikipedia article(https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki)

- Sample5.pdf: World War I Wikipedia article (https://en.wikipedia.org/wiki/World_War_I)


    
