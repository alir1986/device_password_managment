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
{
    'name': "Device Password Management",
    'version': '16.0.0.1',
    'summary': "Project Manager can Create Password list for Customer and give View access to Project Users",
    'description': """
        This module is designed for service companies to efficiently manage customer devices and their access credentials.  
        It allows you to register and maintain essential information such as device name, IP address, username, and password.  
        When tasks are created, the system ensures that only authorized users can access the required credentials, improving both security and workflow efficiency.  

        Key Features:
        - Store and manage customer device details (IP, name, username, password).
        - Assign and control credential access per task.
        - Improve data security and traceability.
        - Streamline service operations for technical teams.
    """,
    'category': 'Project',
    'author': "Alireza (AR)",
    'maintainer': "Alireza",
    'support': "alir.riazi@gmail.com",
    'license': 'LGPL-3',
    'depends': ['mail', 'product', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'data/device_name.xml',
        'wizard/update_password.xml',
        'views/menu.xml',
        'views/password_form_view.xml',
        'views/device_list_view.xml',
        'views/project_task_views.xml',
    ],
    'images': ['static/description/banner.png'],
        'assets': {
    'web.assets_backend': [
        'static/description/index.html',
       ],
     },
    'installable': True,
    'application': False,
    'auto_install': False,
}