from .symbol_type import SymbolType
from .syntax_nonterminal import Nonterminal
import unittest


class NonterminalType(SymbolType):

    prog = 'prog'
    shader_body_elms = 'shader_body_elms'
    shader_body_elm = 'shader_body_elm'
    props = 'props'
    props_body = 'props_body'
    prop_stm = 'prop_stm'
    prop_type = 'prop_type'
    prop_init = 'prop_init'
    enum_items = 'enum_items'
    enum_item = 'enum_item'
    category = 'category'
    category_body_elms = 'category_body_elms'
    category_body_elm = 'category_body_elm'
    subshr = 'subshr'
    subshr_body_elms = 'subshr_body_elms'
    subshr_body_elm = 'subshr_body_elm'
    cmd_stm = 'cmd_stm'
    cmd_name = 'cmd_name'
    id_or_number_or_placeholder = 'id_or_number_or_placeholder'
    placeholder = 'placeholder'
    bind_channel_stms = 'bind_channel_stms'
    bind_channel_stm = 'bind_channel_stm'
    meterial_stms = 'meterial_stms'
    meterial_stm = 'meterial_stm'
    stencil_stms = 'stencil_stms'
    stencil_stm = 'stencil_stm'
    set_texture_stms = 'set_texture_stms'
    set_texture_stm = 'set_texture_stm'
    combine_options = 'combine_options'
    combine_option = 'combine_option'
    combine_option_op = 'combine_option_op'
    tags_stms = 'tags_stms'
    tag_smt = 'tag_smt'
    shr_pass = 'shr_pass'
    pass_body_elms = 'pass_body_elms'
    pass_body_elm = 'pass_body_elm'
    cg_prog = 'cg_prog'
    fall_back_cmd = 'fall_back_cmd'
    custom_editor_cmd = 'custom_editor_cmd'
    dependency_cmd = 'dependency_cmd'
    id_list = 'id_list'
    cg_prog_body = 'cg_prog_body'
    cg_stms = 'cg_stms'
    cg_stm = 'cg_stm'
    function_definition = 'function_definition'
    preprocessing_stm = 'preprocessing_stm'
    pp_if_stm = 'pp_if_stm'
    pp_cmd = 'pp_cmd'
    marco_unfold = 'marco_unfold'
    dec_list = 'dec_list'
    primary_exp = 'primary_exp'
    postfix_exp = 'postfix_exp'
    argument_exp_list = 'argument_exp_list'
    unary_exp = 'unary_exp'
    unary_op = 'unary_op'
    cast_exp = 'cast_exp'
    binary_exp = 'binary_exp'
    binary_op = 'binary_op'
    conditional_exp = 'conditional_exp'
    assignment_exp = 'assignment_exp'
    assignment_op = 'assignment_op'
    exp = 'exp'
    dec = 'dec'
    dec_specifier = 'dec_specifier'
    type_specifier = 'type_specifier'
    buildin_type_name = 'buildin_type_name'
    type_qualifier = 'type_qualifier'
    storage_class_specifier = 'storage_class_specifier'
    typedef_name = 'typedef_name'
    struct_specifier = 'struct_specifier'
    struct_dec_list = 'struct_dec_list'
    struct_dec = 'struct_dec'
    struct_declarator_list = 'struct_declarator_list'
    struct_declarator = 'struct_declarator'
    declarator = 'declarator'
    parameter_list = 'parameter_list'
    parameter_dec = 'parameter_dec'
    parameter_dec_specifier = 'parameter_dec_specifier'
    init_dec_list = 'init_dec_list'
    init_dec = 'init_dec'
    initializer = 'initializer'
    initializer_list = 'initializer_list'
    stm = 'stm'
    exp_stm = 'exp_stm'
    compound_stm = 'compound_stm'
    block_item_list = 'block_item_list'
    block_item = 'block_item'
    selection_stm = 'selection_stm'
    iteration_stm = 'iteration_stm'
    jump_stm = 'jump_stm'


class prog(Nonterminal):
    pass


class shader_body_elms(Nonterminal):
    pass


class shader_body_elm(Nonterminal):
    pass


class props(Nonterminal):
    pass


class props_body(Nonterminal):
    pass


class prop_stm(Nonterminal):
    pass


class prop_type(Nonterminal):
    pass


class prop_init(Nonterminal):
    pass


class enum_items(Nonterminal):
    pass


class enum_item(Nonterminal):
    pass


class category(Nonterminal):
    pass


class category_body_elms(Nonterminal):
    pass


class category_body_elm(Nonterminal):
    pass


class subshr(Nonterminal):
    pass


class subshr_body_elms(Nonterminal):
    pass


class subshr_body_elm(Nonterminal):
    pass


class cmd_stm(Nonterminal):
    pass


class cmd_name(Nonterminal):
    pass


class id_or_number_or_placeholder(Nonterminal):
    pass


class placeholder(Nonterminal):
    pass


class bind_channel_stms(Nonterminal):
    pass


class bind_channel_stm(Nonterminal):
    pass


class meterial_stms(Nonterminal):
    pass


class meterial_stm(Nonterminal):
    pass


class stencil_stms(Nonterminal):
    pass


class stencil_stm(Nonterminal):
    pass


class set_texture_stms(Nonterminal):
    pass


class set_texture_stm(Nonterminal):
    pass


class combine_options(Nonterminal):
    pass


class combine_option(Nonterminal):
    pass


class combine_option_op(Nonterminal):
    pass


class tags_stms(Nonterminal):
    pass


class tag_smt(Nonterminal):
    pass


class shr_pass(Nonterminal):
    pass


class pass_body_elms(Nonterminal):
    pass


class pass_body_elm(Nonterminal):
    pass


class cg_prog(Nonterminal):
    pass


class fall_back_cmd(Nonterminal):
    pass


class custom_editor_cmd(Nonterminal):
    pass


class dependency_cmd(Nonterminal):
    pass


class id_list(Nonterminal):
    pass


class cg_prog_body(Nonterminal):
    pass


class cg_stms(Nonterminal):
    pass


class cg_stm(Nonterminal):
    pass


class function_definition(Nonterminal):
    pass


class preprocessing_stm(Nonterminal):
    pass


class pp_if_stm(Nonterminal):
    pass


class pp_cmd(Nonterminal):
    pass


class marco_unfold(Nonterminal):
    pass


class dec_list(Nonterminal):
    pass


class primary_exp(Nonterminal):
    pass


class postfix_exp(Nonterminal):
    pass


class argument_exp_list(Nonterminal):
    pass


class unary_exp(Nonterminal):
    pass


class unary_op(Nonterminal):
    pass


class cast_exp(Nonterminal):
    pass


class binary_exp(Nonterminal):
    pass


class binary_op(Nonterminal):
    pass


class conditional_exp(Nonterminal):
    pass


class assignment_exp(Nonterminal):
    pass


class assignment_op(Nonterminal):
    pass


class exp(Nonterminal):
    pass


class dec(Nonterminal):
    pass


class dec_specifier(Nonterminal):
    pass


class type_specifier(Nonterminal):
    pass


class buildin_type_name(Nonterminal):
    pass


class type_qualifier(Nonterminal):
    pass


class storage_class_specifier(Nonterminal):
    pass


class typedef_name(Nonterminal):
    pass


class struct_specifier(Nonterminal):
    pass


class struct_dec_list(Nonterminal):
    pass


class struct_dec(Nonterminal):
    pass


class struct_declarator_list(Nonterminal):
    pass


class struct_declarator(Nonterminal):
    pass


class declarator(Nonterminal):
    pass


class parameter_list(Nonterminal):
    pass


class parameter_dec(Nonterminal):
    pass


class parameter_dec_specifier(Nonterminal):
    pass


