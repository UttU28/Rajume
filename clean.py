import glob
import os
import shutil
import subprocess

TEMP_PATTERNS = [
    "*.aux",
    "*.fdb_latexmk",
    "*.fls",
    "*.out",
    "*.log",
    "*.synctex.gz",
]


def script_dir():
    return os.path.dirname(os.path.abspath(__file__))


def resume_dirs():
    root = script_dir()
    names = [
        name
        for name in os.listdir(root)
        if os.path.isdir(os.path.join(root, name)) and not name.startswith(".")
    ]
    return [os.path.join(root, name) for name in sorted(names)]


def tex_files(directory):
    return sorted(glob.glob(os.path.join(directory, "*.tex")))


def pdf_path(tex_path):
    return os.path.splitext(tex_path)[0] + ".pdf"


def delete(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        return False
    except OSError as error:
        print(f"  could not delete {path}: {error}")
        return False
    print(f"  deleted {os.path.relpath(path, script_dir())}")
    return True


def build_pdf(tex_path):
    directory = os.path.dirname(tex_path)
    tex_name = os.path.basename(tex_path)
    latexmk = shutil.which("latexmk")
    if latexmk:
        command = [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error", tex_name]
    else:
        command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_name]

    print(f"  building {os.path.relpath(tex_path, script_dir())}")
    passes = 1 if latexmk else 2
    result = None
    for _ in range(passes):
        result = subprocess.run(
            command,
            cwd=directory,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            tail = (result.stdout or "") + (result.stderr or "")
            print(f"  build failed ({result.returncode})")
            for line in tail.strip().splitlines()[-25:]:
                print(f"    {line}")
            return False
    return os.path.isfile(pdf_path(tex_path))


def clean_temp(directory):
    removed = 0
    for pattern in TEMP_PATTERNS:
        for path in glob.glob(os.path.join(directory, pattern)):
            if delete(path):
                removed += 1
    return removed


def main():
    os.chdir(script_dir())
    built = 0
    failed = []
    removed_pdfs = 0

    print("Rebuild resume PDFs")
    for directory in resume_dirs():
        sources = tex_files(directory)
        if not sources:
            continue
        print(os.path.basename(directory))
        for tex_path in sources:
            pdf = pdf_path(tex_path)
            if os.path.isfile(pdf) and delete(pdf):
                removed_pdfs += 1
            if build_pdf(tex_path):
                built += 1
                print(f"  wrote {os.path.relpath(pdf_path(tex_path), script_dir())}")
            else:
                failed.append(os.path.relpath(tex_path, script_dir()))

    print("\nClean temp files")
    removed_temp = 0
    for directory in resume_dirs():
        if tex_files(directory):
            removed_temp += clean_temp(directory)

    print(
        f"\nRemoved {removed_pdfs} PDFs, rebuilt {built}, "
        f"cleaned {removed_temp} temp files."
    )
    if failed:
        print("Failed:")
        for path in failed:
            print(f"  {path}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
