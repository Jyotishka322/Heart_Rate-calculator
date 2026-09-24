import sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from calculator import calculate_heart_rate

# Test that 60 beats in 60 seconds equals 60 beats per minute

def test_60_beats_in_60_seconds():

assert calculate_heart_rate(60, 60) == 60

# Test that 30 beats in 30 seconds equals 60 beats per minute

test_30_beats_in_30_seconds():

assert calculate_heart_rate(30, 30) == 60

# Test that 75 beats in 60 seconds equals 75 beats, per minute

test_75_beats_in_60_seconds():

assert calculate_heart_rate(75, 60) == 75

# Test that fractional result is rounded

def test_fractional_result():

assert round(calculate_heart_rate(50, 45), 2) == 66.67