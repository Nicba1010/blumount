from typing import IO

from base import LoggingClass
from base.utils import get_flag
from utils.utils import Endianess, read_u64


class U0MaskTable(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.flags: int = read_u64(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Flags: {self.flags}")

        self.menu_call: bool = get_flag(self.flags, 0)
        self.logger.debug(f"Menu Call: {self.menu_call}")

        self.title_search: bool = get_flag(self.flags, 1)
        self.logger.debug(f"Title Search: {self.title_search}")

        self.chapter_search: bool = get_flag(self.flags, 2)
        self.logger.debug(f"Chapter Search: {self.chapter_search}")

        self.time_search: bool = get_flag(self.flags, 3)
        self.logger.debug(f"Time Search: {self.time_search}")

        self.skip_to_next_point: bool = get_flag(self.flags, 4)
        self.logger.debug(f"Skip To Next Point: {self.skip_to_next_point}")

        self.skip_to_prev_point: bool = get_flag(self.flags, 5)
        self.logger.debug(f"Skip To Prev Point: {self.skip_to_next_point}")

        self.reserved_1: bool = get_flag(self.flags, 6)
        self.logger.debug(f"Reserved 1: {self.reserved_1}")

        self.stop: bool = get_flag(self.flags, 7)
        self.logger.debug(f"Stop: {self.stop}")

        self.pause_on: bool = get_flag(self.flags, 8)
        self.logger.debug(f"Pause On: {self.pause_on}")

        self.reserved_2: bool = get_flag(self.flags, 9)
        self.logger.debug(f"Reserved 2: {self.reserved_2}")

        self.still_off: bool = get_flag(self.flags, 10)
        self.logger.debug(f"Still Off: {self.still_off}")

        self.forward_play: bool = get_flag(self.flags, 11)
        self.logger.debug(f"Forward Play: {self.forward_play}")

        self.backward_play: bool = get_flag(self.flags, 12)
        self.logger.debug(f"Backward Play: {self.backward_play}")

        self.resume: bool = get_flag(self.flags, 13)
        self.logger.debug(f"Resume: {self.resume}")

        self.move_up_selected_button: bool = get_flag(self.flags, 14)
        self.logger.debug(f"Move Up Selected Button: {self.move_up_selected_button}")

        self.move_down_selected_button: bool = get_flag(self.flags, 15)
        self.logger.debug(f"Move Down Selected Button: {self.move_down_selected_button}")

        self.move_left_selected_button: bool = get_flag(self.flags, 16)
        self.logger.debug(f"Move Left Selected Button: {self.move_left_selected_button}")

        self.move_right_selected_button: bool = get_flag(self.flags, 17)
        self.logger.debug(f"Move Right Selected Button: {self.move_right_selected_button}")

        self.select_button: bool = get_flag(self.flags, 18)
        self.logger.debug(f"Select Button: {self.select_button}")

        self.activate_button: bool = get_flag(self.flags, 19)
        self.logger.debug(f"Activate Button: {self.activate_button}")

        self.select_and_activate_button: bool = get_flag(self.flags, 20)
        self.logger.debug(f"Select and Activate Button: {self.select_and_activate_button}")

        self.primary_audio_stream_number_change: bool = get_flag(self.flags, 21)
        self.logger.debug(f"Primary Audio Stream Number Change: {self.primary_audio_stream_number_change}")

        self.reserved_3: bool = get_flag(self.flags, 22)
        self.logger.debug(f"Reserved 3: {self.reserved_3}")

        self.angle_number_change: bool = get_flag(self.flags, 23)
        self.logger.debug(f"Angle Number Change: {self.angle_number_change}")

        self.popup_on: bool = get_flag(self.flags, 24)
        self.logger.debug(f"Popup On: {self.popup_on}")

        self.popup_off: bool = get_flag(self.flags, 25)
        self.logger.debug(f"Popup Off: {self.popup_off}")

        self.primary_pg_enable_disable: bool = get_flag(self.flags, 26)
        self.logger.debug(f"Primary PG Enable Disable: {self.primary_pg_enable_disable}")

        self.primary_pg_stream_number_change: bool = get_flag(self.flags, 27)
        self.logger.debug(f"Primary PG Stream Number Change: {self.primary_pg_stream_number_change}")

        self.secondary_video_enable_disable: bool = get_flag(self.flags, 28)
        self.logger.debug(f"Secondary Video Enable Disable: {self.secondary_video_enable_disable}")

        self.secondary_video_stream_number_change: bool = get_flag(self.flags, 29)
        self.logger.debug(f"Secondary Video Stream Number Change: {self.secondary_video_stream_number_change}")

        self.secondary_audio_enable_disable: bool = get_flag(self.flags, 30)
        self.logger.debug(f"Secondary Audio Enable Disable: {self.secondary_audio_enable_disable}")

        self.secondary_audio_stream_number_change: bool = get_flag(self.flags, 31)
        self.logger.debug(f"Secondary Audio Stream Number Change: {self.secondary_audio_stream_number_change}")

        self.reserved_3: bool = get_flag(self.flags, 32)
        self.logger.debug(f"Reserved 3: {self.reserved_3}")

        self.secondary_pg_stream_number_change: bool = get_flag(self.flags, 33)
        self.logger.debug(f"Secondary PG Stream Number Change: {self.secondary_pg_stream_number_change}")
