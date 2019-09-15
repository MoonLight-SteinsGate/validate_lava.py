import sys
import os

validate_bugs = []

def search_file(dirname):
    paths = []
    for root,dirs,files in os.walk(dirname):
        for file in files:
            print file
            if file.startswith("README"):
                continue
            else:
                path = os.path.join(root,file)
                paths.append(path)

    return paths

def execute_file(target, path, other_dir):
    command = target

    prog = target.split("/")[-1]

    if prog == "md5sum":
        command += " -c "
    elif prog == "base64":
        command += " -d "
    elif prog == "uniq":
        command += " "
    elif prog == "who":
        command += " "

    command += path

    ret = os.popen(command)

    for line in ret.readlines():
        if line.startswith("Successfully triggered bug"):
            id = int(line.split(",")[0].split("bug")[-1])
            validate_bugs.append(id)
            return 0

    os.system("cp " + path + " " + other_dir)

def main(argv):
    target = argv[0]
    output_dir = argv[1]
    path_of_result = argv[2]

    os.system("mkdir " + path_of_result)
    validate_file = open(path_of_result+"/validate_bug.txt", "w+")
    dir_of_other_bug = path_of_result + "/others"
    os.system("mkdir " + dir_of_other_bug)

    paths = search_file(output_dir)
    for path in paths:
        execute_file(target, path, dir_of_other_bug)

    uniq_bug = set(validate_bugs)
    for bug in uniq_bug:
        validate_file.write(str(id)+"\n")



if __name__ == "__main__":
    main(sys.argv[1:])