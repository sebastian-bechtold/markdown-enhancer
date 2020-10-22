# Author: Sebastian Bechtold
# https://github.com/sebastian-bechtold
# Last change: 2020-10-22

import sys


infile = open(sys.argv[1], "r")



lines_out = []

toc = []

section_numbers = []

current_level = 0

for line in infile:

    ######### BEGIN Figure out heading level of current line #########
    heading_level = 0

    for char in line:
        if char == '#':
            heading_level += 1
        else:
            break
    ######### END Figure out heading level of current line #########

    if heading_level == 0:
        lines_out.append(line)
        continue

    if heading_level > current_level:
        section_numbers.append(0)
    elif heading_level < current_level:
        section_numbers.pop()
        
    section_numbers[-1] += 1
    current_level = heading_level

    ########### BEGIN Build heading number string ############
    heading_number = ""
    for sn in section_numbers:
        heading_number += str(sn)
        if sn != section_numbers[-1]:
            heading_number += "."
    ########### END Build heading number string ############

    heading_with_number = heading_number + ")" + line[heading_level:]
    toc.append(heading_with_number)
    
    
    lines_out.append(("#" * heading_level) + " " + heading_with_number + "\n")


with open(sys.argv[2], "w") as outfile:

    for line in lines_out:
        if line.strip() == "%%TOC%%":
            outfile.write("# Table of Contents" + "\n")
            for tocline in toc:
                outfile.write(tocline.strip() + "\n\n")
        else:
            outfile.write(line)
