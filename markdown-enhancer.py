# Author: Sebastian Bechtold
# https://github.com/sebastian-bechtold
# Last change: 2020-10-22

import sys

infile = open(sys.argv[1], "r")

lines_out = []
toc = []
section_numbers = []

for line in infile:
    
    # Drop comments:
    if line.strip()[:2] == "//":        
        continue


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

    current_level = len(section_numbers)

    if heading_level > current_level:
        section_numbers.append(0)
    elif heading_level < current_level:
        section_numbers.pop()
        
    section_numbers[-1] += 1
    

    ########### BEGIN Build heading number string ############
    heading_number = ""
    for index,sn in enumerate(section_numbers):
        heading_number += str(sn)
        #if index != len(section_numbers) - 1:
        heading_number += "."
    ########### END Build heading number string ############

    heading_body = line[heading_level:].strip()

    
    toc_line = ""

    #if current_level != heading_level:
    #    toc_line += "\n"

    #toc_line += "* " * heading_level + ") " + heading_with_number + "\n"
    toc_line += "- " * heading_level + " " + heading_number + ") "  + heading_body + "\n"

    
    toc.append(toc_line)
    
    
    lines_out.append(("#" * heading_level) + " " + heading_number + " " + heading_body + "\n")

    


with open(sys.argv[2], "w") as outfile:

    for line in lines_out:
        if line.strip() == "%%TOC%%":
            outfile.write("# Table of Contents" + "\n")
            for tocline in toc:
                outfile.write(tocline)
        else:
            outfile.write(line)
