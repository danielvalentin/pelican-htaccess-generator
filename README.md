This is a small plugin for the [Pelican framework](https://getpelican.com), which generates a .htaccess file in your output folder, when Pelican generates the site. This is useful for removing the .html extension to get clean URLs.

Currently it defaults to the plugin's .htaccess file, but

- If there's a .htaccess file in the current theme's root folder, it will use that
- Alternatively, if the setting 'HTACCESS_USE_CONTENT_VERSION' is set to True, the plugin will look in the /content folder for a .htaccess file, in case you want to use a customized one.

Please note that this was created for personal use, but might be helpful for others. The logic is a bit messy I think. Might clean it up sometime.
