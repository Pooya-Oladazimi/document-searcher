This python application can be used to extract topic(s) from a corpus of documents. Also, it finds the most similar documents to your desire query.
The input query can be a string or another document. 

### Compatibility 
Python 3.6

### Usage 

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
    
    - 5: Jaccard Similarity. Ex: `python run.py sampleData/ 5`
    
### Example
The sampleData contains five documents as targets. The sampleInput contains an input directory as the search query. The input can also be a string.

#### Term Frequency 
Example command:
    
`python run.py "world war" sampleData/ 0`
    
Output:
        
![0](https://user-images.githubusercontent.com/16546640/93804182-3a0c0d00-fc46-11ea-8a7f-838686a9bd3e.png)

    
    
    
