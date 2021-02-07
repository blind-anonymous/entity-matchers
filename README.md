
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
In order to run any of the experiments, cd in `/src`, activate the previously created virtual environment and run the following command:

```
python3 -u run_experiment.py \
        --method METHOD \
        --root_dataset DATASET_ROOT \
        --dataset DATASET \
        --dataset_division DATASET_DIVISION \
        --out_folder OUT_FOLDER \
        --gpu GPU_ID \
        --main_embeds MAIN_FILE \
        --args ARGUMENTS_FILE > LOG_FILE.log 
```
Where the following commands should be substituted with:
  1. `METHOD`: `RDGCN`, `BootEA` or `PARIS`, according to the experiment you want to replicate
  2. `DATASET_ROOT`: path to the directory that contains the dataset you need. For example, assume you want to run the main
  experiment on the DBP_en_YG_en_15K_V1, and you have downloaded the datasets in your `~/Download` folder, then `DATASET_ROOT`
  should be: `~/Downloads/datasets/main` (note that there must be no final slash).
  3. `DATASET`: the name of the dataset, in the example above `DBP_en_YG_en_15K_V1`.
  4. `DATASET_DIVISION`: the dataset division in folds, in our experiments `721_5folds` which stands for 70% test, 20% train, 10% validation, in 5 random folds (in order to repeat the same experiment 5 times, for robustness).
  5. `OUT_FOLDER`: folder where you want to store the output of the approach (and the final alignments). We recommend you create an `output/`  folder in the root directory of the repository, and for every experiment you create its own subfolder (like `output/main/DBP_en_YG_en_15K_V1` and so on).
  6. `GPU_ID`: mention it only if you have more than one GPU on your machine (ids are integers starting from zero, check for them using the command `nvidia-smi`. If you have only one GPU or you are running on CPU, do not use the argument `--gpu` in the first place.
  7. `MAIN_FILE`: the main file, which is `../../OpenEA_Mod/run/main_from_args.py`.
  8. `ARGUMENTS_FILE`: useful only if you are running BootEA or RDGCN, use the correct hyper parameter file that you can find under `/src/experiments/
  9. `LOG_FILE.log`: file where the output will be written. At the end of the log file you will find the F1-score of the run.
