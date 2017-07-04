import unittest
from . import formatter
from .formatter import I, IAA, SSI, G, E, STR


# prog --> 'Shader' String { shader_body_elms }
def _p1(self):
    return I() + STR('Shader') + ' ' + self.String.toCode() + E() \
        + IAA() + STR('{') + E() \
        + G(-1) + self.shader_body_elms.toCode() + G(-1) \
        + SSI() + STR('}')


# shader_body_elms --> shader_body_elm shader_body_elms
def _p2(self):
    return self.shader_body_elm.toCode() + self.shader_body_elms.toCode()


# shader_body_elms -->
def _p3(self):
    return ''

# shader_body_elm --> props
def _p4(self):
    return G() + self.props.toCode() + G()


# shader_body_elm --> category
def _p5(self):
    return G() + self.category.toCode() + G()


# shader_body_elm --> subshr
def _p6(self):
    return G() + self.subshr.toCode() + G()


# shader_body_elm --> cg_prog
def _p7(self):
    return G() + self.cg_prog.toCode() + G()


# shader_body_elm --> fall_back_cmd
def _p8(self):
    return self.fall_back_cmd.toCode()


# shader_body_elm --> custom_editor_cmd
def _p9(self):
    return self.custom_editor_cmd.toCode()


# shader_body_elm --> dependency_cmd
def _p10(self):
    return self.dependency_cmd.toCode()


# props --> 'Properties' { props_body }
def _p11(self):
    return I() + STR('Properties') + E() \
        + IAA() + STR('{') + E() \
        + self.props_body.toCode() \
        + SSI() + STR('}') + E()


# props_body --> prop_stm props_body
def _p12(self):
    return self.prop_stm.toCode() + self.props_body.toCode()


# props_body -->
def _p13(self):
    return ''

# prop_stm --> ID ( String , prop_type ) = prop_init
def _p14(self):
    return I() + self.ID.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_stm --> [ ID ] ID ( String , prop_type ) = prop_init
def _p15(self):
    return I() + STR('[') + self.ID1.toCode() + STR('] ') + self.ID2.toCode() + STR(' (') + self.String.toCode() + STR(',') + self.prop_type.toCode() + STR(')') + STR('=') + self.prop_init.toCode() + E()


