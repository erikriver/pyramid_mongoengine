import os
from paste.script.templates import Template, var
from paste.util.template import paste_script_template_renderer

class PyramidTemplate(Template):
    vars = [
        var('version', 'Version (like 0.1)'),
        var('description', 'One-line description of the package'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name'),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name'),
        ]
    def pre(self, command, output_dir, vars):
        vars['random_string'] = os.urandom(20).encode('hex')
        package_logger = vars['package']
        if package_logger == 'root':
            package_logger = 'app'
        vars['package_logger'] = package_logger
        return Template.pre(self, command, output_dir, vars)

    def post(self, command, output_dir, vars):
        return Template.post(self, command, output_dir, vars)


class MongoengineProjectTemplate(PyramidTemplate):
    _template_dir = 'pyramid_mongoengine'
    summary = 'pyramid MongoDB project via MongoEngine'
    template_renderer = staticmethod(paste_script_template_renderer)
