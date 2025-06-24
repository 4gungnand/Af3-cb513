# Project Name (Thesis Title)
English: BENCHMARKING ALPHAFOLD3 FOR PROTEIN SECONDARY STRUCTURE PREDICTION
Indonesian: Evaluasi performa prediksi AlphaFold3 untuk Prediksi Struktur Sekunder Protein

## Description
Protein Secondary Structure Prediction (PSSP) is a crucial component of computational biology, yet its accuracy remains a challenge, especially for 
non-canonical structures. This study exploratively evaluates AlphaFold3—a state-of-the-art model for tertiary structure prediction—as a PSSP tool by converting 
its 3D outputs using the DSSP algorithm. The evaluation was performed on the CB513, TS115, and CASP10 benchmark datasets using precision, recall, F1-score, 
and Q3/Q8 accuracy metrics. The results show that AlphaFold3 establishes a new, very high-performance baseline, consistently excelling in Q3 accuracy and achieving 
superior F1-scores for major structure classes such as the α-helix (H) and β-strand (E). Significantly, the model demonstrates a unique generalization capability by 
being the only one able to detect the highly rare π-helix (I) class with a meaningful recall. However, the analysis also identifies key limitations, namely a tendency for 
over-prediction in minor classes, which results in low precision, and difficulty in distinguishing flexible structures like turns (T) and bends (S). These findings 
confirm that AlphaFold3 can serve as a very powerful PSSP tool, particularly for common structures. 

## Keywords
AlphaFold3, Protein Secondary Structure Prediction (PSSP), Deep Learning, Q8 Accuracy, DSSP, Bioinformatic

## References
- SADGRU-SS: https://www.sciencedirect.com/science/article/abs/pii/S1568494624003788
- CB513: https://github.com/taneishi/CB513_dataset
- CASP14: https://github.com/Eryk96/CASP-Datasets/tree/main/data/casp14
- TS115: https://www.kaggle.com/datasets/tamzidhasan/protein-secondary-structure-casp12-cb513-ts115
