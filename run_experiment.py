import json
from utils import *
import os

DATA_DIR = 'data/'
ADV_DIR = 'adv_images/'
RES_DIR = 'results/'
N_SAVE = 10

os.makedirs(RES_DIR, exist_ok=True)

overall_stats = {
    'top1': 0,
    'top3': 0,
    'top5': 0,
    'total': 0,
}
for adv in os.listdir(ADV_DIR):
    save_name = (ADV_DIR + adv).replace("/", "_").replace(".", "_")
    new_path, _ = upload_image(ADV_DIR + adv)
    res = {
        'new_path': f'data/{new_path}',
        'top1': 0,
        'top3': 0,
        'top5': 0,
        'total': 0, 
    }
    print(f'Evaluating {ADV_DIR + adv}...')
    try:
        for i, image in enumerate(os.listdir(DATA_DIR)):
            print(f'\t{DATA_DIR + image}...')
            res[f'{DATA_DIR + image}'] = {}
            top_dict = search_image(DATA_DIR + image)
            top_dict.pop(f'data/{image}', None)
            keys = sorted(top_dict, key=top_dict.get)

            res[f'{DATA_DIR + image}']['top1'] = keys[0] == f'data/{new_path}'
            res[f'{DATA_DIR + image}']['top3'] = f'data/{new_path}' in keys[:3]
            res[f'{DATA_DIR + image}']['top5'] = f'data/{new_path}' in keys[:5]
            res[f'{DATA_DIR + image}']['raw'] = top_dict

            res['top1'] += res[f'{DATA_DIR + image}']['top1']
            res['top3'] += res[f'{DATA_DIR + image}']['top3']
            res['top5'] += res[f'{DATA_DIR + image}']['top5']
            res['total'] += 1

            if (i + 1) % N_SAVE == 0:
                with open(f'{RES_DIR + save_name}.json', 'w') as f:
                    json.dump(res, f, indent=4)
    finally:
        print(f'Deleting {ADV_DIR + adv}...')
        delete_image(f'data/{new_path}')
        overall_stats['top1'] += res['top1']
        overall_stats['top3'] += res['top3']
        overall_stats['top5'] += res['top5']
        overall_stats['total'] += res['total']

        with open(f'{RES_DIR[:-1]}/overall_stats.json', 'w') as f:
            json.dump(overall_stats, f, indent=4)
    
        with open(f'{RES_DIR + save_name}.json', 'w') as f:
            json.dump(res, f, indent=4)
