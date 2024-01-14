import muspy

from core.constants import EXAMPLE_MIDI_FILE_PATH
from core.service.midi_processing import retrieve_information_from_midi, retrieve_basic_information, retrieve_metrics


def test_retrieve_basic_info():
    music_file = muspy.read(EXAMPLE_MIDI_FILE_PATH)
    basic_info_data = retrieve_basic_information(music_file)
    assert basic_info_data
    print(basic_info_data)


def test_retrieve_metrics():
    pass


def test_retrieve_info():
    music = retrieve_information_from_midi(EXAMPLE_MIDI_FILE_PATH)
    assert music
    print(music)
