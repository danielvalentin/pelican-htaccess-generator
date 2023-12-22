## Info

This is a small plugin for the [Pelican framework](https://getpelican.com), which generates a .htaccess file in your output folder, when Pelican generates the site. This is useful for removing the .html extension to get clean URLs.

By default, the plugin uses the .htaccess it is shipped with.
Optional setting (in pelicanconf.py):  
**'HTACCESS_PREFERENCE' is a string Enum**

- 'content':
  - Uses the .htaccess file in the content folder (if it exists)
- 'theme':
  - Uses the .htacces file in the current theme's folder (if it exists)
- 'none':
  - The plugin doesn't generate a .htaccess file

Example:
'HTACCESS_PREFERENCE' = 'content'

Please note that this was created for personal use, but might be helpful for others. The logic is a bit messy I think. Might clean it up sometime.

## Remember to configure your server

Here's an example for Apache:

        <Directory /var/www/html/example.com/output> 
                Options -Indexes +FollowSymLinks 
                AllowOverride All 
                Order allow,deny 
                allow from all 
        </Directory> 

### License

Licensed under the [CC0 (or the "do whatever the hell you want") license](https://creativecommons.org/publicdomain/zero/1.0/)
