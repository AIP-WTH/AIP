import openai
import pandas as pd
import glob
import re

# ChatGPT API key
openai.api_key = ''

# maximum article length (token issue)
MAX_ARTICLE_LENGTH = 800

# original article files
file_pattern = 'path/to/data/*.csv'
file_list = glob.glob(file_pattern)

# backup file that stores gpt responses for some unexpected accidents
backup_file = open('./gpt_backup/responses.txt', 'w')

error_count = 0
for category_step, file in enumerate(file_list):
    category = file.split('/')[-1].split('.')[0]

    df = pd.read_csv(file, encoding='cp949', header=None)
    # article length should be less than MAX_ARTICLE_LENGTH
    df = df[df[4].str.len() <= MAX_ARTICLE_LENGTH]
    # randomly pick 1000 / N articles from each category
    df = df.sample(n=min(int(1000 / len(file_list), len(df))), random_state=1234)
    
    row_step = 0
    for index, row in df.iterrows():
        # progress check
        print(f'[{category_step + 1} / {len(file_list)} ({row_step + 1} / {len(df)})]: {file}')
        row_step += 1

        # article content
        original_content = row[4]

        try:
            # generate gpt news
            res = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    { 'role': 'system', 'content': 'You are a Korean news reporter. Rewrite the article in your style.' },
                    { 'role': 'user', 'content': original_content },
                ]
            )
            translated = res.choices[0].message.content
        except Exception as e:
            error_count += 1
            print(e)
            continue
        
        # backup gpt responses
        backup_file.write(f'{category}\t{index}\n{translated}\n===\n')

        # preprocess translated content and save it
        translated = re.sub(r'(\n)+', ' ', translated)
        df.at[index, 4] = translated

    # save csv file
    df.to_csv(f'./news_gpt/{category}.csv', encoding='utf-8-sig', header=None)

print(f'=== error count: {error_count} ===')

backup_file.close()