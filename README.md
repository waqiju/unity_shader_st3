# UnityShaderST3

A sublime text plugin which aim at boosting happiness when editing Unity Shader, behaved as IDE-like, followed the lastest Unity release.

中文说明移步 >> [README_CH.md](doc/README_CH.md)   There is a README.md copied in Chinese.


## Main Functions

- Syntax Highligt

- Code Completions

- Code Format ( achieved by a parser speci for .shader grammer, see [beautify_unity_shader](https://github.com/waqiju/beautify_unity_shader) )

- Goto Definition


## Preview

<div>
    <img src="doc/syntax_highligt_preview.png" height="460" alt="syntax_highligt_preview"  />
    <img src="doc/code_format_preview.gif" height="460" alt="code_format_preview" />
</div>

## Features

- Comprehensive syntax highlight rules for .shader and .cginc files

- Plentiful words for code completions, such as keywords, cg functions and Unity3D built-in marcos/variables/functions etc

- Alterable Unity3D version in response to incompatibility among different Unity3D releases. For Detail, please see Menu->Peferences->Package Settings->Unity Shader->Setting - Default

- Scour and clean your source code in a accurate way

- Goto definition for built-in marcos/variables/functions

- Keep pace with the lastest version of both Sublime Text(3.X) and Unity3D(5.X)


## Installtion

**By Package Control (Recommend)**

Search on Sublime Package Control by ```Unity Shader``` and install.

https://packagecontrol.io/packages/Unity%20Shader

**Manual Install**

1. Download the project as zip

2. Unzip the zip file, rename the folder as UnityShader and move it to sublime text's package folder (Menu->Preferences->Browse Packages)


## Issue

If you discover any mistake or inspire any better idea, welcome to feedback at [Github Issue](https://github.com/waqiju/unity_shader_st3/issues). 


## Credit

At the beginning, [cjsjy123 / Unity-Shader](https://github.com/cjsjy123/Unity-Shader) give me a lot inspirations and a example of Sublime Text plugin.