# prop_stm --> [ ID ] [ ID ] ID ( String , prop_type ) = prop_init
def _p16(self):
    return I() + STR('[') + self.ID1.toCode() + STR('] ') + STR('[') + self.ID2.toCode() + STR('] ') + self.ID3.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_stm --> [ 'Enum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
def _p17(self):
    return I() + STR('[') + STR('Enum') + STR('(') + self.enum_items.toCode() + STR(')') + STR('] ') + self.ID.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_stm --> [ 'MaterialEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
def _p18(self):
    return I() + STR('[') + STR('MaterialEnum') + STR('(') + self.enum_items.toCode() + STR(')') + STR('] ') + self.ID.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_stm --> [ 'KeywordEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
def _p19(self):
    return I() + STR('[') + STR('KeywordEnum') + STR('(') + self.enum_items.toCode() + STR(')') + STR('] ') + self.ID.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_stm --> [ 'Toggle' ( ID ) ] ID ( String , prop_type ) = prop_init
def _p20(self):
    return I() + STR('[') + STR('Toggle') + STR('(') + self.ID1.toCode() + STR(')') + STR('] ') + self.ID2.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_stm --> [ 'MaterialToggle' ] ID ( String , prop_type ) = prop_init
def _p21(self):
    return I() + STR('[') + STR('MaterialToggle') + STR('] ') + self.ID.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_stm --> [ 'ToggleOff' ] ID ( String , prop_type ) = prop_init
def _p22(self):
    return I() + STR('[') + STR('ToggleOff') + STR('] ') + self.ID.toCode() + STR(' (') + self.String.toCode() + STR(', ') + self.prop_type.toCode() + STR(')') + STR(' = ') + self.prop_init.toCode() + E()


# prop_type --> 'Color'
def _p23(self):
    return STR('Color')


# prop_type --> 'Vector'
def _p24(self):
    return STR('Vector')


# prop_type --> 'Range'
def _p25(self):
    return STR('Range')


# prop_type --> 'Int'
def _p26(self):
    return STR('Int')


# prop_type --> 'Float'
def _p27(self):
    return STR('Float')


# prop_type --> '2D'
def _p28(self):
    return STR('2D')


# prop_type --> 'Cube'
def _p29(self):
    return STR('Cube')


# prop_type --> '3D'
def _p30(self):
    return STR('3D')


# prop_type --> 'Any'
def _p31(self):
    return STR('Any')


# prop_type --> 'Range' ( Number , Number )
def _p32(self):
    return STR('Range') + STR('(') + self.Number1.toCode() + STR(', ') + self.Number2.toCode() + STR(')')


# prop_init --> Number
def _p33(self):
    return self.Number.toCode()


# prop_init --> String { }
def _p34(self):
    return self.String.toCode() + STR(' { ') + STR('}')


# prop_init --> String { ID }
def _p35(self):
    return self.String.toCode() + STR('{ ') + self.ID.toCode() + STR(' }')


# prop_init --> ( Number , Number , Number )
def _p36(self):
    return STR('(') + self.Number1.toCode() + STR(', ') + self.Number2.toCode() + STR(', ') + self.Number3.toCode() + STR(')')


# prop_init --> ( Number , Number , Number , Number )
def _p37(self):
    return STR('(') + self.Number1.toCode() + STR(', ') + self.Number2.toCode() + STR(', ') + self.Number3.toCode() + STR(', ') + self.Number4.toCode() + STR(')')


# enum_items --> enum_item
def _p38(self):
    return self.enum_item.toCode()


# enum_items --> enum_item , enum_items
def _p39(self):
    return self.enum_item.toCode() + STR(', ') + self.enum_items.toCode()


# enum_item --> id_list
def _p40(self):
    return self.id_list.toCode()


# enum_item --> Number
def _p41(self):
    return self.Number.toCode()


# category --> 'Category' { category_body_elms }
def _p42(self):
    return I() + STR('Category') + E() \
        + IAA() + STR('{') + E() \
        + self.category_body_elms.toCode() \
        + SSI() + STR('}') + E()


# category_body_elms --> category_body_elm category_body_elms
def _p43(self):
    return self.category_body_elm.toCode() + self.category_body_elms.toCode()


# category_body_elms -->
def _p44(self):
    return ''

# category_body_elm --> cmd_stm
def _p45(self):
    return self.cmd_stm.toCode()


# category_body_elm --> subshr
def _p46(self):
    return self.subshr.toCode()


# subshr --> 'SubShader' { subshr_body_elms }
def _p47(self):
    return I() + STR('SubShader') + E() \
        + IAA() + STR('{') + E() \
        + G(-1) + self.subshr_body_elms.toCode() + G(-1) \
        + SSI() + STR('}') + E()


# subshr_body_elms --> subshr_body_elm subshr_body_elms
def _p48(self):
    return self.subshr_body_elm.toCode() + self.subshr_body_elms.toCode()


# subshr_body_elms -->
def _p49(self):
    return ''

# subshr_body_elm --> cmd_stm
def _p50(self):
    return self.cmd_stm.toCode()


# subshr_body_elm --> shr_pass
def _p51(self):
    return G() + self.shr_pass.toCode() + G()


# subshr_body_elm --> cg_prog
def _p52(self):
    return self.cg_prog.toCode()


# cmd_stm --> cmd_name id_or_number_or_placeholder
def _p53(self):
    return I() + self.cmd_name.toCode() + ' ' + self.id_or_number_or_placeholder.toCode() + E()


# cmd_stm --> 'AlphaTest' ID
def _p54(self):
    return I() + STR('AlphaTest') + ' ' + self.ID.toCode() + E()


# cmd_stm --> 'AlphaTest' ID placeholder
def _p55(self):
    return I() + STR('AlphaTest') + ' ' + self.ID.toCode() + ' ' + self.placeholder.toCode() + E()


# cmd_stm --> 'BindChannels' { bind_channel_stms }
def _p56(self):
    return I() + STR('BindChannels') + E() \
        + IAA() + STR('{') + E() \
        + self.bind_channel_stms.toCode() \
        + SSI() + STR('}') + E()


# cmd_stm --> 'Blend' ID
def _p57(self):
    return I() + STR('Blend') + ' ' + self.ID.toCode() + E()


# cmd_stm --> 'Blend' id_or_number_or_placeholder id_or_number_or_placeholder
def _p58(self):
    return I() + STR('Blend') + ' ' + self.id_or_number_or_placeholder1.toCode() + ' ' + self.id_or_number_or_placeholder2.toCode() + E()


# cmd_stm --> 'Fog' { 'Mode' ID }
def _p59(self):
    return I() + STR('Fog') + STR(' { ') + STR('Mode ') + self.ID.toCode() + STR(' }') + E()


# cmd_stm --> 'Fog' { 'Color' ( Number , Number , Number , Number ) }
def _p60(self):
    return I() + STR('Fog') + STR(' { ') + STR('Color') + STR(' (') + self.Number1.toCode() + STR(', ') + self.Number2.toCode() + STR(', ') + self.Number3.toCode() + STR(', ') + self.Number4.toCode() + STR(')') + STR(' }') + E()


# cmd_stm --> 'Material' { meterial_stms }
def _p61(self):
    return I() + STR('Material') + E() \
        + IAA() + STR('{') + E() \
        + self.meterial_stms.toCode() \
        + SSI() + STR('}') + E()


# cmd_stm --> 'Name' String
def _p62(self):
    return I() + STR('Name ') + self.String.toCode() + E()


# cmd_stm --> 'Offset' id_or_number_or_placeholder , id_or_number_or_placeholder
def _p63(self):
    return I() + STR('Offset ') + self.id_or_number_or_placeholder1.toCode() + STR(', ') + self.id_or_number_or_placeholder2.toCode() + E()


# cmd_stm --> 'Stencil' { stencil_stms }
def _p64(self):
    return I() + STR('Stencil') + STR(' {') + self.stencil_stms.toCode() + STR(' }') + E()


# cmd_stm --> 'SetTexture' placeholder { set_texture_stms }
def _p65(self):
    return I() + STR('SetTexture ') + self.placeholder.toCode() + E() \
        + IAA() + STR('{ ') + E() \
        + self.set_texture_stms.toCode() \
        + SSI() + STR('}') + E()


# cmd_stm --> 'Tags' { tags_stms }
def _p66(self):
    return I() + STR('Tags') + E() \
        + IAA() + STR('{') + E() \
        + self.tags_stms.toCode() \
        + SSI() + STR('}') + E() \


# cmd_name --> 'AlphaToMask'
def _p67(self):
    return STR('AlphaToMask')


# cmd_name --> 'ColorMask'
def _p68(self):
    return STR('ColorMask')


# cmd_name --> 'ColorMaterial'
def _p69(self):
    return STR('ColorMaterial')


# cmd_name --> 'Cull'
def _p70(self):
    return STR('Cull')


# cmd_name --> 'Lighting'
def _p71(self):
    return STR('Lighting')


# cmd_name --> 'LOD'
def _p72(self):
    return STR('LOD')


# cmd_name --> 'SeparateSpecular'
def _p73(self):
    return STR('SeparateSpecular')


# cmd_name --> 'ZTest'
def _p74(self):
    return STR('ZTest')


# cmd_name --> 'ZWrite'
def _p75(self):
    return STR('ZWrite')


# id_or_number_or_placeholder --> ID
def _p76(self):
    return self.ID.toCode()


# id_or_number_or_placeholder --> Number
def _p77(self):
    return self.Number.toCode()


# id_or_number_or_placeholder --> ( Number , Number , Number , Number )
def _p78(self):
    return STR('(') + self.Number1.toCode() + STR(', ') + self.Number2.toCode() + STR(', ') + self.Number3.toCode() + STR(', ') + self.Number4.toCode() + STR(')')


# id_or_number_or_placeholder --> placeholder
def _p79(self):
    return self.placeholder.toCode()


# placeholder --> [ ID ]
def _p80(self):
    return STR('[') + self.ID.toCode() + STR(']')


# bind_channel_stms --> bind_channel_stm bind_channel_stms
def _p81(self):
    return self.bind_channel_stm.toCode() + self.bind_channel_stms.toCode()


# bind_channel_stms -->
def _p82(self):
    return ''

# bind_channel_stm --> 'Bind' String , ID
def _p83(self):
    return I() + STR('Bind ') + self.String.toCode() + STR(', ') + self.ID.toCode() + E()


# meterial_stms --> meterial_stm meterial_stms
def _p84(self):
    return self.meterial_stm.toCode() + self.meterial_stms.toCode()


# meterial_stms -->
def _p85(self):
    return ''

# meterial_stm --> ID id_or_number_or_placeholder
def _p86(self):
    return I() + self.ID.toCode() + ' ' + self.id_or_number_or_placeholder.toCode() + E()


# stencil_stms --> stencil_stm stencil_stms
def _p87(self):
    return self.stencil_stm.toCode() + self.stencil_stms.toCode()


# stencil_stms -->
def _p88(self):
    return ''

# stencil_stm --> ID id_or_number_or_placeholder
def _p89(self):
    return ' ' + self.ID.toCode() + ' ' + self.id_or_number_or_placeholder.toCode()


# set_texture_stms --> set_texture_stm set_texture_stms
def _p90(self):
    return self.set_texture_stm.toCode() + self.set_texture_stms.toCode()


# set_texture_stms -->
def _p91(self):
    return ''

# set_texture_stm --> 'matrix' placeholder
def _p92(self):
    return I() + STR('matrix ') + self.placeholder.toCode() + E()


# set_texture_stm --> 'constantColor' id_or_number_or_placeholder
def _p93(self):
    return I() + STR('constantColor ') + self.id_or_number_or_placeholder.toCode() + E()


# set_texture_stm --> 'combine' combine_options
def _p94(self):
    return I() + STR('combine ') + self.combine_options.toCode() + E()


# combine_options --> combine_option combine_options
def _p95(self):
    return self.combine_option.toCode() + self.combine_options.toCode()


# combine_options --> combine_option , combine_options
def _p96(self):
    return self.combine_option.toCode() + STR(', ') + self.combine_options.toCode()


# combine_options --> combine_option combine_option_op combine_options
def _p97(self):
    return self.combine_option.toCode() + ' ' + self.combine_option_op.toCode() + ' ' + self.combine_options.toCode()


# combine_options -->
def _p98(self):
    return ''

# combine_option --> ID
def _p99(self):
    return self.ID.toCode()


# combine_option --> ( ID )
def _p100(self):
    return STR('(') + self.ID.toCode() + STR(')')


# combine_option_op --> +
def _p101(self):
    return STR('+')


# combine_option_op --> -
def _p102(self):
    return STR('-')


# combine_option_op --> *
def _p103(self):
    return STR('*')


# combine_option_op --> /
def _p104(self):
    return STR('/')


# tags_stms --> tag_smt tags_stms
def _p105(self):
    return self.tag_smt.toCode() + self.tags_stms.toCode()


# tags_stms -->
def _p106(self):
    return ''

# tag_smt --> String = String
def _p107(self):
    return I() + self.String1.toCode() + STR(' = ') + self.String2.toCode() + E()


# shr_pass --> 'Pass' { pass_body_elms }
def _p108(self):
    return I() + STR('Pass') + E() \
        + IAA() + STR('{') + E() \
        + self.pass_body_elms.toCode() \
        + SSI() + STR('}') + E()


# shr_pass --> 'GrabPass' { pass_body_elms }
def _p109(self):
    return I() + STR('GrabPass') + E() \
        + IAA() + STR('{') + E() \
        + self.pass_body_elms.toCode() \
        + SSI() + STR('}') + E()


# shr_pass --> 'UsePass' String
def _p110(self):
    return I() + STR('UsePass ') + self.String.toCode() + E()


# pass_body_elms --> pass_body_elm pass_body_elms
def _p111(self):
    return self.pass_body_elm.toCode() + self.pass_body_elms.toCode()


# pass_body_elms -->
def _p112(self):
    return ''

# pass_body_elm --> cmd_stm
def _p113(self):
    return self.cmd_stm.toCode()


# pass_body_elm --> cg_prog
def _p114(self):
    return self.cg_prog.toCode()


# cg_prog --> 'CGPROGRAM' cg_prog_body 'ENDCG'
def _p115(self):
    return I() + STR('CGPROGRAM') + E() \
        + G(-1)+ self.cg_prog_body.toCode() + G(-1) \
        + I() + STR('ENDCG') + E()


# cg_prog --> 'CGINCLUDE' cg_prog_body 'ENDCG'
def _p116(self):
    return I() + STR('CGINCLUDE') + E() \
        + G(-1)+ self.cg_prog_body.toCode() + G(-1) \
        + I() + STR('ENDCG') + E()


# fall_back_cmd --> 'FallBack' String
def _p117(self):
    return I() + STR('FallBack ') + self.String.toCode() + E()


# fall_back_cmd --> 'FallBack' 'Off'
def _p118(self):
    return I() + STR('FallBack ') + STR('Off') + E()


# custom_editor_cmd --> 'CustomEditor' String
def _p119(self):
    return I() + STR('CustomEditor ') + self.String.toCode() + E()


# dependency_cmd --> 'Dependency' String = String
def _p120(self):
    return I() + STR('Dependency ') + self.String1.toCode() + STR(' = ') + self.String2.toCode() + E()


# id_list --> ID
def _p121(self):
    return self.ID.toCode()


# id_list --> ID id_list
def _p122(self):
    return self.ID.toCode() + ' ' + self.id_list.toCode()


# cg_prog_body --> cg_stms
def _p123(self):
    return self.cg_stms.toCode()


# cg_stms --> cg_stm cg_stms
def _p124(self):
    return self.cg_stm.toCode() + self.cg_stms.toCode()


# cg_stms -->
def _p125(self):
    return ''

# cg_stm --> preprocessing_stm
def _p126(self):
    return self.preprocessing_stm.toCode()


# cg_stm --> function_definition
def _p127(self):
    return G() + self.function_definition.toCode() + G()


# cg_stm --> dec
def _p128(self):
    return self.dec.toCode()


# cg_stm --> 'CBUFFER_START' ( ID ) dec_list 'CBUFFER_END'
def _p129(self):
    return IAA() + STR('CBUFFER_START') + STR('(') + self.ID.toCode() + STR(')') + E() \
        + self.dec_list.toCode() \
        + SSI() + STR('CBUFFER_END')


# function_definition --> dec_specifier declarator compound_stm
def _p130(self):
    return I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + E() \
        + self.compound_stm.toCode()


# function_definition --> dec_specifier declarator : ID compound_stm
def _p131(self):
    return I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + STR(' : ') + self.ID.toCode() + E() \
        + self.compound_stm.toCode()


# function_definition --> [ ID ( Number ) ] dec_specifier declarator compound_stm
def _p132(self):
    return I() + STR('[') + self.ID.toCode() + STR('(') + self.Number.toCode() + STR(')') + STR(']') + E() \
        + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + E() \
        + self.compound_stm.toCode()


# function_definition --> [ ID ( Number ) ] dec_specifier declarator : ID compound_stm
def _p133(self):
    return I() + STR('[') + self.ID1.toCode() + STR('(') + self.Number.toCode() + STR(')') + STR(']') + E() \
        + I() + self.dec_specifier.toCode() + ' ' + self.declarator.toCode() + E() + STR(' : ') + self.ID2.toCode() + E() \
        + self.compound_stm.toCode()


# preprocessing_stm --> pp_if_stm
def _p134(self):
    return self.pp_if_stm.toCode()


# preprocessing_stm --> pp_cmd
def _p135(self):
    return I() + self.pp_cmd.toCode() + E()


# preprocessing_stm --> marco_unfold
def _p136(self):
    return self.marco_unfold.toCode()


# pp_if_stm --> # 'if' PPTokens
def _p137(self):
    return I() + STR('#') + STR('if') + self.PPTokens.toCode() + E()


# pp_if_stm --> # 'ifdef' ID
def _p138(self):
    return I() + STR('#') + STR('ifdef') + ' ' + self.ID.toCode() + E()


# pp_if_stm --> # 'ifndef' ID
def _p139(self):
    return I() + STR('#') + STR('ifndef') + ' ' + self.ID.toCode() + E()


# pp_if_stm --> # 'elif' PPTokens
def _p140(self):
    return I() + STR('#') + STR('elif') + self.PPTokens.toCode() + E()


# pp_if_stm --> # 'else'
def _p141(self):
    return I() + STR('#') + STR('else') + E()


# pp_if_stm --> # 'endif'
def _p142(self):
    return I() + STR('#') + STR('endif') + E()


# pp_cmd --> # 'include' String
def _p143(self):
    return STR('#') + STR('include ') + self.String.toCode()


# pp_cmd --> # 'pragma' PPTokens
def _p144(self):
    return STR('#') + STR('pragma') + self.PPTokens.toCode()


# pp_cmd --> # 'define' PPTokens
def _p145(self):
    return STR('#') + STR('define') + self.PPTokens.toCode()


# marco_unfold --> exp ;
def _p146(self):
    return I() + self.exp.toCode() + STR(';') + E()


# dec_list --> dec
def _p147(self):
    return self.dec.toCode()


# dec_list --> dec_list dec
def _p148(self):
    return self.dec_list.toCode() + self.dec.toCode()


# primary_exp --> ID
def _p149(self):
    return self.ID.toCode()


# primary_exp --> String
def _p150(self):
    return self.String.toCode()


# primary_exp --> Number
def _p151(self):
    return self.Number.toCode()


# primary_exp --> ( exp )
def _p152(self):
    return STR('(') + self.exp.toCode() + STR(')')


# postfix_exp --> primary_exp
def _p153(self):
    return self.primary_exp.toCode()


# postfix_exp --> postfix_exp [ exp ]
def _p154(self):
    return self.postfix_exp.toCode() + STR('[') + self.exp.toCode() + STR(']')


# postfix_exp --> postfix_exp ( )
def _p155(self):
    return self.postfix_exp.toCode() + STR('(') + STR(')')


# postfix_exp --> postfix_exp ( argument_exp_list )
def _p156(self):
    return self.postfix_exp.toCode() + STR('(') + self.argument_exp_list.toCode() + STR(')')


# postfix_exp --> buildin_type_name ( argument_exp_list )
def _p157(self):
    return self.buildin_type_name.toCode() + STR('(') + self.argument_exp_list.toCode() + STR(')')


# postfix_exp --> postfix_exp . ID
def _p158(self):
    return self.postfix_exp.toCode() + STR('.') + self.ID.toCode()


# postfix_exp --> postfix_exp ++
def _p159(self):
    return self.postfix_exp.toCode() + STR('++')


# postfix_exp --> postfix_exp --
def _p160(self):
    return self.postfix_exp.toCode() + STR('--')


# argument_exp_list --> assignment_exp
def _p161(self):
    return self.assignment_exp.toCode()


# argument_exp_list --> argument_exp_list , assignment_exp
def _p162(self):
    return self.argument_exp_list.toCode() + STR(', ') + self.assignment_exp.toCode()


# unary_exp --> postfix_exp
def _p163(self):
    return self.postfix_exp.toCode()


# unary_exp --> ++ unary_exp
def _p164(self):
    return STR('++') + self.unary_exp.toCode()


# unary_exp --> -- unary_exp
def _p165(self):
    return STR('--') + self.unary_exp.toCode()


# unary_exp --> unary_op unary_exp
def _p166(self):
    return self.unary_op.toCode() + self.unary_exp.toCode()


# unary_op --> +
def _p167(self):
    return STR('+')


# unary_op --> -
def _p168(self):
    return STR('-')


# unary_op --> !
def _p169(self):
    return STR('!')


# unary_op --> ~
def _p170(self):
    return STR('~')


# cast_exp --> unary_exp
def _p171(self):
    return self.unary_exp.toCode()


# cast_exp --> ( buildin_type_name ) cast_exp
def _p172(self):
    return STR('(') + self.buildin_type_name.toCode() + STR(')') + self.cast_exp.toCode()


# binary_exp --> cast_exp
def _p173(self):
    return self.cast_exp.toCode()


# binary_exp --> binary_exp binary_op unary_exp
def _p174(self):
    return self.binary_exp.toCode() + ' ' + self.binary_op.toCode() + ' ' + self.unary_exp.toCode()


# binary_op --> *
def _p175(self):
    return STR('*')


# binary_op --> /
def _p176(self):
    return STR('/')


# binary_op --> %
def _p177(self):
    return STR('%')


# binary_op --> +
def _p178(self):
    return STR('+')


# binary_op --> -
def _p179(self):
    return STR('-')


# binary_op --> <<
def _p180(self):
    return STR('<<')


# binary_op --> >>
def _p181(self):
    return STR('>>')


# binary_op --> <
def _p182(self):
    return STR('<')


# binary_op --> >
def _p183(self):
    return STR('>')


# binary_op --> <=
def _p184(self):
    return STR('<=')


# binary_op --> >=
def _p185(self):
    return STR('>=')


# binary_op --> ==
def _p186(self):
    return STR('==')


# binary_op --> !=
def _p187(self):
    return STR('!=')


# binary_op --> &
def _p188(self):
    return STR('&')


# binary_op --> ^
def _p189(self):
    return STR('^')


# binary_op --> |
def _p190(self):
    return STR('|')


# binary_op --> &&
def _p191(self):
    return STR('&&')


# binary_op --> ||
def _p192(self):
    return STR('||')


# conditional_exp --> binary_exp
def _p193(self):
    return self.binary_exp.toCode()


# conditional_exp --> binary_exp ? exp : conditional_exp
def _p194(self):
    return self.binary_exp.toCode() + STR(' ? ') + self.exp.toCode() + STR(' : ') + self.conditional_exp.toCode()


# assignment_exp --> conditional_exp
def _p195(self):
    return self.conditional_exp.toCode()


# assignment_exp --> unary_exp assignment_op assignment_exp
def _p196(self):
    return self.unary_exp.toCode() + ' ' + self.assignment_op.toCode() + ' ' + self.assignment_exp.toCode()


# assignment_op --> =
def _p197(self):
    return STR('=')


# assignment_op --> *=
def _p198(self):
    return STR('*=')


# assignment_op --> /=
def _p199(self):
    return STR('/=')


# assignment_op --> %=
def _p200(self):
    return STR('%=')


# assignment_op --> +=
def _p201(self):
    return STR('+=')


# assignment_op --> -=
def _p202(self):
    return STR('-=')


# assignment_op --> <<=
def _p203(self):
    return STR('<<=')


# assignment_op --> >>=
def _p204(self):
    return STR('>>=')


# assignment_op --> &=
def _p205(self):
    return STR('&=')


# assignment_op --> ^=
def _p206(self):
    return STR('^=')


# assignment_op --> |=
def _p207(self):
    return STR('|=')


# exp --> assignment_exp
def _p208(self):
    return self.assignment_exp.toCode()


# exp --> exp , assignment_exp
def _p209(self):
    return self.exp.toCode() + STR(', ') + self.assignment_exp.toCode()


# dec --> struct_specifier ;
def _p210(self):
    return I() + self.struct_specifier.toCode() + STR(';') + E()


# dec --> dec_specifier init_dec_list ;
def _p211(self):
    return I() + self.dec_specifier.toCode() + ' ' + self.init_dec_list.toCode() + STR(';') + E()


# dec_specifier --> type_specifier
def _p212(self):
    return self.type_specifier.toCode()


# dec_specifier --> type_qualifier dec_specifier
def _p213(self):
    return self.type_qualifier.toCode() + ' ' + self.dec_specifier.toCode()


# dec_specifier --> storage_class_specifier dec_specifier
def _p214(self):
    return self.storage_class_specifier.toCode() + ' ' + self.dec_specifier.toCode()


# type_specifier --> buildin_type_name
def _p215(self):
    return self.buildin_type_name.toCode()


# type_specifier --> typedef_name
def _p216(self):
    return self.typedef_name.toCode()


# buildin_type_name --> 'void'
def _p217(self):
    return STR('void')


# buildin_type_name --> 'char'
def _p218(self):
    return STR('char')


# buildin_type_name --> 'short'
def _p219(self):
    return STR('short')


# buildin_type_name --> 'int'
def _p220(self):
    return STR('int')


# buildin_type_name --> 'long'
def _p221(self):
    return STR('long')


# buildin_type_name --> 'fixed'
def _p222(self):
    return STR('fixed')


# buildin_type_name --> 'half'
def _p223(self):
    return STR('half')


# buildin_type_name --> 'float'
def _p224(self):
    return STR('float')


# buildin_type_name --> 'double'
def _p225(self):
    return STR('double')


# buildin_type_name --> 'sampler2D'
def _p226(self):
    return STR('sampler2D')


# buildin_type_name --> 'float2'
def _p227(self):
    return STR('float2')


# buildin_type_name --> 'float3'
def _p228(self):
    return STR('float3')


# buildin_type_name --> 'float4'
def _p229(self):
    return STR('float4')


# buildin_type_name --> 'half2'
def _p230(self):
    return STR('half2')


# buildin_type_name --> 'half3'
def _p231(self):
    return STR('half3')


# buildin_type_name --> 'half4'
def _p232(self):
    return STR('half4')


# buildin_type_name --> 'fixed2'
def _p233(self):
    return STR('fixed2')


# buildin_type_name --> 'fixed3'
def _p234(self):
    return STR('fixed3')


# buildin_type_name --> 'fixed4'
def _p235(self):
    return STR('fixed4')


# buildin_type_name --> 'float3x3'
def _p236(self):
    return STR('float3x3')


# type_qualifier --> 'uniform'
def _p237(self):
    return STR('uniform')


# type_qualifier --> 'inline'
def _p238(self):
    return STR('inline')


# type_qualifier --> 'const'
def _p239(self):
    return STR('const')


# storage_class_specifier --> 'static'
def _p240(self):
    return STR('static')


# typedef_name --> ID
def _p241(self):
    return self.ID.toCode()


# struct_specifier --> 'struct' ID
def _p242(self):
    return STR('struct') + ' ' + self.ID.toCode()


# struct_specifier --> 'struct' ID { struct_dec_list }
def _p243(self):
    return STR('struct') + ' ' + self.ID.toCode() + E() \
        + IAA() + STR('{') + E() \
        + self.struct_dec_list.toCode() \
        + SSI() + STR('}')


# struct_dec_list --> struct_dec
def _p244(self):
    return self.struct_dec.toCode()


# struct_dec_list --> struct_dec_list struct_dec
def _p245(self):
    return self.struct_dec_list.toCode() + self.struct_dec.toCode()


# struct_dec --> type_specifier struct_declarator_list ;
def _p246(self):
    return I() + self.type_specifier.toCode() + ' ' + self.struct_declarator_list.toCode() + STR(';') + E()


# struct_dec --> ID ;
def _p247(self):
    return I() + self.ID.toCode() + STR(';') + E()


# struct_dec --> ID ( Number )
def _p248(self):
    return I() + self.ID.toCode() + STR('(') + self.Number.toCode() + STR(')') + E()


# struct_dec --> ID ( Number , Number )
def _p249(self):
    return I() + self.ID.toCode() + STR('(') + self.Number1.toCode() + STR(', ') + self.Number2.toCode() + STR(')') + E()


# struct_dec --> pp_if_stm
def _p250(self):
    return self.pp_if_stm.toCode()


# struct_dec --> 'INTERNAL_DATA'
def _p251(self):
    return I() + STR('INTERNAL_DATA') + E()


# struct_dec --> 'UNITY_VERTEX_INPUT_INSTANCE_ID'
def _p252(self):
    return I() + STR('UNITY_VERTEX_INPUT_INSTANCE_ID') + E()


# struct_dec --> 'UNITY_VERTEX_OUTPUT_STEREO'
def _p253(self):
    return I() + STR('UNITY_VERTEX_OUTPUT_STEREO') + E()


# struct_declarator_list --> struct_declarator
def _p254(self):
    return self.struct_declarator.toCode()


# struct_declarator_list --> struct_declarator_list , struct_declarator
def _p255(self):
    return self.struct_declarator_list.toCode() + STR(', ') + self.struct_declarator.toCode()


# struct_declarator --> declarator
def _p256(self):
    return self.declarator.toCode()


# struct_declarator --> declarator : ID
def _p257(self):
    return self.declarator.toCode() + STR(' : ') + self.ID.toCode()


# declarator --> ID
def _p258(self):
    return self.ID.toCode()


# declarator --> declarator [ exp ]
def _p259(self):
    return self.declarator.toCode() + STR('[') + self.exp.toCode() + STR(']')


# declarator --> declarator ( )
def _p260(self):
    return self.declarator.toCode() + STR('(') + STR(')')


# declarator --> declarator ( parameter_list )
def _p261(self):
    return self.declarator.toCode() + STR('(') + self.parameter_list.toCode() + STR(')')


# parameter_list --> parameter_dec
def _p262(self):
    return self.parameter_dec.toCode()


# parameter_list --> parameter_list , parameter_dec
def _p263(self):
    return self.parameter_list.toCode() + STR(', ') + self.parameter_dec.toCode()


# parameter_dec --> parameter_dec_specifier declarator
def _p264(self):
    return self.parameter_dec_specifier.toCode() + ' ' + self.declarator.toCode()


# parameter_dec --> parameter_dec_specifier declarator : ID
def _p265(self):
    return self.parameter_dec_specifier.toCode() + ' ' + self.declarator.toCode() + STR(' : ') + self.ID.toCode()


# parameter_dec_specifier --> dec_specifier
def _p266(self):
    return self.dec_specifier.toCode()


# parameter_dec_specifier --> 'out' dec_specifier
def _p267(self):
    return STR('out ') + self.dec_specifier.toCode()


# parameter_dec_specifier --> 'inout' dec_specifier
def _p268(self):
    return STR('inout ') + self.dec_specifier.toCode()


# parameter_dec_specifier --> 'triangle' dec_specifier
def _p269(self):
    return STR('triangle ') + self.dec_specifier.toCode()


# parameter_dec_specifier --> 'inout' 'TriangleStream' < ID >
def _p270(self):
    return STR('inout ') + STR('TriangleStream ') + STR('<') + self.ID.toCode() + STR('>')


# init_dec_list --> init_dec
def _p271(self):
    return self.init_dec.toCode()


# init_dec_list --> init_dec_list , init_dec
def _p272(self):
    return self.init_dec_list.toCode() + STR(', ') + self.init_dec.toCode()


# init_dec --> declarator
def _p273(self):
    return self.declarator.toCode()


# init_dec --> declarator = initializer
def _p274(self):
    return self.declarator.toCode() + STR(' = ') + self.initializer.toCode()


# initializer --> assignment_exp
def _p275(self):
    return self.assignment_exp.toCode()


# initializer --> { initializer_list }
def _p276(self):
    return IAA() + STR('{') + E() \
        + self.initializer_list.toCode() \
        + SSI() + STR('}')


# initializer --> { initializer_list , }
def _p277(self):
    return STR('{') + self.initializer_list.toCode() + STR(', ') + STR('}')


# initializer_list --> initializer
def _p278(self):
    return self.initializer.toCode()


# initializer_list --> initializer_list , initializer
def _p279(self):
    return self.initializer_list.toCode() + STR(',') + self.initializer.toCode()


# stm --> exp_stm
def _p280(self):
    return self.exp_stm.toCode()


# stm --> compound_stm
def _p281(self):
    return self.compound_stm.toCode()


# stm --> selection_stm
def _p282(self):
    return self.selection_stm.toCode()


# stm --> iteration_stm
def _p283(self):
    return self.iteration_stm.toCode()


# stm --> jump_stm
def _p284(self):
    return self.jump_stm.toCode()


# stm --> pp_if_stm
def _p285(self):
    return self.pp_if_stm.toCode()


# stm --> 'UNITY_BRANCH'
def _p286(self):
    return I() + STR('UNITY_BRANCH')


# stm --> 'UNITY_UNROLL'
def _p287(self):
    return I() + STR('UNITY_UNROLL')  + E()


# stm --> 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' ( ID )
def _p288(self):
    return I() + STR('TRANSFER_SHADOW_CASTER_NORMALOFFSET') + STR('(') + self.ID.toCode() + STR(')') + E()


# stm --> 'SHADOW_CASTER_FRAGMENT' ( ID )
def _p289(self):
    return I() + STR('SHADOW_CASTER_FRAGMENT') + STR('(') + self.ID.toCode() + STR(')') + E()


# stm --> 'SPEEDTREE_COPY_FRAG' ( ID , ID )
def _p290(self):
    return I() + STR('SPEEDTREE_COPY_FRAG') + STR('(') + self.ID1.toCode() + STR(',') + self.ID2.toCode() + STR(')') + E()


# stm --> 'UNITY_TRANSFER_DITHER_CROSSFADE_HPOS' ( argument_exp_list )
def _p291(self):
    return I() + STR('UNITY_TRANSFER_DITHER_CROSSFADE_HPOS') + STR('(') + self.argument_exp_list.toCode() + STR(')') + E()


# stm --> 'UNITY_APPLY_DITHER_CROSSFADE' ( ID )
def _p292(self):
    return I() + STR('UNITY_APPLY_DITHER_CROSSFADE') + STR('(') + self.ID.toCode() + STR(')') + E()


# exp_stm --> exp ;
def _p293(self):
    return I() + self.exp.toCode() + STR(';') + E()


# exp_stm --> ;
def _p294(self):
    return I() + STR(';') + E()


# compound_stm --> { block_item_list }
def _p295(self):
    return IAA() + STR('{') + E() \
        + self.block_item_list.toCode()  \
        + SSI() + STR('}') + E()


# compound_stm --> { }
def _p296(self):
    return STR(' { ') + STR('}')


# block_item_list --> block_item
def _p297(self):
    return self.block_item.toCode()


# block_item_list --> block_item_list block_item
def _p298(self):
    return self.block_item_list.toCode() + self.block_item.toCode()


# block_item --> dec
def _p299(self):
    return self.dec.toCode()


# block_item --> stm
def _p300(self):
    return self.stm.toCode()


# selection_stm --> 'if' ( exp ) stm
def _p301(self):
    return I() + STR('if') + STR(' (') + self.exp.toCode() + STR(')') + E() \
        + self.stm.toCode()


# selection_stm --> 'if' ( exp ) stm 'else' stm
def _p302(self):
    return I() + STR('if') + STR(' (') + self.exp.toCode() + STR(')') + E() \
        + self.stm1.toCode() + STR('else') + self.stm2.toCode()


# iteration_stm --> 'while' ( exp ) stm
def _p303(self):
    return I() + STR('while') + STR('(') + self.exp.toCode() + STR(')') + E() \
        + self.stm.toCode()


# iteration_stm --> 'do' stm 'while' ( exp ) ;
def _p304(self):
    return I() + STR('do') + E() \
        + self.stm.toCode() \
        + I() + STR('while') + STR('(') + self.exp.toCode() + STR(')') + STR(';') + E()


# iteration_stm --> 'for' ( exp ; exp ; exp ) stm
def _p305(self):
    return I() + STR('for') + STR('(') + self.exp1.toCode() + STR('; ') + self.exp2.toCode() + STR('; ') + self.exp3.toCode() + STR(')') + E() \
        + self.stm.toCode()


# iteration_stm --> 'for' ( dec_specifier init_dec_list ; exp ; exp ) stm
def _p306(self):
    return I() + STR('for') + STR('(') + self.dec_specifier.toCode() + self.init_dec_list.toCode() + STR('; ') + self.exp1.toCode() + STR('; ') + self.exp2.toCode() + STR(')') + E() \
        + self.stm.toCode()


# jump_stm --> 'goto' ID
def _p307(self):
    return I() + STR('goto') + ' ' + self.ID.toCode() + E()


# jump_stm --> 'continue'
def _p308(self):
    return I() + STR('continue') + E()


# jump_stm --> 'break'
def _p309(self):
    return I() + STR('break') + E()


# jump_stm --> 'return' exp ;
def _p310(self):
    return I() + STR('return') + ' ' + self.exp.toCode() + STR(';') + E()


def doInjection(productionList, Token, Nonterminal):
    setattr(Token, 'toCode', formatter.Token2Code)

    for p in productionList:
        if p is None :  # production[0]可能是None
            continue
        levelTwoName = p.left + '_' + p.name
        levelTwoCls = Nonterminal.getClass(levelTwoName)
        localMethond = globals()['_' + p.name]
        setattr(levelTwoCls, 'toCode', localMethond)
