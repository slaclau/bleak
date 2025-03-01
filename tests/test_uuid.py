from bleak.uuids import normalize_uuid_str


def test_uuid_length_normalization():
    assert normalize_uuid_str("1801") == "00001801-0000-1000-8000-00805f9b34fb"


def test_uuid_case_normalization():
    assert (
        normalize_uuid_str("00001801-0000-1000-8000-00805F9B34FB")
        == "00001801-0000-1000-8000-00805f9b34fb"
    )
