# various scripts for Thai workflow in Robofont

Hi all, I have customized my Thai workflow in Robofont, and I recommend you do the same. So it's easier to follow through.

### install startup scripts:

* `contextual_filters.py` https://gist.github.com/frankrolf/07d09be24d22413e55ba2a9b4d12a2c8
* `ramsayController.py` https://gist.github.com/frankrolf/d15bf1d1dff97d455238100817e1833a

[How to set up a start up script](https://robofont.com/documentation/tutorials/setting-up-a-startup-script/)


### install RF extensions
Through Extension -> "Mechanic"

* RamsaySt
* Adjust Anchors
* Mark Feature Helper
* Mark Positioning tool


### install RF scripts

Put the whole `Thai Workshop` folder in your Robofont scripts directory.

Various scripts are contained:
* a script to clear anchors from selected glyphs (or current glyph)
* scripts to select Thai glyphs based on category
* scripts to drop approximate anchors per-category (in selected glyphs or current glyph). Please note: the anchors may need to be adjusted manually after dropping. Also, the scripts will not delete anchors for you, so make sure you take care of that first.


## manual intervention:

Change the Thai-specific BOR_HEIGHT variable in `modules/settings.py` to correspond to your specific setup.

## How to
In Thai, we need anchors in both consonant + tonemark. See more in [PDF explanation](https://www.dropbox.com/scl/fi/xdby9ucbn51j1ugky4x95/Thai-MarktoMark.pdf?rlkey=0ebf29qk8isn9gdfy9lotl7vy&dl=0) 

### Set up during the drawing process
1. Open “settings.py” Scripts -> Thai Workshop -> modules -> settings.py
2. Change the BOR_HEIGHT value, it’s the Thai height value 
3. To see/preview the position of the tonemark using plug-in : 
    1. Mark Positioning Tool 
    2. Adjust Anchors

Note: If No.2 is not set properly, the anchors will positioning wrongly, so please make sure to do this step.

### Set up for generating the font file
**Please make sure that the anchors were set on both consonant and tonemark. 
1. Open plug-in “mark feature helper” 
2. Click “Filter Eligible Glyphs” -> you will see the tonemark or / and diacritics show in the overall font view.
3. Then click “Build Group From Selection" -> this will create "COMBINING_MARKS" group (see image below)
![Screenshot of Robofont's group view](https://github.com/boomwooq/Thai-Workshop/blob/main/images/CleanShot%202026-05-06%20at%2012.50.42%402x.png)

Close and reopen the plug-in again at this stage after 1-3 are set.
4. Then re-open Mark Feature Helper again, this time we will make sure that (see image below)
	1. write mark.fea
	2. write mkmk.fea 
	both are selected
5. Then we click "Write Features Files" button -> within the same folder you will notice that there are two new files "mark.fea", and "mkmk.fea"
![Screenshot of Mark Feature Helper option](https://github.com/boomwooq/Thai-Workshop/blob/main/images/CleanShot%202026-05-06%20at%2013.59.28%402x.png)
![Screenshot of mark.fea and mkmk.fea appear in the folder](https://github.com/boomwooq/Thai-Workshop/blob/main/images/CleanShot%202026-05-06%20at%2013.01.15%402x.png)

6. Now you can generate the font through File -> Generate Font

Note: Everytime, you make change with anchors in any glyphs, those mark features have to be rewrite again.

## Check if the feature is working or not
There are multiple ways to check the opentype feature, 
1. You can check it by using [FontGoggles](https://fontgoggles.org)
2. You can do the typesetting in Adobe Indesign, Illustrator or others. If you are using .indd or .ai, please make sure you turn on [this setting](https://www.dropbox.com/scl/fi/7tc1454qn6081l0xxk7u9/BT_Thai_Guideline_InDDandAi2025.pdf?rlkey=2mrcxgi3tr8bxnqv0cukwbrsz&dl=0)
3. You can do the typesetting on your web browsers.


