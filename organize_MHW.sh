sed 's/"//g' $1 | while IFS=, read directory file name paletteSize finalDirectory; 
do
echo "creating $directory and copying $file" 
mkdir -p $(dirname "$directory") && cp "BC1S_$file.png" "$directory"; 
echo "colorizing $name - $directory"
python colorize.py -p $paletteSize -f $directory 
echo "compressing $name - $directory to dds"
nvcompress -color -alpha -bc1 $directory "${directory%.*}.dds"
echo "converting $name - $directory back to .tex"
./MHWTexConverter_by_Jodo.exe "${directory%.*}.dds"
echo "moving $name - $directory to $finalDirectory"
mkdir -p $(dirname "$finalDirectory") && cp "${directory%.*}.tex" "$finalDirectory"
done