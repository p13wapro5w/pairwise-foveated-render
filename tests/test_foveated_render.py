import pytest
from render import foveated_render as mod

CASES = [
    ("predict_add", "m.predict_gaze((0.0, 0.0), (1.0, 0.0), 2.0) == approx((2.0, 0.0))"),
    ("resolution_center", "m.resolution_at(0.0, 1.0, 0.25) == approx(1.0)"),
    ("resolution_edge", "m.resolution_at(1.0, 1.0, 0.25) == approx(0.25)"),
    ("resolution_mid", "m.resolution_at(0.5, 1.0, 0.25) == approx(0.625)"),
    ("ratio_center", "m.compression_ratio(0.0) == approx(1.0)"),
    ("ratio_edge", "m.compression_ratio(1.0) == approx(0.25)"),
    ("latency_add", "m.latency_compensate((0.0, 0.0), (1.0, 0.0), 0.5) == approx((0.5, 0.0))"),
    ("gaze_avg", "m.shared_gaze((0.0, 0.0), (2.0, 0.0)) == approx((1.0, 0.0))"),
    ("fov_grow", "m.fov_scale(60.0, 90.0) == approx(1.5)"),
    ("blend_start", "m.blend_zone(0.0, 0.5, 1.0) == approx(0.0)"),
    ("blend_end", "m.blend_zone(0.5, 0.5, 1.0) == approx(1.0)"),
    ("load_low", "m.adapt_load(0.5, 1.0) == approx(0.5)"),
    ("load_high", "m.adapt_load(0.1, 1.0) == approx(0.5)"),
    ("ui_full", "m.ui_resolution(True) == approx(1.0)"),
    ("reproject_add", "m.reproject_gaze((0.0, 0.0), (1.0, 0.0)) == approx((1.0, 0.0))")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
