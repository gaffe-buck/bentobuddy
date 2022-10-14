
# Bento Buddy
#
# Copyright (C) 2012 - 2022 - Critters LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/ .
import bpy








def get_unique_name():
    
    import uuid
    import time
    idn = str(uuid.uuid4())
    name = idn.replace("-", "")
    idt = str(time.time())
    time_now = idt.replace(".", "_")
    unique_name = name + "_" + time_now
    return unique_name








class BentoBuddyHelpProperties(bpy.types.PropertyGroup):
    def update_help_some_property(self, context):
        bbh = bpy.context.window_manager.bb_help
        
        if bb_settings['terminate'] == True:
            bb_settings['terminate'] = False
            return
        
        bb_settings['terminate'] = True
        bbh.help_some_property = False
        return









    
    
    
    
    
    
        
    
        
            
        
            
        








    
    
    
    
    
    
    
    
        
        

        
        
        
            
            
        
        
        
            
            
            
            
            
        
        
        
        
            
            
            
            

        






    
    
    

    
    
    
        
    
    


    
    
        






 






