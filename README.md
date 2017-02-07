# UnityShaderST3
UnityShaderST3 turns your Sublime Text 3 into a perceptive UnityShader Editor/Semi-IDE, followed the lastest Unity release.

UnityShaderST3 aim at improving the experience of reading and writing Unity Shader by provide three main functions. 
- Syntax Highligt
- Code Completions
- Goto Definition

<img src="misc/syntax_highligt_preview.png" width = "450" alt="syntax_highligt_preview" align=center />

## Features
- Comprehensive syntax highlight rules for .shader and .cginc files
- Provides a wide source of word hints for code completions, such as keywords, cg functions and Unity3D built-in marcos/variables/functions etc
- Alterable Unity3D version in response to incompatibility among different Unity3D releases. For Detail, please see Menu->Peferences->Package Settings->Unity Shader->Setting - Default
- Goto definition for built-in marcos/variables/functions
- Keep pace with the lastest version of both Sublime Text(3.X) and Unity3D(5.X)

## Installtion
**Easy Install (Recommend)**

Search on Package Control by ```Unity Shader``` and install.

https://packagecontrol.io/packages/Unity%20Shader

**Manual Install**

1. Download the project as zip
2. Unzip the zip file, rename the folder as UnityShader and move it to sublime text's package folder (Menu->Preferences->Browse Packages)

## Flaws
- Lacking of testing in MacOS platform. Since I rarely used to working in MacOS platform. But it's welcome for your feedback.
- Code completion is working in global scope. Sometimes, it became a little verbose.

## Thanks
At the beginning, [cjsjy123 / Unity-Shader](https://github.com/cjsjy123/Unity-Shader) give me a lot inspirations and a example of Sublime Text plugin.

------------
In the final, the project is developing. If you discover any mistake, please do not hesitate to tell me.
