import argparse
import os

import copier

import ros2_pkg_create


def parseArguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Creates a ROS2 package from templates")

    parser.add_argument("destination", type=str, help="Destination directory")
    parser.add_argument("--defaults", action="store_true", help="Use defaults for all options")

    parser.add_argument("--template", type=str, required=True, choices=["ros2_cpp_pkg"], help="Template")
    parser.add_argument("--package_name", type=str, help="Package name")
    parser.add_argument("--description", type=str, help="Description")
    parser.add_argument("--maintainer", type=str, help="Maintainer")
    parser.add_argument("--maintainer-email", type=str, help="Maintainer email")
    parser.add_argument("--author", type=str, help="Author")
    parser.add_argument("--author-email", type=str, help="Author email")
    parser.add_argument("--license", type=str, choices=["Apache-2.0", "BSL-1.0", "BSD-2.0", "BSD-2-Clause", "BSD-3-Clause", "GPL-3.0-only", "LGPL-2.1-only", "LGPL-3.0-only", "MIT", "MIT-0"], help="License")
    parser.add_argument("--node-name", type=str, help="Node name")
    parser.add_argument("--node-class-name", type=str, help="Class name of node")
    parser.add_argument("--is-component", action="store_true", help="Make it a component?")
    parser.add_argument("--is-lifecycle", action="store_true", help="Make it a lifecycle node?")
    parser.add_argument("--has-launch-file", action="store_true", help="Add a launch file?")
    parser.add_argument("--launch-file-type", type=str, choices=["xml", "py", "yml"], help="Type of launch file")
    parser.add_argument("--has-params", action="store_true", help="Add parameter loading")
    parser.add_argument("--has-subscriber", action="store_true", help="Add a subscriber?")
    parser.add_argument("--has-publisher", action="store_true", help="Add a publisher?")
    parser.add_argument("--has-service-server", action="store_true", help="Add a service server?")
    parser.add_argument("--has-action-server", action="store_true", help="Add an action server?")
    parser.add_argument("--has-timer", action="store_true", help="Add a timer callback?")

    parser.add_argument("--version", action="version", version=f"%(prog)s v{ros2_pkg_create.__version__}")

    return parser.parse_args()


def main():

    # pass specified arguments as data to copier
    args = parseArguments()
    answers = {k: v for k, v in vars(args).items() if v is not None}

    # run copier
    try:
        copier.run_copy("https://gitlab.ika.rwth-aachen.de/fb-fi/ops/templates/ros2/ros2-pkg-create.git",
                        os.getcwd(),
                        data=answers,
                        defaults=args.defaults,
                        unsafe=True)
    except copier.CopierAnswersInterrupt:
        print("Aborted")
        return

if __name__ == "__main__":
    main()
