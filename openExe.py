import os


def find_file(lookFor, drive):
    for r, d, f in os.walk(drive):
        for file in f:
            filepath = os.path.join(r, file)
            
            if lookFor == file:
                print(os.path.join(r, file))
                return os.path.join(r, file).replace("\\", "\\")


            