class init_dec_list(Nonterminal):
    pass


class init_dec(Nonterminal):
    pass


class initializer(Nonterminal):
    pass


class initializer_list(Nonterminal):
    pass


class stm(Nonterminal):
    pass


class exp_stm(Nonterminal):
    pass


class compound_stm(Nonterminal):
    pass


class block_item_list(Nonterminal):
    pass


class block_item(Nonterminal):
    pass


class selection_stm(Nonterminal):
    pass


class iteration_stm(Nonterminal):
    pass


class jump_stm(Nonterminal):
    pass


class prog_p1(prog):
    # prog --> 'Shader' String { shader_body_elms }
    def __init__(self, Shader, String, LBrace, shader_body_elms, RBrace):
        self.String = String
        self.shader_body_elms = shader_body_elms


class shader_body_elms_p2(shader_body_elms):
    # shader_body_elms --> shader_body_elm shader_body_elms
    def __init__(self, shader_body_elm, shader_body_elms):
        self.shader_body_elm = shader_body_elm
        self.shader_body_elms = shader_body_elms


class shader_body_elms_p3(shader_body_elms):
    # shader_body_elms -->
    def __init__(self):
        pass


class shader_body_elm_p4(shader_body_elm):
    # shader_body_elm --> props
    def __init__(self, props):
        self.props = props


class shader_body_elm_p5(shader_body_elm):
    # shader_body_elm --> category
    def __init__(self, category):
        self.category = category


class shader_body_elm_p6(shader_body_elm):
    # shader_body_elm --> subshr
    def __init__(self, subshr):
        self.subshr = subshr


class shader_body_elm_p7(shader_body_elm):
    # shader_body_elm --> cg_prog
    def __init__(self, cg_prog):
        self.cg_prog = cg_prog


class shader_body_elm_p8(shader_body_elm):
    # shader_body_elm --> fall_back_cmd
    def __init__(self, fall_back_cmd):
        self.fall_back_cmd = fall_back_cmd


class shader_body_elm_p9(shader_body_elm):
    # shader_body_elm --> custom_editor_cmd
    def __init__(self, custom_editor_cmd):
        self.custom_editor_cmd = custom_editor_cmd


class shader_body_elm_p10(shader_body_elm):
    # shader_body_elm --> dependency_cmd
    def __init__(self, dependency_cmd):
        self.dependency_cmd = dependency_cmd


class props_p11(props):
    # props --> 'Properties' { props_body }
    def __init__(self, Properties, LBrace, props_body, RBrace):
        self.props_body = props_body


class props_body_p12(props_body):
    # props_body --> prop_stm props_body
    def __init__(self, prop_stm, props_body):
        self.prop_stm = prop_stm
        self.props_body = props_body


class props_body_p13(props_body):
    # props_body -->
    def __init__(self):
        pass


