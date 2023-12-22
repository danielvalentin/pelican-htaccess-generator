"""
A Pelican plugin that creates a htaccess file in the outut folder.
Useful if you want to get rid of the .html extension for clean URL's.
By default, the plugin uses the .htaccess it is shipped with.
Optional settings (in pelicanconf.py):
    'HTACCESS_PREFERENCE' is a string Enum
        'content':
            Uses the .htaccess file in the content folder (if it exists)
        'theme':
            Uses the .htacces file in the current theme's folder (if it exists)
        'none':
            The plugin doesn't generate a .htaccess file
Example:
'HTACCESS_PREFERENCE' = 'content'
"""
import shutil
from pathlib import Path
from pelican import signals

class Htaccess:
    """ Main class for the plugin
    Methods:
        set_site_paths
        check_for_htaccess_folder
        copy_htaccess_from_file
    """
    htaccess_path = ''
    htaccess_output_path = ''

    def __init__(self, pelican_object):
        self.set_site_paths(pelican_object)
        if self.check_for_htaccess_file():
            self.copy_htaccess_from_file()

    def set_site_paths(self, pelican_object):
        """ Just sets the 2 different paths needed """
        path_obj = Path(pelican_object.settings['OUTPUT_PATH'])
        self.htaccess_output_path = str(path_obj.absolute()) + '/.htaccess'
        self.htaccess_path = pelican_object.settings['PLUGIN_PATHS'][0] + '/htaccess/.htaccess'
        print(self.htaccess_path)
        if 'HTACCESS_PREFERENCE' in pelican_object.settings:
            if pelican_object.settings['HTACCESS_PREFERENCE'] == 'content':
                path_obj = Path(pelican_object.settings['PATH'] + '/.htaccess')
                if path_obj.is_file():
                    self.htaccess_path = pelican_object.settings['PATH'] + '/.htaccess'
            elif pelican_object.settings['HTACCESS_PREFERENCE'] == 'theme':
                path_obj = Path(pelican_object.settings['THEME'] + '/.htaccess')
                if path_obj.is_file():
                    self.htaccess_path = pelican_object.settings['THEME'] + '/.htaccess'
            elif pelican_object.settings['HTACCESS_PREFERENCE'] == 'none':
                self.htaccess_path = ''

    def check_for_htaccess_file(self):
        """Just checks if the selected .htaccess file exists"""
        #if 'HTACCESS_PREFERENCE' in pelican_object.settings:
            #if pelican_object.settings['HTACCESS_PREFERENCE'] == 'none':
                #return false
        path_obj = Path(self.htaccess_path)
        return path_obj.is_file()

    def copy_htaccess_from_file(self):
        """ If 'HTACCESS_PREFERENCE' is not set (default):
                copies the default htaccess file from the plugin dir
            If it is set and is 'content':
                copies the .htaccess file in the content dir (if it exists)
            If is is set and is 'theme':
                copies the file from the current theme's dir (if it exists)
            If is is set and is 'none':
                No .htaccess file is generated
            If 'HTACCESS_PREFERENCE' is set, but the file is not found,
                the plugin will default to the plugin's .htaccess
        """
        shutil.copyfile(self.htaccess_path, self.htaccess_output_path)

def register():
    """" Register the class to the 'finalized' signal """
    signals.finalized.connect(Htaccess)
