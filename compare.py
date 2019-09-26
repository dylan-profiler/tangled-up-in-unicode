import unicodedata

import tangled_up_in_unicode as unicode_data


if __name__ == "__main__":
    basic = [
        {"property": "Name", "standard": unicodedata.name, "new": unicode_data.name},
        {
            "property": "Decimal",
            "standard": lambda x: unicodedata.decimal(x, -1),
            "new": lambda x: unicode_data.decimal(x, -1),
        },
        {
            "property": "Digit",
            "standard": lambda x: unicodedata.digit(x, -1),
            "new": lambda x: unicode_data.digit(x, -1),
        },
        {
            "property": "Numeric",
            "standard": lambda x: unicodedata.numeric(x, -1.0),
            "new": lambda x: unicode_data.numeric(x, -1.0),
        },
        {
            "property": "Category",
            "standard": unicodedata.category,
            "new": unicode_data.category,
        },
        {
            "property": "Bidirectional",
            "standard": unicodedata.bidirectional,
            "new": unicode_data.bidirectional,
        },
        {
            "property": "Combining",
            "standard": unicodedata.combining,
            "new": unicode_data.combining,
        },
        {
            "property": "Mirrored",
            "standard": unicodedata.mirrored,
            "new": unicode_data.mirrored,
        },
        {
            "property": "East Asian Width",
            "standard": unicodedata.east_asian_width,
            "new": unicode_data.east_asian_width,
        },
        {
            "property": "Decomposition",
            "standard": unicodedata.decomposition,
            "new": unicode_data.decomposition,
        },
    ]

    extended = [
        {
            "property": "Category (long)",
            "new": lambda x: unicode_data.category_long(unicode_data.category(x)),
        },
        {"property": "Script (long)", "new": unicode_data.script},
        {
            "property": "Script (short)",
            "new": lambda x: unicode_data.script_abbr(unicode_data.script(x)),
        },
        {"property": "Block (long)", "new": unicode_data.block},
        {
            "property": "Block (short)",
            "new": lambda x: unicode_data.block_abbr(unicode_data.block(x)),
        },
        {
            "property": "East Asian Width (long)",
            "new": lambda x: unicode_data.east_asian_width_long(
                unicode_data.east_asian_width(x)
            ),
        },
        {
            "property": "Bidirectional (long)",
            "new": lambda x: unicode_data.bidirectional_long(
                unicode_data.bidirectional(x)
            ),
        },
        {"property": "Binary Properties", "new": unicode_data.prop_list},
        {"property": "Uppercase character", "new": unicode_data.uppercase},
        {"property": "Lowercase character", "new": unicode_data.lowercase},
        {"property": "Titlecase character", "new": unicode_data.titlecase},
        {"property": "Age (long)", "new": unicode_data.age},
        {
            "property": "Age (short)",
            "new": lambda x: unicode_data.age_long(unicode_data.age(x)),
        },
    ]

    for char in ["Ф", "A", "$", " ", "\n", "/", "9", "a", "\u0660", "א", ")", "Ĳ"]:
        print(
            f"Unicode properties of {repr(char)} (U+{hex(ord(char)).replace('x', '').zfill(4)})"
        )
        print(f"{'Property':>30} {'unicodedata':>30} {'tangled up in unicode':>50}")
        print(f"{'========':>30} {'===========':>30} {'=====================':>50}")
        for row in basic:
            try:
                std = repr(row["standard"](char))
            except ValueError as e:
                std = f"ValueError: {str(e)}"
            try:
                nw = repr(row["new"](char))
            except ValueError as e:
                nw = f"ValueError: {str(e)}"
            print(f"{row['property']:>30} {std:>30} {nw:>50}")

        for row in extended:
            std = "-"
            nw = repr(row["new"](char))
            print(f"{row['property']:>30} {std:>30} {nw:>50}")

        print("")
