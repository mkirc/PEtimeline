import os
from jinja2 import Environment, FileSystemLoader

from events import timelineItems


def setup_jinja2_environment(templates_path=""):

    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, templates_path)
    env = Environment(loader=FileSystemLoader(templates_dir))

    def render_template(template_name, **kwargs):

        template = env.get_template(template_name)
        return template.render(**kwargs)

    return render_template



def generateTimeline():
    render_template = setup_jinja2_environment()

    with open('timeline.html', 'w+') as openFile:
        openFile.write(render_template("base.html", timelineItems=timelineItems))

if __name__ == "__main__":

    generateTimeline()
