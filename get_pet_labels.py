#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels_hints.py
#
# PROGRAMMER: abdelrahman elseadawy
# DATE CREATED: 27/11/2020
# REVISED DATE:
# PURPOSE: This is a *hints* file to help guide students in creating the
#          function get_pet_labels that creates the pet labels from the image's
#          filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: EDIT and ADD code BELOW to do the following that's stated in the
#       comments below that start with "TODO: 2" for the get_pet_labels function
#       Please be certain to replace None in the return statement with
#       results_dic dictionary that you create with this function
#


def get_pet_labels(image_dir):
    # Creates list of files in directory
    in_files = listdir(image_dir)

    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).

    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):

        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if in_files[idx][0] != ".":

            # Creates temporary label variable to hold pet label name extracted
            pet_label = ""
            lp = in_files[idx].lower()
            wlp = lp.split("_")

            # TODO: 2a. BELOW REPLACE pass with CODE that will process each
            #          filename in the in_files list to extract the dog breed
            #          name from the filename. Recall that each filename can be
            #          accessed by in_files[idx]. Be certain to place the
            #          extracted dog breed name in the variable pet_label
            #          that's created as an empty string ABOVE
            for w in wlp:
                if w.isalpha():
                    pet_label = pet_label + w + " "

            pet_label = pet_label.strip()

            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates
            # duplicate files (filenames)
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:",
                      in_files[idx])

    # TODO 2b. Replace None with the results_dic dictionary that you created
    # with this function
    return results_dic
