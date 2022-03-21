sed 's/"//g' $1 | while IFS=, read directory file name finalDirectory; 
do

# HARD CODING ALERT
# this code assumes 10 release folders that look like v1.1_01 to v1.1_10
release_version="0"$((1 + $RANDOM % 10))
folder="v1.1_"${release_version: -2}
# echo $folder

IFS='|' read -r -a directory_arr <<< $directory
IFS='|' read -r -a file_arr <<< $file
IFS='|' read -r -a finalDirectory_arr <<< $finalDirectory

for index in "${!directory_arr[@]}"
do
    # echo "$index $folder/${directory_arr[index]}"
    # echo "$index ${file_arr[index]}"
    # echo "$index ${finalDirectory_arr[index]}"
    echo "copying ${file_arr[index]} from $folder/${directory_arr[index]} to ${finalDirectory_arr[index]}" 
    mkdir -p $(dirname "${finalDirectory_arr[index]}") && cp "$folder/${directory_arr[index]}" "${finalDirectory_arr[index]}"; 
done

# echo "colorizing $name - $directory"
# python colorize.py -p $paletteSize -f $directory 

# for index in "${!directory_arr[@]}"
# do
#     echo "compressing $name - ${directory_arr[index]} to dds"
#     nvcompress -color -alpha -bc1a ${directory_arr[index]} "${directory_arr[index]%.*}.dds"
#     echo "converting $name - ${directory_arr[index]} back to .tex"
#     ./MHWTexConverter_by_Jodo.exe "${directory_arr[index]%.*}.dds"
#     echo "moving $name - ${directory_arr[index]} to ${finalDirectory_arr[index]}"
#     mkdir -p $(dirname "${finalDirectory_arr[index]}") && cp "${directory_arr[index]%.*}.tex" "${finalDirectory_arr[index]}"
# done

done