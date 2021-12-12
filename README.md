# Monster Hunter World Color Randomizer

This is a project to randomize monster colors in Monster Hunter World! A lot of the code and ideas are based on my [Freedom Unite Color Randomizer](https://github.com/nuzcraft/FreedomUniteColorRandomizer) work.

Each generation creates a unique set of monster colorations to discover and enjoy!

Video: [Demo 1 - Lunastra Intro](https://youtu.be/0EAiGU3hEmM)

## Instructions

Basic Rundown - decompress the MHW chunks, get the .tex files, convert them to .dds, convert them to .png, edit the .pngs to recolor the monsters, compress them to .dds, convert them to .tex, use the new .tex files in game.

### Tools you'll need

- MHWNoChunk - this tool allows us to decompress the MHW chunks so that we can see what they are - https://www.nexusmods.com/monsterhunterworld/mods/411?tab=description
- MHWTexConverter - this tool allows us to convert .tex files (from the MHW chunks) into .dds files that are usable/editable. It also converts things back from .dds to .tex - https://www.nexusmods.com/monsterhunterworld/mods/440 and https://github.com/JodoZT/MHWTexConvertor
- Strackers Loader - this .dll allows us to use mods on MHW PC via the nativePC directory - https://www.nexusmods.com/monsterhunterworld/mods/1982
- NVIDIA Texture Tools - this tool makes it really easy to recompress an edited .png to .dds - https://developer.nvidia.com/nvidia-texture-tools-exporter
- Intel Texture Works - this tool allows us to open .dds files compressed with BC7S compression and save them as .png - https://gametechdev.github.io/Intel-Texture-Works-Plugin/
- GIMP dds plugin - this tool allows us to open .dds files and save them as .png - https://code.google.com/archive/p/gimp-dds/

### Steps

These instructions are such that you can use my code to create your own unique monster variations! Unfortunately, the setup is pretty time consuming, mostly because I couldn't find a way to automate the conversion of .dds files to .pngs.

1. Unchunk the chunks into a secondary location using MHWNoChunk.
   - you only need the **em** folder, so you don't need to unchunk everything
2. Go into each of the subfolders in the **em** folder and copy out _most_ of the .tex with the BM or BML suffix from the _mod_ folders out into a new folder (now called tertiary location)
   - em/em001/00/mod/em001_00_BML.tex (main texture file for rathian)
     - copy these out to a tertiary location
   - some BM/BML files aren't necessary, like eye sphere, noImage, fake env
   - see **fileMapping_groups_WCR.csv** for a list of files that I've chosen to colorize
3. Place the MHWTexConverter_by_Jodo in the tertiary folder.
4. Select ALL the .tex files and drag it to the MHWTexConverter to convert them all to .dds
   - this will put a BC1S\_ or BC7S\_ prefix on all the .dds files
5. Open each BC1S\_ file in GIMP and export it to a .png in the same folder
   - this requires the GIMP dds plugin and does not work for the BC7S files
   - load mipmaps for each of these files
6. Open each BC7S\_ file in photoshop and export it to a .png in the same folder
   - this requires the Intel Texture Works plugin
   - this will work for both BC7S and BC1S files, GIMP isn't really needed
   - load mipmaps for each of these
   - this was the only way I found to edit BC7S files (like the main textures for Tigrex and Paolumu)
7. Throughout this process, feel free to run **movefiles_WCR.sh** if you want, it will move all the .tex and .dds files into subfolders as a cleanup process. Not required.
8. Copy the Organize and CSV into that same folder and run the organize script passing in the csv
   - this will copy the pngs to subfolders and begin colorizing them as they get moved
   - this will take a while with the current version of the script (like 60 mins per large monster?) and will take even longer if you bump up the palette size
   - basically, the code is super inefficient and the huge file sizes make it slow to recolor every pixel 4096x4096=16.777 million pixels each
   - this will also use NVIDEA texture tools to convert the png to dds
   - this will also use the TexConverter to convert the dds back into tex
   - finally this will move the final tex files into a new folder structure
9. Copy the contents of the 'final' folder to nativePC to overwrite any existing textures for the recolored monsters

## Special Thanks

- Bonecuss has done some texture editing before, I've reached out to them for advice. They pointed me to NVIDIA texture tools which is amazing in streamlining the process.
- AlbinoDonkey and their randomizer - https://github.com/JHenry2/mhw_randomizer
- IncognitoMan and their FU Complete mod - https://github.com/FUComplete
- The Monster Hunter World Modding wiki might be exactly what I need - https://github.com/Ezekial711/MonsterHunterWorldModding - there's a section devoted to texture editing - https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Obtaining,-Converting-and-Replacing-Textures
