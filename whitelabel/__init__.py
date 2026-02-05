# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
import frappe

__version__ = '0.0.2'

if frappe.conf and frappe.conf.get("app_logo_url"):
    __logo__ = frappe.conf.get("app_logo_url") or '/assets/whitelabel/images/whitelabel_logo.jpg'
else:
    __logo__ = '/assets/whitelabel/images/whitelabel_logo.jpg'

except Exception:
# During pip install, or if frappe is unavailable
pass`
