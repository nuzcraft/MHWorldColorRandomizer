<div align="center">

![Latest Release](https://img.shields.io/github/v/release/nuzcraft/MHWorldColorRandomizer?label=latest&link=https%3A%2F%2Fgithub.com%2Fnuzcraft%2FMHWorldColorRandomizer%2Freleases%2Flatest)![All Releases](https://img.shields.io/github/downloads/nuzcraft/MHWorldColorRandomizer/total?link=https%3A%2F%2Fgithub.com%2Fnuzcraft%2FMHWorldColorRandomizer%2Freleases)

</div>

# Monster Hunter World Color Randomizer

This is a mod to randomize monster colors in Monster Hunter World! A lot of the code and ideas are based on my [Freedom Unite Color Randomizer](https://github.com/nuzcraft/FreedomUniteColorRandomizer) work.

I've included files and instructions for how to colorize and mod your copy of the game which guarantees you'll be fighting 100% unique monsters!

Colorization was changed significantly in v1.2. Existing monster colorizations should be a bit more maintained and there should be less clashing color elements, especially with part breaks and on bigger monsters (like Zorah).
<div align="center">
  
![collage](https://github.com/nuzcraft/MHWorldColorRandomizer/assets/20135847/9c889f67-d4d8-4986-a886-f056bd6f86c9)

</div>

## How does the mod work?

The mod works by updating the texture files for each of the monsters with recolored ones. It tries to group siilar colors together and update them so the monsters maintain some of their original shading.

## Applying the mod

You'll need a mod call [Stracker's Loader](https://www.nexusmods.com/monsterhunterworld/mods/1982). This mod will create a `nativePC` directory next to your game. Any files you put in `nativePC` that match files in the game will be loaded instead of the game files. We will place our recolored texture files in nested folders in this directory so the game can pick them up.

### Option 1 - Use the files provided

---

1. Download the files from the most [recent release](https://github.com/nuzcraft/MHWorldColorRandomizer/releases/latest)
2. Extract one of the .zip files
3. copy the `em` folder into your `nativePC` directory

Note: you only need to copy files from `one` of the .zip files. I included multiple so that you have options of multiple random colorizations to choose from.

### Option 2 - Create your own unique mod!

---

#### Basic Rundown

Decompress the MHW chunks, get the .tex files, convert them to .dds, convert them to .png, edit the .pngs to recolor the monsters, compress them to .dds, convert them to .tex, use the new .tex files in game.

#### Tools you'll need

- [MHWNoChunk](https://www.nexusmods.com/monsterhunterworld/mods/411?tab=description) - this tool allows us to decompress the MHW chunks so that we can see what they are
- [MHWTexConverter](https://www.nexusmods.com/monsterhunterworld/mods/440) - this tool allows us to convert .tex files (from the MHW chunks) into .dds files that are usable/editable. It also converts things back from .dds to .tex
  - also available [here](https://github.com/JodoZT/MHWTexConvertor)
- [Stracker's Loader](https://www.nexusmods.com/monsterhunterworld/mods/1982) - this .dll allows us to use mods on MHW PC via the nativePC directory
- [NVIDIA Texture Tools](https://developer.nvidia.com/nvidia-texture-tools-exporter) - this tool makes it really easy to recompress an edited .png to .dds
- [Intel Texture Works](https://gametechdev.github.io/Intel-Texture-Works-Plugin/) - this tool allows us to open .dds files compressed with BC7S compression and save them as .png
- [GIMP dds plugin](https://code.google.com/archive/p/gimp-dds/) - this tool allows us to open .dds files and save them as .png

#### Steps

These instructions are such that you can use my code to create your own unique monster variations! Unfortunately, the setup is pretty time consuming, mostly because I couldn't find a way to automate the conversion of .dds files to .pngs.

At the moment, full colorization of all files takes a few hours. I've already done a bit of work optimizing the code, but these files are big and colorizing them takes some time.

1. Unchunk the chunks into a secondary location using MHWNoChunk.
   - you only need the `em` folder, so you don't need to unchunk everything
2. Go into each of the subfolders in the `em` folder and copy out _most_ of the .tex with the BM or BML suffix from the `mod` folders out into a new folder (now called tertiary location)
   - `em/em001/00/mod/em001_00_BML.tex` (main texture file for rathian)
     - copy these out to a tertiary location
   - some BM/BML files aren't necessary, like eye sphere, noImage, fake env
   - see `fileMapping_groups_WCR.csv` for a list of files that I've chosen to colorize
3. Place the `MHWTexConverter_by_Jodo` in the tertiary folder.
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
7. Throughout this process, feel free to run `movefiles_WCR.sh` if you want, it will move all the .tex and .dds files into subfolders as a cleanup process. Not required.
8. The csv files have separate uses:
   - `fileMapping_v2_WCR.csv` is the main file we'll be using to actually organize and colorize the files using `organize_WCR.sh`
     - it is a new version of `fileMapping_WCR.csv` that groups more monster textures to be colored similarly. They can be used interchangeably.
     - `fileMapping_v2_WCR.csv` was used for v1.2
   - `fileMapping_groups_WCR.csv` is used in conjunction with `grouping_WCR.sh` to build the `fileMapping_WCR.csv` file. Use these if you want to update the files you want to colorize.
9. `colorize.py` is the script that actually colorizes, you need it in the tertiary folder
10. Copy the `organize_WCR.sh` and `fileMapping_v2_WCR.csv` into the tertiary folder (the one full of .pngs) and run the organize script passing in the csv
    - `./organizeWCR.sh fileMapping_v2_WCR.csv`
    - this will copy the pngs to subfolders and begin colorizing them as they get moved
    - this will also use NVIDEA texture tools to convert the png to dds
    - this will also use the TexConverter to convert the dds back into tex
    - finally this will move the final tex files into a new folder structure
11. Copy the contents of the 'final' folder to nativePC to overwrite any existing textures for the recolored monsters

## Release Randomizer

Included in the release files for v1.1 and onward is a `Release Randomizer`. These 2 scripts for you to generate your own pseudo-random collections yourself! Download and unzip the folder all generations, then use bash to run _./ReleaseRandomizer_MHW.sh fileMapping_ReleaseRandomizer_MHW.csv_. This will randomly assign monster colorations from the available options into a new generation in the _final_ folder. Copy the contents of this folder into your nativePC directory.

For generating, your folder structure should look something like this:

top level folder

- v1.1_01
  - em
- v1.1_02
  - em
- v1.1_03
- v1.1_04
- v1.1_05
- v1.1_06
- v1.1_07
- v1.1_08
- v1.1_09
- v1.1_10
- fileMapping_MHW_ReleaseRandomizer.csv
- ReleaseRandomizer_MHW.sh
- ReleaseRandomizer_MHW_CHAOS.sh

Use `ReleaseRandomizer_MHW_CHAOS.sh` to uncouple any files that would normally move together (i.e. wings and body files or large monster and small monster files) to further randomize larger monsters into abominations.

## Bonus: Greyscale Scripts

Greyscale mod files are only available on itch.io, but the scripts for you to greyscale your own textures are included in `greyscale_organize_WCR.sh`, `greyscale.py`, and `greyscale_saturate_eyes.py`.

The greyscale script will do just that, convert every texture to greyscale. The other script with greyscale everything except the eyes, which it will boost the saturation of to try to make the eyes really pop.

## Special Thanks

- Bonecuss has done some texture editing before, I've reached out to them for advice. They pointed me to NVIDIA texture tools which is amazing in streamlining the process.
- AlbinoDonkey and [their randomizer](https://github.com/JHenry2/mhw_randomizer)
- IncognitoMan and their [FU Complete mod](https://github.com/FUComplete)
- The [Monster Hunter World Modding wiki](https://github.com/Ezekial711/MonsterHunterWorldModding) might be exactly what I need
  - there's a [section](https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Obtaining,-Converting-and-Replacing-Textures) devoted to texture editing
