# window.py
#
# Copyright 2025 Jan-Niklas Kuhn
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/github/heidefinnischen/resolutionary/window.ui')
class ResolutionaryWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ResolutionaryWindow'

    width_entry = Gtk.Template.Child()
    height_entry = Gtk.Template.Child()
    scale_entry = Gtk.Template.Child()
    effective_resolution_output = Gtk.Template.Child()
    scale_factor_output = Gtk.Template.Child()
    about_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_resizable(False)
        #self.entry = Gtk.Entry()

    def calculate_effective_resolution(self, width, height, scale):
        scale_factor = scale / 100
        effective_width = width / scale_factor
        effective_height = height / scale_factor
        return int(effective_width), int(effective_height), scale_factor

    def get_input_values(self):
        """Try to read and convert all three entries to ints.
        Return a tuple (width, height, scale) if valid, else None."""
        try:
            width = int(self.width_entry.get_text())
            height = int(self.height_entry.get_text())
            scale = int(self.scale_entry.get_text())
            return width, height, scale
        except ValueError:
            return None

    @Gtk.Template.Callback()
    def on_entry_changed(self, entry):
        values = self.get_input_values()

        if values is None:
            # Invalid input, mark entries as error if empty or non-digit
            for e in [self.width_entry, self.height_entry, self.scale_entry]:
                text = e.get_text()
                if text == "":
                    e.remove_css_class("error")
                elif not text or not text.isdigit():
                    e.add_css_class("error")
                else:
                    e.remove_css_class("error")
            self.effective_resolution_output.set_text("")
            self.scale_factor_output.set_text("")
            return
        else:
            # Valid input, remove error classes
            for e in [self.width_entry, self.height_entry, self.scale_entry]:
                e.remove_css_class("error")

        width, height, scale = values
        effective_width, effective_height, scale_factor = self.calculate_effective_resolution(width, height, scale)

        output = f"{effective_width}x{effective_height}"
        output_scale_factor = f"at {scale_factor}x"

        print(f"Result: {effective_width}x{effective_height} at {scale_factor}x")
        if scale_factor >= 1:
            self.effective_resolution_output.set_text(output)
            self.scale_factor_output.set_text(output_scale_factor)
        else:
            self.effective_resolution_output.set_text("")
            self.scale_factor_output.set_text("")

