import nltk

def main():
    DATASETS = ['punkt_tab', 'stopwords']

    for dataset in DATASETS:
        nltk.download(DATASETS)
