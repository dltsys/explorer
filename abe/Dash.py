# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .C11Chain import C11Chain

class Dash(C11Chain):
    def __init__(chain, **kwargs):
        chain.name = 'Smash'
        chain.code3 = 'SMASH'
        chain.address_version = '\x4c'
        chain.script_addr_vers = '\x05'
        chain.magic = '\x62\x65\x65\x66'
        C11Chain.__init__(chain, **kwargs)

    datadir_conf_file_name = 'dash.conf'
    datadir_rpcport = 11305
    datadir_p2pport = 11303

