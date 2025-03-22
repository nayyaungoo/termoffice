from .ui import MainMenu, PathSpecifier

MainMenu.run()                  # passed
MainMenu.clear()                # passed

# TODO: PathSpecifier.run()     # failed

print(MainMenu.maxy)            # passed
print(MainMenu.maxx)            # passed

# passed: 4
# failed: 5