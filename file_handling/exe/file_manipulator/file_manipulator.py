while True:
    info = input().split('-')

    if info[0] == 'End':
        break

    command, file_name, *args = info

    if command == 'Create':
        open(file_name, 'w').close()
    elif command == 'Add':
        content = args[0]
        file = open(file_name, 'a')
        file.write(f"{content}\n")

    elif command == 'Replace':
        try:
            result = []
            file = open(file_name, 'r')
            for line in file.readlines():
                line = line.replace(args[0], args[1])
        except FileNotFoundError:
            print("An error occurred")
        else:
            file = open(file_name, 'w')
            file.write('\n'.join(result))

    elif command == 'Delete':
        pass