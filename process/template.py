"""Module with template method."""
# -*- coding: utf-8 -*-
import shutil
import os
import fileinput
from . import helpers
from . import dolibarr


def copy_template_to(variant, major_version, directory):
    """Copy template to directory"""
    shutil.copy(
        f"{helpers.TEMPLATE_DIR}/Dockerfile."+
            f"{dolibarr.BASES_IMAGES_VARIANTS[variant]}."+
            f"{dolibarr.get_php_version(major_version)}.template",
        f"{directory}/Dockerfile"
    )

    shutil.copy(f"{helpers.TEMPLATE_DIR}/entrypoint.sh",
                f"{directory}/entrypoint.sh"
    )

    shutil.copy(f"{helpers.TEMPLATE_DIR}/.env",
                f"{directory}/.env"
    )

    shutil.copy(f"{helpers.TEMPLATE_DIR}/.dockerignore",
                f"{directory}/.dockerignore"
    )

    # shutil.copy(
    #     f"{helpers.TEMPLATE_DIR}/docker-compose.{dolibarr.COMPOSE_VARIANTS[variant]}.test.yml",
    #     f"{directory}/docker-compose.test.yml"
    # )

    server_web_variant = dolibarr.SERVERS_WEB_VARIANTS[variant]
    # If there is a server web variant and its directory exists,
    # copy it to the Docker image directory
    if (
        bool(server_web_variant and server_web_variant.strip()) and
        os.path.exists(f"{helpers.TEMPLATE_DIR}/{server_web_variant}")
        ):

        shutil.copytree(f"{helpers.TEMPLATE_DIR}/{server_web_variant}",
                        f"{directory}/{server_web_variant}")

def replace_variables_in_dockerfile(variant, major_version, version, directory):
    """Replace variables in files"""
    with fileinput.FileInput(directory+'/Dockerfile', inplace=True) as file:
        for line in file:
            print(
                line.replace("%%PHP_VERSION%%", dolibarr.get_php_version(major_version))
                .replace("%%VARIANT%%", variant)
                .replace("%%VERSION%%", version)
                .replace("%%CMD%%", dolibarr.CMD_VARIANTS[variant]), end='')

def replace_variables_in_hooks_run(major_version, docker_repo, directory):
    """Replace variables in all files in hooks"""
    # Replace variables in the "run" hook
    with fileinput.FileInput(directory+'/hooks/run', inplace=True) as file:
        for line in file:
            print(
                line.replace("${VARIANT}", major_version)
                .replace("${DOCKER_REPO_URL}", docker_repo), end='')

def replace_variables_in_file_dockertags(tags, directory):
    """Replace variables in .dockertags file"""
    # Write the list of tags to a file
    with open(f"{directory}/.dockertags", "w", encoding="utf-8") as f:
        f.write(tags)
