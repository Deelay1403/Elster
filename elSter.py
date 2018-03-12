#-*- coding: utf-8 -*-
'''Działa aż miło'''
import sys, os, inspect
cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "GitHub")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
import init_window
import gtk

if __name__ == "__main__":
    i = init_window.__init__()
#   gtk.main()
