# Protein Molecular Function Annotation based on Transformer Embeddings

## Introduction
The next-generation sequencing technologies decreased the cost of protein sequence identification. However, the cost of determining protein functions is still high, due to the laboratory methods needed. With that, computational models have been used to annotate protein functions. In this work, we present and discuss a new approach for protein Molecular Function prediction based on Transformers embeddings. Our method surpassed state-of-the-art classifiers when it used only the amino acid sequence as input and when it employed amino acid sequence and homology search in Fmax and AuPRC metrics.

## Reproducibility
Run the following sequence of files:
```
1. data-augmentation.py
2. fine-tuning.py
3. extract-embeddings.py
4. meta-classifier.py
5. ds-tempo.py
```

## Citation
This repository contains the source codes of Protein Molecular Function Annotation based on Transformer Embeddings, as given in the paper:

Gabriel Bianchin de Oliveira, Helio Pedrini, Zanoni Dias. "Protein Molecular Function Annotation based on Transformer Embeddings", in proceedings of the 11th Brazilian Conference on Intelligent Systems (BRACIS). Campinas, Brazil, November 28 to December 01, 2022.

If you use this source code and/or its results, please cite our publication:
```
@inproceedings{OLIVEIRA_2022_BRACIS,
  author = {G.B. Oliveira and H. Pedrini and Z. Dias},
  title = {{Protein Molecular Function Annotation based on Transformer Embeddings}},
  booktitle = {11th Brazilian Conference on Intelligent Systems (BRACIS)},
  address = {Campinas, Brazil},
  month = {nov-dec},
  year = {2022}
}
```