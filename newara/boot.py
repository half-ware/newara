# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import frappe


def boot_session(bootinfo):
	"""Expose per-site theme name to the Desk via frappe.boot.

	Reads `newara_theme` from site_config.json. If set, makes it available as
	`frappe.boot.newara_theme` for runtime loaders.
	"""
	try:
		theme_name = frappe.conf.get("newara_theme")
	except Exception:
		theme_name = None

	if theme_name:
		bootinfo["newara_theme"] = theme_name

