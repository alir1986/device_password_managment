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
import datetime
from odoo import api, fields, models, _ 
from odoo.exceptions import ValidationError



class UpdatePasswordWizard(models.TransientModel):
    _name = "update.password.wizard"
    _description = "Update Password Wizard"
    
    
    
    @api.model
    def default_get(self, fields):
        res=super(UpdatePasswordWizard,self).default_get(fields)
        res['acitve_id']= self.env.context.get('active_id')
        res["customer_name"]= self.env.context.get('customer_name')
        password_record = self.env['device.list.lines'].with_context(active_test=False).search([('id', '=', res['acitve_id'])], limit=1)
        res.update({
                    'user_name': password_record.user_name,
                    'name': password_record.name,
                    'ip_name': password_record.ip_name,
                    'password_name': password_record.password_name,
                    'description': password_record.description,
                })
        return res
    
    
    acitve_id = fields.Char(string="Record ID")
    device_id = fields.Many2one('device.list')
    user_name = fields.Char(string="User Name")
    name = fields.Char(string="Name")
    ip_name = fields.Char(string="IP")
    password_name = fields.Char(string="Password")
    description = fields.Text(string="Descrition")
    customer_name=fields.Many2one('password.form', string='Customer name')
    

    def action_update(self):
       
        record = self.env['device.list.lines'].with_context(active_test=False).search(
            [('id', '=', self.acitve_id)], limit=1 )

        record.write({
            'user_name': self.user_name,
            'name': self.name,
            'ip_name': self.ip_name,
            'password_name': self.password_name,
            'description': self.description,
        })

        return {'type': 'ir.actions.act_window_close'}
        