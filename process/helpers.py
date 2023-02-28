"""Module with helpers methods."""

TEMPLATE_DIR='template'
IMAGES_DIR='images'

def get_docker_tags(major_version, latest_version, variant, version):
    """Defines docker tags"""

    version_variant = f"{version}-{variant} {major_version}-{variant}"

    if major_version == latest_version:
        if variant == "apache":
            return f"{version_variant} {variant} {version} {major_version} latest"
        else:
            return f"{version_variant} {variant}"
    else:
        if variant == "apache":
            return f"{version_variant} {version} {major_version}"
        else:
            return f"{version_variant}"

def get_directory_name_for_image(major_version, php_version, variant):
    """Get directory name for an image."""
    return f"{IMAGES_DIR}/{major_version}/php{php_version}-{variant}"
