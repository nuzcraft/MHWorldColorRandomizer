savedGroup="999"

sed 's/"//g' $1 | while IFS=, read group directory file name paletteSize finalDirectory compression; 
do

if [[ "${savedGroup}" == "${group}" ]]; then
    newDirectory="${newDirectory}|${directory}"
    newFile="${newFile}|${file}"
    newFinalDirectory="${newFinalDirectory}|${finalDirectory}"
    newCompression="${newCompression}|${compression}"
else
    
    if [[ "${savedGroup}" != "999" || "${group}" == "" ]]; then
        echo "${newDirectory},${newFile},${savedName},${savedPaletteSize},${newFinalDirectory},${newCompression}" >> fileMapping_MHW.csv
    fi
    savedGroup="${group}"
    newDirectory="${directory}"
    newFile="${file}"
    savedName="${name}"
    savedPaletteSize="${paletteSize}"
    newFinalDirectory="${finalDirectory}"
    newCompression="${compression}"
fi

done
