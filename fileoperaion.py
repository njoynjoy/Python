def file_operation(file_path, key, value):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:  
        for line in lines:
            if key in line:
                file.write(f"{key}={value}\n")
                #line = f"{key}={value}\n"
            else:
                file.write(line)
file_operation("/home/njoy/python-zero-hero/server.conf", "SSL_ENABLED", "FALSE")