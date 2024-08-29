import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_excel(file_path)
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = load_and_clean_data('models/crop_yield_data_sheet.xlsx')
    df.to_csv('data/cleaned_data.csv', index=False)  # Save cleaned data to a new directory
