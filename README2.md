<div align="center">

![Latest Release](https://img.shields.io/github/v/release/nuzcraft/MHWorldColorRandomizer?label=latest&link=https%3A%2F%2Fgithub.com%2Fnuzcraft%2FMHWorldColorRandomizer%2Freleases%2Flatest)![All Releases](https://img.shields.io/github/downloads/nuzcraft/MHWorldColorRandomizer/total?link=https%3A%2F%2Fgithub.com%2Fnuzcraft%2FMHWorldColorRandomizer%2Freleases)

</div>

# Monster Hunter World Color Randomizer

This is a mod to randomize monster colors in Monster Hunter World! A lot of the code and ideas are based on my [Freedom Unite Color Randomizer](https://github.com/nuzcraft/FreedomUniteColorRandomizer) work.

I've included files and instructions for how to colorize and mod your copy of the game which guarantees you'll be fighting 100% unique monsters!

Colorization was changed significantly in v1.2. Existing monster colorizations should be a bit more maintained and there should be less clashing color elements, especially with part breaks and on bigger monsters (like Zorah).

## How does the mod work?

The mod works by updating the texture files for each of the monsters with recolored ones. It tries to group siilar colors together and update them so the monsters maintain some of their original shading.

## Applying the mod

You'll need a mod call [Stracker's Loader](https://www.nexusmods.com/monsterhunterworld/mods/1982). This mod will create a `nativePC` directory next to your game. Any files you put in `nativePC` that match files in the game will be loaded instead of the game files. We will place our recolored texture files in nested folders in this directory so the game can pick them up.

1. Download the files from the most [recent release](https://github.com/nuzcraft/MHWorldColorRandomizer/releases/latest)
2. Extract one of the .zip files
3. copy the `em` folder into your `nativePC` directory

Note: you only need to copy files from `one` of the .zip files. I included multiple so that you have options of multiple random colorizations to choose from.

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

## Special Thanks

- Bonecuss has done some texture editing before, I've reached out to them for advice. They pointed me to NVIDIA texture tools which is amazing in streamlining the process.
- AlbinoDonkey and [their randomizer](https://github.com/JHenry2/mhw_randomizer)
- IncognitoMan and their [FU Complete mod](https://github.com/FUComplete)
- The [Monster Hunter World Modding wiki](https://github.com/Ezekial711/MonsterHunterWorldModding) might be exactly what I need
  - there's a [section](https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Obtaining,-Converting-and-Replacing-Textures) devoted to texture editing
