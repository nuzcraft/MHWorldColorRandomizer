sed 's/"//g' $1 | while IFS=, read directory file name paletteSize finalDirectory compression; 
do

IFS='|' read -r -a directory_arr <<< $directory
IFS='|' read -r -a file_arr <<< $file
IFS='|' read -r -a finalDirectory_arr <<< $finalDirectory
IFS='|' read -r -a compression_arr <<< $compression

for index in "${!directory_arr[@]}"
do
    # echo "$index ${directory_arr[index]}"
    # echo "$index ${file_arr[index]}"
    # echo "$index ${finalDirectory_arr[index]}"
    # echo "$index ${compression_arr[index]}"
    echo "creating ${directory_arr[index]} and copying ${file_arr[index]}" 
    mkdir -p $(dirname "${directory_arr[index]}") && cp "${compression_arr[index]}_${file_arr[index]}.png" "${directory_arr[index]}"; 
done

echo "colorizing $name - $directory"
python colorize.py -p $paletteSize -f $directory 

for index in "${!directory_arr[@]}"
do
    echo "compressing $name - ${directory_arr[index]} to dds"
    nvcompress -color -alpha -bc1 ${directory_arr[index]} "${directory_arr[index]%.*}.dds"
    echo "converting $name - ${directory_arr[index]} back to .tex"
    ./MHWTexConverter_by_Jodo.exe "${directory_arr[index]%.*}.dds"
    echo "moving $name - ${directory_arr[index]} to ${finalDirectory_arr[index]}"
    mkdir -p $(dirname "${finalDirectory_arr[index]}") && cp "${directory_arr[index]%.*}.tex" "${finalDirectory_arr[index]}"
done

done