# -*- coding: utf-8 -*-
################################################################################
#
#    Device Password Management
#
#    Copyright (C) 2025 Alireza (AR)
#    Author: Alireza (alir.riazi@gmail.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import api, fields, models


class DeviceList(models.Model):
    _name = "device.list"
    _description = "Device List Names"

    name= fields.Char(String='Device Name', required=True, ondelete='restrict')
    active = fields.Boolean(default=True)

_sql_constraints = [
       ('unique_tag_name', 'unique (sequence)', 'Name not all')
   ]
    