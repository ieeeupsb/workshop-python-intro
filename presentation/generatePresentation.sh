#!/usr/bin/env bash

# Final presentation file

presentation="presentation.md"

# List all the files we want, in order, and their relative path

files_rel_path="separate_slides/"

first_file="slide_templates.md"
files=( "Home.md"
    "Interpreter.md"
    "Variables.md"
    "Data-Types.md"
    "Flow-Control.md"
    "Data-Structures.md"
    "Iteration.md"
    "Functions.md"
    "Comprehensions-and-Generators.md"
    "Modules.md"
    "End.md" )

# Create a new presentation file for the presentation
touch "${presentation}"

# # Final version of md is made, insert into HTML file
# cat remark_base_part1.html > ${presentation}

# Add the content from all files to the final .md file
echo "-> Added ${file}"
cat "${files_rel_path}${first_file}" > "${presentation}"

for file in ${files[*]}
do
    printf "\n---\n" >> "${presentation}"
    cat "${files_rel_path}${file}" >> "${presentation}"
    echo "-> Added ${file}"
done    

# cat remark_base_part2.html >> ${presentation}

echo "    -> Presentation generated on file:" ${presentation}
