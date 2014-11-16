#!/bin/sh

PROJECT = project.pro

UI_FILES := $(wildcard ui/*.ui)
PY_UI_FILES := $(patsubst %.ui, %_ui.py, $(UI_FILES))

%_ui.py: %.ui
	pyuic5 $(patsubst %_ui.py, %.ui, $@) > $@

ui: $(PY_UI_FILES)

translate:
	pylupdate5 $(PROJECT)
	lupdate $(PROJECT)
	lrelease $(PROJECT)