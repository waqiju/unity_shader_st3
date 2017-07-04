# beautify_unity_shader
A simple parser for Unity Shader.


# Usage

格式化代码文件

1. 输出到屏幕

py -m beautify_unity_shader <file> 

2. 输出到源文件

py -m beautify_unity_shader <file> -w

3. 输出到指定文件

py -m beautify_unity_shader <input_file> -o <output_file>


输出语法树（json格式）

py -m beautify_unity_shader --syntax <shader_file> -o <syntax_file>


# Issue

在使用过程中，如果发现任何问题，欢迎提交[Issue](https://github.com/waqiju/beautify_unity_shader/issues)。