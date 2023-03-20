#!/usr/bin/env python3

import argparse
import sys
import multiprocessing
import json
from pprint import pprint

from PIL import Image
import numpy as np
import seaborn as sns

from skimage import measure

#from skimage import data, io
#from matplotlib import pyplot as plt


def analyze_saliency_map(saliency_map):
    with Image.open(saliency_map) as im:
        values = np.array(im) > 128
        #im.show()
        #io.imshow(values)
        #plt.show()

        all_labels = measure.label(values)
        #print(all_labels)
        #print(np.unique(all_labels))
        result = {
            "image": saliency_map,
            "mean_saliency": values.mean(),
            "std_saliency": values.std(),
            "connected_components": len(np.unique(all_labels))
        }
        #pprint(result)
        return result



def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='extracts saliency information from saliency map',
                                     epilog="stg7 2021",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("saliency_map", type=str, nargs="+", help="image of the saliency map, that has been extracted before")
    parser.add_argument('--cpu_count', type=int, default=multiprocessing.cpu_count() // 2, help='thread/cpu count')
    parser.add_argument("--result_file", type=str, default="saliency.json", help="file where all results are stored")

    a = vars(parser.parse_args())

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    result = pool.map(analyze_saliency_map, a["saliency_map"])

    with open(a["result_file"], "w") as rfp:
        json.dump(result, rfp, indent=4, sort_keys=True)





if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

