#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER: abdelrahman elseadawy
# DATE CREATED: 27/11/2020
# REVISED DATE:
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument
#       collection that you created with this function
#


def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, default="pet_images/",
                        help="path to folder of images")
    parser.add_argument("-m", "--arch", default='vgg', help="CNN model")
    parser.add_argument("-f", "--dogfile",
                        default='dognames.txt', help="dognames file")
    return parser.parse_args()
