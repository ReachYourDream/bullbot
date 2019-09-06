def test_clean_up():
    from pajbot.utils import clean_up_message

    assert "󠀀" == "\U000e0000"

    assert "" == clean_up_message("")
    assert "" == clean_up_message("  ")
    assert "" == clean_up_message(" ")

    assert ". .timeout pajlada 5" == clean_up_message(".timeout pajlada 5")
    assert ". /timeout pajlada 5" == clean_up_message("/timeout pajlada 5")
    assert ". .timeout pajlada 5" == clean_up_message("   .timeout pajlada 5")
    assert ". /timeout pajlada 5" == clean_up_message(" /timeout pajlada 5")
    assert ".me xD" == clean_up_message(".me xD")
    assert "/me xD" == clean_up_message("/me xD")
    assert "/me xD" == clean_up_message("   /me xD")
    assert ".me xD" == clean_up_message("   .me xD")
    assert "asd" == clean_up_message("asd")
    assert "asd" == clean_up_message("    asd")
    for prefix in ["!", "$", "-", "<"]:
        assert "\U000e0000{}ping".format(prefix) == clean_up_message("{}ping".format(prefix))
        assert "/me \U000e0000{}ping".format(prefix) == clean_up_message("/me {}ping".format(prefix))
        assert ".me \U000e0000{}ping".format(prefix) == clean_up_message(".me {}ping".format(prefix))
        assert "\U000e0000{}ping".format(prefix) == clean_up_message("    {}ping".format(prefix))
        assert ".me \U000e0000{}ping".format(prefix) == clean_up_message(".me    {}ping".format(prefix))
        assert ".me \U000e0000{}ping".format(prefix) == clean_up_message(" .me    {}ping".format(prefix))
        assert "/me \U000e0000{}ping".format(prefix) == clean_up_message("/me    {}ping".format(prefix))
        assert "/me \U000e0000{}ping".format(prefix) == clean_up_message(" /me    {}ping".format(prefix))

        assert "\U000e0000{}".format(prefix) == clean_up_message("{}".format(prefix))
        assert "/me \U000e0000{}".format(prefix) == clean_up_message("/me {}".format(prefix))
        assert ".me \U000e0000{}".format(prefix) == clean_up_message(".me {}".format(prefix))
        assert "\U000e0000{}".format(prefix) == clean_up_message("    {}".format(prefix))
        assert ".me \U000e0000{}".format(prefix) == clean_up_message(".me    {}".format(prefix))
        assert ".me \U000e0000{}".format(prefix) == clean_up_message(" .me    {}".format(prefix))
        assert "/me \U000e0000{}".format(prefix) == clean_up_message("/me    {}".format(prefix))
        assert "/me \U000e0000{}".format(prefix) == clean_up_message(" /me    {}".format(prefix))
