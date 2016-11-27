# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.desk.doctype.desktop_icon.desktop_icon import set_hidden

class RoleModuleVisibility(Document):
	def autoname(self):
		if self.role:
			self.name = self.role
	def validate(self):
		#self.name = self.role
		for user in frappe.db.sql("""SELECT parent FROM `tabUserRole` WHERE role='{0}'""".format(self.role)):
			for module in self.modules:
				print module.module
				set_hidden(module.module, user=user[0], hidden=self.hidden)
		if self.is_global:
			for module in self.modules:
				hideGlobal(module.module,self.hidden)

def hideGlobal(module,hidden):
	set_hidden(module, user=None, hidden=hidden)