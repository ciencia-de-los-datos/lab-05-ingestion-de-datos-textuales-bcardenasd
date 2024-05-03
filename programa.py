import os
import pandas as pd


def process_directory(directory_path):

    data = []
    sentiments = ['positive', 'negative', 'neutral']

    for sentiment in sentiments:
        folder_path = os.path.join(directory_path, sentiment)

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if filename.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    phrase = file.read().strip()
                    data.append({'phrase': phrase, 'sentiment': sentiment})

    return pd.DataFrame(data)

train_dataset = process_directory(os.path.join('data', 'train'))
test_dataset = process_directory(os.path.join('data', 'test'))

train_dataset.to_csv('train_dataset.csv', index=False)
test_dataset.to_csv('test_dataset.csv', index=False)