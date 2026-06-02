from georisk_atlas.main import main


def test_smoke(capsys):
    main()
    out = capsys.readouterr().out
    assert "GeoRisk Atlas" in out
    assert "Suez Canal" in out
