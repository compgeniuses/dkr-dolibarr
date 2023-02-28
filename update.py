"""Module to upgrade dolibarr docker images."""
#! .venv/bin/python3
import glob
import os
import shutil
import markdown
import process

# Versions of Dolibarr to build Docker images for
versions = []

# Latest version of Dolibarr
LATEST_VERSION = ''

# Fetch the tags for Dolibarr from GitHub API
dolibarr_tags = process.dolibarr.get_dolibarr_tags()

# Loop through the tags to find the versions of Dolibarr to build images for
for tag in dolibarr_tags:
    print(tag['name'])
    versions.append(tag['name'])

# Sort the versions in descending order
versions.sort(reverse=True)

# Find all old Dockerfiles and delete them
old_dockerfiles = glob.glob(f"./{process.helpers.IMAGES_DIR}/*", recursive=True)

# Delete all old dockerfile
for file in old_dockerfiles:
    shutil.rmtree(file)

# Loop through the versions to build Docker images for
for version in versions:
    # Get the major version of the current version
    major_version = version[:4]

    # If latest version hasn't been set, set it to the current major version
    if LATEST_VERSION == '':
        LATEST_VERSION = major_version

    # If the version is less than the minimum version to build images for, skip it
    if version < process.dolibarr.MIN_VERSION:
        continue

    # Loop through the variants and architectures to build images for
    for variant in process.dolibarr.VARIANTS:
        # Initialize variables and directories for the Docker image
        DOCKER_TAGS = ''
        directory_name = process.helpers.get_directory_name_for_image(
            major_version,
            process.dolibarr.get_php_version(major_version),
            variant
        )

        # If the directory for the Docker image already exists, skip it
        if os.path.exists(directory_name):
            continue

        # Create the directory for the Docker image and copy the necessary files
        os.makedirs(directory_name)

        # Determine the Dockerfile template to use based on the variant and architecture
        process.template.copy_template_to(
            variant,
            major_version,
            directory_name
        )


        # Replace variables in files
        process.template.replace_variables_in_dockerfile(
            variant,
            major_version,
            version,
            directory_name
        )

        process.template.replace_variables_in_file_dockertags(
            process.helpers.get_docker_tags(
                major_version,
                LATEST_VERSION,
                variant,
                version
            ),
            directory_name
        )

process.docs.update_docs(versions, process.docker.ARCHIS, LATEST_VERSION)
