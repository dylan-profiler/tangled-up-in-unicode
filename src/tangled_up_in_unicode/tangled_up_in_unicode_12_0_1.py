from tangled_up_in_unicode.tangle import Tangle


class Unicode12Data:
    from tangled_up_in_unicode.u12_0_1_data import (
        prop_list_to_property,
        blocks_to_block_start,
        blocks_to_block_end,
        property_value_alias_age_short_to_long,
        property_value_alias_bc_short_to_long,
        property_value_alias_blk_long_to_short,
        property_value_alias_ccc_short_to_long,
        property_value_alias_ea_short_to_long,
        property_value_alias_gc_short_to_long,
        property_value_alias_sc_long_to_short,
        scripts_to_script_start,
        scripts_to_script_end,
        east_asian_width_to_east_asian_width_start,
        east_asian_width_to_east_asian_width_end,
        derived_age_to_age_start,
        derived_age_to_age_end,
        unicode_data_to_name_start,
        unicode_data_to_category_start,
        unicode_data_to_category_end,
        unicode_data_to_bidirectional_start,
        unicode_data_to_bidirectional_end,
        unicode_data_to_decimal_start,
        unicode_data_to_digit_start,
        unicode_data_to_numeric_start,
        unicode_data_to_combining_start,
        unicode_data_to_mirrored_start,
        unicode_data_to_mirrored_end,
        unicode_data_to_decomposition_start,
        unicode_data_to_uppercase_start,
        unicode_data_to_lowercase_start,
        unicode_data_to_titlecase_start,
    )


tangle = Tangle(
    version="12.0.1",
    data=Unicode12Data,
)
