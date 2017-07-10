This repository contains important python programs which were used to calculate entropy of written Marathi. For more information or questions, write to mihirskulkarni@gmail.com

Description of the files included:

`vishwakosh_book.py`: This program downloads a specified volume of Marathi Vishwakosh and saves it spreading over 20 different files using modulo 20 relation. i.e. 1st, 11th, 21st entries in the Vishwakosh would be saved in vishwakosh_books_1.txt and so on. Type 'python vishwakosh_book.py volume' from terminal to run this file where volume is the number of volume that you want to download.

replace_box.py: This file replaces Devanagari letters which are not part of canonical letter sets with a blank square for specified fraction (r). Canonical letter sets are sets of the most common Marathi letters which have total fractional share equal to r. Type 'python replace_box.py filename r' from terminal to run this file where filename is the name of the file and r is the fraction. r should be one of the following values: 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95. This will write a file named 'box_r_filename' as an output.

entropy_rate.py: This is a module which has multiple functions for calculating entropy_rate of Marathi. You can use it to calculate entropy of a text of your choice.

example:
```
import entropy_rate as er
er.entropy_from_file(filename,fraction, model_order)
```

fraction is same as r mentioned above. model_order is k-1 for calculating k-gram entropy.
