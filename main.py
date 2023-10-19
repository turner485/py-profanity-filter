import csv
import os
import argparse
from timeit import default_timer as timer

profanity_list, code_list, detected_prof_dict = [], [], {'code':[], 'prof':[]}

def open_prof(args):
    _txt_file = args.txt_file
    with open(_txt_file) as f:
        text_doc_lines = f.readlines()
    for profanity_term in text_doc_lines:
        profanity_term = profanity_term.replace('\n', '')
        profanity_list.append(profanity_term)

def open_code_list(args):
    _csv_file = args.csv_file
    with open(_csv_file) as csv_file:
        csv_read = csv.reader(csv_file)
        for row in csv_read:
            code_list.append(' '.join(row))
    for code in code_list:
        for profanity in profanity_list:
            if profanity in code:
                print(f'Profanity detected!! ~ {code} ~ {profanity}')
                detected_prof_dict['code'].append(code)
                detected_prof_dict['prof'].append(profanity)
    new_list = [x for x in code_list if x not in detected_prof_dict['code']]
    return new_list

def update_csv(returned_list, args):
    _csv_file = args.csv_file
    with open(_csv_file, 'w', newline='') as out:
        writer = csv.writer(out)
        for row in returned_list:
            writer.writerow([row])
    print("Removing All codes containing profanity...\nDone!")
    start = timer()
    end = timer()
    print(end - start)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV data import & .txt file")
    parser.add_argument('--csv-file', type=str, help="Path to the CSV file")
    parser.add_argument('--txt-file', type=str, help="Path to the TXT file")
    args = parser.parse_args()  
    
    open_prof(args)
    returned_list = open_code_list(args)
    update_csv(returned_list, args)


