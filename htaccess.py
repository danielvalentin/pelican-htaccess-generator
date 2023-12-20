"""
A Pelican plugin that creates a htaccess file in the outut folder.
Useful if you want to get rid of the .html extension for clean URL's.
Settings:
    'HTACCESS_USE_CONTENT_VERSION' = True/False
- If the above setting is True, the plugin will use the .htaccess
  in the content folder (if one exists)
- if False it will check if the theme comes with a .htaccess file
- If not defined it will use the default .htaccess file in this plugin.
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
        p = Path(pelican_object.settings['OUTPUT_PATH'])
        self.htaccess_output_path = str(p.absolute()) + '/.htaccess'
        if 'HTACCESS_USE_CONTENT_VERSION' in pelican_object.settings:
            if pelican_object.settings['HTACCESS_USE_CONTENT_VERSION'] is True:
                self.htaccess_path = pelican_object.settings['PATH'] + '/.htaccess'
            elif pelican_object.settings['HTACCESS_USE_CONTENT_VERSION'] is False:
                self.htaccess_path = pelican_object.settings["THEME"] + '/' + '.htaccess'
        else:
            self.htaccess_path = pelican_object.settings['PLUGIN_PATHS'][0] + '/htaccess/'

    def check_for_htaccess_file(self):
        """Just checks if the selected .htaccess file exists"""
        p = Path(self.htaccess_path)
        return p.is_file()

    def copy_htaccess_from_file(self):
        """ If 'HTACCESS_USE_CONTENT_VERSION' is not set:
                copies the default htaccess file from the plugin dir
            If it is set and is True:
                copies the .htaccess file in the content dir (if it exists)
            If is is set and is False:
                copies the file from the current theme's dir (if it exists)
        """
        shutil.copyfile(self.htaccess_path, self.htaccess_output_path)

def register():
    """" Register the class to the 'finalized' signal """
    signals.finalized.connect(Htaccess)
