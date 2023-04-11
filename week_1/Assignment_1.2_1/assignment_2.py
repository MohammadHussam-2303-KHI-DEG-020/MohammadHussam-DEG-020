from dataclasses import dataclass

@dataclass
class Mountain:
    name: str
    elevation: int

# To Construct an instance of the dataclass as:
mount_everest = Mountain("Mount Everest", 8348)

# Convert it to string
mount= str(mount_everest)

# now printing it
print(mount)

#for checking the type of of mount ,just for confirmation
print(type(mount))
