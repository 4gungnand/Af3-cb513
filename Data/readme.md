# Flow of the project

1. Protein dataset is downloaded manually from different sources stored in `Original` folder.
2. The dataset is analyzed using EDA (Exploratory Data Analysis) using `EDA.ipynb` to get the appropriate preprocessing methods for each dataset.
3. The dataset is preprocessed using `Preprocessed.ipynb` and stored in `Preprocessed` folder.
4. The processed dataset is used for creating batch files using `Batching.ipynb`and stored in `Input` folder.
5. The batch files are used for predicting the protein structure using AlphaFold3.
6. The predicted protein structure is stored in `Predictions` folder.
7. The predicted protein structure is processed using `Postprocess.ipynb` and stored in `Postprocessed` folder.
8. The proteins of each dataset is evaluated using `Testing_{dataset_name}.ipynb`.
