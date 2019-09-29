#!/usr/bin/env python3

import mathpix
import json

#
# Simple example of calling Mathpix OCR with ../images/algebra.jpg.
#
# We use the default ocr (math-only) and a single return format, latex_simplified.
#
# If you expect the image to be math and want to examine the result
# as math then the return format should either be latex_simplified,
# asciimath, or mathml. If you want to see the text in the image then
# you should include 'ocr': ['math', 'text'] as an argument and
# the return format should be either text or latex_styled
# (depending on whether you want to use the result as a paragraph or an equation).
#
import os
import sys

def main(root):
    savedir = '../out/'
    list = os.listdir(root)
    for filename in list:
        path = os.path.join(rootdir, filename)
        if not os.path.isfile(path):
            break
        portion = os.path.splitext(filename)
        savename = portion[0]+'.txt'
        savepath = os.path.join(savedir, savename)
        r = mathpix.latex({
            'src': mathpix.image_uri(path),
            'formats': ['latex_simplified']
        })

        with open(savepath, 'w+') as f:
            f.write(r['latex_simplified'])
        print(savepath)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        rootdir = sys.argv[1]
        if os.path.isdir(rootdir):
            main(rootdir)
#
# print(json.dumps(r, indent=4, sort_keys=True))
# assert(r['latex_simplified'] == '12 + 5 x - 8 = 12 x - 10')
