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
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import re


class PasswordForm(models.Model):
    _name = "password.form"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Password Form"
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string="Customer",  required=True, tracking=True)   
    active = fields.Boolean(default=True, Tracking=True)
    device_password_ids=fields.One2many('device.list.lines','password_form_id',  string='Password Lines')
    

    @api.onchange('partner_id')
    def password_availability(self):
        password_record = self.env['password.form'].with_context(active_test=False).search([('partner_id', '=', self.partner_id.id)])
        if password_record:
            raise ValidationError(
                        f"Password already exitst for this Customer ")



class DeviceListLines(models.Model):
    _name = "device.list.lines"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Device List Lines"

    device_id = fields.Many2one('device.list')
    user_name = fields.Char(string="User Name",tracking=True)
    name = fields.Char(string="Name",tracking=True)
    ip_name = fields.Char(string="IP",tracking=True)
    password_name = fields.Char(string="Password", tracking=True)
    description = fields.Text(string="Description")
    password_form_id=fields.Many2one('password.form', string='Password Form Id')
    partner_id = fields.Many2one(
        'res.partner',
        string="Customer",
        related='password_form_id.partner_id',
        store=True,
        readonly=True
    )
    
    # @api.constrains('ip_name')
    # def _check_valid_ip(self):
    #     ip_pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
    #     for record in self:
    #         if record.ip_name and not re.match(ip_pattern, record.ip_name):
    #             raise ValidationError("Please enter a valid IPv4 address (e.g. 192.168.1.1).")
    #         if record.ip_name:
    #             parts = record.ip_name.split(".")
    #             for part in parts:
    #                 if int(part) < 0 or int(part) > 255:
    #                     raise ValidationError("Each part of IP must be between 0 and 255.")
    
    @api.constrains('ip_name')
    def _check_valid_ip(self):
        cidr_pattern = r'^(\d{1,3}\.){3}\d{1,3}/([0-9]|[1-2][0-9]|3[0-2])$'
        for record in self:
            if record.ip_name:
                match = re.match(cidr_pattern, record.ip_name)
                if not match:
                    raise ValidationError("Please enter a valid IPv4 CIDR (e.g. 192.168.1.1/24).")
                
                # چک کردن هر بخش آی‌پی
                ip_part = record.ip_name.split('/')[0]
                parts = ip_part.split('.')
                for part in parts:
                    if int(part) < 0 or int(part) > 255:
                        raise ValidationError("Each part of IP must be between 0 and 255.")
                
                # چک کردن subnet
                subnet = int(record.ip_name.split('/')[1])
                if subnet < 0 or subnet > 32:
                    raise ValidationError("Subnet mask must be between 0 and 32.")    