class prop_stm_p14(prop_stm):
    # prop_stm --> ID ( String , prop_type ) = prop_init
    def __init__(self, ID, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p15(prop_stm):
    # prop_stm --> [ ID ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, ID1, RBrack, ID2, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID1 = ID1
        self.ID2 = ID2
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p16(prop_stm):
    # prop_stm --> [ ID ] [ ID ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack1, ID1, RBrack1, LBrack2, ID2, RBrack2, ID3, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID1 = ID1
        self.ID2 = ID2
        self.ID3 = ID3
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p17(prop_stm):
    # prop_stm --> [ 'Enum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, Enum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p18(prop_stm):
    # prop_stm --> [ 'MaterialEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, MaterialEnum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p19(prop_stm):
    # prop_stm --> [ 'KeywordEnum' ( enum_items ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, KeywordEnum, LParen1, enum_items, RParen1, RBrack, ID, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.enum_items = enum_items
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p20(prop_stm):
    # prop_stm --> [ 'Toggle' ( ID ) ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, Toggle, LParen1, ID1, RParen1, RBrack, ID2, LParen2, String, Comma, prop_type, RParen2, Assign, prop_init):
        self.ID1 = ID1
        self.ID2 = ID2
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p21(prop_stm):
    # prop_stm --> [ 'MaterialToggle' ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, MaterialToggle, RBrack, ID, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_stm_p22(prop_stm):
    # prop_stm --> [ 'ToggleOff' ] ID ( String , prop_type ) = prop_init
    def __init__(self, LBrack, ToggleOff, RBrack, ID, LParen, String, Comma, prop_type, RParen, Assign, prop_init):
        self.ID = ID
        self.String = String
        self.prop_type = prop_type
        self.prop_init = prop_init


class prop_type_p23(prop_type):
    # prop_type --> 'Color'
    def __init__(self, Color):
        pass


class prop_type_p24(prop_type):
    # prop_type --> 'Vector'
    def __init__(self, Vector):
        pass


class prop_type_p25(prop_type):
    # prop_type --> 'Range'
    def __init__(self, Range):
        pass


class prop_type_p26(prop_type):
    # prop_type --> 'Int'
    def __init__(self, Int):
        pass


class prop_type_p27(prop_type):
    # prop_type --> 'Float'
    def __init__(self, Float):
        pass


class prop_type_p28(prop_type):
    # prop_type --> '2D'
    def __init__(self, _2D):
        pass


class prop_type_p29(prop_type):
    # prop_type --> 'Cube'
    def __init__(self, Cube):
        pass


class prop_type_p30(prop_type):
    # prop_type --> '3D'
    def __init__(self, _3D):
        pass


class prop_type_p31(prop_type):
    # prop_type --> 'Any'
    def __init__(self, Any):
        pass


class prop_type_p32(prop_type):
    # prop_type --> 'Range' ( Number , Number )
    def __init__(self, Range, LParen, Number1, Comma, Number2, RParen):
        self.Number1 = Number1
        self.Number2 = Number2


class prop_init_p33(prop_init):
    # prop_init --> Number
    def __init__(self, Number):
        self.Number = Number


class prop_init_p34(prop_init):
    # prop_init --> String { }
    def __init__(self, String, LBrace, RBrace):
        self.String = String


class prop_init_p35(prop_init):
    # prop_init --> String { ID }
    def __init__(self, String, LBrace, ID, RBrace):
        self.String = String
        self.ID = ID


class prop_init_p36(prop_init):
    # prop_init --> ( Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3


class prop_init_p37(prop_init):
    # prop_init --> ( Number , Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4


class enum_items_p38(enum_items):
    # enum_items --> enum_item
    def __init__(self, enum_item):
        self.enum_item = enum_item


class enum_items_p39(enum_items):
    # enum_items --> enum_item , enum_items
    def __init__(self, enum_item, Comma, enum_items):
        self.enum_item = enum_item
        self.enum_items = enum_items


class enum_item_p40(enum_item):
    # enum_item --> id_list
    def __init__(self, id_list):
        self.id_list = id_list


class enum_item_p41(enum_item):
    # enum_item --> Number
    def __init__(self, Number):
        self.Number = Number


class category_p42(category):
    # category --> 'Category' { category_body_elms }
    def __init__(self, Category, LBrace, category_body_elms, RBrace):
        self.category_body_elms = category_body_elms


class category_body_elms_p43(category_body_elms):
    # category_body_elms --> category_body_elm category_body_elms
    def __init__(self, category_body_elm, category_body_elms):
        self.category_body_elm = category_body_elm
        self.category_body_elms = category_body_elms


class category_body_elms_p44(category_body_elms):
    # category_body_elms -->
    def __init__(self):
        pass


class category_body_elm_p45(category_body_elm):
    # category_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm


class category_body_elm_p46(category_body_elm):
    # category_body_elm --> subshr
    def __init__(self, subshr):
        self.subshr = subshr


class subshr_p47(subshr):
    # subshr --> 'SubShader' { subshr_body_elms }
    def __init__(self, SubShader, LBrace, subshr_body_elms, RBrace):
        self.subshr_body_elms = subshr_body_elms


class subshr_body_elms_p48(subshr_body_elms):
    # subshr_body_elms --> subshr_body_elm subshr_body_elms
    def __init__(self, subshr_body_elm, subshr_body_elms):
        self.subshr_body_elm = subshr_body_elm
        self.subshr_body_elms = subshr_body_elms


class subshr_body_elms_p49(subshr_body_elms):
    # subshr_body_elms -->
    def __init__(self):
        pass


class subshr_body_elm_p50(subshr_body_elm):
    # subshr_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm


class subshr_body_elm_p51(subshr_body_elm):
    # subshr_body_elm --> shr_pass
    def __init__(self, shr_pass):
        self.shr_pass = shr_pass


class subshr_body_elm_p52(subshr_body_elm):
    # subshr_body_elm --> cg_prog
    def __init__(self, cg_prog):
        self.cg_prog = cg_prog


class cmd_stm_p53(cmd_stm):
    # cmd_stm --> cmd_name id_or_number_or_placeholder
    def __init__(self, cmd_name, id_or_number_or_placeholder):
        self.cmd_name = cmd_name
        self.id_or_number_or_placeholder = id_or_number_or_placeholder


class cmd_stm_p54(cmd_stm):
    # cmd_stm --> 'Alphatest' ID
    def __init__(self, Alphatest, ID):
        self.ID = ID


class cmd_stm_p55(cmd_stm):
    # cmd_stm --> 'Alphatest' ID placeholder
    def __init__(self, Alphatest, ID, placeholder):
        self.ID = ID
        self.placeholder = placeholder


class cmd_stm_p56(cmd_stm):
    # cmd_stm --> 'BindChannels' { bind_channel_stms }
    def __init__(self, BindChannels, LBrace, bind_channel_stms, RBrace):
        self.bind_channel_stms = bind_channel_stms


class cmd_stm_p57(cmd_stm):
    # cmd_stm --> 'Blend' ID
    def __init__(self, Blend, ID):
        self.ID = ID


class cmd_stm_p58(cmd_stm):
    # cmd_stm --> 'Blend' id_or_number_or_placeholder id_or_number_or_placeholder
    def __init__(self, Blend, id_or_number_or_placeholder1, id_or_number_or_placeholder2):
        self.id_or_number_or_placeholder1 = id_or_number_or_placeholder1
        self.id_or_number_or_placeholder2 = id_or_number_or_placeholder2


class cmd_stm_p59(cmd_stm):
    # cmd_stm --> 'Fog' { 'Mode' ID }
    def __init__(self, Fog, LBrace, Mode, ID, RBrace):
        self.ID = ID


class cmd_stm_p60(cmd_stm):
    # cmd_stm --> 'Fog' { 'Color' ( Number , Number , Number , Number ) }
    def __init__(self, Fog, LBrace, Color, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen, RBrace):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4


class cmd_stm_p61(cmd_stm):
    # cmd_stm --> 'Material' { meterial_stms }
    def __init__(self, Material, LBrace, meterial_stms, RBrace):
        self.meterial_stms = meterial_stms


class cmd_stm_p62(cmd_stm):
    # cmd_stm --> 'Name' String
    def __init__(self, Name, String):
        self.String = String


class cmd_stm_p63(cmd_stm):
    # cmd_stm --> 'Offset' id_or_number_or_placeholder , id_or_number_or_placeholder
    def __init__(self, Offset, id_or_number_or_placeholder1, Comma, id_or_number_or_placeholder2):
        self.id_or_number_or_placeholder1 = id_or_number_or_placeholder1
        self.id_or_number_or_placeholder2 = id_or_number_or_placeholder2


class cmd_stm_p64(cmd_stm):
    # cmd_stm --> 'Stencil' { stencil_stms }
    def __init__(self, Stencil, LBrace, stencil_stms, RBrace):
        self.stencil_stms = stencil_stms


class cmd_stm_p65(cmd_stm):
    # cmd_stm --> 'SetTexture' placeholder { set_texture_stms }
    def __init__(self, SetTexture, placeholder, LBrace, set_texture_stms, RBrace):
        self.placeholder = placeholder
        self.set_texture_stms = set_texture_stms


class cmd_stm_p66(cmd_stm):
    # cmd_stm --> 'Tags' { tags_stms }
    def __init__(self, Tags, LBrace, tags_stms, RBrace):
        self.tags_stms = tags_stms


class cmd_name_p67(cmd_name):
    # cmd_name --> 'AlphaToMask'
    def __init__(self, AlphaToMask):
        pass


class cmd_name_p68(cmd_name):
    # cmd_name --> 'ColorMask'
    def __init__(self, ColorMask):
        pass


class cmd_name_p69(cmd_name):
    # cmd_name --> 'ColorMaterial'
    def __init__(self, ColorMaterial):
        pass


class cmd_name_p70(cmd_name):
    # cmd_name --> 'Cull'
    def __init__(self, Cull):
        pass


class cmd_name_p71(cmd_name):
    # cmd_name --> 'Lighting'
    def __init__(self, Lighting):
        pass


class cmd_name_p72(cmd_name):
    # cmd_name --> 'LOD'
    def __init__(self, LOD):
        pass


class cmd_name_p73(cmd_name):
    # cmd_name --> 'SeparateSpecular'
    def __init__(self, SeparateSpecular):
        pass


class cmd_name_p74(cmd_name):
    # cmd_name --> 'ZTest'
    def __init__(self, ZTest):
        pass


class cmd_name_p75(cmd_name):
    # cmd_name --> 'ZWrite'
    def __init__(self, ZWrite):
        pass


class id_or_number_or_placeholder_p76(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> ID
    def __init__(self, ID):
        self.ID = ID


class id_or_number_or_placeholder_p77(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> Number
    def __init__(self, Number):
        self.Number = Number


class id_or_number_or_placeholder_p78(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> ( Number , Number , Number , Number )
    def __init__(self, LParen, Number1, Comma1, Number2, Comma2, Number3, Comma3, Number4, RParen):
        self.Number1 = Number1
        self.Number2 = Number2
        self.Number3 = Number3
        self.Number4 = Number4


class id_or_number_or_placeholder_p79(id_or_number_or_placeholder):
    # id_or_number_or_placeholder --> placeholder
    def __init__(self, placeholder):
        self.placeholder = placeholder


class placeholder_p80(placeholder):
    # placeholder --> [ ID ]
    def __init__(self, LBrack, ID, RBrack):
        self.ID = ID


class bind_channel_stms_p81(bind_channel_stms):
    # bind_channel_stms --> bind_channel_stm bind_channel_stms
    def __init__(self, bind_channel_stm, bind_channel_stms):
        self.bind_channel_stm = bind_channel_stm
        self.bind_channel_stms = bind_channel_stms


class bind_channel_stms_p82(bind_channel_stms):
    # bind_channel_stms -->
    def __init__(self):
        pass


class bind_channel_stm_p83(bind_channel_stm):
    # bind_channel_stm --> 'Bind' String , ID
    def __init__(self, Bind, String, Comma, ID):
        self.String = String
        self.ID = ID


class meterial_stms_p84(meterial_stms):
    # meterial_stms --> meterial_stm meterial_stms
    def __init__(self, meterial_stm, meterial_stms):
        self.meterial_stm = meterial_stm
        self.meterial_stms = meterial_stms


class meterial_stms_p85(meterial_stms):
    # meterial_stms -->
    def __init__(self):
        pass


class meterial_stm_p86(meterial_stm):
    # meterial_stm --> ID id_or_number_or_placeholder
    def __init__(self, ID, id_or_number_or_placeholder):
        self.ID = ID
        self.id_or_number_or_placeholder = id_or_number_or_placeholder


class stencil_stms_p87(stencil_stms):
    # stencil_stms --> stencil_stm stencil_stms
    def __init__(self, stencil_stm, stencil_stms):
        self.stencil_stm = stencil_stm
        self.stencil_stms = stencil_stms


class stencil_stms_p88(stencil_stms):
    # stencil_stms -->
    def __init__(self):
        pass


class stencil_stm_p89(stencil_stm):
    # stencil_stm --> ID id_or_number_or_placeholder
    def __init__(self, ID, id_or_number_or_placeholder):
        self.ID = ID
        self.id_or_number_or_placeholder = id_or_number_or_placeholder


class set_texture_stms_p90(set_texture_stms):
    # set_texture_stms --> set_texture_stm set_texture_stms
    def __init__(self, set_texture_stm, set_texture_stms):
        self.set_texture_stm = set_texture_stm
        self.set_texture_stms = set_texture_stms


class set_texture_stms_p91(set_texture_stms):
    # set_texture_stms -->
    def __init__(self):
        pass


class set_texture_stm_p92(set_texture_stm):
    # set_texture_stm --> 'matrix' placeholder
    def __init__(self, matrix, placeholder):
        self.placeholder = placeholder


class set_texture_stm_p93(set_texture_stm):
    # set_texture_stm --> 'constantColor' id_or_number_or_placeholder
    def __init__(self, constantColor, id_or_number_or_placeholder):
        self.id_or_number_or_placeholder = id_or_number_or_placeholder


class set_texture_stm_p94(set_texture_stm):
    # set_texture_stm --> 'combine' combine_options
    def __init__(self, combine, combine_options):
        self.combine_options = combine_options


class combine_options_p95(combine_options):
    # combine_options --> combine_option combine_options
    def __init__(self, combine_option, combine_options):
        self.combine_option = combine_option
        self.combine_options = combine_options


class combine_options_p96(combine_options):
    # combine_options --> combine_option , combine_options
    def __init__(self, combine_option, Comma, combine_options):
        self.combine_option = combine_option
        self.combine_options = combine_options


class combine_options_p97(combine_options):
    # combine_options --> combine_option combine_option_op combine_options
    def __init__(self, combine_option, combine_option_op, combine_options):
        self.combine_option = combine_option
        self.combine_option_op = combine_option_op
        self.combine_options = combine_options


class combine_options_p98(combine_options):
    # combine_options -->
    def __init__(self):
        pass


class combine_option_p99(combine_option):
    # combine_option --> ID
    def __init__(self, ID):
        self.ID = ID


class combine_option_p100(combine_option):
    # combine_option --> ( ID )
    def __init__(self, LParen, ID, RParen):
        self.ID = ID


class combine_option_op_p101(combine_option_op):
    # combine_option_op --> +
    def __init__(self, Plus):
        pass


class combine_option_op_p102(combine_option_op):
    # combine_option_op --> -
    def __init__(self, Minus):
        pass


class combine_option_op_p103(combine_option_op):
    # combine_option_op --> *
    def __init__(self, Times):
        pass


class combine_option_op_p104(combine_option_op):
    # combine_option_op --> /
    def __init__(self, Divide):
        pass


class tags_stms_p105(tags_stms):
    # tags_stms --> tag_smt tags_stms
    def __init__(self, tag_smt, tags_stms):
        self.tag_smt = tag_smt
        self.tags_stms = tags_stms


class tags_stms_p106(tags_stms):
    # tags_stms -->
    def __init__(self):
        pass


class tag_smt_p107(tag_smt):
    # tag_smt --> String = String
    def __init__(self, String1, Assign, String2):
        self.String1 = String1
        self.String2 = String2


class shr_pass_p108(shr_pass):
    # shr_pass --> 'Pass' { pass_body_elms }
    def __init__(self, Pass, LBrace, pass_body_elms, RBrace):
        self.pass_body_elms = pass_body_elms


class shr_pass_p109(shr_pass):
    # shr_pass --> 'GrabPass' { pass_body_elms }
    def __init__(self, GrabPass, LBrace, pass_body_elms, RBrace):
        self.pass_body_elms = pass_body_elms


class shr_pass_p110(shr_pass):
    # shr_pass --> 'UsePass' String
    def __init__(self, UsePass, String):
        self.String = String


class pass_body_elms_p111(pass_body_elms):
    # pass_body_elms --> pass_body_elm pass_body_elms
    def __init__(self, pass_body_elm, pass_body_elms):
        self.pass_body_elm = pass_body_elm
        self.pass_body_elms = pass_body_elms


class pass_body_elms_p112(pass_body_elms):
    # pass_body_elms -->
    def __init__(self):
        pass


class pass_body_elm_p113(pass_body_elm):
    # pass_body_elm --> cmd_stm
    def __init__(self, cmd_stm):
        self.cmd_stm = cmd_stm


class pass_body_elm_p114(pass_body_elm):
    # pass_body_elm --> cg_prog
    def __init__(self, cg_prog):
        self.cg_prog = cg_prog


class cg_prog_p115(cg_prog):
    # cg_prog --> 'CGPROGRAM' cg_prog_body 'ENDCG'
    def __init__(self, CGPROGRAM, cg_prog_body, ENDCG):
        self.cg_prog_body = cg_prog_body


class cg_prog_p116(cg_prog):
    # cg_prog --> 'CGINCLUDE' cg_prog_body 'ENDCG'
    def __init__(self, CGINCLUDE, cg_prog_body, ENDCG):
        self.cg_prog_body = cg_prog_body


class fall_back_cmd_p117(fall_back_cmd):
    # fall_back_cmd --> 'FallBack' String
    def __init__(self, FallBack, String):
        self.String = String


class fall_back_cmd_p118(fall_back_cmd):
    # fall_back_cmd --> 'FallBack' 'Off'
    def __init__(self, FallBack, Off):
        pass


class custom_editor_cmd_p119(custom_editor_cmd):
    # custom_editor_cmd --> 'CustomEditor' String
    def __init__(self, CustomEditor, String):
        self.String = String


class dependency_cmd_p120(dependency_cmd):
    # dependency_cmd --> 'Dependency' String = String
    def __init__(self, Dependency, String1, Assign, String2):
        self.String1 = String1
        self.String2 = String2


class id_list_p121(id_list):
    # id_list --> ID
    def __init__(self, ID):
        self.ID = ID


class id_list_p122(id_list):
    # id_list --> ID id_list
    def __init__(self, ID, id_list):
        self.ID = ID
        self.id_list = id_list


class cg_prog_body_p123(cg_prog_body):
    # cg_prog_body --> cg_stms
    def __init__(self, cg_stms):
        self.cg_stms = cg_stms


class cg_stms_p124(cg_stms):
    # cg_stms --> cg_stm cg_stms
    def __init__(self, cg_stm, cg_stms):
        self.cg_stm = cg_stm
        self.cg_stms = cg_stms


class cg_stms_p125(cg_stms):
    # cg_stms -->
    def __init__(self):
        pass


class cg_stm_p126(cg_stm):
    # cg_stm --> preprocessing_stm
    def __init__(self, preprocessing_stm):
        self.preprocessing_stm = preprocessing_stm


class cg_stm_p127(cg_stm):
    # cg_stm --> function_definition
    def __init__(self, function_definition):
        self.function_definition = function_definition


class cg_stm_p128(cg_stm):
    # cg_stm --> dec
    def __init__(self, dec):
        self.dec = dec


class cg_stm_p129(cg_stm):
    # cg_stm --> 'CBUFFER_START' ( ID ) dec_list 'CBUFFER_END'
    def __init__(self, CBUFFER_START, LParen, ID, RParen, dec_list, CBUFFER_END):
        self.ID = ID
        self.dec_list = dec_list


class function_definition_p130(function_definition):
    # function_definition --> dec_specifier declarator compound_stm
    def __init__(self, dec_specifier, declarator, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm


class function_definition_p131(function_definition):
    # function_definition --> dec_specifier declarator : ID compound_stm
    def __init__(self, dec_specifier, declarator, Colon, ID, compound_stm):
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID = ID
        self.compound_stm = compound_stm


class function_definition_p132(function_definition):
    # function_definition --> [ ID ( Number ) ] dec_specifier declarator compound_stm
    def __init__(self, LBrack, ID, LParen, Number, RParen, RBrack, dec_specifier, declarator, compound_stm):
        self.ID = ID
        self.Number = Number
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.compound_stm = compound_stm


class function_definition_p133(function_definition):
    # function_definition --> [ ID ( Number ) ] dec_specifier declarator : ID compound_stm
    def __init__(self, LBrack, ID1, LParen, Number, RParen, RBrack, dec_specifier, declarator, Colon, ID2, compound_stm):
        self.ID1 = ID1
        self.Number = Number
        self.dec_specifier = dec_specifier
        self.declarator = declarator
        self.ID2 = ID2
        self.compound_stm = compound_stm


class preprocessing_stm_p134(preprocessing_stm):
    # preprocessing_stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class preprocessing_stm_p135(preprocessing_stm):
    # preprocessing_stm --> pp_cmd
    def __init__(self, pp_cmd):
        self.pp_cmd = pp_cmd


class preprocessing_stm_p136(preprocessing_stm):
    # preprocessing_stm --> marco_unfold
    def __init__(self, marco_unfold):
        self.marco_unfold = marco_unfold


class pp_if_stm_p137(pp_if_stm):
    # pp_if_stm --> # 'if' PPTokens
    def __init__(self, Pound, _if, PPTokens):
        self.PPTokens = PPTokens


class pp_if_stm_p138(pp_if_stm):
    # pp_if_stm --> # 'ifdef' ID
    def __init__(self, Pound, ifdef, ID):
        self.ID = ID


class pp_if_stm_p139(pp_if_stm):
    # pp_if_stm --> # 'ifndef' ID
    def __init__(self, Pound, ifndef, ID):
        self.ID = ID


class pp_if_stm_p140(pp_if_stm):
    # pp_if_stm --> # 'elif' PPTokens
    def __init__(self, Pound, _elif, PPTokens):
        self.PPTokens = PPTokens


class pp_if_stm_p141(pp_if_stm):
    # pp_if_stm --> # 'else'
    def __init__(self, Pound, _else):
        pass


class pp_if_stm_p142(pp_if_stm):
    # pp_if_stm --> # 'endif'
    def __init__(self, Pound, endif):
        pass


class pp_cmd_p143(pp_cmd):
    # pp_cmd --> # 'include' String
    def __init__(self, Pound, include, String):
        self.String = String


class pp_cmd_p144(pp_cmd):
    # pp_cmd --> # 'pragma' PPTokens
    def __init__(self, Pound, pragma, PPTokens):
        self.PPTokens = PPTokens


class pp_cmd_p145(pp_cmd):
    # pp_cmd --> # 'define' PPTokens
    def __init__(self, Pound, define, PPTokens):
        self.PPTokens = PPTokens


class marco_unfold_p146(marco_unfold):
    # marco_unfold --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp


class dec_list_p147(dec_list):
    # dec_list --> dec
    def __init__(self, dec):
        self.dec = dec


class dec_list_p148(dec_list):
    # dec_list --> dec_list dec
    def __init__(self, dec_list, dec):
        self.dec_list = dec_list
        self.dec = dec


class primary_exp_p149(primary_exp):
    # primary_exp --> ID
    def __init__(self, ID):
        self.ID = ID


class primary_exp_p150(primary_exp):
    # primary_exp --> String
    def __init__(self, String):
        self.String = String


class primary_exp_p151(primary_exp):
    # primary_exp --> Number
    def __init__(self, Number):
        self.Number = Number


class primary_exp_p152(primary_exp):
    # primary_exp --> ( exp )
    def __init__(self, LParen, exp, RParen):
        self.exp = exp


class postfix_exp_p153(postfix_exp):
    # postfix_exp --> primary_exp
    def __init__(self, primary_exp):
        self.primary_exp = primary_exp


class postfix_exp_p154(postfix_exp):
    # postfix_exp --> postfix_exp [ exp ]
    def __init__(self, postfix_exp, LBrack, exp, RBrack):
        self.postfix_exp = postfix_exp
        self.exp = exp


class postfix_exp_p155(postfix_exp):
    # postfix_exp --> postfix_exp ( )
    def __init__(self, postfix_exp, LParen, RParen):
        self.postfix_exp = postfix_exp


class postfix_exp_p156(postfix_exp):
    # postfix_exp --> postfix_exp ( argument_exp_list )
    def __init__(self, postfix_exp, LParen, argument_exp_list, RParen):
        self.postfix_exp = postfix_exp
        self.argument_exp_list = argument_exp_list


class postfix_exp_p157(postfix_exp):
    # postfix_exp --> buildin_type_name ( argument_exp_list )
    def __init__(self, buildin_type_name, LParen, argument_exp_list, RParen):
        self.buildin_type_name = buildin_type_name
        self.argument_exp_list = argument_exp_list


class postfix_exp_p158(postfix_exp):
    # postfix_exp --> postfix_exp . ID
    def __init__(self, postfix_exp, Dot, ID):
        self.postfix_exp = postfix_exp
        self.ID = ID


class postfix_exp_p159(postfix_exp):
    # postfix_exp --> postfix_exp ++
    def __init__(self, postfix_exp, Increment):
        self.postfix_exp = postfix_exp


class postfix_exp_p160(postfix_exp):
    # postfix_exp --> postfix_exp --
    def __init__(self, postfix_exp, Decrement):
        self.postfix_exp = postfix_exp


class argument_exp_list_p161(argument_exp_list):
    # argument_exp_list --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class argument_exp_list_p162(argument_exp_list):
    # argument_exp_list --> argument_exp_list , assignment_exp
    def __init__(self, argument_exp_list, Comma, assignment_exp):
        self.argument_exp_list = argument_exp_list
        self.assignment_exp = assignment_exp


class unary_exp_p163(unary_exp):
    # unary_exp --> postfix_exp
    def __init__(self, postfix_exp):
        self.postfix_exp = postfix_exp


class unary_exp_p164(unary_exp):
    # unary_exp --> ++ unary_exp
    def __init__(self, Increment, unary_exp):
        self.unary_exp = unary_exp


class unary_exp_p165(unary_exp):
    # unary_exp --> -- unary_exp
    def __init__(self, Decrement, unary_exp):
        self.unary_exp = unary_exp


class unary_exp_p166(unary_exp):
    # unary_exp --> unary_op unary_exp
    def __init__(self, unary_op, unary_exp):
        self.unary_op = unary_op
        self.unary_exp = unary_exp


class unary_op_p167(unary_op):
    # unary_op --> +
    def __init__(self, Plus):
        pass


class unary_op_p168(unary_op):
    # unary_op --> -
    def __init__(self, Minus):
        pass


class unary_op_p169(unary_op):
    # unary_op --> !
    def __init__(self, NOT):
        pass


class unary_op_p170(unary_op):
    # unary_op --> ~
    def __init__(self, Tilde):
        pass


class cast_exp_p171(cast_exp):
    # cast_exp --> unary_exp
    def __init__(self, unary_exp):
        self.unary_exp = unary_exp


class cast_exp_p172(cast_exp):
    # cast_exp --> ( buildin_type_name ) cast_exp
    def __init__(self, LParen, buildin_type_name, RParen, cast_exp):
        self.buildin_type_name = buildin_type_name
        self.cast_exp = cast_exp


class binary_exp_p173(binary_exp):
    # binary_exp --> cast_exp
    def __init__(self, cast_exp):
        self.cast_exp = cast_exp


class binary_exp_p174(binary_exp):
    # binary_exp --> binary_exp binary_op unary_exp
    def __init__(self, binary_exp, binary_op, unary_exp):
        self.binary_exp = binary_exp
        self.binary_op = binary_op
        self.unary_exp = unary_exp


class binary_op_p175(binary_op):
    # binary_op --> *
    def __init__(self, Times):
        pass


class binary_op_p176(binary_op):
    # binary_op --> /
    def __init__(self, Divide):
        pass


class binary_op_p177(binary_op):
    # binary_op --> %
    def __init__(self, Percent):
        pass


class binary_op_p178(binary_op):
    # binary_op --> +
    def __init__(self, Plus):
        pass


class binary_op_p179(binary_op):
    # binary_op --> -
    def __init__(self, Minus):
        pass


class binary_op_p180(binary_op):
    # binary_op --> <<
    def __init__(self, LeftShift):
        pass


class binary_op_p181(binary_op):
    # binary_op --> >>
    def __init__(self, RightShift):
        pass


class binary_op_p182(binary_op):
    # binary_op --> <
    def __init__(self, LT):
        pass


class binary_op_p183(binary_op):
    # binary_op --> >
    def __init__(self, GT):
        pass


class binary_op_p184(binary_op):
    # binary_op --> <=
    def __init__(self, LE):
        pass


class binary_op_p185(binary_op):
    # binary_op --> >=
    def __init__(self, GE):
        pass


class binary_op_p186(binary_op):
    # binary_op --> ==
    def __init__(self, EQ):
        pass


class binary_op_p187(binary_op):
    # binary_op --> !=
    def __init__(self, NEQ):
        pass


class binary_op_p188(binary_op):
    # binary_op --> &
    def __init__(self, Ampersand):
        pass


class binary_op_p189(binary_op):
    # binary_op --> ^
    def __init__(self, Caret):
        pass


class binary_op_p190(binary_op):
    # binary_op --> |
    def __init__(self, VerticalBar):
        pass


class binary_op_p191(binary_op):
    # binary_op --> &&
    def __init__(self, AND):
        pass


class binary_op_p192(binary_op):
    # binary_op --> ||
    def __init__(self, OR):
        pass


class conditional_exp_p193(conditional_exp):
    # conditional_exp --> binary_exp
    def __init__(self, binary_exp):
        self.binary_exp = binary_exp


class conditional_exp_p194(conditional_exp):
    # conditional_exp --> binary_exp ? exp : conditional_exp
    def __init__(self, binary_exp, Question, exp, Colon, conditional_exp):
        self.binary_exp = binary_exp
        self.exp = exp
        self.conditional_exp = conditional_exp


class assignment_exp_p195(assignment_exp):
    # assignment_exp --> conditional_exp
    def __init__(self, conditional_exp):
        self.conditional_exp = conditional_exp


class assignment_exp_p196(assignment_exp):
    # assignment_exp --> unary_exp assignment_op assignment_exp
    def __init__(self, unary_exp, assignment_op, assignment_exp):
        self.unary_exp = unary_exp
        self.assignment_op = assignment_op
        self.assignment_exp = assignment_exp


class assignment_op_p197(assignment_op):
    # assignment_op --> =
    def __init__(self, Assign):
        pass


class assignment_op_p198(assignment_op):
    # assignment_op --> *=
    def __init__(self, AddAssign):
        pass


class assignment_op_p199(assignment_op):
    # assignment_op --> /=
    def __init__(self, SubAssign):
        pass


class assignment_op_p200(assignment_op):
    # assignment_op --> %=
    def __init__(self, MulAssign):
        pass


class assignment_op_p201(assignment_op):
    # assignment_op --> +=
    def __init__(self, DivAssign):
        pass


class assignment_op_p202(assignment_op):
    # assignment_op --> -=
    def __init__(self, ModAssign):
        pass


class assignment_op_p203(assignment_op):
    # assignment_op --> <<=
    def __init__(self, LeftShiftAssign):
        pass


class assignment_op_p204(assignment_op):
    # assignment_op --> >>=
    def __init__(self, RightShiftAssign):
        pass


class assignment_op_p205(assignment_op):
    # assignment_op --> &=
    def __init__(self, AndAssign):
        pass


class assignment_op_p206(assignment_op):
    # assignment_op --> ^=
    def __init__(self, XorAssign):
        pass


class assignment_op_p207(assignment_op):
    # assignment_op --> |=
    def __init__(self, OrAssign):
        pass


class exp_p208(exp):
    # exp --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class exp_p209(exp):
    # exp --> exp , assignment_exp
    def __init__(self, exp, Comma, assignment_exp):
        self.exp = exp
        self.assignment_exp = assignment_exp


class dec_p210(dec):
    # dec --> struct_specifier ;
    def __init__(self, struct_specifier, Semicolon):
        self.struct_specifier = struct_specifier


class dec_p211(dec):
    # dec --> dec_specifier init_dec_list ;
    def __init__(self, dec_specifier, init_dec_list, Semicolon):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list


class dec_specifier_p212(dec_specifier):
    # dec_specifier --> type_specifier
    def __init__(self, type_specifier):
        self.type_specifier = type_specifier


class dec_specifier_p213(dec_specifier):
    # dec_specifier --> type_qualifier dec_specifier
    def __init__(self, type_qualifier, dec_specifier):
        self.type_qualifier = type_qualifier
        self.dec_specifier = dec_specifier


class dec_specifier_p214(dec_specifier):
    # dec_specifier --> storage_class_specifier dec_specifier
    def __init__(self, storage_class_specifier, dec_specifier):
        self.storage_class_specifier = storage_class_specifier
        self.dec_specifier = dec_specifier


class type_specifier_p215(type_specifier):
    # type_specifier --> buildin_type_name
    def __init__(self, buildin_type_name):
        self.buildin_type_name = buildin_type_name


class type_specifier_p216(type_specifier):
    # type_specifier --> typedef_name
    def __init__(self, typedef_name):
        self.typedef_name = typedef_name


class buildin_type_name_p217(buildin_type_name):
    # buildin_type_name --> 'void'
    def __init__(self, void):
        pass


class buildin_type_name_p218(buildin_type_name):
    # buildin_type_name --> 'char'
    def __init__(self, char):
        pass


class buildin_type_name_p219(buildin_type_name):
    # buildin_type_name --> 'short'
    def __init__(self, short):
        pass


class buildin_type_name_p220(buildin_type_name):
    # buildin_type_name --> 'int'
    def __init__(self, int):
        pass


class buildin_type_name_p221(buildin_type_name):
    # buildin_type_name --> 'long'
    def __init__(self, long):
        pass


class buildin_type_name_p222(buildin_type_name):
    # buildin_type_name --> 'fixed'
    def __init__(self, fixed):
        pass


class buildin_type_name_p223(buildin_type_name):
    # buildin_type_name --> 'half'
    def __init__(self, half):
        pass


class buildin_type_name_p224(buildin_type_name):
    # buildin_type_name --> 'float'
    def __init__(self, float):
        pass


class buildin_type_name_p225(buildin_type_name):
    # buildin_type_name --> 'double'
    def __init__(self, double):
        pass


class buildin_type_name_p226(buildin_type_name):
    # buildin_type_name --> 'sampler2D'
    def __init__(self, sampler2D):
        pass


class buildin_type_name_p227(buildin_type_name):
    # buildin_type_name --> 'float2'
    def __init__(self, float2):
        pass


class buildin_type_name_p228(buildin_type_name):
    # buildin_type_name --> 'float3'
    def __init__(self, float3):
        pass


class buildin_type_name_p229(buildin_type_name):
    # buildin_type_name --> 'float4'
    def __init__(self, float4):
        pass


class buildin_type_name_p230(buildin_type_name):
    # buildin_type_name --> 'half2'
    def __init__(self, half2):
        pass


class buildin_type_name_p231(buildin_type_name):
    # buildin_type_name --> 'half3'
    def __init__(self, half3):
        pass


class buildin_type_name_p232(buildin_type_name):
    # buildin_type_name --> 'half4'
    def __init__(self, half4):
        pass


class buildin_type_name_p233(buildin_type_name):
    # buildin_type_name --> 'fixed2'
    def __init__(self, fixed2):
        pass


class buildin_type_name_p234(buildin_type_name):
    # buildin_type_name --> 'fixed3'
    def __init__(self, fixed3):
        pass


class buildin_type_name_p235(buildin_type_name):
    # buildin_type_name --> 'fixed4'
    def __init__(self, fixed4):
        pass


class buildin_type_name_p236(buildin_type_name):
    # buildin_type_name --> 'float3x3'
    def __init__(self, float3x3):
        pass


class type_qualifier_p237(type_qualifier):
    # type_qualifier --> 'uniform'
    def __init__(self, uniform):
        pass


class type_qualifier_p238(type_qualifier):
    # type_qualifier --> 'inline'
    def __init__(self, inline):
        pass


class type_qualifier_p239(type_qualifier):
    # type_qualifier --> 'const'
    def __init__(self, const):
        pass


class storage_class_specifier_p240(storage_class_specifier):
    # storage_class_specifier --> 'static'
    def __init__(self, static):
        pass


class typedef_name_p241(typedef_name):
    # typedef_name --> ID
    def __init__(self, ID):
        self.ID = ID


class struct_specifier_p242(struct_specifier):
    # struct_specifier --> 'struct' ID
    def __init__(self, struct, ID):
        self.ID = ID


class struct_specifier_p243(struct_specifier):
    # struct_specifier --> 'struct' ID { struct_dec_list }
    def __init__(self, struct, ID, LBrace, struct_dec_list, RBrace):
        self.ID = ID
        self.struct_dec_list = struct_dec_list


class struct_dec_list_p244(struct_dec_list):
    # struct_dec_list --> struct_dec
    def __init__(self, struct_dec):
        self.struct_dec = struct_dec


class struct_dec_list_p245(struct_dec_list):
    # struct_dec_list --> struct_dec_list struct_dec
    def __init__(self, struct_dec_list, struct_dec):
        self.struct_dec_list = struct_dec_list
        self.struct_dec = struct_dec


class struct_dec_p246(struct_dec):
    # struct_dec --> type_specifier struct_declarator_list ;
    def __init__(self, type_specifier, struct_declarator_list, Semicolon):
        self.type_specifier = type_specifier
        self.struct_declarator_list = struct_declarator_list


class struct_dec_p247(struct_dec):
    # struct_dec --> ID ;
    def __init__(self, ID, Semicolon):
        self.ID = ID


class struct_dec_p248(struct_dec):
    # struct_dec --> ID ( Number )
    def __init__(self, ID, LParen, Number, RParen):
        self.ID = ID
        self.Number = Number


class struct_dec_p249(struct_dec):
    # struct_dec --> ID ( Number , Number )
    def __init__(self, ID, LParen, Number1, Comma, Number2, RParen):
        self.ID = ID
        self.Number1 = Number1
        self.Number2 = Number2


class struct_dec_p250(struct_dec):
    # struct_dec --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class struct_dec_p251(struct_dec):
    # struct_dec --> 'INTERNAL_DATA'
    def __init__(self, INTERNAL_DATA):
        pass


class struct_dec_p252(struct_dec):
    # struct_dec --> 'UNITY_VERTEX_INPUT_INSTANCE_ID'
    def __init__(self, UNITY_VERTEX_INPUT_INSTANCE_ID):
        pass


class struct_dec_p253(struct_dec):
    # struct_dec --> 'UNITY_VERTEX_OUTPUT_STEREO'
    def __init__(self, UNITY_VERTEX_OUTPUT_STEREO):
        pass


class struct_declarator_list_p254(struct_declarator_list):
    # struct_declarator_list --> struct_declarator
    def __init__(self, struct_declarator):
        self.struct_declarator = struct_declarator


class struct_declarator_list_p255(struct_declarator_list):
    # struct_declarator_list --> struct_declarator_list , struct_declarator
    def __init__(self, struct_declarator_list, Comma, struct_declarator):
        self.struct_declarator_list = struct_declarator_list
        self.struct_declarator = struct_declarator


class struct_declarator_p256(struct_declarator):
    # struct_declarator --> declarator
    def __init__(self, declarator):
        self.declarator = declarator


class struct_declarator_p257(struct_declarator):
    # struct_declarator --> declarator : ID
    def __init__(self, declarator, Colon, ID):
        self.declarator = declarator
        self.ID = ID


class declarator_p258(declarator):
    # declarator --> ID
    def __init__(self, ID):
        self.ID = ID


class declarator_p259(declarator):
    # declarator --> declarator [ exp ]
    def __init__(self, declarator, LBrack, exp, RBrack):
        self.declarator = declarator
        self.exp = exp


class declarator_p260(declarator):
    # declarator --> declarator ( )
    def __init__(self, declarator, LParen, RParen):
        self.declarator = declarator


class declarator_p261(declarator):
    # declarator --> declarator ( parameter_list )
    def __init__(self, declarator, LParen, parameter_list, RParen):
        self.declarator = declarator
        self.parameter_list = parameter_list


class parameter_list_p262(parameter_list):
    # parameter_list --> parameter_dec
    def __init__(self, parameter_dec):
        self.parameter_dec = parameter_dec


class parameter_list_p263(parameter_list):
    # parameter_list --> parameter_list , parameter_dec
    def __init__(self, parameter_list, Comma, parameter_dec):
        self.parameter_list = parameter_list
        self.parameter_dec = parameter_dec


class parameter_dec_p264(parameter_dec):
    # parameter_dec --> parameter_dec_specifier declarator
    def __init__(self, parameter_dec_specifier, declarator):
        self.parameter_dec_specifier = parameter_dec_specifier
        self.declarator = declarator


class parameter_dec_p265(parameter_dec):
    # parameter_dec --> parameter_dec_specifier declarator : ID
    def __init__(self, parameter_dec_specifier, declarator, Colon, ID):
        self.parameter_dec_specifier = parameter_dec_specifier
        self.declarator = declarator
        self.ID = ID


class parameter_dec_specifier_p266(parameter_dec_specifier):
    # parameter_dec_specifier --> dec_specifier
    def __init__(self, dec_specifier):
        self.dec_specifier = dec_specifier


class parameter_dec_specifier_p267(parameter_dec_specifier):
    # parameter_dec_specifier --> 'out' dec_specifier
    def __init__(self, out, dec_specifier):
        self.dec_specifier = dec_specifier


class parameter_dec_specifier_p268(parameter_dec_specifier):
    # parameter_dec_specifier --> 'inout' dec_specifier
    def __init__(self, inout, dec_specifier):
        self.dec_specifier = dec_specifier


class parameter_dec_specifier_p269(parameter_dec_specifier):
    # parameter_dec_specifier --> 'triangle' dec_specifier
    def __init__(self, triangle, dec_specifier):
        self.dec_specifier = dec_specifier


class parameter_dec_specifier_p270(parameter_dec_specifier):
    # parameter_dec_specifier --> 'inout' 'TriangleStream' < ID >
    def __init__(self, inout, TriangleStream, LT, ID, GT):
        self.ID = ID


class init_dec_list_p271(init_dec_list):
    # init_dec_list --> init_dec
    def __init__(self, init_dec):
        self.init_dec = init_dec


class init_dec_list_p272(init_dec_list):
    # init_dec_list --> init_dec_list , init_dec
    def __init__(self, init_dec_list, Comma, init_dec):
        self.init_dec_list = init_dec_list
        self.init_dec = init_dec


class init_dec_p273(init_dec):
    # init_dec --> declarator
    def __init__(self, declarator):
        self.declarator = declarator


class init_dec_p274(init_dec):
    # init_dec --> declarator = initializer
    def __init__(self, declarator, Assign, initializer):
        self.declarator = declarator
        self.initializer = initializer


class initializer_p275(initializer):
    # initializer --> assignment_exp
    def __init__(self, assignment_exp):
        self.assignment_exp = assignment_exp


class initializer_p276(initializer):
    # initializer --> { initializer_list }
    def __init__(self, LBrace, initializer_list, RBrace):
        self.initializer_list = initializer_list


class initializer_p277(initializer):
    # initializer --> { initializer_list , }
    def __init__(self, LBrace, initializer_list, Comma, RBrace):
        self.initializer_list = initializer_list


class initializer_list_p278(initializer_list):
    # initializer_list --> initializer
    def __init__(self, initializer):
        self.initializer = initializer


class initializer_list_p279(initializer_list):
    # initializer_list --> initializer_list , initializer
    def __init__(self, initializer_list, Comma, initializer):
        self.initializer_list = initializer_list
        self.initializer = initializer


class stm_p280(stm):
    # stm --> exp_stm
    def __init__(self, exp_stm):
        self.exp_stm = exp_stm


class stm_p281(stm):
    # stm --> compound_stm
    def __init__(self, compound_stm):
        self.compound_stm = compound_stm


class stm_p282(stm):
    # stm --> selection_stm
    def __init__(self, selection_stm):
        self.selection_stm = selection_stm


class stm_p283(stm):
    # stm --> iteration_stm
    def __init__(self, iteration_stm):
        self.iteration_stm = iteration_stm


class stm_p284(stm):
    # stm --> jump_stm
    def __init__(self, jump_stm):
        self.jump_stm = jump_stm


class stm_p285(stm):
    # stm --> pp_if_stm
    def __init__(self, pp_if_stm):
        self.pp_if_stm = pp_if_stm


class stm_p286(stm):
    # stm --> 'UNITY_BRANCH'
    def __init__(self, UNITY_BRANCH):
        pass


class stm_p287(stm):
    # stm --> 'UNITY_UNROLL'
    def __init__(self, UNITY_UNROLL):
        pass


class stm_p288(stm):
    # stm --> 'TRANSFER_SHADOW_CASTER_NORMALOFFSET' ( ID )
    def __init__(self, TRANSFER_SHADOW_CASTER_NORMALOFFSET, LParen, ID, RParen):
        self.ID = ID


class stm_p289(stm):
    # stm --> 'SHADOW_CASTER_FRAGMENT' ( ID )
    def __init__(self, SHADOW_CASTER_FRAGMENT, LParen, ID, RParen):
        self.ID = ID


class stm_p290(stm):
    # stm --> 'SPEEDTREE_COPY_FRAG' ( ID , ID )
    def __init__(self, SPEEDTREE_COPY_FRAG, LParen, ID1, Comma, ID2, RParen):
        self.ID1 = ID1
        self.ID2 = ID2


class stm_p291(stm):
    # stm --> 'UNITY_TRANSFER_DITHER_CROSSFADE_HPOS' ( argument_exp_list )
    def __init__(self, UNITY_TRANSFER_DITHER_CROSSFADE_HPOS, LParen, argument_exp_list, RParen):
        self.argument_exp_list = argument_exp_list


class stm_p292(stm):
    # stm --> 'UNITY_APPLY_DITHER_CROSSFADE' ( ID )
    def __init__(self, UNITY_APPLY_DITHER_CROSSFADE, LParen, ID, RParen):
        self.ID = ID


class exp_stm_p293(exp_stm):
    # exp_stm --> exp ;
    def __init__(self, exp, Semicolon):
        self.exp = exp


class exp_stm_p294(exp_stm):
    # exp_stm --> ;
    def __init__(self, Semicolon):
        pass


class compound_stm_p295(compound_stm):
    # compound_stm --> { block_item_list }
    def __init__(self, LBrace, block_item_list, RBrace):
        self.block_item_list = block_item_list


class compound_stm_p296(compound_stm):
    # compound_stm --> { }
    def __init__(self, LBrace, RBrace):
        pass


class block_item_list_p297(block_item_list):
    # block_item_list --> block_item
    def __init__(self, block_item):
        self.block_item = block_item


class block_item_list_p298(block_item_list):
    # block_item_list --> block_item_list block_item
    def __init__(self, block_item_list, block_item):
        self.block_item_list = block_item_list
        self.block_item = block_item


class block_item_p299(block_item):
    # block_item --> dec
    def __init__(self, dec):
        self.dec = dec


class block_item_p300(block_item):
    # block_item --> stm
    def __init__(self, stm):
        self.stm = stm


class selection_stm_p301(selection_stm):
    # selection_stm --> 'if' ( exp ) stm
    def __init__(self, _if, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class selection_stm_p302(selection_stm):
    # selection_stm --> 'if' ( exp ) stm 'else' stm
    def __init__(self, _if, LParen, exp, RParen, stm1, _else, stm2):
        self.exp = exp
        self.stm1 = stm1
        self.stm2 = stm2


class iteration_stm_p303(iteration_stm):
    # iteration_stm --> 'while' ( exp ) stm
    def __init__(self, _while, LParen, exp, RParen, stm):
        self.exp = exp
        self.stm = stm


class iteration_stm_p304(iteration_stm):
    # iteration_stm --> 'do' stm 'while' ( exp ) ;
    def __init__(self, do, stm, _while, LParen, exp, RParen, Semicolon):
        self.stm = stm
        self.exp = exp


class iteration_stm_p305(iteration_stm):
    # iteration_stm --> 'for' ( exp ; exp ; exp ) stm
    def __init__(self, _for, LParen, exp1, Semicolon1, exp2, Semicolon2, exp3, RParen, stm):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.stm = stm


class iteration_stm_p306(iteration_stm):
    # iteration_stm --> 'for' ( dec_specifier init_dec_list ; exp ; exp ) stm
    def __init__(self, _for, LParen, dec_specifier, init_dec_list, Semicolon1, exp1, Semicolon2, exp2, RParen, stm):
        self.dec_specifier = dec_specifier
        self.init_dec_list = init_dec_list
        self.exp1 = exp1
        self.exp2 = exp2
        self.stm = stm


class jump_stm_p307(jump_stm):
    # jump_stm --> 'goto' ID
    def __init__(self, goto, ID):
        self.ID = ID


class jump_stm_p308(jump_stm):
    # jump_stm --> 'continue'
    def __init__(self, _continue):
        pass


class jump_stm_p309(jump_stm):
    # jump_stm --> 'break'
    def __init__(self, _break):
        pass


class jump_stm_p310(jump_stm):
    # jump_stm --> 'return' exp ;
    def __init__(self, _return, exp, Semicolon):
        self.exp = exp


class Test(unittest.TestCase):


    def test(self):
        pass
