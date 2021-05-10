import pytest

from tangled_up_in_unicode import *


@pytest.mark.parametrize(
    "char,expected_value",
    [
        (
            "Ф",
            {
                "name": "CYRILLIC CAPITAL LETTER EF",
                "decimal": -1,
                "digit": -1,
                "numeric": -1,
                "category": "Lu",
                "bidirectional": "L",
                "combining": 0,
                "east_asian_width": "A",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "A",
            {
                "name": "LATIN CAPITAL LETTER A",
                "decimal": -1,
                "digit": -1,
                "numeric": -1,
                "category": "Lu",
                "bidirectional": "L",
                "combining": 0,
                "east_asian_width": "Na",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "$",
            {
                "name": "DOLLAR SIGN",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Sc",
                "bidirectional": "ET",
                "combining": 0,
                "east_asian_width": "Na",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            " ",
            {
                "name": "SPACE",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Zs",
                "bidirectional": "WS",
                "combining": 0,
                "east_asian_width": "Na",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "/",
            {
                "name": "SOLIDUS",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Po",
                "bidirectional": "CS",
                "combining": 0,
                "east_asian_width": "Na",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "9",
            {
                "name": "DIGIT NINE",
                "decimal": 9,
                "digit": 9,
                "numeric": 9.0,
                "category": "Nd",
                "bidirectional": "EN",
                "combining": 0,
                "east_asian_width": "Na",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "a",
            {
                "name": "LATIN SMALL LETTER A",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Ll",
                "bidirectional": "L",
                "combining": 0,
                "east_asian_width": "Na",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "\u0660",
            {
                "name": "ARABIC-INDIC DIGIT ZERO",
                "decimal": 0,
                "digit": 0,
                "numeric": 0.0,
                "category": "Nd",
                "bidirectional": "AN",
                "combining": 0,
                "east_asian_width": "N",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "א",
            {
                "name": "HEBREW LETTER ALEF",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Lo",
                "bidirectional": "R",
                "combining": 0,
                "east_asian_width": "N",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            ")",
            {
                "name": "RIGHT PARENTHESIS",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Pe",
                "bidirectional": "ON",
                "combining": 0,
                "east_asian_width": "Na",
                "mirrored": 1,
                "decomposition": "",
            },
        ),
        (
            "Ĳ",
            {
                "name": "LATIN CAPITAL LIGATURE IJ",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Lu",
                "bidirectional": "L",
                "combining": 0,
                "east_asian_width": "A",
                "mirrored": 0,
                "decomposition": "<compat> 0049 004A",
            },
        ),
        (
            "㐁",
            {
                "name": "CJK UNIFIED IDEOGRAPH-3401",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Lo",
                "bidirectional": "L",
                "combining": 0,
                "east_asian_width": "W",
                "mirrored": 0,
                "decomposition": "",
            },
        ),
        (
            "가",
            {
                "name": "HANGUL SYLLABLE GA",
                "decimal": -1,
                "digit": -1,
                "numeric": -1.0,
                "category": "Lo",
                "bidirectional": "L",
                "combining": 0,
                "east_asian_width": "W",
                "mirrored": 0,
                "decomposition": "4352 4449",
            },
        ),
    ],
)
def test_values(char, expected_value):
    results = {
        "name": name(char),
        "decimal": decimal(char, -1),
        "digit": digit(char, -1),
        "numeric": numeric(char, -1.0),
        "category": category(char),
        "bidirectional": bidirectional(char),
        "combining": combining(char),
        "east_asian_width": east_asian_width(char),
        "mirrored": mirrored(char),
        "decomposition": decomposition(char),
    }
    assert results == expected_value


@pytest.mark.parametrize(
    "char,expected_value",
    [
        (
            "Ф",
            {
                "Category_Long": "Uppercase_Letter",
                "Script_Long": "Cyrillic",
                "Script_Short": "Cyrl",
                "Block_Long": "Cyrillic",
                "Block_Short": "Cyrillic",
                "East_Asian_Width_Long": "Ambiguous",
                "Bidirectional_Long": "Left_To_Right",
                "Binary_Properties": set(),
                "Uppercase": "",
                "Lowercase": "0444",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "A",
            {
                "Category_Long": "Uppercase_Letter",
                "Script_Long": "Latin",
                "Script_Short": "Latn",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Narrow",
                "Bidirectional_Long": "Left_To_Right",
                "Binary_Properties": {"Hex_Digit", "ASCII_Hex_Digit"},
                "Uppercase": "",
                "Lowercase": "0061",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "$",
            {
                "Category_Long": "Currency_Symbol",
                "Script_Long": "Common",
                "Script_Short": "Zyyy",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Narrow",
                "Bidirectional_Long": "European_Terminator",
                "Binary_Properties": {"Pattern_Syntax"},
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            " ",
            {
                "Category_Long": "Space_Separator",
                "Script_Long": "Common",
                "Script_Short": "Zyyy",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Narrow",
                "Bidirectional_Long": "White_Space",
                "Binary_Properties": {"White_Space", "Pattern_White_Space"},
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "\n",
            {
                "Category_Long": "Control",
                "Script_Long": "Common",
                "Script_Short": "Zyyy",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Neutral",
                "Bidirectional_Long": "Paragraph_Separator",
                "Binary_Properties": {"White_Space", "Pattern_White_Space"},
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "/",
            {
                "Category_Long": "Other_Punctuation",
                "Script_Long": "Common",
                "Script_Short": "Zyyy",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Narrow",
                "Bidirectional_Long": "Common_Separator",
                "Binary_Properties": {"Pattern_Syntax"},
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "9",
            {
                "Category_Long": "Decimal_Number",
                "Script_Long": "Common",
                "Script_Short": "Zyyy",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Narrow",
                "Bidirectional_Long": "European_Number",
                "Binary_Properties": {"Hex_Digit", "ASCII_Hex_Digit"},
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "a",
            {
                "Category_Long": "Lowercase_Letter",
                "Script_Long": "Latin",
                "Script_Short": "Latn",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Narrow",
                "Bidirectional_Long": "Left_To_Right",
                "Binary_Properties": {"Hex_Digit", "ASCII_Hex_Digit"},
                "Uppercase": "0041",
                "Lowercase": "",
                "Titlecase": "0041",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "\u0660",
            {
                "Category_Long": "Decimal_Number",
                "Script_Long": "Arabic",
                "Script_Short": "Arab",
                "Block_Long": "Arabic",
                "Block_Short": "Arabic",
                "East_Asian_Width_Long": "Neutral",
                "Bidirectional_Long": "Arabic_Number",
                "Binary_Properties": set(),
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "א",
            {
                "Category_Long": "Other_Letter",
                "Script_Long": "Hebrew",
                "Script_Short": "Hebr",
                "Block_Long": "Hebrew",
                "Block_Short": "Hebrew",
                "East_Asian_Width_Long": "Neutral",
                "Bidirectional_Long": "Right_To_Left",
                "Binary_Properties": set(),
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            ")",
            {
                "Category_Long": "Close_Punctuation",
                "Script_Long": "Common",
                "Script_Short": "Zyyy",
                "Block_Long": "Basic Latin",
                "Block_Short": "ASCII",
                "East_Asian_Width_Long": "Narrow",
                "Bidirectional_Long": "Other_Neutral",
                "Binary_Properties": {"Pattern_Syntax"},
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "Ĳ",
            {
                "Category_Long": "Uppercase_Letter",
                "Script_Long": "Latin",
                "Script_Short": "Latn",
                "Block_Long": "Latin Extended-A",
                "Block_Short": None,
                "East_Asian_Width_Long": "Ambiguous",
                "Bidirectional_Long": "Left_To_Right",
                "Binary_Properties": set(),
                "Uppercase": "",
                "Lowercase": "0133",
                "Titlecase": "",
                "Age_Short": "1.1",
                "Age_Long": "V1_1",
            },
        ),
        (
            "㐁",
            {
                "Category_Long": "Other_Letter",
                "Script_Long": "Han",
                "Script_Short": "Hani",
                "Block_Long": "CJK Unified Ideographs Extension A",
                "Block_Short": "CJK Ext A",
                "East_Asian_Width_Long": "Wide",
                "Bidirectional_Long": "Left_To_Right",
                "Binary_Properties": {"Ideographic", "Unified_Ideograph"},
                "Uppercase": "",
                "Lowercase": "",
                "Titlecase": "",
                "Age_Short": "3.0",
                "Age_Long": "V3_0",
            },
        ),
    ],
)
def test_extended_values(char, expected_value):
    results = {
        "Category_Long": category_long(category(char)),
        "Script_Long": script(char),
        "Script_Short": script_abbr(script(char)),
        "Block_Long": block(char),
        "Block_Short": block_abbr(block(char)),
        "East_Asian_Width_Long": east_asian_width_long(east_asian_width(char)),
        "Bidirectional_Long": bidirectional_long(bidirectional(char)),
        "Binary_Properties": prop_list(char),
        "Uppercase": uppercase(char),
        "Lowercase": lowercase(char),
        "Titlecase": titlecase(char),
        "Age_Short": age(char),
        "Age_Long": age_long(age(char)),
    }

    print(f"(\n\t{repr(char)},\n\t{{")
    for key, value in results.items():
        print(f"\t\t{repr(key)}: {repr(value)},")
    print(f"\t}}")
    print("),")

    assert results == expected_value


@pytest.mark.parametrize("char", ["a"])
def test_return_type_numeric(char):
    with pytest.raises(ValueError, match=r"not a decimal"):
        decimal(char)

    with pytest.raises(ValueError, match=r"not a digit"):
        digit(char)

    with pytest.raises(ValueError, match=r"not a numeric character"):
        numeric(char)


@pytest.mark.parametrize("char", ["\n"])
def test_defaults_name(char):
    with pytest.raises(ValueError, match=r"no such name"):
        name(char)


@pytest.mark.parametrize("char", ["z"])
def test_defaults_decomposition(char):
    assert decomposition(char) == ""


@pytest.mark.parametrize("char", ["a"])
def test_defaults_combining(char):
    assert combining(char) == 0


@pytest.mark.parametrize("char", ["􀉆"])
def test_defaults_script(char):
    assert script(char) == "Unknown"


@pytest.mark.parametrize("char", ["1", "9", "5"])
def test_numeric_types(char):
    results = {
        "decimal": decimal(char, 0),
        "digit": digit(char, 0),
        "numeric": numeric(char),
    }

    assert type(results["decimal"]) == int
    assert type(results["digit"]) == int
    assert type(results["numeric"]) == float


@pytest.mark.parametrize("char", ["A", "a", "!"])
def test_set_types(char):
    results = {"Binary_Properties": prop_list(char)}

    assert type(results["Binary_Properties"]) == set


@pytest.mark.parametrize("char", [120000000])
def test_out_of_range(char):
    with pytest.raises(ValueError, match=r"chr\(\) arg not in range\(0x110000\)"):
        chr(char)


def test_version():
    assert unidata_version == "13.0.0"


@pytest.mark.parametrize(
    "idx,expected_value",
    [
        (32, "SPACE"),
        (97293, "TANGUT IDEOGRAPH-17C0D"),
        (13312, "CJK UNIFIED IDEOGRAPH-3400"),
        (178208, "CJK UNIFIED IDEOGRAPH-2B820"),
        (178209, "CJK UNIFIED IDEOGRAPH-2B821"),
        (4360, "HANGUL CHOSEONG SSANGPIEUP"),
        (48764, "HANGUL SYLLABLE BBAE"),
        (65475, "HALFWIDTH HANGUL LETTER AE"),
    ],
)
def test_name(idx, expected_value):
    assert name(chr(idx)) == expected_value


@pytest.mark.parametrize(
    "idx,expected_value", [(0, "Cc"), (13312, "Lo"), (19894, "Lo")]
)
def test_category(idx, expected_value):
    assert category(chr(idx)) == expected_value


@pytest.mark.parametrize(
    "idx,expected_value",
    [
        (0, "BN"),
        (917994, "NSM"),
        (13312, "L"),
        (13313, "L"),
        (20000, "L"),
        (19893, "L"),
        (19894, "L"),
    ],
)
def test_bidirectional(idx, expected_value):
    assert bidirectional(chr(idx)) == expected_value


def test_decimal():
    assert decimal(chr(0), -1) == -1
    assert decimal(chr(53)) == 5
    assert decimal(chr(1637)) == 5
    assert decimal(chr(1989)) == 5
    assert decimal(chr(2411)) == 5
    assert decimal(chr(2539)) == 5
    assert decimal(chr(13312), -1) == -1
    assert decimal(chr(2), -1) == -1


def test_digit():
    assert digit(chr(0), -1) == -1
    assert digit(chr(53)) == 5
    assert digit(chr(1637)) == 5
    assert digit(chr(1989)) == 5
    assert digit(chr(2411)) == 5
    assert digit(chr(2539)) == 5
    assert digit(chr(13312), -1) == -1
    assert digit(chr(2), -1) == -1


def test_numeric():
    assert numeric(chr(0), -1.0) == -1.0
    assert numeric(chr(53)) == 5.0
    assert numeric(chr(1637)) == 5.0
    assert numeric(chr(1989)) == 5.0
    assert numeric(chr(2411)) == 5.0
    assert numeric(chr(2539)) == 5.0
    assert numeric(chr(13312), -1) == -1
    assert numeric(chr(2), -1) == -1.0


def test_combining():
    assert combining(chr(0)) == 0
    assert combining(chr(2539)) == 0
    assert combining(chr(13312)) == 0
    assert combining(chr(821)) == 1


def test_mirrored():
    assert mirrored(chr(0)) == 0
    assert mirrored(chr(2539)) == 0
    assert mirrored(chr(13312)) == 0
    assert mirrored(chr(10630)) == 1


@pytest.mark.parametrize(
    "idx,expected_value",
    [
        (5, ""),
        (13312, ""),
        (54491, "4369 4465 4534"),
        (44032, "4352 4449"),
        (8450, "<font> 0043"),
        (13071, "<square> 30AC 30F3 30DE"),
    ],
)
def test_decomposition(idx, expected_value):
    assert decomposition(chr(idx)) == expected_value


def test_uppercase():
    assert uppercase(chr(80)) == ""
    assert uppercase(chr(112)) == "0050"  # 80


def test_lowercase():
    assert lowercase(chr(80)) == "0070"  # 112
    assert lowercase(chr(112)) == ""


def test_titlecase():
    assert titlecase(chr(456)) == "01C8"


def test_east_asian_width():
    assert east_asian_width(chr(165)) == "Na"
    assert east_asian_width(chr(20000)) == "W"
    assert east_asian_width(chr(127386)) == "W"


def test_block():
    assert block(chr(0)) == "Basic Latin"
    assert block(chr(80)) == "Basic Latin"
    assert block(chr(20000)) == "CJK Unified Ideographs"
    assert block(chr(13312)) == "CJK Unified Ideographs Extension A"
    assert block(chr(54491)) == "Hangul Syllables"
    assert block(chr(1049158)) == "Supplementary Private Use Area-B"
    assert block(chr(243)) == "Latin-1 Supplement"


def test_block_abbr():
    assert block_abbr(block(chr(1049158))) == "Sup PUA B"
    assert block_abbr(block(chr(243))) == "Latin 1 Sup"


def test_age():
    assert age(chr(0)) == "1.1"
    assert age(chr(8)) == "1.1"
    assert age(chr(20000)) == "1.1"
    assert age(chr(13312)) == "3.0"
    assert age(chr(78610)) == "5.2"
    assert age(chr(13055)) == "12.1"
    assert age(chr(1049158)) == "2.0"


def test_script():
    assert script(chr(0)) == "Common"
    assert script(chr(8)) == "Common"
    assert script(chr(20000)) == "Han"
    assert script(chr(13312)) == "Han"
    assert script(chr(78610)) == "Egyptian_Hieroglyphs"
    assert script(chr(13055)) == "Common"


@pytest.mark.parametrize(
    "idx,expected_value",
    [
        (0, set()),
        (8, set()),
        (33, {"Pattern_Syntax", "Terminal_Punctuation", "Sentence_Terminal"}),
        (20000, {"Unified_Ideograph", "Ideographic"}),
        (13312, {"Unified_Ideograph", "Ideographic"}),
        (78610, set()),
        (13055, set()),
    ],
)
def test_proplist(idx, expected_value):
    assert prop_list(chr(idx)) == expected_value
