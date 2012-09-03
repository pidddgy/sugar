import os

from gi.repository import Gtk

from sugar3 import env
from sugar3.profile import get_profile

from jarabe.intro.window import IntroWindow
from jarabe.intro.window import create_profile


def check_profile():
    profile = get_profile()

    path = os.path.join(os.path.expanduser('~/.sugar'), 'debug')
    if not os.path.exists(path):
        profile.create_debug_file()

    path = os.path.join(env.get_profile_path(), 'config')
    if os.path.exists(path):
        profile.convert_profile()

    if not profile.is_valid():
        win = IntroWindow()
        win.show_all()
        Gtk.main()
