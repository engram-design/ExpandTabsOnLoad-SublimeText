"""ExpandTabsOnLoad SublimeText plugin."""
import os

import sublime
import sublime_plugin


class ExpandTabsOnLoad(sublime_plugin.EventListener):
    """Expand tabs / spaces on file open."""

    def on_load_async(self, view):
        """Run ST's 'expand_tabs' command when opening a file."""
        if view.settings().get('convert_tabspaces_on_load') == 1:
            if view.settings().get('translate_tabs_to_spaces') == 1:
                view.run_command('expand_tabs')
            else:
                view.run_command('unexpand_tabs')

