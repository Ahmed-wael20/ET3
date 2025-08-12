import os
import shutil
import sys

# File type categories
file_type = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".txt", ".pdf", ".docx"],
    "Videos": [".mp4", ".mkv"],
}

# Simulation mode check
simulate = False
if "--simulate" in sys.argv:
    simulate = True
    print("Simulation mode ON. No files will be moved.\n")
else:
    print("Simulation mode OFF. Files will be moved.\n")

# Ask user for folder path
folder_path = input("Enter the folder path to organize: ").strip()

# Validate folder path
if not os.path.exists(folder_path):
    print(f"❌ Error: Path '{folder_path}' does not exist.")
    sys.exit(1)
elif not os.path.isdir(folder_path):
    print(f"❌ Error: '{folder_path}' is not a folder.")
    sys.exit(1)

# Summary dictionary
summary = {cat: 0 for cat in file_type.keys()}
summary["Others"] = 0

try:
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Skip if not a file
        if not os.path.isfile(file_path):
            continue

        # Get file extension
        extension = os.path.splitext(file)[1].lower()
        category = "Others"

        # Match category
        for cat, exts in file_type.items():
            if extension in exts:
                category = cat
                break

        if simulate:
            print(f"[SIMULATE] Would move: {file} -> {category}")
        else:
            try:
                destination_folder = os.path.join(folder_path, category)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_folder, file))
                print(f"File '{file}' moved to '{category}'")
            except PermissionError:
                print(f"Skipping '{file}': Permission denied.")
            except FileExistsError:
                print(f"Skipping '{file}': File already exists in destination.")
            except Exception as e:
                print(f"Error moving '{file}': {e}")

        # Count file in summary
        summary[category] += 1

except PermissionError:
    print(f"Error: Permission denied for accessing '{folder_path}'.")
    sys.exit(1)
except FileNotFoundError:
    print(f"Error: The folder '{folder_path}' was not found.")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)

# Print summary
print("\n📊 Summary:")
for cat, count in summary.items():
    print(f"{cat}: {count} files")
