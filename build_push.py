"""Module to upgrade dolibarr docker images."""
#! .venv/bin/python3
import argparse
import os
from python_on_whales import docker
from datetime import datetime
import process

# Vérifiez que les informations d'identification de votre compte Docker Hub sont définies
docker_username = os.environ.get('DOCKER_LOGIN')
docker_password = os.environ.get('DOCKER_PASS')
vcs_ref = os.environ.get('CI_COMMIT_SHORT_SHA')
if not docker_username or not docker_password:
    raise ValueError(
        "Veuillez définir les variables d'environnement DOCKER_LOGIN et "+
        "DOCKER_PASS pour vous connecter à Docker Hub."
    )

# Initialisez le client Docker
print("Connexion a docker")
docker.login(username=docker_username, password=docker_password)

# Parsez les arguments en ligne de commande pour récupérer les chemins et les architectures
parser = argparse.ArgumentParser(
    description='Construire et pousser des images Docker pour différentes architectures'
)
parser.add_argument('-v', '--version',
                    metavar='version',
                    type=str,
                    nargs='+',
                    help='Dolibarr version to update '
)
parser.add_argument('-p', '--push',
                    action='store_true',
                    help='Les images doivent-êtres poussées'
)
args = parser.parse_args()

print("Build docker images")
# Construisez et poussez les images pour chaque architecture spécifiée
for variant in process.dolibarr.VARIANTS:
    print(f"  -> Variant {variant}")

    directory_path=process.helpers.get_directory_name_for_image(
        args.version[0],
        process.dolibarr.get_php_version(args.version[0]),
        variant
    )

    for arch in process.docker.ARCHIS:
        print(f"      -> Arch {arch}")

        # Construisez l'image Docker pour chaque tag spécifié dans le fichier .dockertags
        with open(
            os.path.join(directory_path, '.dockertags'),
            'r', encoding="utf-8"
        ) as f:
            tags = f.read().split(' ')

            # Construisez l'image Docker à partir du Dockerfile
            build_args = {
                'TAG': args.version[0],
                'BUILD_DATE': datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
                'VCS_REF': vcs_ref,
                'ARCHI': arch
            }
            print(f"        -- Image to build : {process.docker.DOCKER_REPO} -> {tags}")
            docker.buildx.build(
                context_path=directory_path+"/",
                tags=[f"{process.docker.DOCKER_REPO}:{tag}-{arch}" for tag in tags],
                platforms=[f"linux/{arch}"],
                build_args=build_args,
                push=False,
                stream_logs=False,
            )
            print("        -- Image build ok")

            if args.push:
                print("      -- Push image")
                # Connectez-vous à Docker Hub et poussez l'image pour l'architecture spécifiée
                docker.image.push([f"{process.docker.DOCKER_REPO}:{tag}-{arch}" for tag in tags] )
                print("      -- Image pushed")

    if args.push:
        print("    -> Create manifest")
        for tag in tags:
            tags_to_add = []
            for arch in process.docker.ARCHIS:
                print(f"        -- {tag} / {arch}")
                # Déterminez le nom complet de l'image à partir du tag et de l'architecture
                image_name = f"{process.docker.DOCKER_REPO}:{tag}"

                # Vérifiez si l'image existe localement
                try:
                    image = docker.image.inspect(image_name+f"-{arch}")
                except docker.errors.ImageNotFound:
                    print(f"L'image {image_name} n'existe pas.")
                    continue
                # Si l'image existe, créez un manifest pour les tags correspondants
                tags_to_add.append(f"{process.docker.DOCKER_REPO}:{tag}-{arch}")

            print(f"      -> Manifest to create :{image_name}")
            docker.manifest.create(image_name,tags_to_add)
            print(f"      -> Manifest {image_name} created, with tags : {tags_to_add}.")
            print(f"      -> Manifest to push: {image_name}.")
            docker.manifest.push(image_name)
            print(f"      -> Manifest {image_name} pushed.")
