import os

def main():
    print("🎨 Palette Pre-build Check...")

    cwd = os.getcwd()

    # 1. Check for spaces in path as warned in README
    if " " in cwd:
        print(f"\n❌ ERROR: Space detected in project path:\n   {cwd}")
        print("   The build tools may fail if the path contains spaces.")
        print("   Please move the project to a path without spaces (e.g., C:\\WRK).")

        # The README suggests this causes fatal errors.
        # We warn strongly but allow execution to proceed in case the user has a workaround.
        print("\n⚠️  WARNING: Continuing despite spaces in path. Build failures expected.")

    print(f"\n📂 Working in: {cwd}")
    print("   Creating build directories...")

    dir_count = 0

    # Create dirs in build folders
    for root, dirs, files in os.walk(cwd):
        for dir in dirs:
            if dir.lower() == "build":
                target_root = os.path.join(root, dir)

                # Check/Create OBJI386
                path_i386 = os.path.join(target_root, "OBJI386")
                if not os.path.exists(path_i386):
                    os.makedirs(path_i386, exist_ok=True)
                    dir_count += 1

                # Check/Create OBJAMD64
                path_amd64 = os.path.join(target_root, "OBJAMD64")
                if not os.path.exists(path_amd64):
                    os.makedirs(path_amd64, exist_ok=True)
                    dir_count += 1

    # Define specific directories to create
    specific_dirs = [
        os.path.join(cwd, "WRK-V1.2", "BASE", "NTOS", "BUILD", "EXE"),
        os.path.join(cwd, "ProjectOZ", "BasicOZ", "OBJI386"),
        os.path.join(cwd, "ProjectOZ", "SPACE", "OBJI386"),
        os.path.join(cwd, "ProjectOZ", "runx86"),
        os.path.join(cwd, "ProjectOZ", "files", "i386"),
    ]

    for path in specific_dirs:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            dir_count += 1

    if dir_count > 0:
        print(f"\n✅ Done! Created {dir_count} missing directories.")
    else:
        print("\n✅ Done! All directories already verified.")

    print("   You are ready to build WRK and ProjectOZ.")

if __name__ == "__main__":
    main()
