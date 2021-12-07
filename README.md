# Monster Hunter World Color Randomizer

This is the start of a project to randomize monster colors in Monster Hunter World! A lot of the code and ideas are based on my [Freedom Unite Color Randomizer](https://github.com/nuzcraft/FreedomUniteColorRandomizer) work.

This is still a WIP and not quite ready for consumption. The colorization code is taking way too long, and the settings in it aren't quite right. The monsters are coming out too light without enough variation.

## Current Instructions

The current iteration is configured to colorize the 3 rathian types and barroth only. Note that colorization takes a LONG time at the moment

1. Unchunk the chunks into a secondary location - go in into the unchunked folder and copy all the texture files from the spreadsheet out into a new folder.
2. Place the MHWTexConverter_by_Jodo in this folder.
3. Select ALL the .tex files and drag it to the MHWTexConverted to convert them all to .dds
   - this will put a BC1S\_ prefix on all the .dds files, which will make them easy to pick out
   - eventually this will be handled by the organize script
4. Open each file in GIMP and export it to a .png in the same folder
   - eventually this will be handled by NVIDIA texture tools I think
5. Copy the Organize and CSV into that same folder and run the organize script passing in the csv
   - this will copy the pngs to subfolders and begin colorizing them as they get moved
   - this will take a while with the current version of the script (like 60 mins per large monster?) and will take even longer if you bump up the palette size
   - basically, the code is super inefficient and the huge file sizes make it slow to recolor every pixel 4096x4096=16.777 million pixels each
   - this will also use NVIDEA texture tools to convert the png to dds
   - this will also use the TexConverter to convert the dds back into tex
   - finally this will move the final tex files into a new folder structure
6. Copy the contents of the 'final' folder to nativePC to overwrite any existing textures for the recolored monsters

## Resources Necessary

MHWNOChunk - this tool allows us to decompress the MHW chunks so that we can see what they are - https://www.nexusmods.com/monsterhunterworld/mods/411?tab=description

Texture Converter that I should be able to use to convert the .tex files to .dds - https://www.nexusmods.com/monsterhunterworld/mods/440 I don't know if this is better than something like Textconv, but I'll try this first. https://github.com/JodoZT/MHWTexConvertor

Strackers Loader allows us to use mods on MHW PC https://www.nexusmods.com/monsterhunterworld/mods/1982

NVIDIA Texture Tools - https://developer.nvidia.com/nvidia-texture-tools-exporter

## Special Thanks

Bonecuss has done some texture editing before, I've reached out to them for advice. They pointed me to NVIDIA texture tools which is amazing in streamlining the process.

AlbinoDonkey and their randomizer - https://github.com/JHenry2/mhw_randomizer

IncognitoMan and their FU Complete mod - https://github.com/FUComplete

OH SHIT! This Monster Hunter World Modding wiki might be exactly what I need - https://github.com/Ezekial711/MonsterHunterWorldModding - there's a section devoted to texture editing - https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Obtaining,-Converting-and-Replacing-Textures

https://gametechdev.github.io/Intel-Texture-Works-Plugin/ allows us to open files saved with BC7S compression and save them as pngs
