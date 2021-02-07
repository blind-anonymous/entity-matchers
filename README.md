# entity-matchers
Source code for "Progression or Stagnation? A Worrying Analysis of Neural Entity Matchers"

## Installation process
In order to run the code, you need to do the following steps: 
  1. Clone the repository using the command `git clone https://github.com/blind-anonymous/entity-matchers.git` 
  and `cd` in it: `cd entity-matchers`.
  (In case you have an ssh key set up with Github, you can clone the repository using the more convenient command 
  `git clone git@github.com:blind-anonymous/entity-matchers.git`)
  
  2. Install Anaconda (follow the instructions that you can find on the official documentation
  page https://docs.anaconda.com/anaconda/install/).
  
  3. Create a virtual environment with Anaconda, and install the dependencies 
  (we have already created a yml file with all the necessary dependencies). 
  If you do not have a GPU on your machine, then it is necessary for you change the line 151 of
  the file `env.yml`, and substitute `tensorflow-gpu==1.15.0` with `tensorflow==1.15.0`. 
  After you have done, just run `conda env create --file env.yml --name entity_match`. 
  If you prefer another name for the virtual environment, just change `entity_match` with your 
  desired name. This may take a while, depending on your internet connection. When it has finished,
  activate the virtual environment: `conda activate entity_match`.
  
  4. Download the datasets: you can find them following the link 
  https://drive.google.com/drive/folders/1x-8OonL8SMDpNyfGyBmwzsgQL_zVMojx?usp=sharing. 
  Extract the zip in any directory (you will need to provide the path to the datasets later).
  
  5. Download the word embeddings at the link https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip.
  Unzip them and put them in any directory (you will need to provide the path to the .vec file as well).

## Reproduction of results
