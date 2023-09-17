from src.descriptive_stats import get_descriptive_stats


def test_stat_validity():
    '''
    Test that the descriptive statistics are valid.
    '''
    stas_dict = get_descriptive_stats()
    assert int(stas_dict["Weight"]["mean"]) == 398
    assert int(stas_dict["Length"]["mean"]) == 28
    assert int(stas_dict["Height"]["mean"]) == 8
    assert int(stas_dict["Weight"]["std"]) == 357
    assert int(stas_dict["Length"]["std"]) == 10